# Example Decision Memo

## Decision question
Should the team adopt Vendor A or Vendor B for the first internal knowledge-search rollout?

## Context
The team needs a lightweight search layer for internal use within the next month. Speed of setup matters, but long-term maintenance burden also matters.

## Evidence
- Vendor A has the faster setup path and better starter documentation.
- Vendor B offers stronger long-term flexibility but requires more initial configuration.
- Internal bandwidth for setup is limited this month.
- Security review requirements appear manageable for both options, but details are still incomplete.

## Options
### Option 1: Vendor A
- Benefits: fast launch, lower onboarding friction, clearer quickstart
- Costs: less flexible architecture later
- Risks: may require migration if needs become more complex

### Option 2: Vendor B
- Benefits: more extensible foundation, better long-term fit
- Costs: slower initial setup, higher short-term complexity
- Risks: launch timing may slip

## Trade-offs
- Fast launch favors Vendor A
- Long-term extensibility favors Vendor B
- Given current bandwidth limits, setup complexity has immediate cost

## Recommendation
Choose Vendor A for the first rollout, with an explicit review point after initial internal adoption.

## Uncertainty / caveats
Final security review details are incomplete. Re-evaluate if a hard blocker appears during review.
