# Product

<!-- impeccable:product-schema 1 -->

## Platform

adaptive

Native desktop: macOS first demo, with Linux and Windows as later implementation targets. Mobile is deferred. This is not a website or an Electron application.

## Stack

Chromium Content through the existing Pliant-owned embedder. The embedder exposes a Rust API over a native bridge. The user delegated remaining engineering choices to Hermes and Copilot, subject to the documented requirements and no unapproved installation. The first native renderer may use existing macOS facilities; that does not select a permanent cross-platform UI toolkit.

## Users and purpose

A user wants to define a personal browser independently, quickly, and safely. The first demo proves real browsing with replaceable interface composition and one bounded behavior customization, not only themes or preset selection.

## Operating context

Users edit a local definition directly or with their existing coding tools, preview the result, apply or reject it, and recover a usable default. No browser-native agent service is needed for this milestone. The first demo uses disposable browsing data and controlled local pages for verification.

## Constraints

- Preserve real Chromium navigation, rendering, lifecycle and sandboxing.
- Custom definitions use declared capabilities; no arbitrary host code or hidden privileged commands.
- A meaningful customization change must not rebuild Chromium.
- Two contrasting native layouts must use the same runtime and contracts. A third independently authored definition must work without runtime edits.
- Preview, application, rejection and recovery need behavioral tests and native E2E evidence.
- Keep recovery controls outside user-defined layout authority.
- Do not implement model services, agent collaboration, marketplace, production credential providers or a universal plugin framework.
- Parallel workers use independent worktrees; never share one checkout between writers.

## Confirmed product principles

Customization flexibility with safety guards. Stable mechanisms with replaceable policies and presentation. Official examples receive no private shortcuts. A smaller working vertical slice is better than a broad unverified framework.

## Evidence and open choices

The native embedder and customization demo build on macOS arm64; the full native acceptance checklist in `apps/browser/README.md` has not been recorded as passing. The UI vocabulary and host integration seam must be verified through the demo. No performance, production-security or cross-platform completion claims have been established.

## Working visual direction

For this proof, use restrained, familiar native controls and readable system typography. Workspace and classic layouts are contrasting reference organizations, not marketing designs. This is an implementation recommendation under the user's delegated engineering scope, not a permanent brand decision.
