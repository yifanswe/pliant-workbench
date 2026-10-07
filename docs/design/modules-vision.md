# Pliant modules: owner vision (2026-10-07)

**Status:** owner direction, recorded for design. Not implemented. This is the
source of truth for the four-module structure and the agent model.

Pliant has four modules. The core principle: Pliant is designed from the start
to support user customization. Users do not build the data layer, IPC or
stability themselves. A user tells an AI "I want this workflow", and the AI
builds it on Pliant APIs.

## 1. UI customization interface (DSL)

Users define the UI with a DSL. Customizable areas: the browse area, the edit
area and the agent area.

**Reference example (keep for future API design):**
1. The user selects text on a web page and right-clicks.
2. Pliant opens an agent area, or opens an edit area on the right and copies
   the selected text into it.
3. This edit area is a scratch pad. The user writes questions freely. The
   agent watches the scratch pad and responds or completes tasks.
4. The scratch pad can contain images, voice and other media.

The example defines what "UI customization" means: users compose workflows,
not only change appearance.

## 2. Browser layer

Implement the browser capability modules in the Pliant-owned embedder over
Chromium Content (see [engine capabilities](../contracts/engine-capabilities.md)). Expose them as Pliant APIs. A local, authorized
agent calls these APIs to browse together with the user and to connect
browsing with the editor, the custom UI and the agent.

### Communication through the browser layer

**Decision (2026-10-07):** Pliant does not build its own chat or meeting
service. People communication (Slack, Discord, Zoom, Google Meet and similar)
runs as web apps in the browse area.

- Messages and meeting content become information objects (`message` source)
  through browser-layer APIs or the service's own API/MCP.
- The agent can read messages and draft replies. A message to another person
  is sent only after the user confirms it.
- Real-time meetings need browser capabilities: camera, microphone, screen
  share, notifications and background audio. These come from the embedder.

## 3. Editor layer (edit and run)

The editor is the main place where the user steers agent work. Chat-only
collaboration ends here. The user can still give direct instructions, but the
agent should watch what the user does and help at the right time.

Trigger sources:
- Hard-coded triggers in the UI layer.
- The user's activity stream, for fast responses.

Examples:
- In a shared scratch pad, the user only keeps typing. No @mention or button.
  The scratch pad is owned by both the user and the agent.
- The user writes "you can refer to this website (to be found)". The agent
  finds the page from context and history, replaces the placeholder, and shows
  a small control to revert or pick another option.
- A terminal is part of the editor layer. The user and the agent share it:
  the user sees every command the agent runs and can step in. Terminal output
  can become an information object (for example, select an error and send it
  to a scratch pad). Agent command permissions are designed with the
  code-execution sandbox.
- The agent gets a code execution environment. The user takes in information,
  reworks it, and takes it in again, on one screen.

## 4. Agent layer

**Decision (2026-10-07):** Pliant has a built-in agent. The user's existing
external agent is reused, not copied. Its memory is never imported.

Connection directions are one-way:

| Channel | Direction | Purpose |
| --- | --- | --- |
| MCP | external agent → Pliant | Pliant exposes its capabilities (browse, edit, objects) as an MCP server. |
| A2A | built-in agent → external agent | The built-in agent asks the user's agent for memory and long-term context. |
| none | — | The built-in agent is not exposed outside Pliant. |

Roles:
- **Built-in agent:** local, fast, frequent work. It watches user activity,
  decides when to help, fills placeholders, writes in shared scratch pads and
  proposes Changes.
- **External agent:** owns the user's memory and identity context. It answers
  A2A requests with only what the request needs. It may also act in Pliant
  through MCP.
- Without an external agent, the built-in agent still works, without personal
  memory.
- Agents express input requests and uncertain edits through the editor
  (proposed Changes), not plain text or simple pickers.

## Design notes (assistant, for review)

1. **MCP and A2A outside, Mojo inside.** Mojo stays the IPC between Pliant
   processes, including the built-in agent process. It is never an external
   contract ([ADR 0002](../decisions/0002-editor-browser-agent-scope.md)).
   A2A adoption is still early; MCP ships first and A2A follows.
2. **Push, not only pull.** "The agent watches the user" needs events from
   Pliant to the agent. MCP has resource subscriptions and notifications, but
   not every agent runtime supports them. Pliant needs an activity event
   stream with clear permission scopes.
3. **Shared ownership = the Change model.** The co-owned scratch pad and the
   "(to be found)" replacement use actor-tagged, revertible Changes from
   [information-objects.md](information-objects.md). The placeholder can be a
   "hole" anchor that the agent fills with a proposed Change.
4. **Code execution needs a sandbox.** The sandbox technology is not chosen.
   Define its file, network and process limits before the first version.
