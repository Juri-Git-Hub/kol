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


def plotTwoLines(points_line1, points_line2):
    """
    Plottet zwei Linien basierend auf Listen von (x, y)-Punkten.

    Parameter:
    ----------
    points_line1 : Liste/Array von (x, y)-Tupeln
        Die Stützstellen für die erste Linie.
    points_line2 : Liste/Array von (x, y)-Tupeln
        Die Stützstellen für die zweite Linie.
    """
    # Entpacke x- und y-Werte für Linie 1
    x_values_line1 = [point[0] for point in points_line1]
    y_values_line1 = [point[1] for point in points_line1]

    # Entpacke x- und y-Werte für Linie 2
    x_values_line2 = [point[0] for point in points_line2]
    y_values_line2 = [point[1] for point in points_line2]

    plt.figure(figsize=(8, 5))

    # Linie 1
    plt.plot(x_values_line1, y_values_line1, label='Linie 1', color='blue', marker='o')
    # Linie 2
    plt.plot(x_values_line2, y_values_line2, label='Linie 2', color='red', marker='x')

    # Achsenbeschriftungen, Titel und Legende
    plt.xlabel('X-Achse')
    plt.ylabel('Y-Achse')
    plt.title('Zwei Linien basierend auf (x, y)-Punkten')
    plt.legend()

    # Diagramm anzeigen
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
        x_coord, y_coord = zip(*line)
        plt.plot(x_coord, y_coord, label="Line Group 1", color="blue")

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


def plot_triangle(p1, p2, p3):
    """
    Zeichnet das Dreieck p1->p2->p3->p1 mit matplotlib.
    """
    x_coords = [p1[0], p2[0], p3[0], p1[0]]
    y_coords = [p1[1], p2[1], p3[1], p1[1]]

    plt.figure(figsize=(5,5))
    plt.title("Rechtwinkliges Dreieck (Hypotenuse = p1->p2, rechter Winkel bei p3)")
    plt.plot(x_coords, y_coords, marker='o')
    plt.grid(True)
    plt.axis('equal')

    # Achsen-Puffer
    all_x = [p1[0], p2[0], p3[0]]
    all_y = [p1[1], p2[1], p3[1]]
    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)
    buffer = 1.0
    plt.xlim(min_x - buffer, max_x + buffer)
    plt.ylim(min_y - buffer, max_y + buffer)

    plt.show()