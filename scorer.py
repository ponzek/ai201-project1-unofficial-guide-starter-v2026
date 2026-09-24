"""
scorer.py — Unit 2 auto-scorer.

run_eval.py looks for a function with this exact signature:

    judge(question, expects, answer, results) -> bool

Return True if the answer passes, False if it fails.

This scorer does a case-insensitive substring check: if the word or short
phrase in `expects` appears anywhere in the answer, it's a pass.

That's intentionally simple — the lesson is deciding what "correct" means,
not building a complex NLP pipeline.
"""

from __future__ import annotations


def judge(question: str, expects: str, answer: str, results: list) -> bool:
    """
    Return True if `expects` appears in `answer` (case-insensitive).

    Parameters
    ----------
    question : str
        The question that was asked.
    expects : str
        A word or short phrase a correct answer should contain, as written
        in questions.py.
    answer : str
        The system's generated answer (or the refusal string if the gate
        blocked the question).
    results : list
        The retrieval results (store.Result objects). Available if you want
        to check sources, distances, etc.

    Returns
    -------
    bool
        True = pass, False = fail.
    """
    if not expects:
        # No expected phrase set — can't auto-judge.
        return False

    # Normalize both sides for a fair comparison.
    return expects.strip().lower() in answer.strip().lower()
