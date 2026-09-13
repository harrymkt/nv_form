# add_checkbox
Creates a new checkbox and adds it to the form.

`nv_form_checkbox@add_checkbox(const string &in caption, const string &in id = "", bool selected = false, int position = -1);`

## Arguments:
- `const string &in caption`: the label to associate with the checkbox.
- `const string &in id = ""`: The ID.
- `bool selected = false`: Should this checkbox be checked by default?
- `int position = -1`: The position to insert at.

## Returns:
`nv_form_checkbox@`: An NV control checkbox type on success, null otherwise.
