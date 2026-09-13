# add_switch
Creates a new switch and adds it to the form.

`nv_form_switch@ add_switch(const string &in caption, const string &in id = "", nv_form_switch_item@[] items = {}, int position = -1);`

## Arguments:
- `const string &in caption`: the label to associate with the switch.
- `const string &in id = ""`: The ID.
- `nv_form_switch_item@[] items = {}`: The initial array of `nv_form_switch_item` handles to add.
- `int max_items = 0`: The maximum allowed items in this switch. 0 is unlimited.
- `int position = -1`: The position to insert at.

## Returns:
`nv_form_switch@`: An NV control switch type on success, null otherwise.
