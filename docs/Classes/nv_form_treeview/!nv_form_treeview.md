# nv_form_treeview
A hierarchical list of nodes, where each node can hold children that are expanded and collapsed with the arrow keys.

`nv_form_treeview(nv_form@ parent, const string &in caption, const string &in id = "", bool speak_level = true);`

## Arguments:
- `nv_form@ parent`: A handle to the parent `nv_form` class.
- `const string &in caption`: The caption / label of the tree.
- `const string &in id = ""`: The ID of the tree.
- `bool speak_level = true`: Whether or not the level (i.e. level {x}) should be spoken.

## Remarks:
Use `nv_form::add_treeview` rather than constructing the tree yourself, unless you are subclassing it.

You build the tree by adding root nodes to it and children to those nodes, so `nv_form_treeview::add` and `nv_form_tree_node::add` are two different methods. Nodes start collapsed.

### Keys:
- Up and Down: move through the nodes that are currently visible.
- Right: expand the current node, or move to its first child when it is already expanded.
- Left: collapse the current node, or move to its parent when it has no children or is already collapsed.
- Home and End: jump to the first or last visible node.
