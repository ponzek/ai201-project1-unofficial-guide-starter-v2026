# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
In `campus_life`, each topic (such as laundry policies, library hours, or add/drop rules) is contained within a dedicated short document. Because semantic search with `all-MiniLM-L6-v2` easily identifies the relevant document when the query matches the topic closely, at least 4 should succeed; 4 of 5 accounts for occasional vocabulary disconnect between casual student phrasing and official wording.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
All five answers should name a source because each retrieved chunk carries the filename in its metadata, and the prompt template in `generate.py` instructs the model to cite its source document. As long as retrieval returns at least one chunk passing the gate, the model always has a concrete filename to cite.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

**Why this target:**
Completely unrelated questions (like diesel engines or world geography) have cosine distances typically exceeding 0.70 to 0.85 against university campus documents. With a relevance cutoff around 0.60, the gate cleanly blocks out-of-domain queries, while 4 of 5 leaves margin for anomalous semantic overlap.

---

## 4. Something about your chunks

At least 4 of 5 sampled chunks read as a complete thought, with no sentence cut in half at either boundary.

**Why this target:**
In `campus_life`, essential facts like deadlines, fee amounts, and office hours are often stated within a single sentence. If chunking splits across a sentence boundary, that factual context is fractured and unrecoverable during retrieval. Choosing 4 of 5 ensures our chunking strategy respects sentence or paragraph boundaries while allowing tolerance for rare formatting quirks.

---

## 5. Your choice

For at least 4 of my 5 test questions, the primary source cited in the generated answer matches the ground-truth source document.

**Why this target:**
Simply citing *any* document (as in criterion 2) is not enough for an informational guide; the system must attribute the answer to the correct origin document (e.g. citing `dining_kestrel_commons.txt` for dining queries). Setting this to 4 of 5 tests true attribution precision without failing on queries that legitimately touch upon two related documents.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
