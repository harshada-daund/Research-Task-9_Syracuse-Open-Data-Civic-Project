# Architecture Review

## System Design
- Raw data stored locally outside version control
- Modular processing in `src/`
- Streamlit dashboard reads processed CSV
- Outputs saved as figures and tables

## Design Rationale
The design emphasizes reproducibility, low operational complexity, and easy handoff to a non-expert reviewer.
