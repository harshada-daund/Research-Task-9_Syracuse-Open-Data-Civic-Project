# Syracuse Housing Code Violations Dashboard  
**Research Task 09 – Civic Data Capstone**

---

## Overview

This project analyzes housing code violation data from the Syracuse Open Data portal to identify trends in violation activity, neighborhood patterns, case status, and resolution performance.

The goal is to transform a large, real-world municipal dataset into clear, accessible insights through a reproducible data pipeline and an interactive dashboard.

---

## Problem

Housing code violations are often used to understand housing conditions and neighborhood well-being. However, these records are influenced by reporting behavior, inspection practices, and administrative processes.

Without careful analysis, comparisons across neighborhoods may be misleading.

This project addresses:

**How can housing code violation data be analyzed responsibly to provide meaningful civic insights while acknowledging its limitations?**

---

## Data

- Source: Syracuse Open Data  
- Dataset: Code Violations  
- Size: 143,470 records, 28 columns  

Key fields:
- violation type  
- violation date  
- case status  
- neighborhood  
- location data  

---

## Approach

The project follows a structured pipeline:

**Raw Data → Cleaning → Analysis → QA → Outputs → Dashboard**

Key steps:
- data cleaning and standardization  
- feature engineering (year, case status, resolution time)  
- aggregation and statistical summaries  
- visualization and dashboard development  

---

## Dashboard Features

The Streamlit dashboard includes:

- Violations by Year  
- Top Violation Types  
- Top Neighborhoods  
- Open vs Closed Cases  
- Average Resolution Time by Neighborhood  
- Data Preview Table  

---

## Key Insights

- Violation activity varies across time  
- A small number of violation types dominate  
- Some neighborhoods have higher violation counts  
- Most cases are closed  
- Resolution time differs across neighborhoods  

---

## Impact

This project provides:

- transparent view of housing code violations  
- insight into neighborhood-level patterns  
- understanding of system performance  
- a reusable framework for civic data analysis  

Stakeholders include residents, community organizations, researchers, and policymakers.

---

## Limitations

- dataset reflects reported violations only  
- reporting bias may affect results  
- no causal conclusions are made  
- missing data and inconsistencies exist  

---

## Deliverables

- reproducible data pipeline  
- interactive dashboard  
- analytical documentation  
- presentation materials  

---

## Conclusion

This project demonstrates how open civic data can be transformed into meaningful, responsible insights through data engineering, analysis, and visualization, while maintaining transparency about limitations and uncertainty.
