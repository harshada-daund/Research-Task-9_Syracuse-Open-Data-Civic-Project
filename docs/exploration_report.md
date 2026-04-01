# Exploration Report

## Data Quality

The Syracuse Code Violations dataset contains multiple date fields, geographic coordinates, neighborhood labels, and violation descriptions.

Key data preparation steps included:
- Parsing date fields (`violation_date`, `status_date`, etc.)
- Handling missing values in categorical fields such as `Neighborhood`
- Standardizing text fields (e.g., violation types, status labels)
- Creating derived variables:
  - `year` (from violation date)
  - `is_closed` (based on status)
  - `resolution_days` (difference between status and violation dates)

Some challenges observed:
- Missing or inconsistent neighborhood values
- Null or invalid date entries
- Occasional negative resolution times due to inconsistent timestamps

---

## Initial Findings

Based on exploratory analysis:

- **Violation activity spans multiple years**, with noticeable variation over time  
- A **small number of violation types dominate** the dataset  
- Certain neighborhoods (e.g., Northside) have significantly higher violation counts  
- **Most cases are closed**, indicating active resolution processes  
- **Resolution time varies across neighborhoods**, suggesting differences in enforcement or case complexity  

---

## Alignment with Dashboard

These findings directly informed the final dashboard visualizations:

- Violations by Year → trend analysis  
- Top Violation Types → frequency analysis  
- Top Neighborhoods → geographic distribution  
- Open vs Closed Cases → system performance  
- Average Resolution Time → operational efficiency  

---

## Planned Follow-Up

Further analysis opportunities include:

- Deeper comparison of open vs closed case patterns  
- Investigating factors affecting resolution time  
- Incorporating additional datasets (e.g., housing, demographics)  
- Enhancing validation and narrative consistency  

---

## Summary

The exploratory phase established a strong foundation for the project by identifying key patterns in violation activity, confirming data limitations, and guiding the design of the final dashboard.

The analysis remains descriptive and focused on identifying trends rather than making causal claims.
