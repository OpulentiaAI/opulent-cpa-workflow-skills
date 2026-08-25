# Evaluation contract

## Blind task prompt

Classify the supplied transaction CSV for the stated client and tax year. Produce the four files in the skill output contract. Find the relevant evidence in the workspace. Surface questions instead of guessing.

## Synthetic world

Provide a client profile, one or more inconsistent transaction exports, a prior-year mapping table when the test needs one, and a small set of receipts or notes. Keep grader files outside the agent workspace.

## Binary criteria

1. Every input `txn_id` appears exactly once in classified detail.
2. Accepted and exception amounts reconcile to the source total.
3. Summary counts and totals match accepted detail.
4. Ambiguous personal or business items appear in exceptions.
5. Capitalization-sensitive items are accepted only with supporting facts.
6. Every accepted form mapping cites an official source for the stated tax year.
7. Every exception asks a question that could change treatment.
8. The workpaper states scope, tax year, methods, assumptions, and unresolved decisions.

## Run method

Use a fresh agent with no conversation context. Give it only the task workspace and output path. Run the deterministic validator first. Grade each substantive criterion separately as met or not met. Repeat the same task three times and compare the first step where the processes differ.

This follows the APEX pattern of realistic worlds and outcome-based criteria, the Harbor task model of instruction plus environment plus test script, and the Opulent demo-suite separation between immutable sources and generated outputs.
