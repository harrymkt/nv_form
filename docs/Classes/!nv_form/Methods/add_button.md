# add_button
Creates a new button and adds it to the form.

`nv_form_button@ add_button(const string &in caption, const string &in id = "", bool primary = false, bool cancel = false, int position = -1, nv_form_control_callback@callback = null);`

## Arguments:
- `const string &in caption`: the label to associate with the button.
- `const string &in id = ""`: The ID.
- `bool primary = false`: Should this button be activated by pressing enter anywhere in the form?
- `bool cancel = false`: Should this button be activated by pressing escape anywhere in the form?
- `int position = -1`: The position to insert at.

## Returns:
`nv_form_button@`: An NV control button type on success, null otherwise.
