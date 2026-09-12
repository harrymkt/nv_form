# add_spin
Creates a new spin box and adds it to the form.

`nv_form_spin@add_spin(const string &in caption, const string &in id = "", const string &in default_text = "", double min = 0, double max = 100, bool read_only = false, double step = 1, double page = 0, int position = -1, nv_form_control_callback@callback = null);`

## Arguments:
- `const string &in caption`: The label to associate.
- `const string &in id = ""`: The ID.
- `const string &in default_text = ""`: The initial text value.
- `double min = 0`: Minimum value.
- `double max = 100`: The maximum value.
- `bool read_only = false`: Toggle read only mode.
- `double step = 1`: Step size when pressing arrow keys.
- `double page = 0`: Page size, the number of values that will be increased or decreased when you press PageUp and PageDown. If this is set to 0, the page size will be the step size value multiplied by 10.
- `int position = -1`: The position to insert at.
- nv_form_control_callback@callback = null`: Control callback.

## Returns:
`nv_form_spin@`: A handle to the control on success, null otherwise.
