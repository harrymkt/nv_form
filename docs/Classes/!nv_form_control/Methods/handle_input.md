# handle_input
Handles input, custom keys, of the control.

`bool handle_input();`

## Returns:
`bool`: `true` if this control is used, `false` otherwise.

## Remarks:
When defining this method, the control should execute any necessary actions, like checking specific keys for the control, and always return `true` if any of execution is carried.
This method should return `false` only when none of the key the user presses is used or triggered.

For example:
```nvgt
class my_custom_control: nv_form_control {
	bool handle_input() {
		if (key_pressed (KEY_F1)) {
			return true; // This key is now used.
		}
		return false;
	}
}
```
