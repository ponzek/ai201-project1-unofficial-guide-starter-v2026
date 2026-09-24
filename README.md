# The Unofficial Guide

**Student:** Karina Ponze | **Corpus:** campus_life

---

# Unit 1

## What This Does

This system is a question-answering guide for campus life at university. It answers practical student questions about dining halls, dorm laundry, course workloads, and registrar rules. It retrieves relevant advice from the `campus_life` corpus and generates grounded answers citing the exact source documents.

## Chunking Strategy

**Chunk size:** 550 characters
**Overlap:** 100 characters

When I read through `campus_life`, I saw that most posts are short (around 317 characters on average). The first line is usually the title, and the rest of the post talks about it using words like "here" or "the building".

The starter's 800-character window didn't split anything and didn't care about sentences. If I chopped posts by paragraph, the lower paragraphs lost their title and didn't make sense on their own.

So I wrote my chunker to:
- Keep posts under 550 characters in one piece so the title stays attached to the advice.
- For anything longer, split along sentence ends (`.`, `!`, `?`) with 100 characters of overlap so no sentence gets cut in half.

## Sample Chunks

**Chunk 1** — source: `admin_add_drop_deadline.txt#0` — produced by: `chunker.py::split_documents`

```
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: `course_biol_160.txt#0` — produced by: `chunker.py::split_documents`

```
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.
```

**Chunk 3** — source: `course_hist_118_workload.txt#0` — produced by: `chunker.py::split_documents`

```
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** — source: `dining_pellew_dining_hall_followup.txt#0` — produced by: `chunker.py::split_documents`

```
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.
```

**Chunk 5** — source: `housing_innisfree_hall.txt#0` — produced by: `chunker.py::split_documents`

```
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.
```

## Sample Answer

**Question:** What are the lunch wait times at Kestrel Commons between 12:15 and 1:00?

**Answer:**

```
The wait times at Kestrel Commons between 12:15 and 1:00 are 20 to 25 minutes. 

Source: `dining_kestrel_commons.txt` (also mentioned in `dining_kestrel_commons_followup.txt`).
```

**My relevance cutoff:** `0.60`

My in-corpus questions had distances between 0.205 and 0.412. My out-of-scope questions had distances between 0.825 and 0.934. There is a wide gap between 0.412 and 0.825. I picked 0.60 because it sits right in the middle: it accepts all valid campus questions and blocks off-topic ones.

| Question | In corpus? | Best distance |
|---|---|---|
| What are the lunch wait times at Kestrel Commons between 12:15 and 1:00? | yes | 0.205 |
| How much printing money do students receive each semester, and does it roll over? | yes | 0.316 |
| What notation appears on your transcript if you drop a course after week two? | yes | 0.310 |
| What time does the library close during reading week? | yes | 0.412 |
| What payment method is required for the laundry machines in Aldridge Hall? | yes | 0.337 |
| What is the capital of Mongolia? | no | 0.825 |
| How do I change the oil in a diesel engine? | no | 0.934 |
| Who won the 1994 World Cup? | no | 0.886 |
| What is the recommended dosage of ibuprofen for a headache? | no | 0.844 |
| How do I write a for loop in Rust? | no | 0.896 |

## How I Used AI

**1.** I used AI to develop a chunking strategy for short posts. The initial suggestion was splitting on every paragraph, which broke up title context. I updated it to keep posts under 550 characters intact and use sentence boundaries for longer text, then used AI to verify and inspect the resulting chunks.

**2.** I used AI to measure the retrieval distance scores across all 10 questions. I used AI to verify each distance calculation, confirmed the clear gap between in-corpus (0.205–0.412) and out-of-scope questions (0.825–0.934), and verified that a 0.60 cutoff properly filters off-topic queries.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks read as complete thoughts | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Cited source matches ground-truth | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

Run logs written by `run_eval.py::main`, retrieval by `store.py::search`, chunks by `chunker.py::split_documents`.
Files: `results/run_2026-09-23_2123_before.md`, `results/run_2026-09-23_2125_before.md`, `results/run_2026-09-23_2127_before.md`.

**Real output from Run 1 (`results/run_2026-09-23_2123_before.md`):**

*Kestrel Commons lunch wait (expects "20 to 25 minutes"):*
```
The wait times at Kestrel Commons between 12:15 and 1:00 are 20 to 25 minutes.

Source: `dining_kestrel_commons.txt` (and also mentioned in `dining_kestrel_commons_followup.txt`)
```

*Printing money (expects "$30"):*
```
Students receive $30 of printing per semester, and it does not roll over.

Document: admin_printing_quota.txt
```

*Drop notation (expects "W"):*
```
If you drop a course after week two, it shows as a W on your transcript.
This information comes from `admin_add_drop_deadline.txt`.
```

*Library reading week (expects "10pm"):*
```
The library closes at 10pm during reading week (from study_library_hours.txt).
```

*Laundry payment (expects "card only"):*
```
The laundry machines in Aldridge Hall require card only.

Source: housing_aldridge_hall.txt and housing_aldridge_hall_laundry.txt
```

*Criterion 3 — gate on out-of-corpus questions (`run_eval.py::check_out_of_scope`, cutoff 0.6):*

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.825 | refused |
| How do I change the oil in a diesel engine? | 0.934 | refused |
| Who won the 1994 World Cup? | 0.886 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.844 | refused |
| How do I write a for loop in Rust? | 0.896 | refused |

## Verdicts

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | scorer.py confirmed pass for all 5 questions on all 3 runs — the expected phrase appeared in every answer, confirming the right chunk was retrieved every time. |
| 2 | Every answer names a source | MET | I read the real output in the run log: every answer includes a filename. No answer was sourceless across any of the 3 runs. |
| 3 | Gate stops out-of-corpus questions | MET | check_out_of_scope showed all 5 refused. Distances ranged 0.825–0.934, well above the 0.60 cutoff. Retrieval is deterministic so the result is the same every run. |
| 4 | Chunks read as complete thoughts | MET | I read the sample chunks and the returned answers — no sentence was cut mid-way. The chunker keeps short posts whole and splits longer ones only at sentence boundaries. All 5 sampled chunks end on a complete sentence. |
| 5 | Cited source matches ground-truth | MET | I verified each answer's primary cited source: Kestrel Commons to dining_kestrel_commons.txt, printing to admin_printing_quota.txt, drop notation to admin_add_drop_deadline.txt, library to study_library_hours.txt, laundry to housing_aldridge_hall_laundry.txt. All 5 of 5 matched. |

## Diagnoses

All five criteria were met across all three runs. There were no misses to diagnose.

**Were the targets set too low?** Honestly, yes — for this corpus. The `campus_life` documents are short, single-topic posts with clear filenames, which makes every stage easy:

- Retrieval (criterion 1): each post covers exactly one topic, so there is little ambiguity between documents.
- Source citation (criterion 2): every chunk carries its filename in metadata and the prompt instructs the model to cite it, so a source is always available.
- Gate (criterion 3): campus posts use domain-specific vocabulary that shares almost nothing with diesel engines or world geography.
- Chunk quality (criterion 4): most posts are under 550 characters and stay whole; the sentence-boundary splitter only ran on a handful of longer posts.
- Source matching (criterion 5): one topic per file means the right file is almost always the top retrieval hit.

**What I would tighten:** Criterion 1 and 5 could both be raised to 5/5 — they passed 5/5 every time. Criterion 3 would be stronger with questions that share vocabulary with the corpus (e.g., "What is the best way to wash a diesel stain from clothes?" — laundry-adjacent but out of scope).

## The Improvement

**What I changed:** Increased `TOP_K` from 5 to 8 in `config.py`.

**Why I picked it:** The library question had the weakest retrieval distance of any in-corpus question (0.412), only 0.188 below the 0.60 cutoff. Retrieving more chunks gives the generation stage more context for borderline questions and makes the system more robust as the corpus grows. A larger `top_k` doesn't change what is retrieved — it adds more candidates so the model has more to draw from when the best match is not a perfect hit.

### Run Log — After

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks read as complete thoughts | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Cited source matches ground-truth | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

Files: `results/run_2026-09-23_2133_after.md`, `results/run_2026-09-23_2136_after.md`, `results/run_2026-09-23_2138_after.md`.

**Did it help?**

Yes, in the sense that it didn't break anything, and it measurably increased the context available to the generator. Before the change, each prompt contained 5 retrieved chunks; after, each contained 8. The token count per session went from ~9,130 to ~13,640 — a 49% increase in input tokens — confirming the model received substantially more material to work from. All five criteria stayed MET across all three runs.

The improvement didn't visibly change the pass/fail outcomes because the system was already passing everything at top-k=5. The real benefit would show on a harder corpus or a borderline question where the correct answer chunk ranked 6th, 7th, or 8th. For this corpus, top-k=5 was already sufficient — but the change reduces the risk of a miss as the corpus grows.

## What's Still Broken

No criterion was missed before or after the fix. The system passes all five targets as written.

What I would do next: raise the targets. Criterion 1 and 5 should be 5/5. Criterion 3 needs harder out-of-corpus questions — ones that share vocabulary with campus life — to genuinely stress-test the gate. The current questions were easy enough that the gate had distances 0.20 above the cutoff; a harder set would probe whether the cutoff is actually calibrated correctly.

## What I'd Do Differently

I would write criterion 3 differently. My current version uses completely unrelated questions (diesel engines, world capitals) with distances of 0.825–0.934. A stronger criterion would use plausible but out-of-scope questions — like questions about a different university's housing policies. Those would embed much closer to my corpus and actually test whether the 0.60 cutoff is in the right place.

I would also add a criterion about hallucination: "the answer contains no information not present in the retrieved chunks." That is what I actually care about from a trust perspective, but I had no way to measure it automatically before building scorer.py. Now that scorer.py exists and the judge function has access to the retrieved results, this would be measurable.

