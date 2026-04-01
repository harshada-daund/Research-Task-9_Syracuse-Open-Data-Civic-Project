## Architecture Overview

The project follows a modular and reproducible data pipeline:

**Raw Data → Cleaning → QA → Analysis → Outputs → Streamlit Dashboard**

This architecture ensures clear separation between data processing, validation, and presentation layers.

---

## Modules

### `src/data_cleaning.py`

Responsible for data preprocessing:

- standardizing column names  
- parsing date fields (`violation_date`, `status_date`, etc.)  
- cleaning categorical fields (`Neighborhood`, `status_type_name`, `Vacant`)  
- generating derived features:
  - `year`
  - `is_closed`
  - `resolution_days`  

---

### `src/analysis.py`

Performs aggregation and statistical analysis:

- violations by year  
- top violation types  
- top neighborhoods  
- open vs closed case summary  
- average resolution time by neighborhood  
- summary metrics (row count, column count, closed cases)  

---

### `src/visualization.py`

Generates static visual outputs:

- bar charts for:
  - violations by year  
  - violation types  
  - neighborhoods  
  - open vs closed cases  
  - resolution time  

- saves figures to `outputs/figures/`

---

### `src/qa.py`

Performs data validation checks:

- dataset size (rows, columns)  
- missing values  
- coordinate completeness  
- date parsing success  
- detection of invalid resolution values  

---

### `src/llm_validation.py`

Provides a framework for validating narrative claims:

- compares text statements against computed statistics  
- ensures consistency between analysis outputs and written interpretation  

---

### `src/run_pipeline.py`

Main pipeline entry point:

1. load raw dataset  
2. apply cleaning and feature engineering  
3. run QA checks  
4. compute summary tables  
5. generate visual outputs  
6. save processed dataset  

---

## Dashboard Components (`app.py`)

The Streamlit dashboard provides an interactive interface displaying:

- summary metrics:
  - total rows  
  - number of columns  
  - number of closed cases  

- visualizations:
  - violations by year  
  - top violation types  
  - top neighborhoods  
  - open vs closed case distribution  
  - average resolution time by neighborhood  

- data preview table for transparency  

---

## Data Flow

```

Raw CSV → Cleaning → QA → Analysis → Outputs → Dashboard

````

All transformations are reproducible and executed through the pipeline.

---

## Reproducibility

- Raw data is stored locally in `data/raw/` and not committed to GitHub  
- Processed outputs are generated entirely from code  
- `.gitignore` prevents accidental inclusion of:
  - datasets  
  - environment files  
  - temporary artifacts  

---

## Dependencies

Core libraries:

- pandas  
- numpy  
- matplotlib  
- plotly  
- streamlit  
- pytest  
- requests  

---

## Deployment Notes

### Local Execution

```bash
python -m src.run_pipeline --input data/raw/Code_Violations.csv --output-dir outputs --processed-dir data/processed
streamlit run app.py
````

---

### Potential Deployment Options

* Streamlit Community Cloud
* Render
* Azure App Service

---

## Summary

This technical architecture provides a clean, modular, and reproducible framework for analyzing and visualizing Syracuse housing code violations.

The design supports both academic evaluation and real-world usability while maintaining transparency and data integrity.

```
