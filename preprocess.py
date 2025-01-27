from math import degrees, atan2
from utility import test_orientation


def read_goals(file_path):
    with open(file_path, "r") as file:
        num_goals, ball_radius = file.readline().strip().split()

        list_goals = []
        for line in file:
            coords_goal = tuple(int(num) for num in line.strip().split(" "))
            coords_posts = ((coords_goal[0], coords_goal[1]), (coords_goal[2], coords_goal[3]))
            list_goals.append(coords_posts)
    return int(num_goals), float(ball_radius), list_goals


def calculate_clockwise_angle(a, x, b):
    # this function calculates the angle for three given points
    x1, y1 = a
    x2, y2 = x
    x3, y3 = b
    deg1 = (360 + degrees(atan2(x1 - x2, y1 - y2))) % 360
    deg2 = (360 + degrees(atan2(x3 - x2, y3 - y2))) % 360

    angle = deg2 - deg1 if deg1 <= deg2 else 360 - (deg1 - deg2)
    return angle


def calculate_counter_clockwise_angle(a, x, b):
    # Extrahiere die Koordinaten der Punkte
    x1, y1 = a
    x2, y2 = x
    x3, y3 = b

    # Berechne die Winkel relativ zu Punkt x
    deg1 = (360 + degrees(atan2(x1 - x2, y1 - y2))) % 360
    deg2 = (360 + degrees(atan2(x3 - x2, y3 - y2))) % 360

    # Berechne den Winkel gegen den Uhrzeigersinn
    angle = deg1 - deg2 if deg1 >= deg2 else 360 - (deg2 - deg1)
    return angle


# a = (0, 0)
# b = (0, 5)
# c = (5, 5)
# print(calculate_clockwise_angle(c, b, a))
# print(calculate_counter_clockwise_angle(c, a, b))
# from testing import plot_triangle
# plot_triangle(a, b, c)

def new_angle_test(list_goals):
    # Richtung der Tore (>180° oder <180°)
    direction = None

    # Die richtigen Orientierungen aller Tore wird hier gespeichert
    correct_orientations = []

    # die möglichen Orientierungen des vorherigen Tores
    previous_goal_orientations = [list_goals[0]]

    # mögliche Tore zwischen den previous und new goal (Beispiel 1 Tor 4)
    middle_goals = []

    for new_goal in list_goals[1:]:
        # wenn
        if len(previous_goal_orientations) == 1:
            # todo letztes Tor noch hinzufügen
            orientations = test_orientation(previous_goal_orientations[0], new_goal)
            new_goal_orientations = [orientation[2:4] for orientation in orientations]

        else:
            # Beide Orientierungsmöglichkeiten
            new_goal_orientations = [new_goal, [new_goal[1], new_goal[0]]]

        # Die Orientierungen des previous und new goal herausfinden
        new_orientations, previous_orientations, new_direction = workstuff(
            new_goal_orientations,
            previous_goal_orientations,
            direction
        )
        direction = new_direction

        if not new_orientations or not previous_orientations:
            return None

        # Wenn es nur eine mögliche Orientierung gibt, dann kann sie zu den richtigen Orientierungen hinzugefügt werden
        if len(previous_orientations) == 1:
            for element in previous_orientations:
                correct_orientations.append(element)

            for goal in middle_goals:
                # middle_orientations = test_orientation(previous_orientations[0], goal)
                # middle_goal_orientations = [orientation[2:4] for orientation in middle_orientations]
                correct_orientations.append(goal)
            middle_goals = []

            previous_goal_orientations = new_orientations
        else:
            # todo this isn't correct, but maybe works just fine
            orientations = test_orientation(list_goals[0], new_goal)
            new_goal_orientations = [orientation[2:4] for orientation in orientations]

            # if len(new_orientations) == 1:
            middle_goals.append(new_goal_orientations[0])
            # else:
            #     print(previous_orientations)
            #     print(new_orientations)
            #     raise ValueError("wtf!!!")

        if new_goal == list_goals[-1]:
            # if len(new_goal_orientations) > 1:
            #     print(new_goal_orientations)
            #     raise ValueError("heeelp")
            # else:
            correct_orientations.append(new_goal_orientations[0])

    return correct_orientations


def workstuff(new_goal_orientations, previous_goal_orientations, direction):
    current_direction = direction

    previous_working_orientations = []
    new_working_orientations = []
    for previous_orientation in previous_goal_orientations:

        for new_orientation in new_goal_orientations:
            cl = new_orientation[0]
            bl = previous_orientation[0]
            al = previous_orientation[1]
            angle_l = calculate_clockwise_angle(cl, bl, al)

            cr = new_orientation[1]
            br = previous_orientation[1]
            ar = previous_orientation[0]
            angle_r = calculate_counter_clockwise_angle(cr, br, ar)

            if angle_l > 180 and angle_r > 180:
                if current_direction is None:
                    current_direction = "backwards"

                if current_direction == "forwards":
                    continue

            elif angle_l < 180 and angle_r < 180:
                if current_direction is None:
                    current_direction = "forwards"

                if current_direction == "backwards":
                    continue

            if previous_orientation not in previous_working_orientations:
                previous_working_orientations.append(previous_orientation)

            if new_orientation not in new_working_orientations:
                new_working_orientations.append(new_orientation)

    return new_working_orientations, previous_working_orientations, current_direction


new_goal = [[(1, 1), (-0.25, 7)], [(-0.25, 7), (1, 1)]]
previous_goal = [[(0, 0), (0, 5)]]
direction = "backwards"
print(workstuff(new_goal, previous_goal, direction))
from testing import plotTwoLines
plotTwoLines(new_goal[0], previous_goal[0])


def linear_ordering_test(list_goals: list[tuple[(float, float), (float, float)]]) -> bool:
    richtung = None

    for i, goal in enumerate(list_goals):
        if i == len(list_goals) - 1:
            break

        # für ein Tor berechne ich den Winkel an dem ersten Pfosten von dem Tor und dem zweiten Pfosten von dem Tor
        # und irgendeinem Pfosten vom nächsten Tor und den Winkel an dem zweiten Pfosten von dem Tor
        # und dem ersten Pfosten von dem Tor und dem anderen Pfosten von dem nächsten Tor.
        a1 = goal[1]
        x1 = goal[0]
        b1 = list_goals[i + 1][0]

        a2 = goal[0]
        x2 = goal[1]
        b2 = list_goals[i + 1][1]

        # Zur Berechnung der Winkel muss der Winkel gegen den Uhrzeigersinn beschrieben werden.
        # Wenn der erste Punkt auf der y-Achse höher ist als der zweite Punkt desselben Tors müssen die Winkel so
        # beschrieben werden, dass
        if x1[1] > x2[1]:
            angle1 = calculate_clockwise_angle(b1, x1, a1)
            angle2 = calculate_clockwise_angle(a2, x2, b2)
        else:
            angle1 = calculate_clockwise_angle(a1, x1, b1)
            angle2 = calculate_clockwise_angle(b2, x2, a2)

        # wir erhalten zwei Winkel, die zwei Tore verbinden. Wenn diese beiden Innenwinkel größer als 180° sind, wird
        # beim ersten Mal die Richtung festgelegt, und bei jedem weiteren Tor überprüft, ob die Richtung sich geändert
        # hat. Wenn die beiden Innenwinkel in jeweils andere Richtungen zeigen, bleibt die Richtung None.
        # Ab der ersten Richtungsübereinstimmung beider Innenwinkel muss jede weitere Richtungsübereinstimmung
        # der beiden Innenwinkel dieselbe Richtung vorgeben. Ansonsten ist der Pfad unmöglich. Zeigen beide Innenwinkel
        # in jeweils unterschiedliche Richtungen ist unklar, ob der Schusspfad existiert und deswegen kann er hier nicht
        # verworfen werden.
        if angle1 > 180 and angle2 > 180:
            if richtung is None:
                richtung = "backwards"

            if richtung == "forwards":
                return False

        elif angle1 < 180 and angle2 < 180:
            if richtung is None:
                richtung = "forwards"

            if richtung == "backwards":
                return False

    return True
