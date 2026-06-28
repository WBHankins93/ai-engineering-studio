# Contributing

## Workflow
- **PR per deliverable.** A **lab is always its own branch + PR.** A signature
  artifact (decision frame, POC playbook, visual, ADR) is its own PR too, unless a
  few are small and tightly related — then they may share one PR (as the Phase 1
  spine did). "Phase" is a roadmap label, **not** a PR unit.
- **Branch naming:** `phase-N/<deliverable-slug>` (e.g. `phase-2/lab-01-first-llm-app`,
  `phase-2/apps-agents-lessons`). Phase 0 (scaffold) landed directly on `main` —
  the only direct-to-`main` exception.
- **Commit often inside the branch** — one logical unit per commit (a page, a fix),
  committed the moment it builds green. The branch accumulates meaningful commits;
  the PR is the deliverable.
- **Merge after review.** Keep the per-commit trail in history (merge commit or
  rebase) — don't squash a deliverable into one commit.
- **Dead-link CI is the gate.** `npm run docs:build` compiles every page and
  fails on broken internal links (`ignoreDeadLinks: false`). Run it locally
  before opening a PR, and keep every commit green. It's a required check on `main`.

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
