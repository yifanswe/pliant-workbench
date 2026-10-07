# Pliant project guidelines

## Scope

- Pliant is one application that combines an editor, a browser, and an agent. See `docs/decisions/0002-editor-browser-agent-scope.md`.
- Keep the Pliant-owned Chromium Content embedder as the browser engine. Do not substitute CEF or Electron for it.
- Separate confirmed decisions, recommendations, and open questions. Do not describe editor or agent work as implemented without runtime evidence.
- Do not choose the next milestone; it is an open owner decision.
- Committed files must not contain absolute personal paths or secrets. Use environment variables such as `PLIANT_CHROMIUM_ROOT`.

## Meaningful tests only

- Do not add tests or custom validators just for directory layouts, documentation links, source pins, Git checkouts, or other development scaffolding unless explicitly requested.
- Add tests when they protect implemented browser behavior, authorization/isolation, lifecycle, native integration, data integrity, upgrades, or a concrete regression.
- Unit/model tests and synthetic browser fixtures are useful when they exercise real product logic or failure cases. Do not mistake tests of bookkeeping or mocks alone for browser implementation or integration evidence.
- Prioritize product implementation over new validation infrastructure. If prerequisites block implementation, report the blocker rather than substituting test-only work.