# default_event_handler
The event handler that every control created on this form gets registered automatically.

`nv_form_event_handler@ default_event_handler;`

## Remarks:
Set this before adding your controls. Each control registers it on its own `event` dispatcher as it is constructed, so controls added earlier are not affected.

It is registered through `nv_form_event_dispatcher::add`, which means a control can have both this handler and its own, and both get called.

The form picks up its starting value from the global `default_nv_form_event_handler` whenever it is reset, so setting that global once gives every form in your program the same default. Assigning null here leaves new controls without a default handler.

## Example:
```nvgt
nv_form f;
@f.default_event_handler = ui_sounds;
f.create_window("Settings");
void ui_sounds(nv_form_event@ event) {
	if (event.type == nv_form_event_focus_gained) play_focus_sound();
}
```
