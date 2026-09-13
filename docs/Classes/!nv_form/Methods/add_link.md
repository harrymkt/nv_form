# add_link
Creates a new link and adds it to the form.

`nv_form_link@ add_link(const string &in caption, const string &in url, const string &in id = "", bool primary = false, bool cancel = false, int position = -1, nv_form_control_callback@callback = null);`

## Arguments:
- `const string &in caption`: the label to associate with the link.
- `const string &in url`: The URL.
- `const string &in id = ""`: The ID.
- `bool primary = false`: Should this link be activated by pressing enter anywhere in the form?
- `bool cancel = false`: Should this link be activated by pressing escape anywhere in the form?
- `int position = -1`: The position to insert at.

## Returns:
`nv_form_link@`: An NV control link type on success, null otherwise.
