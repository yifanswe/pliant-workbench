# Architecture decisions

**Responsibility:** record accepted decisions, evidence, trade-offs, and
rejected alternatives. This directory does not decide through placeholder code.

- [ADR 0001: own the Chromium embedding layer](0001-own-chromium-embedding.md).
  Pliant owns its embedder over Chromium Content, not CEF. Acceptance selects
  the architecture; it does not prove a cross-platform implementation.
- [ADR 0002: editor, browser, and agent](0002-editor-browser-agent-scope.md).
  Product scope, owner decisions, superseded statements, and the only list of
  open product questions. It keeps ADR 0001.

See the [module map](../../MODULES.md).
