# add_keyboard_area
Creates a new UI keyboard area and adds it to the form.

`nv_form_keyboard_area@ add_keyboard_area(const string &in caption, const string &in id = "", int position = -1);`

## Arguments:
- `const string &in caption`: the label to associate.
- `const string &in id = ""`: The ID.
- `int position = -1`: The position to insert at.

## Returns:
`nv_form_keyboard_area@`: A handle to the control on success, null otherwise.
