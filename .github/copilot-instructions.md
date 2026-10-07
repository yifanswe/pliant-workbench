# Pliant project guidelines

## Scope

- Pliant is an editor, a browser, and an agent in one application. Source of truth: `docs/decisions/0002-editor-browser-agent-scope.md` and `docs/design/modules-vision.md`.
- Four modules: UI customization DSL (browse, edit, and agent areas); browser layer (embedder capabilities exposed as Pliant APIs); editor layer (where the user steers agents); agent layer.
- Agent model: a built-in agent on internal Mojo IPC, never exposed externally. External agents reach Pliant through MCP. The built-in agent reaches the external agent through A2A, one way. MCP first, A2A later. Do not describe Mojo as an external agent contract.
- Keep the Pliant-owned Chromium Content embedder as the browser engine. Do not substitute CEF or Electron. The shell UI is AppKit plus Pliant's own DSL (no SwiftUI); do not add Electron or another UI engine.
- macOS first; Linux and Windows later. Next milestone: a minimal browse + edit loop.
- Separate confirmed decisions, recommendations, and open questions. Open questions live only in ADR 0002. Do not describe editor or agent work as implemented without runtime evidence.
- Committed files must not contain absolute personal paths or secrets. Use environment variables such as `PLIANT_CHROMIUM_ROOT`.

## Meaningful tests only

- Do not add tests or custom validators just for directory layouts, documentation links, source pins, Git checkouts, or other development scaffolding unless explicitly requested.
- Add tests when they protect implemented browser behavior, authorization/isolation, lifecycle, native integration, data integrity, upgrades, or a concrete regression.
- Unit/model tests and synthetic browser fixtures are useful when they exercise real product logic or failure cases. Do not mistake tests of bookkeeping or mocks alone for browser implementation or integration evidence.
- Prioritize product implementation over new validation infrastructure. If prerequisites block implementation, report the blocker rather than substituting test-only work.
