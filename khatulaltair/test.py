import random
import matplotlib.pyplot as plt
import khatulaltair as kva

# Apply theme globally (optional, but recommended)
kva.apply_theme()

chart = kva.styled_line(
    x=[1, 2, 3, 4],
    y=[10, 5, 8, 12],
    title="Business performance"
)

hist_data = [random.gauss(0, 1) for _ in range(1000)]
fig, ax = kva.styled_histogram(
    data=hist_data,
    bins=30,
    title="Histogram of Random Data",
    xlabel="Value",     
    ylabel="Frequency"
)
plt.show()  # Show the plot if not already displayed