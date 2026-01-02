# Phase 2: Data Acquisition and Exploration (Weeks 3–4)
**Research Task 09: Syracuse Open Data Civic Project**

**Project Title:** A Descriptive Analysis of Housing Code Violations in Syracuse  
**Dataset:** Code Violations (City of Syracuse Open Data Portal)

---

## 1. Data Acquisition & Validation

### 1.1 Dataset Acquisition

- **Source:** City of Syracuse Open Data Portal (data.syr.gov)
- **Dataset Name:** Code Violations
- **Dataset URL:** https://data.syr.gov/datasets/107745f070b049feb38273a7ab200487_0/explore
- **Data Format:** CSV
- **Acquisition Method:** Manual CSV export from the Open Data portal
- **Acquisition Date:** Recorded at time of download
- **API Usage:** Although the dataset supports API access, Phase 2 uses a static CSV to simplify reproducibility during exploratory analysis.

**Planned Storage Structure:**
```

data/
├── raw/
│   └── Code_Violations.csv
├── processed/
│   └── code_violations_clean.csv

```

The raw CSV file is preserved unchanged to ensure auditability and reproducibility. All data cleaning and transformations are applied only to derived datasets.

---

## 2. Data Dictionary (Refined from CSV Columns)

| Column Name | Description |
|------------|------------|
| ObjectId | Unique identifier for each violation record |
| violation | Text description of the housing code violation |
| violation_code | Code representing the violation type |
| open_date | Date the violation was opened |
| violation_date | Date the violation was recorded |
| status_type_name | Current status (e.g., Open, Closed) |
| status_date | Date when the current status was applied |
| Neighborhood | Neighborhood or district name (if present) |
| Council District | City council district |
| zipcode | ZIP code of the property |
| Latitude | Latitude coordinate (if present) |
| Longitude | Longitude coordinate (if present) |

*Note: Not all columns were used in the core exploratory analysis. No personally identifying information is included in analysis outputs.*

---

## 3. Data Quality Assessment

### 3.1 Missing Values

- `status_date`, `open_date`, and `violation_date` contain missing or malformed values.
- A substantial portion of records are marked as open and therefore lack closure dates.
- Neighborhood identifiers are missing for some records, particularly older entries.

**Impact:**
- Resolution-time analysis is limited to closed cases with valid date information.
- Neighborhood-level comparisons require explicit acknowledgment of uneven coverage.
- Recent time periods must be labeled as incomplete.

---

### 3.2 Inconsistencies & Formatting Issues

**Date Fields**
- Date strings appear in mixed formats and require normalization.
- Invalid or missing values are coerced to null rather than removed.

**Categorical Fields**
- Inconsistent capitalization and spelling in `violation` and `status_type_name`.
- Neighborhood labels vary in formatting.

**Mitigation Steps**
- Standardized all date fields using Pandas datetime parsing.
- Normalized text fields via lowercasing and trimming.
- Created derived indicator variables (e.g., `Is_Open`) instead of overwriting raw fields.

---

### 3.3 Temporal Coverage

- The dataset spans multiple years with increased reporting in more recent periods.
- Recent years have a high proportion of open cases, indicating administrative lag.

**Implications**
- Annual comparisons for recent periods are incomplete.
- Closure-based metrics are restricted to closed records.

---

### 3.4 Geographic Coverage

- Neighborhood and council district coverage is uneven.
- Some areas are underrepresented due to missing or inconsistent reporting.

**Conclusion**
Geographic patterns are interpreted descriptively and do not support strong inferential claims.

---

## 4. Documented Limitations & Bias Risks

### 4.1 What the Data Cannot Answer

- The dataset does not directly measure housing quality or safety outcomes.
- It cannot distinguish increased enforcement from increased violations.
- It does not explain underlying causes for neighborhood-level differences.

### 4.2 Structural Biases

- Reporting is complaint- and inspection-driven.
- Enforcement intensity and public awareness vary by area.
- Status updates may lag actual case resolution.

**Conclusion**
All findings are framed as descriptive and exploratory rather than causal.

---

## 5. Exploratory Data Analysis (Grounded & Reproducible)

All exploratory analysis was conducted in a Jupyter notebook using Pandas for data processing and Matplotlib/Seaborn for visualization.

### 5.1 Summary Statistics

Key metrics computed include:
- Total violations per year
- Open versus closed violations over time
- Most common violation descriptions
- Violations by neighborhood
- Resolution time (days) for closed cases only

---

### 5.2 Initial Visualizations

#### Chart 1 — Housing Code Violations per Year
**Interpretation:**  
Reported violations increase over time. The most recent year contains many open cases and should be treated as incomplete.

#### Chart 2 — Top Violation Types
**Interpretation:**  
A small number of violation categories account for a large share of records. Text normalization was required to consolidate similar labels.

#### Chart 3 — Open vs Closed Violations by Year
**Interpretation:**  
Recent periods show a higher proportion of open cases, consistent with reporting and processing lag.

#### Chart 4 — Violations by Neighborhood
**Interpretation:**  
Certain neighborhoods show higher counts, though uneven coverage limits direct comparison.

#### Chart 5 — Resolution Time Distribution (Closed Cases Only)
**Interpretation:**  
Resolution times are right-skewed, with most cases resolving within a moderate timeframe and a smaller number taking substantially longer.

---

## 6. LLM-Assisted Analysis (Controlled & Validated)

### 6.1 Hypothesis Generation

Large language models were used to suggest exploratory hypotheses, including:
- Certain violation types take longer to resolve.
- Reporting patterns vary across neighborhoods.
- Resolution timelines differ across time periods.

### 6.2 Validation Against Ground Truth

All LLM-generated claims were validated against Pandas-based calculations and visual evidence. Unsupported claims were removed or reframed as inconclusive.

### 6.3 Bias & Framing Checks

- Prompts avoided causal or evaluative language.
- Alternative prompt phrasing was tested to detect narrative drift.
- LLMs were instructed not to speculate on demographic or socioeconomic factors.

---

## 7. Key Findings & Hypotheses for Phase 3

- **Reporting Lag:** A large portion of recent violations remain open due to administrative lag.
- **Category-Level Differences:** Some violation types exhibit longer median resolution times.
- **Geographic Variation:** Neighborhood-level differences exist but must be interpreted cautiously.

These findings will inform Phase 3 development, including pipeline refinement and dashboard design.

---

## Appendix: Summary of Chart Generation Workflow

All visualizations follow a consistent workflow:
1. Date parsing and text normalization
2. Creation of derived variables (`Year`, `Is_Open`, `Resolution_Days`)
3. Aggregation using Pandas groupby operations
4. Visualization with clear titles and labels
5. Interpretation with explicit caveats

---
