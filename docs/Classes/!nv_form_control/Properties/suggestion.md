# suggestion
The autocomplete manager attached to this control, or null when it has none.

`nv_form_suggestion_manager@ suggestion;`

## Remarks:
Only useful on `nv_form_input` and the controls derived from it, because it is the input control that tells the manager to refresh whenever its text changes, whether the user typed, deleted, or pasted.
