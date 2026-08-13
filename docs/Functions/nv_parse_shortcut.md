# nv_parse_shortcut
Parses a shortcut from  a given value.

`nv_shortcut@ parse_nv_shortcut(const string &in value);`

## Arguments:
- `const string &in value`: Value of the shortcut to parse, see remarks.

## Returns:
`nv_shortcut@`: A handle to the `nv_shortcut` object with the parsed shortcut on success, null otherwise.

## Remarks:
Never use this function without verification, like `nv_parse_shortcut(value).name` as this function may return null if the value is invalid.

Value can contain compatible key names from `get_key_name(int)` function, and separate by `+` (plus sign). In addition, the following value can be used as key modifiers:

- `Ctrl` (case insensitive): Either Control key.
- `Shift` (case insensitive): Either Shift key.
- `Alt` (case insensitive): Either Alt key.

When writing value, be sure to capitalize and lower respectively unless that value is deemed case insensitive, as the keys are usually case sensitive.

Add a star character (`*`) followed by a number at the end of the key to make multitap. For example, `Ctrl+A*2` will make double press the `Ctrl+A` key.
