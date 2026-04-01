# Architecture Review

## System Design

The project follows a modular and reproducible architecture designed for clarity, scalability, and ease of use.

### Data Flow

Raw Data → Cleaning → Analysis → QA → Outputs → Dashboard

### Components

- **Raw Data**
  - Stored locally in `data/raw/`
  - Not included in version control

- **Data Processing (`src/`)**
  - `data_cleaning.py`: handles data parsing, standardization, and feature engineering
  - `analysis.py`: computes summary statistics and aggregations
  - `qa.py`: performs data validation checks
  - `visualization.py`: generates charts and figures
  - `run_pipeline.py`: orchestrates the full pipeline

- **Processed Data**
  - Saved to `data/processed/cleaned_code_violations.csv`

- **Outputs**
  - Tables saved in `outputs/tables/`
  - Figures saved in `outputs/figures/`

- **Dashboard (`app.py`)**
  - Built using Streamlit
  - Reads processed data
  - Displays:
    - summary metrics (rows, columns, closed cases)
    - violations by year
    - top violation types
    - top neighborhoods
    - open vs closed cases
    - average resolution time by neighborhood
    - preview table

---

## Design Rationale

The architecture emphasizes:

### Reproducibility
- The pipeline ensures consistent results from raw data to final outputs
- All transformations are explicitly defined in code

### Modularity
- Each component has a clear responsibility
- Easy to modify or extend individual modules

### Simplicity
- Minimal dependencies
- Easy setup and execution
- Suitable for non-expert users

### Data Integrity
- QA checks validate data quality
- Invalid or inconsistent values (e.g., negative resolution time) are handled explicitly

### Separation of Concerns
- Raw data, processed data, outputs, and code are clearly separated
- Prevents accidental data modification

---

## Scalability

The design allows for:
- adding new datasets
- extending analysis modules
- integrating additional visualizations
- deploying the dashboard to cloud platforms

---

## Summary

This architecture supports a clean, maintainable, and reproducible workflow.
