# Bibliography reorganization plan — "Agency and CG" (target collection)

Goal: merge the useful papers from the old **"Agency and GC"** (99 entries — likely from an earlier paper/proposal) into **"Agency and CG"** (29 entries — the collection you started for this thesis), clean up tags, and set up a light folder structure, so you can reimport/rebuild this in Zotero yourself. Everything below is a proposal for you to execute in the Zotero GUI — I haven't touched your library.

**Note on scope:** all relevance calls below are based on title + abstract + existing tags/annotations from the exported `.bib` files — not a full read of each PDF. Treat "KEEP" as "worth keeping in the library," not "read in full" — you'll still want to check the actual pages that matter within each paper yourself; a tag on an item doesn't mean the whole PDF is relevant cover-to-cover, just that the paper as a whole belongs in that bucket.

---

## 1. Folder structure (Zotero subcollections under "Agency and CG")

Kept deliberately shallow, per your steer:

```
Agency and CG
├── Gaze Cuing (GC)
│   ├── Classic papers
│   └── Reviews
├── Sense of Agency (SoA)
│   ├── Classic papers
│   └── Reviews
├── Social Cognition
└── Methods & Materials        (software, stats, power analysis — not lit-review content)
```

Modulator-type distinctions (face / observer / interaction characteristics) live in **tags**, not extra folders, since you wanted this brief.

## 2. Tag remapping (old → new)

| Old tag | New tag |
|---|---|
| `GC_GENERAL` | `gc-general` |
| `GC_ToM` | `gc-tom` |
| `GC_JA` | `gc-joint-attention` |
| `SocialCognition` | `social-cognition` |
| `characteristics of the cueing face` | `mod-face` |
| `characteristics of the Observer` | `mod-observer` |
| `characteristics of interaction` | `mod-interaction` |
| `chars_NO_RES` | `mod-null-result` (co-tag alongside whichever `mod-*` it belongs to — it means "this modulator category was tested and *didn't* show an effect," which is still worth keeping as a boundary condition) |
| `SofA motor movement` | `soa-motor` |
| `SofA measurements` | `soa-measurement` |
| `measuring SA, temporal bindin` | `soa-measurement` (typo "bindin" → dropped, redundant with the above) |
| `eyeTracking` | `method-eyetracking` |
| `attention` | `method-stats` *or* keep as general background — see Lavie 2005 below |
| `statistics` | `method-stats` |
| `gc modifiers` / `gc neural mechanisms` / `gc paradigm` (McKay meta-analysis) | `gc-general`, `mod-face` + `mod-observer` + `mod-interaction` (it's a meta-analysis covering all three) |

## 3. Duplicates to resolve first

**Cross-collection (same paper in both "Agency and GC" and "Agency and CG") — merge into one entry, don't import twice:**

| Paper | Which copy to keep |
|---|---|
| Ulloa et al. 2019 — eye contact & sense of agency | CG's copy (`ulloa_impact_2019`) — GC's has a garbled author field and a stray "MAG ID" note |
| Friesen & Kingstone 1998 | either, identical |
| Driver et al. 1999 | GC's copy — has the PDF attached, CG's doesn't |
| Dalmaso et al. 2020 (modulators review) | merge tags: `gc-general` + `mod-face` + `mod-observer` + `mod-interaction` (it's tagged differently in each collection, both apply — it's the review) |
| Capellini et al. 2019 | either, identical tag (`mod-observer`) |
| Cui et al. 2014 | either, identical tag (`mod-observer`) |
| Talipski et al. 2021 | either, identical tag (`mod-null-result`) |
| Haggard, Clark & Kalogeras 2002 (classic intentional binding) | merge: GC's tag (`soa-general`, was `SoA`) + CG's annotation ("classic paper... used in discussion Exp1") |
| Metcalfe & Terrace (eds.) 2013, *Agency and Joint Attention* | CG's copy — correctly typed as an edited collection with DOI/publisher; GC's is a bare stub |
| E-Prime / FaceGen software entries | keep one clean copy of each — FaceGen exists **3 times** total across both collections (2 in "Agency and GC" alone), only one has full metadata (Demo 3.34, facegen.com) |

**Within "Agency and GC" itself (same collection, added twice):**
- Hietanen & Leppänen 2003 ("Does Facial Expression Affect Attention Orienting by Gaze Direction Cues?") — exists as both `hietanen_does_2003` and `hietanen_does_2003-1`. Same paper, drop one.
- FaceGen software — bare stub + full entry, drop the bare one.

---

## 4. The 87 papers only in "Agency and GC" — keep / skip / where they go

Only **one** paper looks genuinely off-topic. Everything else is directly on-topic for this thesis (unsurprising — it's an earlier gaze-cuing-focused collection). Recommended folder is listed; tags in `code`.

### → Gaze Cuing / Classic papers
`gc-general` unless noted:
- Langton & Bruce 1999 — Reflexive Visual Orienting in Response to the Social Attention of Others
- Hietanen 1999 — Does your gaze direction and head orientation shift my visual attention?
- Bayliss, Di Pellegrino, & Tipper 2004 — Orienting of attention via observed eye gaze is head-centred
- Posner 1980 — Orienting of Attention (foundational paradigm root — the Frischen review excerpt already in your literature notes cites this directly)
- Mansfield, Farroni, & Johnson 2003 — Does gaze perception facilitate overt orienting? `method-eyetracking`
- Matsunaka & Hiraki 2019 — Rapid saccadic response with fearful gaze cue `method-eyetracking`
- Murray, Drake, & Klein 2023 — Is gaze cuing more like endogenous or exogenous orienting? (directly answers your "Is gaze cuing automatic?" question — high priority)

### → Gaze Cuing / Reviews
- Langton, Watt, & Bruce 2000 — Do the eyes have it? Cues to the direction of social attention `gc-general`
- Emery 2000 — The eyes have it: neuroethology, function and evolution of social gaze `gc-tom`, `gc-joint-attention`
- Dalmaso, Castelli, & Galfano 2020 — Social modulators of gaze-mediated orienting (see duplicates above)

### → Gaze Cuing, tagged `mod-face` (Face factors)
- Kürten et al. 2025 — eccentricity, direct face/gaze, motion onset
- Fox, Mathews, Calder, & Yiend 2007 — Anxiety and sensitivity to gaze direction in emotionally expressive faces
- Dalmaso, Galfano, & Castelli 2015 — same/other-race gaze distractors
- Dalmaso, Pavan, Castelli, & Galfano 2012 — Social status gates social attention
- Süßenbach & Schönbrodt 2014 — Trustworthiness moderates gaze cueing
- Bayliss & Tipper 2006 — Predictive Gaze Cues and Personality Judgments
- King, Rowe, & Leonards 2011 — Gaze Cueing and Sender Trustworthiness
- Pletti, Dalmaso, Sarlo, & Galfano 2015 — snake-phobic women, facial expression
- Bayliss, Schuch, & Tipper 2010 — affective context
- McCrackin & Itier 2018 — fearful/happy expressions, 200ms SOA
- Bayless, Glover, Taylor, & Itier 2011 — emotion vs. perceptual features
- Jones et al. 2010 — facial dominance
- Ohlsen, Van Zoest, & Van Vugt 2013 — gender & facial dominance
- Hori et al. 2005 — facial expression, shared attention
- Pecchinenda & Petrucci 2016 — cognitive load
- Tollenaar et al. 2013 — oxytocin
- Coy, Nelson, & Mondloch 2019 `mod-null-result` — no emotion-specific effect in threat context
- Bayliss, Frischen, Fenske, & Tipper 2007 `mod-null-result`
- Holmes, Mogg, Garcia, & Bradley 2010 `mod-null-result`
- Mathews, Fox, Yiend, & Calder 2003 — face of fear
- Lassalle & Itier 2015 — autistic traits, happy vs. fearful faces
- Tipples 2006 — fear potentiates orienting
- Deaner, Shepherd, & Platt 2007 `mod-interaction` too — familiarity, sex differences
- Hietanen & Leppänen 2003 (keep one copy — see duplicates)

### → Gaze Cuing, tagged `mod-observer` (Observer factors)
- Alwall, Johansson, & Hansen 2010 — gender, empathizing/systemizing
- Bayliss, Di Pellegrino, & Tipper 2005 — sex differences
- Cooney, Brady, & Ryan 2017 — gender of viewer
- Feng et al. 2011 — gender, ERP
- Hayward & Ristic 2017 — reduced social competence
- Kuhn, Pagano, Maani, & Bunce 2015 — age-related decline
- Slessor, Phillips, & Bull 2008 `mod-null-result` too — age-related basic social perception
- Slessor, Phillips, & Bull 2010 — age, gaze+emotion integration
- Slessor et al. 2016 — specificity of age differences
- Dodd, Hibbing, & Smith 2011 — political temperament
- Wu, Bischof, Anderson, Jakobsen, & Kingstone 2014 — personality
- Ponari, Trojano, Grossi, & Conson 2013 — introversion/extraversion
- Wilkowski, Robinson, & Friesen 2009 — belongingness self-regulation
- Carraro, Dalmaso, Castelli, & Galfano 2015 — political temperament, contextualized
- Hudson, Nijboer, & Jellema 2012 — autistic-like traits *(currently tagged `mod-interaction`, arguably fits `mod-observer` better since it's about the perceiver's traits — your call)*
- Boll, Bartholomaeus, Peter, Lupke, & Gamer 2016 — social phobia

### → Gaze Cuing, tagged `mod-interaction` (Social/relational factors)
- Frischen & Tipper 2006 — long-term gaze cueing effects, memory
- Porciello et al. 2014 — Interpersonal Multisensory Stimulation
- Chauhan, Visconti Di Oleggio Castello, Soltani, & Gobbini 2017 — social saliency
- Pavan, Dalmaso, Galfano, & Castelli 2011 — racial group membership
- Chen, Zhao, Song, Guan, & Wu 2017 — intergroup threat, fMRI
- Strachan & Tipper 2017 — durability of learned trust
- Cazzato, Liuzza, Caprara, Macaluso, & Aglioti 2015 — politicians, fMRI
- Liuzza et al. 2011 — politicians, ingroup voters
- Kawai 2011 — joint attention required for gaze-triggered shift
- Kuhn, Vacaityte, D'Souza, Millett, & Cole 2018 — mental states modulate gaze following
- Morgan, Freeth, & Smith 2018 — mental state attributions mediate GCE
- Nuku & Bekkering 2008 — joint attention, inferring perception `gc-joint-attention` too
- Schulz, Velichkovsky, & Helmert 2014 — 3-D noninformative gaze-cueing, perspective
- Teufel, Alexis, Clayton, & Davis 2010 — mental-state attribution, reflexive gaze following
- Wiese, Wykowska, Zwickel, & Müller 2012 — ascribing intentions to others
- Kingstone, Kachkovski, Vasilyev, Kuk, & Welsh 2019 — mental attribution not necessary/sufficient

### → Social Cognition
- Baron-Cohen 1995 — *Mindblindness* `gc-tom`
- Tomasello, Carpenter, Call, Behne, & Moll 2005 — Understanding and sharing intentions `gc-tom`, `gc-joint-attention`

### → Sense of Agency / Classic papers
- Gallagher 2000 — Philosophical conceptions of the self
- Friston 2012 — Prediction, perception and agency (predictive-processing model — matches your Part III theoretical-models table directly)
- Wolpert & Kawato 1998 — forward/inverse models (comparator-model precursor)
- Wegner, Sparrow, & Winerman 2004 — **Vicarious Agency: control over others' movements** (directly answers "can people experience agency over another's behaviour?" — high priority)
- Gutzeit, Weller, Muth, Kürten, & Huestegge 2024 — **Eye did this! Sense of agency in eye movements** (agency over eye movements specifically — core to this thesis, high priority)
- Blakemore, Wolpert, & Frith 1998 — self-produced tickle, sensory attenuation
- Shergill, Bays, Frith, & Wolpert 2003 — force escalation, self–other attribution
- Wenke, Fleming, & Haggard 2010 — subliminal priming, sense of control (already cited in your intro drafts)
- Martin & Pacherie 2013 — thought insertion, ownership `soa` clinical angle — matches your Part III pathological-cases material
- James W. Moore, Middleton, Haggard, & Fletcher 2012 — implicit/explicit SoA dissociation (Perruchet paradigm) — matches your Classification I directly
- Stephenson, Edwards, Howard, & Bayliss 2018 — **Eyes that bind us** — gaze leading induces implicit SoA (core GC+SoA intersection paper) `soa-measurement`
- Metcalfe & Terrace (eds.) 2013 — *Agency and Joint Attention* (see duplicates — use CG's copy)

### → Sense of Agency / Reviews
- Haggard & Tsakiris 2009 — The Experience of Agency: Feelings, Judgments, Responsibility
- Wen & Imamizu 2022 — The sense of agency in perception, behaviour, human–machine interactions

### → Methods & Materials
- Schneider, Eschman, & Zuccolotto 2002 — E-Prime `method-software`
- FaceGen Modeller `method-software`
- Faul, Erdfelder, Lang, & Buchner 2007 — G\*Power 3 `method-stats`
- Proctor, Miles, & Baroni 2011 — RT distribution analysis of spatial correspondence effects `method-stats` (directly relevant to the bin/RT-distribution analysis work from earlier this session)
- Janyan, Shtyrov, Andriushchenko, Blinova, & Shcherbakova 2022 — audiovisual correspondence, selective attention `method-stats` (Armina Janyan's own work — likely cited for methodological reasons, not gaze-cueing content)
- Lavie 2005 — Distracted and confused? Selective attention under load — general attention-load theory, not gaze-cueing specific; keep as background-theory support rather than core lit, tag `method-stats` or leave untagged — your call

### SKIP — looks miscategorized, not on-topic
- **Kurowski & Blumstein 2016 — "Phonetic basis of phonemic paraphasias in aphasia: Evidence for cascading activation."** This is a speech-language pathology paper on aphasic paraphasias, tagged `characteristics of interaction` — almost certainly a mis-tag/mis-drag rather than an intentional inclusion. Flagging rather than dropping silently, in case there's a reason (e.g., cascading-activation as a theoretical analogy) I'm not seeing.

---

## 5. What's already only in "Agency and CG" (19 papers, no action needed — just apply the new tag names)

These stay put; just retag per §2: McKay et al. 2022 (PsyArXiv preprint), McKay et al. 2021 (published version — keep both, preprint + published), Engbert, Wohlschläger, & Haggard 2008, Antusch, Custers, Marien, & Aarts 2021, Fagioli, Hommel, & Schubotz 2007, Brown, Friston, & Bestmann 2011, Barlas & Obhi 2013, Beck, Di Costa, & Haggard 2017, Minohara et al. 2016, Pacherie 2007, Bart et al. 2019, Simchon, Hadar, & Gilead 2023, Dewey & Knoblich 2014, Pashler 1994, Braun et al. 2018, Edwards (thesis, no date), Frischen, Bayliss, & Tipper 2007 (**the core GC review** — good that it's here already), Stephenson, Edwards, & Bayliss 2021 — *From Gaze Perception to Social Cognition: The Shared-Attention System*.

---

## Next steps (your call)

1. Confirm/adjust the folder + tag scheme above.
2. In Zotero: create the 4 subcollections, resolve the duplicates listed in §3 (drag/merge), then work through §4's list adding each kept paper into "Agency and CG" with its new tag.
3. Once done, re-export "Agency and CG" as BibLaTeX again so I can spot-check the result if useful.
