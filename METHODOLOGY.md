## Analytical Goal

The goal of this project is to produce a civic-facing, reproducible analysis of Syracuse housing code violations using publicly available data from the Syracuse Open Data portal.

The project focuses on identifying patterns in violation activity, case status, and resolution performance, while clearly communicating the limitations of the dataset.

---

## Data Processing Steps

The analysis follows a structured pipeline:

1. Load raw dataset from:
   `data/raw/Code_Violations.csv`

2. Parse date fields:
   - `open_date`
   - `violation_date`
   - `comply_by_date`
   - `status_date`

3. Standardize categorical fields:
   - `Neighborhood`
   - `status_type_name`
   - `Vacant`

4. Create derived features:
   - `year` → extracted from `violation_date`
   - `is_closed` → identifies closed cases
   - `resolution_days` → time difference between `status_date` and `violation_date`

---

## Exploratory Analysis

The project computes descriptive statistics including:

- violations by year  
- violations by neighborhood  
- top violation types  
- open vs closed case distribution  
- average resolution time for closed cases  

These summaries form the foundation for the dashboard visualizations.

---

## Additional Analysis

The final dashboard includes two operational metrics:

- **Open vs Closed Case Distribution**
- **Average Resolution Time by Neighborhood**

These metrics provide insight into system performance, not just violation frequency.

---

## Resolution Time Calculation

Resolution time is calculated as:
resolution_days = status_date − violation_date

- Computed only for closed cases  
- Negative values are treated as invalid and removed  
- Missing values are excluded from analysis  

---

## LLM Usage and Validation

Large language models (LLMs) were used for:

- drafting explanations  
- refining documentation  
- assisting with interpretation  

Validation approach:

- all numerical outputs are generated through code  
- LLM-generated statements are verified against computed results  
- narratives are treated as interpretive, not factual  

---

## Bias and Ethics

This analysis reflects reported housing code violations, not actual housing conditions.

Observed patterns may be influenced by:

- complaint-driven reporting  
- differences in inspection practices  
- administrative processes  
- data entry inconsistencies  

The project avoids causal claims and presents findings descriptively.

---

## Limitations

- The dataset does not capture all housing issues  
- Reporting bias may affect neighborhood comparisons  
- Case status may not reflect real-time conditions  
- Missing and inconsistent data may impact results  

---

## Success Criteria

The project is considered successful if it:

- runs end-to-end from raw data to dashboard  
- produces accurate and interpretable summaries  
- generates a functional interactive dashboard  
- clearly communicates assumptions and limitations  
- provides meaningful but responsible civic insights  
