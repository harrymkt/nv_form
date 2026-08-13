# nv_form_treeview_event
The event a treeview fires when the focused item changes. Derives from `nv_form_event`.

`nv_form_treeview_event(nv_form_treeview@ ctrl);`

## Arguments:
- `nv_form_treeview@ ctrl`: The treeview the item changed on.

## Remarks:
Its `type` is always `NV_FORM_EVENT_TREEVIEW`.

The treeview fires this when the user moves with the arrow keys, jumps with home or end, lands on an item by typing its first letters, or finds one through the search dialog. It does not fire when you move the cursor by assigning to `list_position` directly, use `set_pos` with `fire_event` set to true for that.
