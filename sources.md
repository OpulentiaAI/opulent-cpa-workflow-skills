# Sources shared in the thread

These are the distinct links confirmed in the August 17, 2026 message cluster. The notes explain how each link fits the surrounding discussion.

## Skill construction

### Letta creating-skills baseline

https://github.com/letta-ai/letta-code/tree/main/src/skills/builtin/creating-skills

The user supplied this after the Messages retrieval and required it as the construction baseline. The finished package follows its required `SKILL.md` anatomy, gerund names, concise routing descriptions, progressive disclosure, bundled scripts, references, assets, validators, and distributable `.skill` archives.

### Writing for agents

https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-for-agents

This was shared as a meta reference for writing strong agent instructions and skills.

The Messages thread mentioned `letta-code` as another meta reference. The exact Letta URL above came from the user's follow-up request rather than the original message cluster.

## Eval construction

### Harbor evals

https://www.harborframework.com/docs/run-jobs/run-evals

This was shared as the standard construction reference for evals.

## Benchmarks and task sets

### APEX Accounting leaderboard

https://www.mercor.com/apex/apex-accounting-leaderboard/

This was shared as an accounting task benchmark and model ranking reference.

### APEX Accounting dataset

https://huggingface.co/datasets/mercor/apex-accounting

This is the dataset paired with the APEX Accounting benchmark.

### OSWorld

https://osworld-v1.xlang.ai/

This was shared as a benchmark for agents that complete open ended tasks in real computer environments.

### Opulent knowledge work demo suite

https://github.com/OpulentiaAI/knowledge-work-demo-suite

This source began as the twenty task suite shared after the construction discussion. The pinned checkout used here now contains 58 tasks from ten dataset families, with prompts, source documents, rubrics, answer keys where available, and provenance.

## Local source locks

The source package stores the exact live checkouts under `upstream/`. `upstream-lock.json` pins these revisions:

* APEX Accounting at `bf5e8c99117b7ee763d79ad2c64563ac844d77d2`.
* Opulent knowledge work demo suite at `3d8997b493c0b28dd11bf61c352959fef4baee74`.
* Letta Code at `0521b230fe0f4fbed00ceab40c66a2ae55d3be7e`.
* Matt Pocock skills at `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`.
* Harbor at `72f7dd0134162c5b7229f6a31286e05a49c0f8a4`.
* OSWorld at `84aee655c2afb6b77ecf39884432615ba345c031`.

The APEX task data is licensed under CC BY 4.0. The Opulent suite is MIT, while its third party task files keep their own upstream terms. Every generated environment includes the matching license and notices.

## Example use cases and source data

### Shortcut case library

https://shortcut.ai/cases

This was shared as a library of accounting agent examples.

### Shortcut accounting use cases

https://shortcut.ai/cases/how-accounting-teams-use-shortcut

This page describes four ways accounting teams use Shortcut.

### Financial Datasets

https://www.financialdatasets.ai/

This was shared as a stock market data API for agents and as a possible source for example financial data.

### CWU library guide

https://libguides.lib.cwu.edu/c.php?g=358343&p=2419792

This was shared with the source gathering references. The preview only exposed the `lib.cwu.edu` domain in Messages, so the exact URL was copied from the message.

## Link inventory notes

Messages showed OSWorld twice within the nearby link sequence. This file records the link once because both previews copied to the same URL.

The commercial deck and later demo discussion belong to the next part of the conversation. They are not part of this skill, eval, source, and construction package.
