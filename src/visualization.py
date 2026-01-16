import matplotlib.pyplot as plt

def plot_violations_per_year(series):
    series.plot.bar(
        title="Housing Code Violations per Year",
        ylabel="Count",
        figsize=(7,4)
    )
    plt.show()
