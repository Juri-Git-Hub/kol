import matplotlib.pyplot as plt


def plotPerpendicularIntersection(a, b, c, intersection):
    plt.plot([a[0], b[0]], [a[1], b[1]], label="Linie AB")
    plt.scatter(*c, color="red", label="Punkt C")
    plt.scatter(*intersection, color="green", label="Schnittpunkt")
    plt.plot([c[0], intersection[0]], [c[1], intersection[1]], label="Senkrechte")

    plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
    plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
    plt.legend()
    plt.gca().set_aspect("equal", adjustable="box")
    plt.show()


def plotTwoLines(a, b, c):
    # Extracting x and y values for each line
    line_ab_x = [a[0], b[0]]
    line_ab_y = [a[1], b[1]]

    # Plotting the lines
    plt.figure(figsize=(8, 6))
    plt.plot(line_ab_x, line_ab_y, label="Line AB", marker='o')
    plt.scatter(*c, color="red")
    # Adding labels and legend
    plt.title("Lines AB and CD")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.legend()
    plt.grid(True)

    # Displaying the plot
    plt.show()


def plotPerpLines(left_data, right_data):
    # Set up the plot
    plt.figure(figsize=(10, 8))

    # Plot left data as blue lines
    for segment in left_data:
        start, end, length = segment
        plt.plot([start[0], end[0]], [start[1], end[1]], color='blue', label='Left' if 'Left' not in plt.gca().get_legend_handles_labels()[1] else "")
        midpoint = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
        plt.text(midpoint[0] - 5, midpoint[1] + 2, f"{length:.2f}", color='blue', fontsize=8, ha='center', va='center')

    # Plot right data as red lines
    for segment in right_data:
        start, end, length = segment
        plt.plot([start[0], end[0]], [start[1], end[1]], color='red', label='Right' if 'Right' not in plt.gca().get_legend_handles_labels()[1] else "")
        midpoint = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
        plt.text(midpoint[0] - 5, midpoint[1] + 2, f"{length:.2f}", color='red', fontsize=8, ha='center', va='center')

    # Additional lines to plot
    plt.plot([10, 230], [20, 135], color='green', label='Additional Line 1')
    plt.plot([12, 245], [3, 110], color='purple', label='Additional Line 2')

    plt.axis('equal')
    # Add labels and legend
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Lines with Lengths for Left and Right")
    plt.legend()
    plt.grid(True)
    plt.show()



#a = (10, 10)
#b = (0, 0)
#c = (3, 2)
#print(crossProduct([a, b], c))
#plotTwoLines(a, b, c)

stri = "string"

print(stri[2:])
