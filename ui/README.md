# UI

**Responsibility:** define the declarative UI package boundary, validation,
state bindings, interactions, and native rendering.

**Boundary:** UI code uses public operations and observable state. It cannot
access Chromium, protected profile data, credentials, or core implementation details.
The renderer is native and AppKit-centered; the DSL layer translates definitions
to native views with diff-based partial refresh. DSL syntax is not designed yet.

**Scope:** the DSL covers the browse, edit, and agent areas
([module 1](../docs/design/modules-vision.md#1-ui-customization-interface-dsl)).
Editor version 1 reuses the VS Code core; its hosting is open
([ADR 0002](../docs/decisions/0002-editor-browser-agent-scope.md#open-questions)).

**Status:** [`definition/`](definition/) implements the bounded JSON definition,
validation, preview/apply/reject/reset state machine, and address-open policy
used by the native customization demo. The AppKit renderer remains app-local;
there is no general UI runtime or plugin-facing UI API yet. See the
[module map](../MODULES.md).
