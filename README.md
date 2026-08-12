# NV Form
`nv_form` is a new, redesigned auditory form written in and for [NVGT](https://nvgt.dev) scripting game engine. This is written to make audio form more modernized, now that the old form in NVGT is legacy.

This is a modified version of [NV Form](https://github.com/ivansoto0/nv_form) originally written by Ivan Soto, as that repository is not being actively maintained.

Original copyright notice:
`Copyright (c) 2025 Ivan Soto`

**Warning**! This version is no longer compatible with the old form from Ivan, such as enum value names are now uppercase as the API standards.

You can run [test.nvgt](test.nvgt) to get to know all the features. Usually every feature gets added to it as soon as implemented. For more tests, view the [test directory](test).

## Notes
- This module is a new and redesigned module, but some parts may have copied from the original auditory form.
- This module is also a modified version of the original NV Form created by Ivan Soto, and is no longer compatible with the origin.
- Controls, functions, events, and shortcut handlers, are now completely different from the ones that you use in the legacy modules. Therefore, if you cannot find a specific function, enum value, or constant; you cannot use a functionality; or functionality is different, it may not actually be a bug.
- Shortcuts in the caption (label) with an ampersand (`&`) is no longer supported. Your form can now utilize `Ctrl`, `Shift`, and `Alt` all together rather than a limited `Alt` key alone in the legacy auditory form, as well as multitap shortcuts. Tip: If you want to use the old behavior, the only possible action is to create custom instance of `nv_form` as a child class, and modify and extend the `add_control` method.
- Functionalities should be backwards compatible with the legacy form or even the origin NV Form, but please note that this is not the main intent of this module. If we believe that if a specific functionality is deemed unworthy, or having performance issues, it may be removed, modified, or replaced with an equivalent functionality.
- NV Form module is also available to install right directly into your NVGT's installed directory for global use with [NVGTPM Package Manager](https://github.com/harrymkt/nvgtpm). Install using the following command: `nvgtpm install form`.

## Contribution
We accept contributions as long as the established [contributions guidelines](.github/CONTRIBUTING.md) are followed.

## Documentation Status
[Documentation](docs) for the form has been written, but this does not mean that it is complete. We appreciate any contributions regarding the documentation.

## Features
NV Form module advertises the following features:

- Ease of Use: NV Form is easy to integrate, use, and make changes.
- Form Controls: NV Form supports many controls out of the box, including buttons, check boxes, text fields, lists, sliders, progress bars, switches, context menus, suggestions, and more. Please see a list of [available control types](docs/Enums/nv_form_control_type.md) in the documentation.
- Custom Controls: Add to or modify any control as you wish if it does not meet your requirements. Add custom controls by directly making child classes of specific controls you want, as well as extend and modify existing controls by directly making a child class of them. See [nv_form_control Documentation](docs/Classes/nv_form_control).
- Custom Form: Add to or otherwise modify the NV Form module by making a child class of `nv_form` to integrate your changes, custom logic, custom verifications and how controls are added, without ever directly touching the main NV Form module which would otherwise be painful especially if you have to copy and paste , and update all the time when the main NV Form module is updated.
- Events: Make your projects more integrated by using events dispatched by the form without having to modify controls, i.e. [adding keyboard / navigation sounds](test/input_event.nvgt).
- Extensive Shortcuts: Utilize advanced shortcut combinations, key modifiers, multitap keys, all from just one shortcut manager.
- Organized Forms: Make your project more clean and categorized by utilizing [tab controls](test/tab.nvgt), known as child forms.
