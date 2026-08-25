# Evaluation contract

## Blind task prompt

Source the supplied income by state for the stated tax year. Determine which state returns require review or filing, calculate supported allocations, and write the multistate workpaper.

## World design

Provide W-2s, 1099s, a residency timeline, workday log, travel calendar, payer contracts, withholding, and prior state returns. Seed a payer-address trap, incomplete workday log, one reciprocal-state issue, and one business nexus fact.

## Binary criteria

1. Every income form appears in sourcing detail.
2. State allocations for each income item equal its gross amount.
3. Physical service facts override payer address when the applicable rule requires them.
4. State summaries equal sourcing detail.
5. Resident-return income is separate from state-source income.
6. Every filing conclusion cites current official authority for the tax year.
7. Credits, withholding, reciprocity, and pass-through interaction are addressed when facts trigger them.
8. Missing residency, threshold, nexus, or allocation facts are marked for review.

Run a fresh agent against immutable sources and a separate output path. Keep the expected allocations and rubric outside the workspace. Run the validator, grade one outcome per criterion, and compare three trajectories.
