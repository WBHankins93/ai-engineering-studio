# Contributing

## Workflow
- **PR per deliverable** — one lab, lesson, decision frame, talk track, or
  signature artifact per branch. Not one PR per phase.
- **Branch naming:** `phase-N/slug` (e.g. `phase-1/poc-playbook-first`).
- **Squash-merge** to `main`. Your in-branch commits can be frequent and messy;
  only the PR title becomes the permanent `main` commit — so polish PR titles
  (e.g. `Lab 02 · Production RAG`).
- **Dead-link CI is the gate.** `npm run docs:build` compiles every page and
  fails on broken internal links (`ignoreDeadLinks: false`). Run it locally
  before opening a PR. It's a required check on `main`.

## Commits
- Plain, single-author. **No co-authoring or generation trailers** — a
  `commit-msg` hook rejects `Co-Authored-By` / `Generated with`.
- Imperative subject, no trailing period. Body only when the "why" isn't obvious
  from the subject.
- **Commit meaningfully and often.** One logical unit per commit (a page, a fix, a
  config change), committed the moment it builds green. Don't batch a whole phase
  into one commit; don't leave finished work uncommitted. In-branch commits can be
  frequent and granular — squash-merge collapses them into the polished PR title.

## Adding a page
1. Create the markdown file in the right folder (see `product/BUILD-PLAN.md` §6).
2. Add its link to the sidebar/nav in `.vitepress/config.mts` — or the build
   fails on the dead link.
3. Apply the Depth Standard for that folder's tier (`DEPTH-STANDARD.md`).
4. Run `npm run docs:build` until green, then commit.

## Local setup
```
npm ci            # Node 20
npm run docs:dev  # hot-reload preview
npm run docs:build
```

See `AGENTS.md` for the full project source of truth and `product/BUILD-PLAN.md`
for the complete implementation spec.
