# add_item
Appends an entry to the menu.

1. `void add_item(const string &in text, nv_form_context_menu_callback@ callback);`
2. `void add_item(const string &in text, const string &in id, nv_form_context_menu_callback@ callback);`

## Arguments:
- `const string &in text`: The text spoken for this entry.
- `const string &in id`: The ID of this item. `text` value is used if not specified. This argument can be entirely skipped.
- `nv_form_context_menu_callback@ callback`: Called with the owning control after the menu closes, when the user chooses this entry. Can be omitted entirely.

## Remarks:
If callback value is omitted, it will use the default callback provided in the constructor.

Entries appear in the order you add them. There is no way to remove one, rebuild the menu instead.

Context menu callback is declared as the following:
```
funcdef bool nv_form_context_menu_callback(nv_form_context_menu@ ctx);
```
