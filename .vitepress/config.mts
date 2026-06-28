import { defineConfig } from 'vitepress'

// ---------------------------------------------------------------------------
// Sidebar groups — mirror the repo's SE/SA structure. Each array is one
// collapsible section. Links are root-relative and must resolve, or the build
// fails (ignoreDeadLinks: false below). Add a page here when you add the file.
//
// Phase 0 ships the foundations on-ramp. The Phase 1+ sections below are kept
// here, commented, as the roadmap — uncomment each link as its page is built so
// `main` stays green at every commit.
// ---------------------------------------------------------------------------

const foundations = [
  { text: 'How LLMs Actually Work (no math)', link: '/foundations/how-llms-actually-work' },
  { text: 'The Four-Layer Map', link: '/foundations/the-four-layer-map' },
  { text: 'AI Vocabulary for SAs', link: '/foundations/ai-vocabulary-for-sas' },
  { text: 'LangGraph in 10 Minutes', link: '/foundations/langgraph-how-to' },
]

const standards = [
  { text: 'Depth Standard', link: '/DEPTH-STANDARD' },
  { text: 'Canonical Cast', link: '/CANONICAL-CAST' },
  { text: 'Contributing', link: '/CONTRIBUTING' },
]

// --- Phase 1+ sections (uncomment links as pages are built) ----------------
// const decisionFrames = [
//   { text: 'Managed API vs Self-Host', link: '/decision-frames/managed-vs-self-host' },
// ]
// const pocPlaybooks = [
//   { text: 'Scoping an AI POC', link: '/poc-playbooks/scoping-an-ai-poc' },
// ]
// const talkTracks = [
//   { text: 'Explaining a Hallucination', link: '/talk-tracks/explaining-a-hallucination' },
// ]
// const lessons = [{ text: 'Overview', link: '/lessons/' }]
// const labs = [{ text: 'Overview', link: '/labs/' }]
// const visuals = [{ text: 'The Four-Layer Map', link: '/visuals/four-layer-map' }]
// const decisions = [
//   { text: 'ADR 001 — LangGraph as orchestration standard', link: '/decisions/001-langgraph-orchestration' },
// ]

export default defineConfig({
  title: 'AI Engineering Studio',
  description:
    'The AI engineering ecosystem, made legible — a Solutions Engineer / Architect lens on LLM apps, infrastructure, MLOps, and governance.',
  lang: 'en-US',

  // The gate. A broken internal link fails the build, which fails CI.
  ignoreDeadLinks: false,

  // Served under a repo subpath on GitHub Pages.
  base: '/ai-engineering-studio/',

  // Render ```mermaid fences into <div class="mermaid"> so the client-side
  // renderer in theme/index.ts picks them up. Lets authors fence with
  // ```mermaid (per AGENTS.md) instead of hand-writing the wrapper div.
  markdown: {
    config: (md) => {
      const defaultFence = md.renderer.rules.fence!.bind(md.renderer.rules)
      md.renderer.rules.fence = (tokens, idx, options, env, self) => {
        const token = tokens[idx]
        if (token.info.trim() === 'mermaid') {
          return `<div class="mermaid">${token.content}</div>`
        }
        return defaultFence(tokens, idx, options, env, self)
      }
    },
  },

  themeConfig: {
    nav: [
      { text: 'Start Here', link: '/START-HERE' },
      { text: 'Foundations', link: '/foundations/how-llms-actually-work' },
      // Phase 1+: POC Playbooks, Labs, Decisions return here as pages are built.
    ],

    sidebar: [
      { text: 'Foundations', collapsed: false, items: foundations },
      { text: 'Standards', collapsed: true, items: standards },
      // --- Phase 1+ (uncomment as built) ---
      // { text: 'Decision Frames', collapsed: false, items: decisionFrames },
      // { text: 'POC Playbooks', collapsed: false, items: pocPlaybooks },
      // { text: 'Talk Tracks', collapsed: false, items: talkTracks },
      // { text: 'Lessons', collapsed: true, items: lessons },
      // { text: 'Labs', collapsed: true, items: labs },
      // { text: 'Visuals', collapsed: true, items: visuals },
      // { text: 'Decisions (ADRs)', collapsed: true, items: decisions },
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/WBHankins93/ai-engineering-studio' },
    ],

    search: { provider: 'local' },

    outline: { level: [2, 3] },
  },
})
