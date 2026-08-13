# nv_form_event
The base class of everything an `nv_form_event_dispatcher` passes to your handlers.

`nv_form_event(nv_form_control@ ctrl, int type);`

## Arguments:
- `nv_form_control@ ctrl`: The control the event happened on.
- `int type`: What happened, see the event types enum. Any other value is also accepted, for example to make your own custom events.
