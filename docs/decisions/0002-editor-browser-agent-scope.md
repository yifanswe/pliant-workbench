# ADR 0002: Expand scope to editor, browser, and agent

**Status:** accepted product scope, 2026-10-07. This ADR changes product scope
and records the structural direction. It does not establish an implementation.
No editor, agent process, or shared information-object model exists in this
repository yet.

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

| Part | Direction |
| --- | --- |
| Browser base | Chromium is the main base. The Pliant-owned embedder over Chromium Content ([ADR 0001](0001-own-chromium-embedding.md)) remains the engine boundary. |
| Agent | The agent runs as a separate process. It registers with the platform and gets only the service interfaces that the platform grants. |
| Editor, version 1 | Reuse the VS Code core. |
| Editor, long term | Build an independent editor implementation, because VS Code is too heavy. Keep good VS Code compatibility. |
| Application size | Size is not an early optimization priority. A total size of approximately 0.8–1.2 GB is acceptable. |

## Recommendations (not decisions)

These recommendations come from the assistant's review of the scope. The owner
has not accepted them. Treat them as default proposals that need evidence.

1. **One Chromium.** Run the VS Code workbench on Pliant's own Chromium. Do not
   bundle a second Electron/Chromium runtime for the editor.
2. **Compatibility levels.** Commit to protocol-level compatibility for the
   long term: Language Server Protocol (LSP), Debug Adapter Protocol (DAP),
   themes, and keybindings. Support the VS Code extension API on a
   best-effort, selective basis.
3. **Shared information objects.** Use one information-object model across the
   browse, edit, and agent views. This model is the key differentiator. Without
   it, Pliant is three applications in one window.
4. **Agent controls from the first design.** Design agent permissions,
   observability, and reversibility from the start, not as later hardening.

## What remains valid

- The Pliant-owned Chromium Content embedder. Pliant does not use CEF or
  Electron as the browser engine.
- The kernel-versus-application principle: a small trusted core with stable
  interfaces; replaceable behavior, services, and UI.
- Declarative UI customization with preview, Apply, Reject, and restore.
- No Chrome/Firefox extension compatibility. This ADR does not change that
  non-goal. VS Code extension support is a separate, editor-specific question.
- The completed native customization demo. It is delivered history and a
  working base, not cancelled work.
- Storage layout: source on the main disk; Chromium source, dependencies, and
  build outputs in a separately provisioned workspace selected through
  environment variables such as `PLIANT_CHROMIUM_ROOT`.

## What this ADR supersedes

| Earlier statement | New status |
| --- | --- |
| Pliant is infrastructure to build a personal **browser**. | Superseded. The product is an editor, browser, and agent in one application. Browser customization stays a part of the product. |
| "Native UI, without Electron" for the whole application. | Partly superseded. Electron is still not the browser engine. The editor version 1 reuses the VS Code core, which is web UI. Whether the browser shell stays native, and how the editor is hosted, are open. |
| The agent is a future direction, deferred from the first milestone. | Superseded for product scope. The agent is a confirmed part of the product. Its delivery order is open. |
| Built-in agent and Mojo registration are design ideas only. | Partly superseded. A separate agent process that registers with the platform is confirmed. The transport (Mojo or other), the permission model, and the API are not decided. |
| "Lightweight operation" as a product goal. | Changed. Distribution size is not an early priority. Measure startup, memory, and idle activity before you set budgets. |

## Owner decisions (2026-10-07)

1. **Next milestone:** a minimal browse-and-edit loop.
2. **Editor hosting:** to be decided.
3. **Shell UI:** native. The owner does not want an extra UI engine such as
   Electron. AI writes the user's layout, so the priorities are correctness,
   performance and stability, not human coding speed. The DSL layer translates
   definitions to native views and refreshes only the changed parts. The exact
   AppKit/SwiftUI split is still under review.
4. **VS Code extensions:** out of scope for version 1.
5. **Information-object model:** the assistant drafts a design; the owner
   reviews it. See [information-objects.md](../design/information-objects.md).
6. **Agent model:** Pliant has a built-in agent, internal only, on Mojo IPC.
   Pliant capabilities are exposed to the user's external agent through MCP.
   The built-in agent reaches the external agent through A2A (one-way). The
   external agent's memory is reused, never imported. See
   [modules-vision.md](../design/modules-vision.md).
7. **License:** Apache-2.0. The project is not commercial now.
8. **Platforms:** macOS first. Linux and Windows come later.

## Open questions

1. Editor hosting for version 1 (VS Code workbench on Pliant's Chromium, or
   another option).
2. AppKit vs SwiftUI split for the native shell renderer.
3. Owner review of the information-object model draft.

## Consequences

- Existing documents keep their browser-specific content. Where it conflicts
  with this ADR, this ADR takes precedence.
- New directories (for example an editor or agent module) are added only when a
  real feature needs them.
- Claims about the editor or agent need runtime evidence, the same as claims
  about the embedder.
