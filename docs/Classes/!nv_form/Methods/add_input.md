# add_input
Creates a new input box and adds it to the form.

`nv_form_input@add_input(const string &in caption, const string &in id = "", const string &in default_text = "", const string &in password_mask = "", int max_length = 0, bool read_only = false, bool multiline = false, int position = -1, nv_form_control_callback@callback = null);`

## Arguments:
- `const string &in caption`: The label to associate.
- `const string &in id = ""`: The ID.
- `const string &in default_text = ""`: The initial text value.
- `const string &in password_mask = ""`: Character if it is a password protected field.
- `int max_length = 0`: The maximum characters this input can have, 0 is unlimited.
- `bool read_only = false`: Toggle read only mode.
- `bool multiline = false`: Multiline field.
- `int position = -1`: The position to insert at.
- nv_form_control_callback@callback = null`: Control callback.

## Returns:
`nv_form_input@`: A handle to the control on success, null otherwise.
