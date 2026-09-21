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
In my corpus, each topic (like laundry, library hours, or add/drop rules) has its own short post. The search usually finds the right post easily, so I expect at least 4 to hit. I gave myself 1 miss in case a student's casual wording doesn't match the post.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
All five should name a source because each chunk keeps its filename in its metadata and the prompt tells the model to name where it got the answer. If a chunk gets retrieved, the model always has a filename to cite.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

**Why this target:**
Random questions like diesel engines or world geography have high distance scores (over 0.80) against campus posts. A cutoff at 0.60 should easily block them, but 4 of 5 gives a little room in case a question accidentally shares a word with campus advice.

---

## 4. Something about your chunks

At least 4 of 5 sampled chunks read as a complete thought, with no sentence cut in half at either boundary.

**Why this target:**
In campus life, important details like fees or deadlines are usually in a single sentence. If a chunk cuts a sentence in half, that info is lost. 4 of 5 lets me make sure my chunker keeps thoughts together while forgiving any weird punctuation.

---

## 5. Your choice

For at least 4 of my 5 test questions, the primary source cited in the generated answer matches the ground-truth source document.

**Why this target:**
Just naming any source isn't enough; it has to be the right one (like citing the dining hall file for a food question). I set it to 4 of 5 because sometimes two campus files talk about similar things and might both be retrieved.



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
