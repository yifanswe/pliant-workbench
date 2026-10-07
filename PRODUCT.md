# Product

<!-- impeccable:product-schema 1 -->

## Platform

adaptive

Desktop: macOS first; Linux and Windows later. Mobile is deferred. This is not a website. The shell UI is native and AppKit-centered, with no Electron or other extra UI engine. Editor version 1 reuses the VS Code core; its hosting is open ([ADR 0002](docs/decisions/0002-editor-browser-agent-scope.md)).

## Stack

Chromium Content through the Pliant-owned embedder, with a Rust API over a native bridge. Built-in agent on internal Mojo IPC; external agents through MCP; built-in → external agent through A2A, one way. Information objects in a local SQLite database; files on disk remain the source of truth. The owner delegated remaining engineering choices to the assistant, within the documented requirements and with no unapproved installation.

## Users and purpose

Pliant is a new application species: an editor, a browser, and an agent in one ([ADR 0002](docs/decisions/0002-editor-browser-agent-scope.md)). AI agents give unlimited malleability between browsing and editing information. One person's needs grow inside one application. Users tell an AI the workflow they want; Pliant supplies the APIs, so users never build the data layer, IPC, or stability. The four modules are in [modules-vision.md](docs/design/modules-vision.md).

**Next milestone:** a minimal browse + edit loop.

**Delivered history:** the first demo proved real browsing with replaceable interface composition and one bounded behavior customization, with preview → Apply/Reject → restore.

## Operating context (completed customization demo)

Users edit a local definition directly or with their existing coding tools, preview the result, apply or reject it, and recover a usable default. The demo had no agent; that limit applied to the demo only. The first demo uses disposable browsing data and controlled local pages for verification.

## Constraints of the customization demo

These constraints governed the completed demo. Except for the demo-only exclusion of agent work, they remain valid.

- Preserve real Chromium navigation, rendering, lifecycle and sandboxing.
- Custom definitions use declared capabilities; no arbitrary host code or hidden privileged commands.
- A meaningful customization change must not rebuild Chromium.
- Two contrasting native layouts must use the same runtime and contracts. A third independently authored definition must work without runtime edits.
- Preview, application, rejection and recovery need behavioral tests and native E2E evidence.
- Keep recovery controls outside user-defined layout authority.
- (Demo only) Do not implement model services, agent collaboration, marketplace, production credential providers or a universal plugin framework.
- Parallel workers use independent worktrees; never share one checkout between writers.

## Confirmed product principles

Editing and browsing as one experience, with the agent as a proactive participant, not only a chat partner. Customization flexibility with safety guards. Stable mechanisms with replaceable policies and presentation. Official examples receive no private shortcuts. A smaller working vertical slice is better than a broad unverified framework.

## Evidence and open choices

The native embedder and customization demo build on macOS arm64; the full native acceptance checklist in `apps/browser/README.md` has not been recorded as passing. No performance, production-security or cross-platform claims are established. No editor, agent, MCP/A2A interface, or information-object model is implemented.

Open questions are listed only in [ADR 0002](docs/decisions/0002-editor-browser-agent-scope.md#open-questions).

## Working visual direction

For this proof, use restrained, familiar native controls and readable system typography. Workspace and classic layouts are contrasting reference organizations, not marketing designs. This is an implementation recommendation under the user's delegated engineering scope, not a permanent brand decision.
