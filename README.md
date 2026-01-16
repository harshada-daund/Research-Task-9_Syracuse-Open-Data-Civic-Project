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
