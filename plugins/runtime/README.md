# Plugin runtime

**Responsibility:** eventually enforce plugin grants, isolation, lifecycle,
resource limits, cancellation, conflicts, and service registration.

**Boundary:** plugins use explicit service contracts and cannot patch core,
access platform or Chromium internals, or gain authority from a returned value.
Chrome and Firefox extension compatibility is out of scope. VS Code extensions
are out of scope for editor version 1
([ADR 0002](../../docs/decisions/0002-editor-browser-agent-scope.md)). The execution
technology and protocol are not designed yet.

**Status:** scaffold only; no runtime or ABI exists. See the
[module map](../../MODULES.md).
