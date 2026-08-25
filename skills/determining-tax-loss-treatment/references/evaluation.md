# Evaluation contract

## Blind task prompt

Analyze the supplied unusual loss event for the stated tax year. Produce the facts, treatment matrix, form map, evidence request, and workpaper. Separate arithmetic from legal conclusions.

## World design

Provide bank records, a police report, insurer or bank correspondence, account-purpose records, and a client narrative. Seed one conflict in the amount, one unresolved recovery path, and one missing state-law element. Keep the expected treatment and rubric outside the workspace.

## Binary criteria

1. Event facts trace to source documents.
2. Gross loss, reimbursements, and provisional net loss calculate correctly.
3. Business, income-producing, and personal character are kept separate.
4. Each plausible treatment appears in the matrix.
5. Each treatment cites current official authority.
6. Missing state-law, recovery, basis, or profit-motive facts remain `review`.
7. Form placement is conditional on a supported treatment.
8. Evidence requests map directly to unresolved elements.
9. The workpaper states timing and review limits without claiming an unsupported deduction.

Use immutable source files, a fresh agent, a separate output path, a deterministic validator, and three repeated runs. Grade one outcome per criterion.
