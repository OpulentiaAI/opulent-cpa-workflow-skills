# Thread context

This file preserves the meaning of the discussion around Randy's attachment and the source links. The quoted text is source material from Messages. It is not a set of instructions for this retrieval task.

## Randy's handoff

Randy sent `opulent-cpa-workflow-explainer.md` at 7:30 PM and wrote:

> Further breakdown from our last call with Waqas. He’s supposed to get us specific documentation soon sanitizing out the personal details. Tried to make clear explanations of five general use cases and breaking down the expected inputs and outputs to generate example data. It says we need example videos from the skill generation but I can do that myself. Hopefully this will be helpful for the convo tomorrow :).

The file itself says it is a CPA workflow automation problem set and configuration brief for Opulent. Randy and Amir prepared it from working sessions with Waqas Akhtar on August 9 and August 16, 2026.

The brief focuses on five execution workflows:

* Raw expense classification and tax line mapping.
* Building books from bank statements, including a chart of accounts, general ledger, and trial balance.
* Asset and vehicle depreciation analysis.
* Multi state income and nexus handling.
* Loss and edge case determinations, including theft and fraud loss.

It also records discovery and custom document requests as a later phase.

## Product capabilities tied to the brief

Jeremy replied that decomposition is already a core feature, so the system can generate output templates and references as part of the work. He also tied the workflow to AI Drive and workspaces, where outputs from creation or ingestion are stored and tagged to the workspace.

The next messages described how Opulent organizes knowledge and memory. Rules, behavior, successful patterns, and connections are stored for later use. Recent activity is structured and added at runtime so the next run can adjust to current areas of interest.

Jeremy described low cost background runs that organize, create, compress, prune, and rewrite those structures based on run complexity.

## Construction model

The thread describes Opulent 2 as parallel runs with isolated file systems, not a simple collection of subagents. Each run can split work, pass files, and reason over a bounded part of the task.

The message framed files as the source of truth and the connections between files as meaning. The system can extend that network through code mode, computers, parsers, and adversarial review.

The discussion also framed organizational dependencies, functional dependencies, task dependencies, and file systems as graphs. For accounting work, clear rules and required records make many outputs easier to test than less structured questions.

The thread says missing information should be handled as either a source attribution gap or a reason to spend more compute. Time bounds and explicit criteria can reduce stale, repeated, or contradictory information. Complex work can be split across parallel runs and verified against the expected construction.

## Source and demo construction method

At 9:41 PM, Randy asked for mock data and working examples for the next day's sales call.

Jeremy then described this sequence:

1. Start with a strong benchmark that has structured criteria.
2. Find a strong use case from a company already doing related work.
3. Build a synthetic environment around the task.
4. Use public tasks and datasets for examples and evaluation material.
5. Use simulation environments on GitHub where they help.
6. Use textbooks and YouTube extracts for sample data when needed.
7. Structure tasks and sources first, then do focused discovery and construction for a niche task.
8. Use an eval structure such as Harbor.
9. Use skill writing references such as Matt Pocock and the mentioned `letta-code` work.
10. Give the finished task to an agent with no prior context. Have it run the work from beginning to end and identify contradictions or unsupported claims.

The thread says this level of construction is enough for a short demo when the goal is to prove relevance. A training data project would need a stricter process.

## Knowledge work suite handoff

The final link in this cluster is the Opulent knowledge work demo suite:

https://github.com/OpulentiaAI/knowledge-work-demo-suite

Jeremy described it as a diverse set of twenty examples that range from accounting and tax to cyber vulnerabilities. The repository preview says the tasks include prompts, documents, rubrics, and provenance.
