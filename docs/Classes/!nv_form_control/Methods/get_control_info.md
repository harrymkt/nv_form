# get_control_info
Retrieves more information of the control (if any).

`string get_control_info();`

## Returns:
`string`: A string defining the information.

## Remarks:
In form, this information is spoken last. If the `form.speak_control_attributes_separately` property is set to `true`, this information will be spoken separately. Most controls usually leave this method empty, i.e. unmodified.
