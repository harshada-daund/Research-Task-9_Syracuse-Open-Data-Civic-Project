# Task_09_Syracuse_Open_Data_Civic_Project

## Phase 1 – Project Framing & Data Selection (Weeks 1–2)

During Phase 1, the project focused on defining a clear civic-technology question grounded in real-world housing accountability: what publicly reported housing code violations can reveal about patterns in housing-related issues and how they are handled administratively over time in Syracuse.

The work began by surveying the City of Syracuse Open Data portal and selecting the Housing Code Violations dataset as a suitable source because it is structured, machine-readable, and directly connected to housing quality, neighborhood conditions, and municipal enforcement practices. A key emphasis in this phase was clarifying that violation records reflect reported or observed issues and administrative actions rather than a comprehensive measure of housing conditions across the city, which affects how trends and resolution timelines should be interpreted.

Phase 1 also documented initial ethical and bias considerations, including uneven inspection practices, administrative lag between violation identification and closure, and the limitations of drawing strong conclusions without additional contextual or demographic data. Finally, this phase established reproducible workflow conventions—such as a raw/processed data directory structure, notebook-based analysis, and a clear separation between data transformation, visualization, and narrative explanation—to support transparency, auditability, and future extensibility of the project.

---

## Phase 2 – Exploration & Visual Analytics (Weeks 3–4)

Phase 2 translated the conceptual framing into hands-on exploratory data analysis using the Housing Code Violations CSV in a Jupyter notebook environment. The work started with careful data validation, including refining a column-by-column data dictionary, parsing and standardizing violation and status dates, normalizing categorical fields such as violation descriptions and neighborhood names, and quantifying missingness in administrative and resolution-related fields.

Building on this foundation, Phase 2 implemented a set of core visualizations to construct a multi-angle view of housing code enforcement activity, including violations reported per year, open versus closed violations, the most common violation categories, neighborhood-level distributions, and resolution timelines for closed cases where valid data exists. Each visualization was paired with interpretation text that foregrounded uncertainty, particularly the effects of partial temporal coverage and missing closure information on any conclusions about enforcement efficiency or housing conditions.

---

## Phase 3 – Development Overview (Weeks 5–6)

In Phase 3, the project evolves from exploratory analysis into a reproducible, testable analysis pipeline for the Housing Code Violations dataset, with a clear focus on software engineering practices and responsible use of civic data.

The repository is organized into distinct layers: `data/` for raw and processed CSVs (excluded from version control), `src/` for pipeline code handling data acquisition, cleaning, analysis, visualization, and validation, and `notebooks/` for narrative and exploratory work. The core pipeline loads the raw CSV, applies standardized cleaning and transformation steps—including date parsing, open/closed status flags, yearly aggregation, category normalization, and resolution time calculation—and produces a processed dataset used consistently across all analyses and visualizations.

Phase 3 also introduces quality assurance practices. Key transformations are validated using assertions and consistency checks, derived metrics explicitly respect known data limitations such as missing closure dates, and plotting logic includes safeguards for empty or incomplete subsets. Exploratory visualizations developed in Phase 2 are refactored into reusable plotting functions, positioning the project for future dashboard development or automation while maintaining transparency and reproducibility.

---

## Phase 3 - Enhancements (Week 7–8)

During Weeks 7–8, the project was strengthened to improve reproducibility, validation, and documentation:

- Added a reproducible pipeline runner (`src/run_pipeline.py`) to execute the full workflow end-to-end.
- Implemented quality assurance checks in `src/qa.py` to validate cleaned data and catch edge cases.
- Ensured all tables and plots are saved to the `outputs/` directory for reproducible presentation.
- Replaced placeholder LLM validation logic with checks grounded in computed metrics.
- Added minimal unit tests under the `tests/` directory to validate critical transformations.

---
## Phase 3 – Testing & Feature Completion (Weeks 9–10)

Weeks 9–10 finalized Phase 3 by hardening the Syracuse Open Data Housing Violations analysis pipeline and declaring the project feature-complete. This period focused on expanding unit and integration tests for all critical transformations (safe datetime parsing, open vs. closed case logic, resolution time calculations, and aggregation logic feeding summary tables and visualizations), adding automated validation summaries for data quality, and strengthening edge-case handling for empty datasets, missing closure dates, malformed categorical fields, and sparse neighborhood groupings. The reproducible pipeline was stabilized with clear QA checks and explicit warnings for anomalous conditions, ensuring reliable end-to-end execution from raw data ingestion through saved outputs. Documentation was brought to submission quality with an updated README, clarified architecture notes, QA documentation, and a clearly stated limitations section. By the end of Week 10, the project delivered a fully reproducible, well-tested civic data analysis pipeline that cleanly separates acquisition, cleaning, analysis, and presentation, providing a strong foundation for future enhancements such as dashboard deployment or advanced analytics.

---
## Phase 4 – Final Review & Project Consolidation (Weeks 11–12)

Weeks 11–12 focused on reviewing, stabilizing, and consolidating the Syracuse Open Data Housing Violations analysis project. During this period, I re-ran the full pipeline to confirm reproducibility from raw data ingestion through cleaning, validation, analysis, and saved outputs. I reviewed unit tests and QA checks to ensure coverage of key transformations, including date parsing, open vs. closed classification, and resolution time calculations.

I refined the codebase for clarity and maintainability by confirming proper separation between acquisition, transformation, analysis, validation, and presentation modules. Minor improvements were made to enhance readability and reduce redundancy. Documentation was carefully aligned with the implemented architecture to ensure consistency between described system design and actual code structure.

This phase emphasized stability, reproducibility verification, and preparation for future enhancements. By the end of Week 12, the project stands as a fully reproducible, validated, and well-documented civic data analysis pipeline, ready for potential future extensions such as advanced analytics or interactive visualization.
