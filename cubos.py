from matplotlib import pyplot as plt

# Create variables to populate the graph
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

# Define which values will go in the x and y axes
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Define the title of the graph and the axes
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of the Value", fontsize=14)

# Define the size of the rotules in the scales markings
ax.tick_params(axis="both", labelsize=14)

# Show plot.
plt.show()
