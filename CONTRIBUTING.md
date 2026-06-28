# Contributing

## Workflow
- **Branch + PR per phase.** Each phase (Phase 1 onward) gets its own branch; all
  that phase's deliverables land there, then one PR is opened, reviewed, and
  merged. Phase 0 (scaffold + on-ramp) landed directly on `main` — allowed for the
  initial scaffold only.
- **Branch naming:** `phase-N/<short-slug>` (e.g. `phase-1/se-sa-spine`).
- **Commit often inside the branch** — one logical unit per commit (a page, a fix),
  committed the moment it builds green. The branch accumulates many meaningful
  commits; the PR is the phase.
- **Merge after review.** Keep the per-deliverable commits in history (merge
  commit or rebase) so the frequent-commit trail survives — don't squash a whole
  phase into one commit.
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
