import json
import os
import shutil
import re
import string
import sys
from pathlib import Path

class DocGen:
	def __init__(self, src_dir: str, output_dir: str):
		self.src_dir = Path(src_dir).resolve()
		self.output_dir = Path(output_dir).resolve()
		self.output_dir.mkdir(parents=True, exist_ok=True)
		self.output_md_dir = Path(self.output_dir, "MD").resolve()
		self.output_md_dir.mkdir(parents=True, exist_ok=True)
		self.output_html_dir = Path(self.output_dir, "HTML").resolve()
		self.output_html_dir.mkdir(parents=True, exist_ok=True)
	
	def clean_display_name(self, name: str) -> str:
		"""Removes leading punctuation (including '!') to allow flexible sorting levels while displaying cleanly."""
		return re.sub(r"^[^\w\s]+", "", name)
	
	def clean_file_stem(self, stem: str) -> str:
		"""Removes `@`, `+`, and leading `!` markers from file stems for clean output names."""
		stem = re.sub(r"^[^\w\s]+", "", stem)
		return stem.rstrip("+").rstrip("@")
	
	def adjust_heading_levels(self, markdown_text: str, target_level: int) -> str:
		"""Normalizes markdown headings so that the highest-level heading in the text matches `target_level`, scaling all lower sub-headings proportionally."""
		lines = markdown_text.split("\n")
		# Find the minimum heading level in the file (i.e. 1 for '#', 2 for '##')
		min_level = 7
		for line in lines:
			match = re.match(r"^(#{1,6})\s+(.*)$", line)
			if match:
				min_level = min(min_level, len(match.group(1)))
		if min_level > 6:
			return markdown_text
		level_offset = target_level - min_level
		adjusted_lines = []
		for line in lines:
			match = re.match(r"^(#{1,6})\s+(.*)$", line)
			if match:
				hashes, title = match.groups()
				new_level = min(6, max(1, len(hashes) + level_offset))
				new_hashes = "#" * new_level
				adjusted_lines.append(f"{new_hashes} {title}")
			else:
				adjusted_lines.append(line)
		return "\n".join(adjusted_lines)
	
	def parse_code_doc_file(self, file_path: Path) -> str:
		"""Extracts embedded markdown from code files using block comments."""
		with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
			content = f.read()
		output_md = []
		topic_name = self.clean_file_stem(file_path.stem)
		output_md.append(f"# {topic_name}\n")
		comment_pattern = re.compile(r"/\*\*(?P<no_linefeed>\\)?(?P<body>.*?)\*/", re.DOTALL)
		for match in comment_pattern.finditer(content):
			body = match.group("body")
			no_linefeed = bool(match.group("no_linefeed"))
			if not no_linefeed:
				lines = body.split("\n")
				body = "\n\n".join([line.rstrip() for line in lines if line.strip()])
			output_md.append(body)
		full_md = "\n".join(output_md)
		full_md = re.sub(r"//\s*example:", "## example", full_md, flags=re.IGNORECASE)
		full_md = full_md.replace("\t", "")
		return full_md
	
	def parse_md_file(self, file_path: Path) -> str:
		"""Reads Markdown content."""
		with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
			content = f.read()
		return content
	
	def get_topic_display_name(self, file_path: Path, raw_name_override: str = None) -> str:
		"""Determines topic display name based on index override, '+' suffix, or cleaned filename."""
		if raw_name_override:
			return self.clean_display_name(raw_name_override)
		stem = file_path.stem
		# Rule: '+' before extension uses the first line of the file (minus heading markers)
		if stem.endswith("+") or "+" in stem:
			try:
				with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
					for line in f:
						clean_line = line.strip().lstrip("#").strip()
						if clean_line:
							return self.clean_display_name(clean_line)
			except Exception:
				pass
		clean_stem = self.clean_file_stem(stem)
		return self.clean_display_name(clean_stem.title())
	
	def scan_directory(self, current_dir: Path) -> list:
		"""Scans a directory using .index.json or alphabetical sorting rules."""
		items = []
		index_file = current_dir / ".index.json"
		if index_file.exists():
			with open(index_file, "r", encoding="utf-8") as f:
				index_data = json.load(f)
			for entry in index_data:
				if isinstance(entry, str):
					path = current_dir / entry
					items.append((path, self.get_topic_display_name(path)))
				elif isinstance(entry, list) and len(entry) == 2:
					path = current_dir / entry[0]
					items.append((path, self.get_topic_display_name(path, entry[1])))
		else:
			all_entries = list(current_dir.iterdir())
			# Rule: Sort alphabetically. "!C" will sort before :F" because raw filename is used for sorting, but files (topics) still show up before directories (subsections).
			def sort_key(p: Path):
				raw_name = p.name.lower()
				is_dir = p.is_dir()
				return (is_dir, raw_name)
			all_entries.sort(key=sort_key)
			for entry in all_entries:
				if entry.name.startswith("."):
					continue
				if entry.is_file() and entry.suffix.lower() in [".md", ".nvgt"]:
					items.append((entry, self.get_topic_display_name(entry)))
				elif entry.is_dir():
					items.append((entry, self.get_topic_display_name(entry)))
		return items
	
	def process_node(self, node_path: Path, display_name: str, category_name: str = "", depth: int = 1) -> str:
		"""Recursively parses markdown and source files with heading level scaling and root delegations."""
		if node_path.is_file():
			ext = node_path.suffix.lower()
			if ext == ".nvgt":
				content = self.parse_code_doc_file(node_path)
			elif ext == ".md":
				content = self.parse_md_file(node_path)
			else:
				return ""
			# Rule: If first topic heading matches containing category, strip it
			if category_name:
				lines = content.strip().split("\n")
				if lines and lines[0].startswith("#"):
					first_heading = lines[0].lstrip("#").strip()
					if first_heading.lower() == category_name.lower():
						content = "\n".join(lines[1:]).strip()
			# Rule: File contains '@' before extension -> treated as a new root document
			if "@" in node_path.stem:
				base_name = self.clean_file_stem(node_path.stem)
				root_content = self.adjust_heading_levels(content, target_level=1)
				self.write_outputs(base_name, display_name, root_content)
				return f"- [{display_name}]({base_name}.html)\n"
			# Standard nested content: shift headings to match current depth
			content = self.adjust_heading_levels(content, target_level=depth)
			return f"\n\n{content}\n\n"
		elif node_path.is_dir():
			has_md_root = (node_path / ".MDRoot").exists()
			sub_content = ""
			#next_depth = 1 if has_md_root else depth + 1
			next_depth = depth + 1
			items = self.scan_directory(node_path)
			for child_path, child_name in items:
				sub_content += self.process_node(
					child_path, child_name, category_name=display_name, depth=next_depth
				)
			# Rule: `.MDRoot` present -> output directory contents as new separate document
			if has_md_root:
				base_name = self.clean_file_stem(node_path.name)
				self.write_outputs(base_name, display_name, sub_content)
				return f"- [{display_name}]({base_name}.html)\n"
			header_hashes = "#" * depth
			return f"\n\n{header_hashes} {display_name}\n\n" + sub_content
		return ""
	
	def write_outputs(self, base_name: str, title: str, body_content: str):
		"""Outputs formatted Markdown with front matter and standard HTML."""
		body = body_content.strip()
		# Write TOML front matter formatted .md file
		md_file_content = f'+++\ntitle="{title}"\n+++\n\n{body}\n'
		md_target_path = self.output_md_dir / f"{base_name}.md"
		md_target_path.write_text(md_file_content, encoding="utf-8")
		# Write corresponding .html file
		try:
			import markdown
			html_body = markdown.markdown(body, extensions=["tables", "fenced_code"])
		except ImportError:
			html_body = f"<pre>{body}</pre>"
		htmlt = string.Template("""<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>$title</title>
	<style>
		body {{ font-family: sans-serif; margin: 20px; line-height: 1.6; }}
		pre {{ background: #f4f4f4; padding: 10px; border-radius: 5px; }}
		code {{ background: #f4f4f4; padding: 2px 5px; }}
	</style>
</head>
<body>
$html_body
<script>
document.querySelectorAll("pre").forEach(pre => {
	const code_block = pre.querySelector("code"); // Check if <code> exists inside <pre>
	// Get the content (if there"s <code>, use it; otherwise, fallback to <pre>)
	const code_content = code_block ? code_block.textContent : pre.textContent;
	// Create a container to hold the language label, button, and the code block
	const container = document.createElement("div");
	// Extract the language from <pre>"s data-lang or <code>"s class
	let language = pre.getAttribute("data-lang");
	if (!language && code_block && code_block.className) {
		const match = code_block.className.match(/language-(\\w+)/);
		language = match ? match[1] : "";
	}
	// If language is found, create and insert a language label
	if (language) {
		const lang_label = document.createElement("span");
		lang_label.textContent = `${language}`;
		container.appendChild(lang_label); // Add language label before the button
	}
	// Create the copy button
	const copy_button = document.createElement("button");
	const copy_text="Copy " + (language ? language + " " : "") + "code to clipboard";
	copy_button.textContent = copy_text;
	container.appendChild(copy_button); // Add the button to the container
	// Insert the container before the <pre> tag
	pre.parentNode.insertBefore(container, pre);
	container.appendChild(pre); // Add the pre inside the container
	// Copy functionality
	copy_button.addEventListener("click", () => {
		navigator.clipboard.writeText(code_content)
		.then(() => {
			copy_button.textContent = "Copied " + code_content.length + " characters";
			setTimeout(() => {
				copy_button.textContent = copy_text;
			}, 1500);
		})
		.catch(err => {
			console.error("Failed to copy: ", err);
		});
	});
});
</script>
</body>
</html>""")
		full_html = htmlt.safe_substitute({
			"title": title,
			"html_body": html_body
		})
		html_target_path = self.output_html_dir / f"{base_name}.html"
		html_target_path.write_text(full_html, encoding="utf-8")
	
	def run(self):
		"""Main execution workflow."""
		main_markdown = ""
		items = self.scan_directory(self.src_dir)
		for path, display_name in items:
			main_markdown += self.process_node(path, display_name, depth=1)
		# Write root index files (.md and .html)
		self.write_outputs("docs", "NV Form Module Documentation", main_markdown)
		print(f"Documentation generated successfully in: {self.output_dir}")

if __name__ == "__main__":
	src_folder = sys.argv[1] if len(sys.argv) > 1 else "./docs"
	out_folder = sys.argv[2] if len(sys.argv) > 2 else "./docbuild"
	generator = DocGen(src_folder, out_folder)
	generator.run()
	shutil.move("docbuild/MD/docs.md", "Web/content/docs.md")
