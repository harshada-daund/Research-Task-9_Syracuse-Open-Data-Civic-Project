# Project Proposal

## Research Task 09 – Syracuse Open Data Civic Project

---

## Project Title

**A Descriptive Analysis of Housing Code Violations in Syracuse: Patterns, Limitations, and Data Quality**

---

## Project Summary

This project will analyze housing code violation data published on the Syracuse Open Data portal to explore temporal and neighborhood-level patterns in reported violations. The primary goal is to gain hands-on experience working with large, API-accessed municipal datasets while documenting the technical, analytical, and interpretive challenges that arise in real-world public data analysis. Rather than producing predictive models or policy prescriptions, the project emphasizes descriptive statistics, transparent documentation of data quality issues, and careful communication of uncertainty. Final deliverables will include a reproducible analysis pipeline, visualizations, and a professional analytical report suitable for inclusion in a personal data science portfolio.

---

## Problem Statement

Housing code violation data is often used as an indicator of housing conditions and neighborhood well-being. However, such data is typically generated through inspections and resident complaints, which introduces variability in reporting frequency, geographic coverage, and timing. Without careful analysis, neighborhood-level comparisons based on this data risk overstating what can be reliably concluded.

This project addresses the question: **What patterns are observable in Syracuse housing code violations across neighborhoods and over time, and what limitations constrain meaningful interpretation of these patterns?** By focusing on descriptive analysis and data quality assessment, the project aims to clarify what Syracuse Open Data can—and cannot—support in terms of neighborhood-level insight. Stakeholders who may benefit from this work include Syracuse residents, community organizations, researchers, and journalists seeking to responsibly interpret open civic data.

---

## Data Sources

### Primary Dataset

**Housing_Code_Violations** (Syracuse Open Data Portal)

**Description:**
This dataset contains records of housing code violations reported to the City of Syracuse Code Enforcement division. Each record represents an individual violation associated with a property, including violation type, reported date, status, and location information. This dataset will serve as the core source for time-series and neighborhood-level analysis.

**Observations & quality notes:**

* Includes categorical violation types, date fields, and location identifiers.
* Date fields require normalization due to mixed formats and missing values.
* Violation categories exhibit inconsistent labeling and legacy codes.
* Reporting is complaint-driven, introducing potential geographic and demographic bias.
* Some records contain incomplete or ambiguous location information.
* A stable unique identifier is available and will be used as the primary key.
* Dataset size necessitates API-based access rather than manual downloads.

---

### Supporting Dataset

**Neighborhood or Council District Boundaries** (Syracuse Open Data Portal)

**Description:**
This dataset provides official geographic boundaries for neighborhoods or council districts in Syracuse and will be used exclusively for aggregation and visualization purposes.

**Observations & quality notes:**

* Enables neighborhood-level summaries without exposing personally identifying information.
* Boundary definitions may not align perfectly with all violation records.
* Used only for aggregation; no advanced geospatial modeling will be performed.
* Boundary mismatches will be documented as part of the data quality assessment.

---

### Data Access & Handling

* All data will be accessed via the Syracuse Open Data API.
* Raw datasets will not be committed to the GitHub repository.
* Data acquisition and processing scripts will be provided for reproducibility.
* Any personally identifying information present in raw data will be excluded from outputs.

---

## Technical Approach

The analysis will follow a structured pipeline: API-based data acquisition → data cleaning → exploratory data analysis → aggregation → visualization → reporting. Python and Pandas will be used for data profiling, missingness analysis, time-based aggregation, and summary statistics. Visualizations will be created using standard Python visualization libraries to illustrate trends, distributions, and coverage diagnostics.

Large language models may be used to assist with exploratory hypothesis generation and narrative drafting for non-technical audiences. All LLM-generated statements will be validated against ground-truth calculations, with prompts, outputs, and validation steps documented explicitly. Techniques from prior research tasks, including prompt engineering, uncertainty communication, and bias detection, will be applied to ensure narratives do not imply causality or overstate certainty.

---

## Deliverable Description

The final deliverables will include:

* A fully reproducible analysis pipeline from raw API data to cleaned and analyzed outputs
* A written analytical report containing:

  * Data quality assessment
  * Descriptive statistics
  * 5–10 visualizations with interpretation
  * Explicit discussion of limitations and bias
* Documentation files (README.md, METHODOLOGY.md, TECHNICAL.md) detailing:

  * Analytical decisions
  * LLM usage and validation
  * Reproducibility instructions

---

## Success Criteria

The project will be considered successful if it:

* Successfully acquires and processes Syracuse Open Data via API
* Produces clear descriptive summaries of housing code violations
* Transparently documents data quality issues and analytical limitations
* Demonstrates validated and responsible use of LLM-assisted analysis
* Delivers professional-quality documentation and visualizations

---

## Timeline

| Weeks | Milestone                                                      |
| ----- | -------------------------------------------------------------- |
| 1–2   | Proposal finalization, dataset review, API testing             |
| 3–4   | Data acquisition, profiling, cleaning, data dictionary         |
| 5–6   | Exploratory data analysis and initial visualizations           |
| 7–8   | Neighborhood aggregation and LLM-assisted narrative generation |
| 9–10  | Bias analysis, limitation documentation, report drafting       |
| 11    | Validation, testing, documentation completion                  |
| 12    | Final polish and presentation preparation                      |

---

## Risks and Mitigations


**Risk:** Complaint-driven reporting introduces bias
**Mitigation:** Avoid causal claims; explicitly document reporting limitations

**Risk:** Uneven neighborhood coverage leads to misleading comparisons
**Mitigation:** Produce coverage diagnostics and frame findings descriptively

**Risk:** LLM-generated narratives introduce framing or hallucination risk
**Mitigation:** Validate all LLM outputs against computed statistics and label LLM-assisted content

**Risk:** Time constraints across multi-week phases
**Mitigation:** Maintain narrow scope; prioritize core deliverables over optional extensions
