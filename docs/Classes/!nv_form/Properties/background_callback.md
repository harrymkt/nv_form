# background_callback
Background callback of the form.

`nv_form_callback@background_callback = default_nv_form_callback;`

## Remarks:
By default, newly created forms are fetched from the `default_nv_form_callback` global property.

Background callback is declared as the following:

```nvgt
funcdef bool nv_form_callback(nv_form@f, dictionary@args = null);
```
