# Visual Prompt Standard

System for generating showcase architecture/translation diagrams at consistent
style and verified accuracy. **Spec first, image second, review mandatory.** The
image is disposable; the spec is the record.

Ported from the sibling repos (`solutions-playbook`, `devops-studio`) so the
trilogy reads as one body of work — with the **palette swapped to this repo's
violet brand** so embedded images match the site.

---

## Workflow

1. Write the **Content Spec** (below). This is ground truth — see `IMAGERY-PLAN.md`
   for which diagrams are queued and `visual-specs/showcase-prompts.md` for the
   filled, ready-to-paste specs.
2. Assemble the prompt: **Style Preamble** + Content Spec.
3. Generate (GPT Image, Midjourney, etc.). Expect 2–4 passes — dense labels are the
   hardest case for image models.
4. Run **Self-Review** against the spec.
5. Save the PNG to `assets/diagrams/<name>.png`, embed it, and keep the spec.

---

## Style Preamble (paste on every prompt, unchanged)

```
Clean modern technical system-architecture diagram, flat vector infographic style.
Generous whitespace, precise alignment, airy spacing. White background.
Systems as soft rounded rectangles with thin borders and very light fills.
Group related systems inside labeled boundary containers.
Connectors are clean thin arrows with short labels; arrow direction is meaningful.
Simple flat line icons only, minimal and consistent. No photorealism, no 3D,
no heavy gradients, no drop-shadow clutter, no decorative noise.

Palette (this repo's violet brand):
- Ink / text: deep navy (#0f1923)
- Primary accent / active path: violet (#6d4aff)
- Control / reliability layer: deep indigo (#3b2d8c)
- Success: green (#1a6b35)   - Warning: amber (#b8860b)   - Failure: red (#8b1a1a)
- Soft fills: very light tints of the above on white

Typography: clean sans-serif. Short bold labels in title case. High contrast,
fully legible at presentation size.

CRITICAL: render every text label EXACTLY as written in the spec — correct spelling,
no added words, no invented boxes, no extra arrows. If a label is unclear, leave it
blank rather than guessing.
```

> The accent is the site violet (`#6d4aff`) so diagrams match the brand. Keep it
> violet for anything embedded in a page. Swap only if producing a standalone
> reference that won't sit on the site.

---

## Content Spec (fill before generating)

```
TITLE:            <one line>
SUBTITLE:         <optional one line>
CANVAS:           <landscape 16:9 | square | portrait>
BOUNDARIES:       <left-to-right or top-to-bottom zones, e.g. Indexing | Query>
SYSTEMS:          <name — role — which boundary>   (one per line)
FLOW (ordered):   <from> --[label]--> <to>          (one per line)
ERROR / ALT PATHS:<from> --[condition]--> <to>      (e.g. low score --> "say I don't know")
ANNOTATIONS:      <numbers / policies, mark each (verified) or (illustrative)>
LEGEND:           <what the colors mean in this image>
EXACT LABEL LIST: <flat list of every text string that must appear, spelled correctly>
```

> The EXACT LABEL LIST is the accountability anchor. Review checks the image
> against it, item by item.

---

## Self-Review (the gate before it ships)

- [ ] Every system in the spec is present
- [ ] Every arrow points the correct direction
- [ ] Every string in EXACT LABEL LIST appears and is spelled right
- [ ] Nothing invented — no extra boxes, labels, or arrows
- [ ] Numbers match spec; illustrative ones acceptable, none fabricated as fact
- [ ] Palette and style match the preamble (violet accent, navy ink, white bg)
- [ ] Legend is correct
- [ ] Reads in one glance — target 10–18 in-image labels; split if denser

If any box fails → fix the label by hand if trivial, otherwise regenerate. Don't
ship a near-miss.

---

## Accuracy rule (same as the site's Depth Standard)

No fake specificity *inside the image*. If a number is illustrative (cost,
latency, accuracy, retry count), it belongs in the page caption marked
illustrative — not stated as fact inside the diagram. Universal facts (a retry
doubles the backoff; hybrid = keyword + vector) can appear in-image.

---

## When a label keeps failing

If one label misses across 3+ generations: reduce total label count, split the
diagram into two frames, or render that label as a caption beside the image
instead of inside it. Don't fight the model past three tries.
