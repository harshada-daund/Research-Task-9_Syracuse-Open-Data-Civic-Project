# Phase 3: Architecture Review (Weeks 5–6)
Research Task 09 – Syracuse Open Data Civic Project

## Project Title
A Descriptive Analysis of Housing Code Violations in Syracuse

---

## 1. System Architecture Overview

### High-Level Data Flow
1. Data acquisition from Syracuse Open Data (CSV export or API-ready)
2. Data cleaning and normalization
3. Exploratory and descriptive analysis
4. Visualization and narrative interpretation
5. Validation and documentation of limitations


---

## 2. Repository Structure

```

.
├── Project Proposal.md
├── Phase_2_Exploration_Report.md
├── Phase_3_Architecture_Review.md
├── notebooks/
│   ├── Phase_2_Exploration.ipynb
│   └── Phase_3_Pipeline_and_EDA_UPDATED.ipynb
├── src/
│   ├── data_acquisition.py
│   ├── data_cleaning.py
│   ├── analysis.py
│   ├── visualization.py
│   └── llm_validation.py
├── requirements.txt
└── .gitignore

```


---

## 3. Data Acquisition Layer

**Module:** `src/data_acquisition.py`

- Loads housing code violations data from a local CSV file exported from the Syracuse Open Data Portal.
- Designed to be API-compatible if transitioned in future phases.
- Raw data is not modified and is excluded from version control.


---

## 4. Data Cleaning & Transformation

**Module:** `src/data_cleaning.py`

Primary transformations include:
- Standardizing date fields and coercing invalid values to null
- Creating derived variables such as:
  - `Year`
  - `Is_Open`
  - `Resolution_Days`
- Normalizing text fields for violation types and neighborhoods
- Preserving original fields while operating on cleaned copies


---

## 5. Analysis Layer

**Module:** `src/analysis.py`

Implements descriptive, non-causal analyses including:
- Violations per year
- Open vs closed case counts
- Most frequent violation categories
- Neighborhood-level distributions
- Resolution time summaries (where valid)


---

## 6. Visualization Layer

**Module:** `src/visualization.py`

- Uses Matplotlib exclusively to avoid environment dependency issues
- Generates bar charts and histograms used in exploratory analysis
- Includes guarded logic to prevent plotting when data is missing or insufficient

Example:
- Resolution time plots are skipped when no valid closed cases exist


---

## 7. LLM Integration & Validation

**Module:** `src/llm_validation.py`

Large Language Models (LLMs) are used in a controlled manner to:
- Generate exploratory hypotheses
- Assist with narrative clarity and documentation

Validation safeguards include:
- All LLM-generated claims are checked against Pandas computations
- Unsupported or speculative statements are removed or reframed
- Prompts are written to avoid causal or demographic speculation

LLMs do not replace analysis and are not treated as authoritative sources.

---

## 8. Quality Assurance

Quality assurance measures include:
- Assertions verifying required columns exist
- Checks ensuring resolution days are non-negative
- Guarded plotting logic for empty subsets
- Explicit documentation of missing or incomplete data


---

## 9. Dependencies & Environment

**Dependencies (requirements.txt):**
```

pandas
numpy
matplotlib
jupyter

```


---

## 10. Current Progress & Blockers

### Progress
- Complete Phase 3 pipeline implementation
- Reproducible notebook execution
- Expanded EDA with multiple visualizations
- Architecture and QA fully documented

### Blockers
- Resolution-time analysis is limited due to missing or incomplete closure dates
- Neighborhood coverage is uneven across records

