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


def plotPerpLines(left_data, right_data, lines):
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
    for linie in lines:
        x_coords = [punkt[0] for punkt in linie]
        y_coords = [punkt[1] for punkt in linie]
        plt.plot(x_coords, y_coords, marker='o')  # Verbinde die Punkte und markiere sie

    plt.axis('equal')
    # Add labels and legend
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Lines with Lengths for Left and Right")
    plt.legend()
    plt.grid(True)
    plt.show()

stri = "string"
print(stri[2:-1])


def plotSolution(lines1, lines2):
    # Plot vorbereiten
    plt.figure(figsize=(10, 6))

    # Linien aus der ersten Gruppe plotten
    for line in lines1:
        x_coords, y_coords = zip(*line)
        plt.plot(x_coords, y_coords, label="Line Group 1", color="blue")

    # Linien aus der zweiten Gruppe plotten
    for line in lines2:
        x_coords, y_coords = zip(*line)
        plt.plot(x_coords, y_coords, label="Line Group 2", color="orange")

    # Achsen anpassen
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

    # Diagramm beschriften
    plt.title("Line Plot")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.legend()

    # Anzeige des Plots
    plt.show()


left = [[(20, 20), (12.703448275862069, 24.44137931034483), 8.541985556144386], [(33, 15), (13.997241379310346, 26.566896551724138), 22.246301513610813], [(0, 60), (25.06206896551724, 44.744827586206895), -29.339863431974194], [(120, 70), (61.9448275862069, 105.33793103448276), 67.96449377280098], [(126, 149), (98.65379310344828, 165.6455172413793), 32.013876301723734], [(123, 167), (105.83724137931034, 177.44689655172414), 20.092235590757014], [(156, 202), (130.30344827586208, 217.64137931034483), 30.082644784682394]]
right = [[(14, 3), (13.229270364393102, 3.9733627792406354), -1.2415551825085325], [(23, 16), (25.087845069226198, 13.363237917268325), 3.3632738981569172], [(60, 0), (40.042444576573516, 25.204612248364903), -32.149284549886424], [(48, 16), (40.45372462413998, 25.53027265777627), -12.156165883199737], [(238, 121), (208.3359551516181, 158.4630425549987), -47.785302282652324], [(251, 162), (236.28014949460632, 180.58985815000426), -23.711955316641824], [(206, 183), (218.84187547778816, 166.78185679096237), 20.686757477571746]]
lines = [[(10, 20), (136, 227)], [(281, 216), (12, 3)]]

plotPerpLines(left, right, lines)