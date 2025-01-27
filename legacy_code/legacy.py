def solveTask(list_goals, ball_radius):
    first_goal = list_goals.pop(0)
    last_goal = list_goals.pop(-1)
    # within these two lines is the solution, if there is one
    # ll and rr are the boundaries of the shot
    ll_line = (first_goal[0], last_goal[0])
    rr_line = (first_goal[1], last_goal[1])

    # jede mögliche Konfiguration durchgehen
    # todo eigentlich für mehrere konfigurationen??
    # for configuration in configurations:
    # linke und rechte Pfosten aufteilen
    left_posts = [goal[0] for goal in list_goals]
    right_posts = [goal[1] for goal in list_goals]

    # Entfernung von den Pfosten zu jeweils einer Linie
    left_distances = getDistances(left_posts, ll_line, left=True)
    right_distances = getDistances(right_posts, rr_line, left=False)
    from testing import plotPerpLines
    print(left_posts)
    print(right_posts)
    plotPerpLines(left_distances[0:10], right_distances[0:10], lines=[((0, 0), (1, 1))])
    # die Begrenzenden Linen bekommen
    left_choke_point = getChokePoint(left_distances)[0]
    right_choke_point = getChokePoint(right_distances)[0]

    # lr orientation für die Chokepoints bekommen -> in welche richtung schießt man durch die Chokepoints
    orientations = test_orientation(first_goal, (left_choke_point, right_choke_point))
    choke_point_orientation = [orientation[2:4] for orientation in orientations]

    # 1. Parallelen von den Grundlinien durch die Chokepoints zeichnen
    l_parallel = getParallel(ll_line[0], ll_line[1], left_choke_point)
    r_parallel = getParallel(rr_line[0], rr_line[1], right_choke_point)

    # TODO wtf??? hardcoded numbers????
    xMin = first_goal[0][0] - 200
    xMax = last_goal[1][0] + 200
    left_parallel = extend_line_linear(l_parallel[0], l_parallel[1], xMin, xMax)
    right_parallel = extend_line_linear(r_parallel[0], r_parallel[1], xMin, xMax)

    # 2. Schauen an welchem Tor die Parallelen einen geringeren Abstand haben
    first_goal_intersection1 = intersection(first_goal[0], first_goal[1], left_parallel[0], left_parallel[1])
    first_goal_intersection2 = intersection(first_goal[0], first_goal[1], right_parallel[0], right_parallel[1])
    last_goal_intersection1 = intersection(last_goal[0], last_goal[1], left_parallel[0], left_parallel[1])
    last_goal_intersection2 = intersection(last_goal[0], last_goal[1], right_parallel[0], right_parallel[1])

    # 3. Diesen Abstand messen
    if (first_goal_intersection1 and first_goal_intersection2) and (last_goal_intersection1 and last_goal_intersection2):
        first_length = lengthVector((first_goal_intersection1, first_goal_intersection2))
        last_length = lengthVector((last_goal_intersection1, last_goal_intersection2))

        smallest_distance = min(first_length, last_length)

        # 5. Wenn der Abstand größer als der Balldurchmesser ist, dann die Parallelen benutzen und schauen ob das klappt
        if smallest_distance > ball_radius * 2:
            print("works with distance")
            print(left_parallel)
            print(right_parallel)
            return middle_line_between(left_parallel, right_parallel)
    else:
        return chokePointOrientation(list_goals, choke_point_orientation, ball_radius)


def chokepoints(lines, first_goal, last_goal, left):
    # den maximalen Abstand bekommen
    maxValue, maxIndex = maxDistance(lines)
    print(lines)
    # wenn es keinen maximalen Abstand gibt, dann ist die begrenzende Linie die Linie von dem ersten und letzten Pfosten
    if maxValue == 0:
        return [[first_goal, last_goal]]
    else:
        # die Pfosten werden in zwei Gruppen aufgeteilt. Die Grenze ist der Pfosten mit dem größten Abstand
        first_posts = lines[0:maxIndex + 1]
        last_posts = lines[maxIndex:]

        # bei der zweiten Gruppe muss die Reihenfolge der Elemente umgekehrt werden
        last_posts = last_posts[::-1]

        # für jede Gruppe wird die Linie ermittelt, welche
        first_line = getLine(first_posts, left, first_goal[0])
        last_line = getLine(last_posts, left, first_goal[1])
        return [first_line, last_line]


def getLine(posts, left, line_post):
    # die neue Linie ist die vom ersten zum letzten Pfosten
    new_line = [line_post, posts[-1][0]]

    # alle anderen Pfosten werden in eine Liste gespeichert
    list_posts = [line[0] for line in posts[:-1]]

    # die Entfernung der Pfosten zu der neuen Linie wird berechnet
    distances = getDistances(list_posts, new_line, left=left)

    # findet die maximale Entfernung
    maxValue, maxIndex = maxDistance(distances)

    # wenn die maximale Entfernung null ist, kann die Linie zurückgegeben werden
    if maxValue == 0:
        return new_line
    else:
        # die neue Linie geht von dem Pfosten mit der größten Entfernung zu dem letzten Pfosten
        test_line = [posts[maxIndex + 1][0], posts[-1][0]]

        # uns interessieren nur noch die Pfosten, welche innerhalb der Pfosten von der Linie Liegen
        updated_posts = posts[maxIndex:]
        return recursive(test_line, updated_posts, left)


def recursive(line, posts, left):
    # die Liste der Pfosten
    list_posts = [post[0] for post in posts[1:-1]]
    # die Abstände der Pfosten zu den Linien
    distances = getDistances(list_posts, line, left=left)
    # der maximale Abstand
    maxValue, maxIndex = maxDistance(distances)
    if maxValue == 0:
        return line
    else:
        # neue Linie und neue Pfosten
        new_line = [posts[maxIndex][0], posts[-1][0]]
        new_posts = posts[maxIndex:]

        return recursive(new_line, new_posts, left=left)


def possible(left_lines, right_lines):
    # jede linke Linie mit jeder rechten Linie überprüfen
    for line in left_lines:
        p1, p2 = line
        q1, q2 = right_lines[0]
        # wenn sich die beiden Linien überschneiden ist es unmöglich mit einem Schuss durchzuschießen
        intersection1 = intersection(p1, p2, q1, q2)

        c1, c2 = right_lines[1]
        # wenn sich die beiden Linien überschneiden ist es unmöglich mit einem Schuss durchzuschießen
        intersection2 = intersection(p1, p2, c1, c2)

        if intersection1 or intersection2:
            return False

    return True