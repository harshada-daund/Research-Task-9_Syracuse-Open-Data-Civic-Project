import os
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Syracuse Housing Code Violations Dashboard", layout="wide")

st.title("Syracuse Housing Code Violations Dashboard")
st.caption("Research Task 9 civic data deliverable")

processed_path = "data/processed/cleaned_code_violations.csv"

if not os.path.exists(processed_path):
    st.error("Processed data not found. Run the pipeline first.")
    st.code("python -m src.run_pipeline --input data/raw/Code_Violations.csv --output-dir outputs --processed-dir data/processed")
    st.stop()

df = pd.read_csv(
    processed_path,
    parse_dates=["open_date", "violation_date", "comply_by_date", "status_date"],
    low_memory=False
)

for col in ["Neighborhood", "violation", "status_type_name"]:
    if col in df.columns:
        df[col] = df[col].fillna("Unknown").astype(str).str.strip()

if "status_type_name" in df.columns:
    df["is_closed"] = df["status_type_name"].str.lower().eq("closed")
else:
    df["is_closed"] = False

if "resolution_days" not in df.columns and {"status_date", "violation_date"}.issubset(df.columns):
    df["resolution_days"] = (df["status_date"] - df["violation_date"]).dt.days
    df.loc[df["resolution_days"] < 0, "resolution_days"] = pd.NA

neighborhoods = sorted([n for n in df["Neighborhood"].dropna().unique().tolist() if str(n).strip()])
selected = st.multiselect("Filter by neighborhood", neighborhoods)

view = df[df["Neighborhood"].isin(selected)].copy() if selected else df.copy()

rows_count = len(view)
cols_count = view.shape[1]
closed_count = int(view["is_closed"].fillna(False).sum())

c1, c2, c3 = st.columns(3)
c1.metric("Rows", f"{rows_count:,}")
c2.metric("Columns", f"{cols_count:,}")
c3.metric("Closed cases", f"{closed_count:,}")

st.markdown("---")

year_counts = (
    view.dropna(subset=["year"])
    .groupby("year", as_index=False)
    .size()
    .rename(columns={"size": "violations"})
    .sort_values("year")
)

top_violation_types = (
    view["violation"]
    .fillna("Unknown")
    .value_counts()
    .head(10)
    .reset_index()
)
top_violation_types.columns = ["violation", "count"]

top_neighborhoods = (
    view["Neighborhood"]
    .fillna("Unknown")
    .value_counts()
    .head(10)
    .reset_index()
)
top_neighborhoods.columns = ["Neighborhood", "count"]

row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("Violations by Year")
    if not year_counts.empty:
        fig_year = px.bar(
            year_counts,
            x="year",
            y="violations",
            labels={"year": "Year", "violations": "Violations"}
        )
        st.plotly_chart(fig_year, use_container_width=True)
    else:
        st.info("No year data available for the current filter.")

with row1_col2:
    st.subheader("Top Violation Types")
    fig_types = px.bar(
        top_violation_types,
        x="violation",
        y="count",
        labels={"violation": "Violation", "count": "Count"}
    )
    fig_types.update_layout(xaxis_tickangle=-35)
    st.plotly_chart(fig_types, use_container_width=True)

st.subheader("Top Neighborhoods")
fig_neighborhoods = px.bar(
    top_neighborhoods,
    x="Neighborhood",
    y="count",
    labels={"Neighborhood": "Neighborhood", "count": "Count"}
)
st.plotly_chart(fig_neighborhoods, use_container_width=True)

st.markdown("---")

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("Open vs Closed Cases")
    status_counts = (
        view["is_closed"]
        .map({True: "Closed", False: "Open/Other"})
        .value_counts()
        .reset_index()
    )
    status_counts.columns = ["status_group", "count"]

    fig_status = px.bar(
        status_counts,
        x="status_group",
        y="count",
        labels={"status_group": "Case Status", "count": "Count"}
    )
    st.plotly_chart(fig_status, use_container_width=True)

with row2_col2:
    st.subheader("Average Resolution Time by Neighborhood")
    resolution_view = view[(view["is_closed"] == True) & (view["resolution_days"].notna())].copy()

    if not resolution_view.empty:
        avg_resolution = (
            resolution_view.groupby("Neighborhood", as_index=False)["resolution_days"]
            .mean()
            .sort_values("resolution_days", ascending=False)
            .head(10)
        )

        fig_resolution = px.bar(
            avg_resolution,
            x="Neighborhood",
            y="resolution_days",
            labels={"Neighborhood": "Neighborhood", "resolution_days": "Average Resolution Days"}
        )
        st.plotly_chart(fig_resolution, use_container_width=True)
    else:
        st.info("No closed-case resolution data available for the current filter.")

st.markdown("---")

st.subheader("Preview")
preview_cols = [
    c for c in [
        "complaint_address",
        "Neighborhood",
        "violation",
        "status_type_name",
        "violation_date",
        "resolution_days"
    ] if c in view.columns
]
st.dataframe(view[preview_cols].head(25), use_container_width=True)
