# nv_form_control
This is the base abstract class for all controls.

`nv_form_control(const string &in caption, const string &in id, int type, nv_form@parent);`

## Arguments:
- `const string &in caption`: The caption / label of the control.
- `const string &in id`: The ID of the control.
- `int type`: One of the control types, see the specific enum for available types. Any other number is allowed too, so a custom control can pick a type of its own.
- `nv_form@parent`: A handle to the parent `nv_form` class.

## Remarks:
You cannot directly use this class. Instead, you can make your own custom control.

Every control created here registers the `default_event_handler` of its parent form on its own `event` dispatcher, so a custom control gets that for free as long as it calls `super`.
