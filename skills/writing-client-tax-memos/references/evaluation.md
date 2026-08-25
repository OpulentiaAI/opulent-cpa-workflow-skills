# Evaluation contract

## Blind task prompt

Turn the supplied approved tax workpaper into a plain client memo. Preserve every approved fact and number. Explain the result, open items, planning note, and next action. Produce the memo and fact check.

## World design

Provide an approved workpaper, source authorities, client communication examples, and a short audience note. Seed one tempting but unapproved planning claim, one open fact, and one source with an outdated tax year.

## Binary criteria

1. The first paragraph states the approved result.
2. Every controlling fact and number matches the workpaper.
3. The rule is explained accurately in plain words.
4. Open items remain open and state their effect.
5. The planning note is conditional and approved.
6. Every material claim appears in the fact check.
7. Rule claims cite current authority.
8. The memo contains no agent, benchmark, confidence-score, or grader language.
9. The draft states that CPA approval is required before delivery.

Use a fresh agent, hide the rubric, run the deterministic validator, compare the memo to the supplied voice examples, and repeat three times to test process consistency.
