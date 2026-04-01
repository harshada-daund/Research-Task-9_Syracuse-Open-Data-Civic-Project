## Analytical Goal
The purpose of this project is to produce a civic-facing summary of Syracuse housing code violations using public data from the Syracuse Open Data portal.

## Data Processing Steps
1. Read the raw CSV from `data/raw/Code_Violations.csv`
2. Parse date fields:
   - `open_date`
   - `violation_date`
   - `comply_by_date`
   - `status_date`
3. Standardize selected categorical fields:
   - `Neighborhood`
   - `status_type_name`
   - `Vacant`
4. Derive analysis fields:
   - `year`
   - `is_closed`
   - `resolution_days`

## Exploratory Analysis
The project computes:
- counts by year
- counts by neighborhood
- counts by violation type
- open/closed status distribution
- average resolution time for closed cases

## Additional Analysis
The dashboard includes two operational metrics:
- Open vs Closed case distribution
- Average resolution time by neighborhood for closed cases

Resolution time was calculated as the difference in days between `status_date` and `violation_date` for closed cases. Negative values were treated as invalid and excluded from aggregate summaries.

## LLM Usage and Validation
LLMs were used only for:
- drafting narrative summaries
- brainstorming hypotheses
- improving stakeholder-oriented wording

Validation approach:
- all numeric claims should be checked against the pipeline outputs
- narrative claims are treated as suggestions, not facts
- no claim should appear in the final report unless it can be traced back to a generated summary table or chart

## Bias and Ethics
This project documents housing-code activity, not intrinsic neighborhood quality. Reported patterns may reflect:
- differences in reporting behavior
- inspection intensity
- data-entry practices
- timing and case-closure procedures

For that reason, results are framed descriptively and carefully. The project avoids overclaiming and does not make causal or predictive statements.

## Limitations
- The dataset does not include every contextual factor needed to explain violations.
- Case status may lag behind on-the-ground conditions.
- Missing values and category inconsistencies may affect summaries.

## Success Criteria
A successful project:
- runs end-to-end from raw CSV to dashboard
- produces readable summary tables and figures
- documents assumptions clearly
- communicates limits honestly
