# Devin GLM-5.2 skill evaluation

## Result

All eight Opulent tax workflow skills completed end to end in separate Devin CLI sessions. Every accepted run used `glm-5-2`, which the current Devin model catalog labels `GLM-5.2 High [200K context, Free]`. No paid GLM variant appears in any accepted trajectory.

The final score is 94 of 94 hidden checks passed. Each workflow earned a reward of 1.0.

| Skill | Devin session | Hidden checks | Result |
|---|---|---:|---:|
| Classifying expenses for tax | `picayune-dirigible` | 11 of 11 | 1.0 |
| Building books from bank data | `stream-drum` | 11 of 11 | 1.0 |
| Analyzing asset depreciation | `lime-sand` | 12 of 12 | 1.0 |
| Handling multistate income | `crocus-bathroom` | 13 of 13 | 1.0 |
| Determining tax loss treatment | `celestial-emoji` | 10 of 10 | 1.0 |
| Screening tax deductions and credits | `cookie-ethernet` | 12 of 12 | 1.0 |
| Creating custom document requests | `free-helium` | 13 of 13 | 1.0 |
| Writing client tax memos | `cookie-city` | 12 of 12 | 1.0 |

## Source ground truth

The source verification was rerun after the agent work. It passed with six pinned, clean Git checkouts, ten complete APEX Accounting tasks, five byte exact APEX mirrors inside the knowledge work suite, and 58 verified knowledge work suite tasks.

The full Mercor APEX Accounting checkout is pinned to `bf5e8c99117b7ee763d79ad2c64563ac844d77d2`. All fourteen Git LFS files are resolved. The full OpulentiaAI knowledge work demo suite is pinned to `3d8997b493c0b28dd11bf61c352959fef4baee74`. Its validator confirms 688 source files and their hashes.

The Letta creating skills baseline is pinned to `0521b230fe0f4fbed00ceab40c66a2ae55d3be7e`. Harbor, OSWorld, and the writing for agents reference are also pinned in `upstream-lock.json`.

Each skill remains independent. It has its own `SKILL.md`, workflow, source map, evaluation contract, real sample fixtures, and deterministic validator. Each Harbor environment keeps its tests, rubric, and reference answer outside the agent workspace during execution.

## Independent review and corrections

The hidden graders alone were not treated as sufficient. Every accepted response and deliverable was reviewed after the run. The review found and corrected several issues through the same saved free GLM-5.2 sessions:

* The Augusta Rule workbook now uses real Excel time values, an overnight safe duration formula, one daily payment per event, and a 14 day total of $5,390.
* The cross border package now includes the required Swedish loss amount and risk matrix language. Description cells that began with an equals sign were converted to literal text. Workbook clipping, excessive blank rows, and the memo page breaks were fixed.
* The settlement entry now uses the stated generic chart of accounts and avoids a separate unsupported interest entry.
* The HSA memo now states the no double benefit rule. Its schedule no longer treats narrative text as a formula.
* The child employment workbook no longer treats a description as a formula. Source URLs and row heights render in full.
* The Solo 401(k) model no longer reduces adjusted compensation twice. The corrected total contribution is $55,956.68, with $47,956.68 counted under the section 415 limit.

The final spreadsheet review imported and rendered six workbooks with 30 sheets. It scanned 206 formula records and found zero formula error matches. Every rendered sheet was inspected for clipping and layout problems.

The cross border memo was rendered to 12 pages and inspected page by page. The final version has no clipped text, overlap, broken tables, orphaned headings, or avoidable blank sections. All withholding tax rows remain together with their header.

## Trajectory controls

Every accepted trajectory reports `GLM-5.2 High`. Every recorded generation step uses `glm-5-2`. The audit found no hidden test path, grader specification, reference answer, or required answer group in any trajectory. Skill activation evidence is present in every run.

Earlier runs that did not lock to the requested model were rejected and are not part of this results set. The accepted evidence folder contains only the eight free GLM-5.2 runs.

## Evidence

* `manifest.json` is the machine readable result summary.
* `audits/model-and-leakage-audit.json` records the model, generation count, skill activation, and hidden test isolation for each run.
* `audits/spreadsheet-audit.json` records workbook imports, sheets, formulas, hashes, and render paths.
* `audits/docx-render-audit.json` records the final memo render review.
* Each skill folder contains the accepted trajectory, agent log, grader log, reward record, answer, and declared deliverables.
* `SHA256SUMS` covers the complete evidence bundle.

The final source and environment verification commands also passed:

```text
PASS: 6 pinned clean checkouts, 10 complete APEX tasks, 5 byte-exact suite mirrors, and 58 verified suite tasks
PASS: 8 isolated environments, 8 oracle scenarios, 8 negative scenarios, all source hashes verified
```
