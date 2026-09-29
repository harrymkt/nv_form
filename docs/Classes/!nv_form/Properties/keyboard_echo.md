# keyboard_echo
Retrieve or set how text should be echoed.

`int keyboard_echo;`

## Remarks:
This property (if retrieved) returns the value depending on the `rely_on_nvform_echo` boolean property. If this is set to `true`, which is default, this value will always be the value of `nvform_keyboard_echo` global property.

You can also use `void set_keyboard_echo(int echo, bool update)` method if you want to control whether changes to the echo value automatically updates input controls.
