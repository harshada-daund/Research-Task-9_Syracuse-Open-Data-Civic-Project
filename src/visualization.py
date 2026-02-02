import matplotlib.pyplot as plt

def plot_violations_per_year(series, save_path=None):
    ax = series.plot.bar(
        title="Housing Code Violations per Year",
        ylabel="Count",
        figsize=(7, 4)
    )
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

    plt.close()
