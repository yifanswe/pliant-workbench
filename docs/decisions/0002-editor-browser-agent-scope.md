# ADR 0002: Expand scope to editor, browser, and agent

**Status:** accepted, 2026-10-07. It records product scope and owner decisions.
It does not establish an implementation. No editor, agent, MCP/A2A interface,
or information-object model exists in this repository yet.

## Decision

Pliant is no longer only a customizable browser. Pliant is one application
that combines an **editor**, a **browser**, and an **agent**.

Browsing and editing are the two most important activities that people do with
information. Today, browsers are for browsing, editors are for editing, and
agent applications are for chat with an agent. The categories overlap: users
edit in browsers and show web pages in editors. But each product still
starts from one activity and adds the other as a secondary feature.

AI agents make it possible to move freely between browsing and editing the
same information. Pliant's goal is the most efficient and most comfortable
browsing and editing experience for each user. One person's needs should grow
inside one application, without constant switches between applications.

## Confirmed structure

The four modules (UI customization DSL, browser layer, editor layer, agent
layer) are described in [modules-vision.md](../design/modules-vision.md).

| Part | Decision |
| --- | --- |
| Browser base | The Pliant-owned embedder over Chromium Content ([ADR 0001](0001-own-chromium-embedding.md)). |
| Agents | A built-in agent, internal only, on Mojo IPC. It is never exposed outside Pliant. Pliant exposes its capabilities to the user's external agent through MCP (external agent → Pliant). The built-in agent reaches the external agent through A2A, one way (built-in → external), to reuse its memory without importing it. MCP ships first; A2A follows. The built-in agent works without an external agent. |
| Editor, version 1 | Reuse the VS Code core. VS Code extensions are out of scope. |
| Editor, long term | An own, lighter editor with VS Code compatibility. |
| Shell UI | Native, AppKit-centered. No Electron or other extra UI engine. AI writes the user's layout, so correctness, performance, and stability come first. The DSL layer translates definitions to native views and refreshes only the changed parts. |
| Data | One local SQLite database for information objects. Files on disk remain the source of truth. |
| Next milestone | A minimal browse + edit loop. |
| Platforms | macOS first. Linux and Windows later. Mobile deferred. |
| Application size | About 0.8–1.2 GB is acceptable. Size is not an early priority. |
| License | Apache-2.0. The project is not commercial now. |

## Recommendations (not decisions)

These come from the assistant's review. The owner has not accepted them.

1. **One Chromium.** If the VS Code workbench needs a web runtime, run it on
   Pliant's own Chromium. Do not bundle a second Chromium.
2. **Compatibility levels.** Long-term protocol-level compatibility: Language
   Server Protocol (LSP), Debug Adapter Protocol (DAP), themes, and keybindings.
3. **Shared information objects.** One model across the browse, edit, and agent
   areas. Without it, Pliant is three applications in one window. Draft:
   [information-objects.md](../design/information-objects.md).
4. **Agent controls from the first design.** Permissions, observability, and
   reversibility from the start.

## What remains valid

- The Pliant-owned Chromium Content embedder. Pliant does not use CEF or
  Electron as the browser engine.
- The kernel-versus-application principle: a small trusted core with stable
  interfaces; replaceable behavior, services, and UI.
- Declarative UI customization with preview, Apply, Reject, and restore.
- No Chrome/Firefox extension compatibility.
- The completed native customization demo. It is delivered history and a
  working base, not cancelled work.
- Storage layout: source on the main disk; Chromium source, dependencies, and
  build outputs in a separately provisioned workspace selected through
  environment variables such as `PLIANT_CHROMIUM_ROOT`.

## What this ADR supersedes

| Earlier statement | New status |
| --- | --- |
| Pliant is infrastructure to build a personal **browser**. | Superseded. Pliant is an editor, a browser, and an agent. Browser customization is one part. |
| The agent is a future direction; the first milestone has no agent. | Superseded. The built-in agent is part of the product. The "no agent" rule applied only to the completed customization demo. |
| An agent process registers with the platform over Mojo as its external contract. | Superseded. Mojo is internal IPC only. External agents use MCP. The built-in agent uses A2A outward, one way. |
| Desktop targets are Linux, macOS, and Windows now. | Superseded. macOS first; Linux and Windows later. |
| The next milestone is open. | Decided: a minimal browse + edit loop. |
| "Lightweight operation" as a product goal. | Changed. Size is not an early priority. Measure startup, memory, and idle activity before setting budgets. |

## Open questions

This is the only list of open product questions. Other documents link here.

1. Editor version 1 hosting.
2. The AppKit/SwiftUI split for the native shell renderer.
3. Owner review of the [information-object draft](../design/information-objects.md),
   including its listed open points.

Engineering details (DSL syntax, plugin runtime, code-execution sandbox, MCP
permission scopes) are designed with their features; they are not product
questions.

## Consequences

- Where any document conflicts with this ADR, this ADR takes precedence.
- New directories (for example an editor or agent module) are added only when a
  real feature needs them.
- Claims about the editor or agent need runtime evidence, the same as claims
  about the embedder.
