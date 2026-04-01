# Project Proposal

## Research Task 09 – Syracuse Open Data Civic Project

---

## Project Title

**A Descriptive Analysis of Housing Code Violations in Syracuse: Patterns, System Performance, and Data Limitations**

---

## Project Summary

This project analyzes housing code violation data from the Syracuse Open Data portal to explore temporal trends, neighborhood-level patterns, case status distribution, and resolution performance.

The primary goal is to transform a large, real-world municipal dataset into clear, interpretable insights through a reproducible data pipeline and an interactive dashboard. The project emphasizes descriptive analysis, transparency in data quality issues, and responsible interpretation of civic data.

In addition to statistical summaries, the project includes a Streamlit dashboard that allows users to explore violation trends, compare neighborhoods, and evaluate operational metrics such as case closure rates and resolution time.

---

## Problem Statement

Housing code violation data is often used as a proxy for housing conditions and neighborhood well-being. However, such data is typically complaint-driven and influenced by reporting behavior, inspection practices, and administrative processes.

Without careful analysis, comparisons across neighborhoods may be misleading or incomplete.

This project addresses the question:

**What patterns are observable in Syracuse housing code violations across neighborhoods and over time, and what do case status and resolution time reveal about system performance, while accounting for the limitations of the dataset?**

The project aims to provide insights while clearly communicating what the data can—and cannot—support.

---

## Data Sources

### Primary Dataset

**Housing Code Violations (Syracuse Open Data Portal)**

This dataset contains records of housing code violations reported to the City of Syracuse Code Enforcement division.

Each record includes:
- violation type
- violation date
- status information
- location data (neighborhood, coordinates)

**Data Characteristics:**
- Over 140,000 records and multiple attributes
- Contains categorical, temporal, and geographic fields
- Includes case status and resolution timing information

**Data Quality Considerations:**
- Mixed date formats and missing values
- Inconsistent violation labeling
- Complaint-driven reporting introduces bias
- Some incomplete or ambiguous location data

---

### Supporting Dataset

**Neighborhood Boundaries (Syracuse Open Data Portal)**

Used for aggregation and visualization of neighborhood-level patterns.

---

### Data Access

- Data is accessed via the Syracuse Open Data API  
- Raw datasets are not stored in the repository  
- Processing scripts ensure reproducibility  

---

## Technical Approach

The project follows a structured pipeline:

Raw Data → Cleaning → Analysis → QA → Outputs → Dashboard

### Key Steps

- Data acquisition via API  
- Data cleaning and standardization  
- Feature engineering:
  - year
  - case status (open vs closed)
  - resolution time  
- Exploratory data analysis  
- Aggregation and summary statistics  
- Visualization and dashboard development  

### Dashboard

An interactive Streamlit dashboard is developed to present:

- Violations by Year  
- Top Violation Types  
- Top Neighborhoods  
- Open vs Closed Cases  
- Average Resolution Time by Neighborhood  
- Data Preview  

---

## Use of LLMs

Large language models may be used for:

- drafting explanations  
- generating narrative summaries  
- assisting with documentation  

All outputs are validated against computed statistics.  
No LLM-generated content is treated as ground truth.

---

## Deliverables

- Reproducible Python data pipeline  
- Cleaned dataset and summary outputs  
- Interactive Streamlit dashboard  
- Analytical report including:
  - data quality assessment  
  - visualizations  
  - interpretation  
- Documentation:
  - README.md  
  - TECHNICAL.md  
  - METHODOLOGY.md  

---

## Success Criteria

The project is successful if it:

- Successfully processes raw Syracuse Open Data  
- Produces clear descriptive summaries and visualizations  
- Builds a fully functional dashboard  
- Communicates operational insights such as:
  - case closure rates  
  - resolution time differences  
- Transparently documents data limitations  
- Demonstrates responsible use of LLMs  

---

## Expected Impact

This project provides:

- Greater transparency into housing code violations  
- Insight into neighborhood-level patterns  
- Understanding of system performance (closure rates and resolution time)  
- A reproducible framework for civic data analysis  

Stakeholders include:
- Syracuse residents  
- community organizations  
- researchers and journalists  
- policymakers  

---

## Timeline

| Weeks | Milestone |
|------|----------|
| 1–2 | Proposal and data exploration |
| 3–4 | Data cleaning and preprocessing |
| 5–6 | Exploratory analysis |
| 7–8 | Dashboard development |
| 9–10 | Bias and limitation analysis |
| 11 | Documentation and validation |
| 12 | Final submission |

---

## Risks and Mitigations

**Risk:** Reporting bias in complaint-driven data  
**Mitigation:** Avoid causal claims; clearly document limitations  

**Risk:** Misleading neighborhood comparisons  
**Mitigation:** Frame results descriptively and include caveats  

**Risk:** Data quality issues  
**Mitigation:** Apply cleaning, validation, and QA checks  

**Risk:** LLM hallucination  
**Mitigation:** Validate all outputs against computed data  

---

## Summary

This project transforms Syracuse housing code violation data into an accessible and interpretable analytical tool.

By combining data engineering, statistical analysis, and interactive visualization, the project provides meaningful civic insights while maintaining transparency about data limitations and uncertainty.
