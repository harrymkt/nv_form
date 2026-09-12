# str
A string representation of the control.

`string get_str() property;`

## Remarks:
This property contains entire information of the control. For example, "Play music  check box  not checked".

A default implementation respects the `form.speak_control_attributes_separately` property, and is defined like this:
```nvgt
	string get_str() property {
		string[] texts = {caption, parent.get_fixed_type(this)};
		if (!enabled) texts.insert_last(" unavailable");
		if (@shortcut != null && speak_shortcut) texts.insert_last(shortcut.name);
		if (!parent.speak_control_attributes_separately) {
			string v = get_control_info();
			if (v != "") texts.insert_last(v);
		}
		return join(texts, "  ");
	}
```
