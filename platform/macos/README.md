# macOS platform adapter

**Responsibility:** provide macOS native-window, input, accessibility,
credential-facility, packaging, signing, and update integration selected by
public platform interfaces.

**Boundary:** it hosts platform mechanisms, not browser UI policy or private
shortcuts for presets. The shell UI is native and AppKit-centered; the AppKit/SwiftUI split is an open
question in [ADR 0002](../../docs/decisions/0002-editor-browser-agent-scope.md#open-questions).
Minimum OS versions are not chosen yet. macOS is the first platform.

**Status:** scaffold only. See the [module map](../../MODULES.md).
