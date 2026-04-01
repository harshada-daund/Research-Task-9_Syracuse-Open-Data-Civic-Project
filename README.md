# Syracuse Housing Code Violations Dashboard

## Overview
This project is an independent civic data capstone built with Syracuse Open Data. It analyzes Syracuse housing code violations to identify neighborhood patterns, high-frequency violation types, open-versus-closed case patterns, and citywide trends over time.

The project also evaluates operational performance by analyzing case closure rates and resolution time across neighborhoods.

The final deliverable is a reproducible analysis pipeline and an interactive Streamlit dashboard that can be used by residents, community groups, journalists, and city stakeholders to better understand housing-code enforcement activity in Syracuse.

---

## Problem Statement

Housing conditions affect safety, neighborhood quality of life, and public accountability. The Syracuse Code Violations dataset makes it possible to explore where violations are concentrated, what kinds of property issues are most common, and whether some neighborhoods appear to carry a heavier burden of unresolved cases.

This project answers the question:

**How are Syracuse housing code violations distributed across neighborhoods and time, and what patterns in violation type, case status, and resolution time are most useful for public understanding and civic decision-making?**

---

## Stakeholders

- Syracuse residents  
- Community organizations  
- Journalists and researchers  
- City officials and policy staff  

---

## Dataset

- **Source:** Syracuse Open Data  
- **Dataset:** Code Violations  
- **Expected file path:** `data/raw/Code_Violations.csv`  

### Key fields used

- `complaint_address`  
- `violation`  
- `violation_date`  
- `open_date`  
- `comply_by_date`  
- `status_type_name`  
- `status_date`  
- `Neighborhood`  
- `Vacant`  
- `Latitude`  
- `Longitude`  

---

## Features

The dashboard includes:

- Violations by Year  
- Top Violation Types  
- Top Neighborhoods  
- Open vs Closed Case Summary  
- Average Resolution Time by Neighborhood  
- Interactive Neighborhood Filter  
- Data Preview Table  

---

## Final Dashboard Snapshot

The current final dashboard version shows:

- **143,470 rows**  
- **28 columns**  
- **125,266 closed cases**  

It includes charts for:

- Violations by Year  
- Top Violation Types  
- Top Neighborhoods  
- Open vs Closed Cases  
- Average Resolution Time by Neighborhood  
- Preview table  

---

## Repository Structure

```

.
├── app.py
├── requirements.txt
├── README.md
├── TECHNICAL.md
├── METHODOLOGY.md
├── Project Proposal.md
├── One-Page Poject Summary.md
├── docs/
│   ├── data_dictionary.md
│   ├── exploration_report.md
│   ├── architecture_review.md
│   └── demo_script.md
├── src/
│   ├── data_cleaning.py
│   ├── analysis.py
│   ├── visualization.py
│   ├── qa.py
│   ├── llm_validation.py
│   └── run_pipeline.py
├── tests/
│   ├── conftest.py
│   ├── test_analysis.py
│   └── test_cleaning.py
├── data/
│   ├── raw/
│   └── processed/
└── outputs/
├── figures/
└── tables/

````

---

## How to Run

### 1) Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
# or
.venv\Scripts\activate      # Windows
````

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Add the Syracuse CSV

Save your dataset as:

```
data/raw/Code_Violations.csv
```

### 4) Run the pipeline

```bash
python -m src.run_pipeline --input data/raw/Code_Violations.csv --output-dir outputs --processed-dir data/processed
```

### 5) Launch the dashboard

```bash
streamlit run app.py
```

---

## Outputs

The pipeline writes:

* `data/processed/cleaned_code_violations.csv`

* `outputs/tables/summary_metrics.csv`

* `outputs/tables/violations_by_year.csv`

* `outputs/tables/top_violation_types.csv`

* `outputs/tables/top_neighborhoods.csv`

* `outputs/tables/status_summary.csv`

* `outputs/tables/avg_resolution_by_neighborhood.csv`

* `outputs/tables/qa_report.csv`

* `outputs/figures/violations_by_year.png`

* `outputs/figures/top_violation_types.png`

* `outputs/figures/top_neighborhoods.png`

* `outputs/figures/open_vs_closed_cases.png`

* `outputs/figures/avg_resolution_by_neighborhood.png`

These outputs directly power the dashboard visualizations and ensure reproducibility of results.

---

## LLM Integration

LLMs were used in a limited and controlled manner to support narrative framing and documentation.

* LLM outputs were not treated as ground truth
* All insights were validated against computed statistics

---

## Limitations

* The dataset reflects reported violations, not all housing issues
* Differences across neighborhoods may reflect reporting patterns and enforcement practices
* The analysis is descriptive and does not establish causality

---

## Ethical Considerations

* No raw dataset is committed to the repository
* Analysis focuses on aggregated patterns
* Results are presented carefully to avoid misinterpretation

---

## Pain Points and Workarounds

### Challenges

* Missing and inconsistent data
* Mixed date formats
* Complaint-driven reporting bias
* Invalid resolution times

### Workarounds

* Data cleaning and standardization
* QA validation checks
* Exclusion of invalid values
* Modular pipeline design

---

## Submission Notes

This project aligns with Research Task 9 requirements:

* reproducible analysis pipeline
* stakeholder-facing dashboard
* technical documentation
* methodology documentation
* presentation materials

The dashboard serves as the primary stakeholder-facing deliverable for this project.
