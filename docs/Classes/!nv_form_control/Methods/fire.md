# fire
Triggers the main action.

`void fire();`

## Remarks:
By default, this method executes the callback of the control. You can define this method in order to change the behavior of action. For example, a button uses this method when the user presses the Enter or the Spacebar key.

When defining this method, unless you recall the `nv_form_control::fire();` statement, you should call the `on_fire` method.

These methods are separated so that you can modify only the methods you need. For example if you make a child class of the button control, you might want to modify the `on_fire` method, but not the `fire` method.
