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
  { text: 'Visual Prompt Standard', link: '/VISUAL-PROMPT-STANDARD' },
  { text: 'Imagery Plan', link: '/IMAGERY-PLAN' },
  { text: 'Contributing', link: '/CONTRIBUTING' },
]

// --- Phase 1 — the SE/SA spine ---------------------------------------------
const pocPlaybooks = [
  { text: 'Scoping an AI POC', link: '/poc-playbooks/scoping-an-ai-poc' },
]

const decisionFrames = [
  { text: 'Managed API vs Self-Host', link: '/decision-frames/managed-vs-self-host' },
  { text: 'The Real Cost of a RAG System', link: '/decision-frames/rag-tco' },
  { text: 'Do We Even Need an Agent?', link: '/decision-frames/do-we-need-an-agent' },
]

const talkTracks = [
  { text: 'Explaining a Hallucination', link: '/talk-tracks/explaining-a-hallucination' },
]

const visuals = [
  { text: 'The Four-Layer Map', link: '/visuals/four-layer-map' },
]

const decisions = [
  { text: 'ADR 001 — LangGraph as orchestration standard', link: '/decisions/001-langgraph-orchestration' },
]

// --- Phase 2+ sections (uncomment links as pages are built) ----------------
// const lessons = [{ text: 'Overview', link: '/lessons/' }]
// const labs = [{ text: 'Overview', link: '/labs/' }]

export default defineConfig({
  title: 'AI Engineering Studio',
  description:
    'The AI engineering ecosystem, made legible — a Solutions Engineer / Architect lens on LLM apps, infrastructure, MLOps, and governance.',
  lang: 'en-US',

  // The gate. A broken internal link fails the build, which fails CI.
  ignoreDeadLinks: false,

  // Served under a repo subpath on GitHub Pages.
  base: '/ai-engineering-studio/',

  // Render ```mermaid fences into <pre class="mermaid"> so the client-side
  // renderer in theme/index.ts picks them up. Lets authors fence with
  // ```mermaid (per AGENTS.md) instead of hand-writing the wrapper.
  //
  // Critical: must be a <pre> with `v-pre`, and the content HTML-escaped.
  // VitePress compiles rendered markdown as a Vue template — without v-pre,
  // Vue (a) condenses the diagram's newlines into single spaces, which mermaid
  // then rejects as a syntax error, and (b) treats `{{ }}` as interpolation.
  // `v-pre` skips compilation; `<pre>` preserves whitespace; escaping keeps
  // any `<`/`>`/`&` in labels from being parsed as HTML.
  markdown: {
    config: (md) => {
      const defaultFence = md.renderer.rules.fence!.bind(md.renderer.rules)
      md.renderer.rules.fence = (tokens, idx, options, env, self) => {
        const token = tokens[idx]
        if (token.info.trim() === 'mermaid') {
          const esc = token.content
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
          return `<pre class="mermaid" v-pre>${esc}</pre>`
        }
        return defaultFence(tokens, idx, options, env, self)
      }
    },
  },

  themeConfig: {
    nav: [
      { text: 'Start Here', link: '/START-HERE' },
      { text: 'Foundations', link: '/foundations/how-llms-actually-work' },
      { text: 'POC Playbooks', link: '/poc-playbooks/scoping-an-ai-poc' },
      { text: 'Decision Frames', link: '/decision-frames/managed-vs-self-host' },
      { text: 'Decisions', link: '/decisions/001-langgraph-orchestration' },
      // Phase 2+: Labs return here as pages are built.
    ],

    sidebar: [
      { text: 'Foundations', collapsed: false, items: foundations },
      { text: 'POC Playbooks', collapsed: false, items: pocPlaybooks },
      { text: 'Decision Frames', collapsed: false, items: decisionFrames },
      { text: 'Talk Tracks', collapsed: false, items: talkTracks },
      { text: 'Visuals', collapsed: false, items: visuals },
      { text: 'Decisions (ADRs)', collapsed: true, items: decisions },
      { text: 'Standards', collapsed: true, items: standards },
      // --- Phase 2+ (uncomment as built) ---
      // { text: 'Lessons', collapsed: true, items: lessons },
      // { text: 'Labs', collapsed: true, items: labs },
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/WBHankins93/ai-engineering-studio' },
    ],

    search: { provider: 'local' },

    outline: { level: [2, 3] },
  },
})
