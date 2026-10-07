# Information-object model (draft for review)

**Status:** draft, 2026-10-07. Not implemented. Owner review required.

## Goal

Browsing, editing and the agent work on the same information. The user does
not copy content between applications. A web page, a file, a note and an agent
result are all objects that the user can open, edit, reference and transform.

## Core terms

| Term | Meaning |
| --- | --- |
| Object | A unit of information with a stable ID. |
| Source | Where the object content comes from: `web`, `file`, `note`, `agent`. |
| Revision | An immutable snapshot of object content. Each change makes a new revision. |
| Anchor | A stable reference to a part of an object (text range, DOM node, line range). |
| Link | A typed relation between two objects or anchors. |
| View | A way to show an object: browse view, edit view, agent view. |
| Change | A proposed or applied edit to an object. Every change has an actor. |

## Object

```
Object {
  id: ObjectId            // stable, local
  source: web | file | note | agent
  origin: URL | path | null
  title: string
  media_type: string      // text/html, text/markdown, text/x-rust, ...
  head: RevisionId        // current revision
  created_by: Actor       // user | agent:<id>
}
```

Rules:
1. An object exists once. Views do not copy it.
2. A web page becomes an object when the user or the agent acts on it
   (select, annotate, clip, edit). Ordinary browsing does not create objects.
3. A file object follows the file on disk. The file stays the source of truth.

## Anchor

An anchor must survive small content changes.

```
Anchor {
  object: ObjectId
  revision: RevisionId    // where the anchor was created
  selector: TextQuote | TextPosition | DomPath | LineRange
}
```

Use the W3C Web Annotation selector style. Store a text quote with prefix and
suffix as a fallback, so the anchor can re-attach after the page changes.

## Link

```
Link { from: ObjectId|Anchor, to: ObjectId|Anchor,
       kind: derived_from | references | annotates | replaces }
```

Example: the user clips a paragraph from a web page into a note. The note gets
a `derived_from` link to an anchor on the web object.

## Change and actor

```
Change {
  id, object, base: RevisionId,
  actor: user | agent:<id>,
  state: proposed | applied | rejected | reverted,
  patch: TextEdit[] | DomEdit[]
}
```

Rules:
1. The agent can only create `proposed` changes. The user applies them.
   (A later permission level can allow auto-apply for chosen objects.)
2. Every applied change can be reverted.
3. The change log shows who changed what and when.

This reuses the preview → Apply / Reject → restore pattern from the
customization demo.

## Ownership

| Part | Owner |
| --- | --- |
| Object store, revisions, anchors, links, change log | `core` (small, trusted) |
| Web capture (DOM → object, anchor resolve) | browser service over the embedder |
| File sync | editor service |
| Agent reads and proposals | built-in agent over internal Mojo; external agent over MCP; both with granted permissions |

Storage for version 1 (decided): one local SQLite database. Files on disk remain
the source of truth. No sync, no cloud.

## Minimal browse-and-edit loop (milestone fit)

1. The user selects text on a web page.
2. Pliant creates a web object and an anchor.
3. The user sends the selection to a note or a file in the editor. A
   `derived_from` link is stored.
4. The user clicks the link in the editor. The browser opens the page and
   highlights the anchor.
5. The agent can propose a change to the note (for example, a summary). The
   user applies or rejects it.

## Open points for review

1. Should ordinary browsing history also become objects, or only acted-on pages?
2. Does a file object store its own revisions, or rely on git/disk only?
3. Is step 5 (agent proposal) in the first milestone, or later?
