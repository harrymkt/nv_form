# add_item
Appends an entry to the menu.

1. `void add_item(const string &in text, nv_form_control_callback@ callback);`
2. `void add_item(const string &in text, const string &in id, nv_form_control_callback@ callback);`

## Arguments:
- `const string &in text`: The text spoken for this entry.
- `const string &in id`: The ID of this item. `text` value is used if not specified. This argument can be entirely skipped.
- `nv_form_control_callback@ callback`: Called with the owning control after the menu closes, when the user chooses this entry.

## Remarks:
Entries appear in the order you add them. There is no way to remove one, rebuild the menu instead.
