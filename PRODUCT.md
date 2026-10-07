# Product

<!-- impeccable:product-schema 1 -->

## Platform

adaptive

Desktop: macOS first, with Linux and Windows as later implementation targets. Mobile is deferred. This is not a website. Electron is not the browser engine. The completed customization demo uses native AppKit UI; the editor version 1 reuses the VS Code core, so editor UI is web-based. How the editor is hosted is open (see [ADR 0002](docs/decisions/0002-editor-browser-agent-scope.md)).

## Stack

Chromium Content through the existing Pliant-owned embedder. The embedder exposes a Rust API over a native bridge. The user delegated remaining engineering choices to Hermes and Copilot, subject to the documented requirements and no unapproved installation. The first native renderer may use existing macOS facilities; that does not select a permanent cross-platform UI toolkit.

Confirmed for the new scope: a separate agent process that registers with the platform; editor version 1 on the VS Code core; a long-term independent editor with good VS Code compatibility. Application size of approximately 0.8–1.2 GB is acceptable. Recommended, not decided: run the VS Code workbench on Pliant's own Chromium instead of a second Electron runtime; protocol-level compatibility (LSP, DAP, themes, keybindings) with best-effort extension API support; one shared information-object model across browse, edit, and agent views; agent permissions, observability, and reversibility from the first design.

## Users and purpose

Pliant combines an editor, a browser, and an agent in one application (scope change 2026-10-07, [ADR 0002](docs/decisions/0002-editor-browser-agent-scope.md)). Browsing and editing are the two main information activities. Agents let a user move freely between them on the same information. Each user should get the most efficient and comfortable browsing and editing experience, and their needs should grow inside one application without switches between applications.

**Delivered history:** the first demo proved real browsing with replaceable interface composition and one bounded behavior customization. A user defines a personal browser layout independently, quickly, and safely.

## Operating context (completed customization demo)

Users edit a local definition directly or with their existing coding tools, preview the result, apply or reject it, and recover a usable default. No browser-native agent service is needed for this milestone. The first demo uses disposable browsing data and controlled local pages for verification.

## Constraints of the customization demo

These constraints governed the completed demo. The "no agent" constraint is superseded as product scope by ADR 0002; the others remain valid.

- Preserve real Chromium navigation, rendering, lifecycle and sandboxing.
- Custom definitions use declared capabilities; no arbitrary host code or hidden privileged commands.
- A meaningful customization change must not rebuild Chromium.
- Two contrasting native layouts must use the same runtime and contracts. A third independently authored definition must work without runtime edits.
- Preview, application, rejection and recovery need behavioral tests and native E2E evidence.
- Keep recovery controls outside user-defined layout authority.
- Do not implement model services, agent collaboration, marketplace, production credential providers or a universal plugin framework.
- Parallel workers use independent worktrees; never share one checkout between writers.

## Confirmed product principles

Editing and browsing as one experience, with the agent as a participant. Customization flexibility with safety guards. Stable mechanisms with replaceable policies and presentation. Official examples receive no private shortcuts. A smaller working vertical slice is better than a broad unverified framework.

## Evidence and open choices

The native embedder and customization demo build on macOS arm64; the full native acceptance checklist in `apps/browser/README.md` has not been recorded as passing. The UI vocabulary and host integration seam must be verified through the demo. No performance, production-security or cross-platform completion claims have been established. No editor, agent process, or shared information-object model is implemented.

Open: the next milestone (a minimal browse-and-edit loop, or the customizable browser first); editor hosting; shell UI technology; the VS Code extension scope; the information-object model; the agent transport and permission model.

## Working visual direction

For this proof, use restrained, familiar native controls and readable system typography. Workspace and classic layouts are contrasting reference organizations, not marketing designs. This is an implementation recommendation under the user's delegated engineering scope, not a permanent brand decision.
