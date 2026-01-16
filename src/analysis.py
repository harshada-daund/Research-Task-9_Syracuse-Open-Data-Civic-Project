def violations_per_year(df):
    return df.groupby("Year")["ObjectId"].count()

def open_vs_closed(df):
    return (
        df.groupby(["Year", "Is_Open"])["ObjectId"]
        .count()
        .unstack(fill_value=0)
    )

def resolution_summary(df):
    closed = df[
        (~df["Is_Open"]) &
        (df["Resolution_Days"].notna()) &
        (df["Resolution_Days"] >= 0)
    ]
    return closed["Resolution_Days"].describe()
