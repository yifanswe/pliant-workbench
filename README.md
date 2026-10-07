# Pliant

**One application for editing, browsing, and working with your agent.**

[Design philosophy](DESIGN_PHILOSOPHY.md) · [Implementation plan](IMPLEMENTATION_PLAN.md) · [Module map](MODULES.md) · [Discuss an idea](https://github.com/yifanswe/pliant-browser/issues)

![Pliant: one foundation, your browser on every device. Concept illustration.](assets/hero.png)

Pliant is a new kind of application: an **editor, a browser, and an agent** in one. Browsing and editing are the two most important things people do with information. Today they live in separate applications, and agent chat lives in a third. Pliant uses AI agents to let each user move freely between browsing and editing the same information, so that one person's needs grow inside one application. See [ADR 0002](docs/decisions/0002-editor-browser-agent-scope.md).

The foundation stays customizable: users and their AI can replace the **entire interface and behavior** without forking the foundation. We also plan **ready-to-use defaults** built through the same public interfaces available to everyone.

**Confirmed structure:** Chromium is the main base, through the existing Pliant-owned embedder. The agent runs as a separate process that registers with the platform. The editor version 1 reuses the VS Code core; the long-term goal is an independent, lighter editor with good VS Code compatibility. None of the editor or agent work is implemented yet.

The repository includes a working macOS arm64 vertical slice: a Pliant-owned
Chromium Content embedder, its Rust trusted-host API, an independent manual API
test app, a bounded JSON UI-definition crate, two distinct definitions, and a
native customization-demo browser. Chromium source, dependencies, and build
outputs remain in a separately provisioned workspace at the pinned revision.

The editor and agent parts do not exist yet. This is also not yet a complete or cross-platform browser platform. Core service
contracts, plugin isolation, recovery, broader engine capabilities, Linux, and
Windows remain planned work; see the [implemented module map](MODULES.md).

## Customization with safety guards

**No Chrome/Firefox extension compatibility by design.** (VS Code extension support for the editor is a separate open question.) Users customize Pliant through its own plugins and declarative layouts, written directly or with their local coding agent.

Make an Arc-style workspace, a traditional tab bar, or your own desktop layout. Replace account-routing policies, credential providers, and session workflows through plugin contracts. Personal choices should not need an upstream PR.

The core should enforce safety boundaries while users change their experience. Infrastructure upgrades should remain possible **with or without AI**, independent of personal customizations.

## What we plan to provide

| Component | Purpose |
| --- | --- |
| **Editor** | Version 1 reuses the VS Code core; later, an independent editor with protocol-level VS Code compatibility (planned). |
| **Agent process** | A separate process that registers with the platform and uses granted services, with permissions, observability, and undo (planned). |
| **Web-engine abstraction** | Stable browser capabilities over a Pliant-owned Chromium Content embedder. |
| **Profile and data management** | Isolated accounts, cookies, passwords, permissions, and persistent data. |
| **Plugin runtime** | Extensible services and behavior with permissions and failure isolation. |
| **Declarative UI engine** | A concise DSL for complete interfaces and platform-specific desktop layouts. |
| **Tests and developer tools** | Comprehensive validation, isolated previews, and diagnostics for users and their AI. |
| **Upgrades and recovery** | Versioned contracts, migrations, and safe recovery without relying on AI. |

## Help shape Pliant

The engine direction is **our own embedding layer over Chromium's Content API and selected components**, targeting **Linux, macOS, and Windows**. We reuse Chromium's web infrastructure, not its complete browser application, CEF, or Electron as the engine. Mobile is deferred. DSL syntax, shell UI technology, editor hosting, agent transport, and plugin execution remain open decisions. The next milestone is also open: a minimal browse-and-edit loop, or the customizable browser first.

Bring an editing or browsing experience you want to build. The useful question is **which capabilities should the platform guarantee, and which decisions should users control?**

Read the [design philosophy](DESIGN_PHILOSOPHY.md) for the architecture, safety boundaries, and proposed acceptance criteria.

---

Concept by [Yifan Li](https://github.com/yifanswe).
