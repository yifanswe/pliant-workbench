# Plugin runtime

**Responsibility:** eventually enforce plugin grants, isolation, lifecycle,
resource limits, cancellation, conflicts, and service registration.

**Boundary:** plugins use explicit service contracts and cannot patch core,
access platform or Chromium internals, or gain authority from a returned value.
Chrome and Firefox extension compatibility is out of scope. VS Code extension
support for the editor is a separate open question
([ADR 0002](../../docs/decisions/0002-editor-browser-agent-scope.md)). The execution
technology and protocol remain undecided.

**Status:** scaffold only; no runtime or ABI exists. See the
[module map](../../MODULES.md).
