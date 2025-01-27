from utility import crossProduct, perpendicularIntersectionPoint, lengthVector, intersection
from utility import test_orientation
from linear import constructShotPath


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

    # TODO wtf??? hardcoded numbers????
    xMin = first_goal[0][0] - 200
    xMax = last_goal[1][0] + 200

    # jede Orientierung der Choke points durchgehen
    for p_orientation in choke_point_orientation:
        # wenn der 1. Pfosten weiter rechts ist, dann ist above true
        # above legt fest, wie das Dreieck konstruiert wird
        above = False
        if p_orientation[0][0] > p_orientation[1][0]:
            above = True
        # das Dreieck konstruieren um den dritten Punkt herauszubekommen
        shotPathPoint = constructShotPath(p_orientation[0], p_orientation[1], ball_radius * 2, above_line=above)

        print(p_orientation)
        print(shotPathPoint)
        # der shotPath ist immer die Verbindung aus dem dritten Punkt und dem zweiten
        # diese Strecke muss verlängert werden, sodass sie länger als alle Tore ist
        shotPath = extend_line_linear(p_orientation[1], shotPathPoint, xMin, xMax)

        # die Parallele wird gefunden und auch verlängert
        parallel = getParallel(shotPath[0], shotPath[1], p_orientation[0])
        parallel_path = extend_line_linear(parallel[0], parallel[1], xMin, xMax)
        print("PATHS:")
        print(shotPath)
        print(parallel_path)
        # mit beiden Linien kann überprüft werden, ob sie durch alle Tore gehen.
        is_possible = True
        for goal in list_goals:
            intersectionPoint1 = intersection(goal[0], goal[1], shotPath[0], shotPath[1])
            intersectionPoint2 = intersection(goal[0], goal[1], parallel_path[0], parallel_path[1])
            if not intersectionPoint1 or not intersectionPoint2:
                print("THIS IS IT")
                print(goal)
                is_possible = False
                break

        # wenn sie durch alle Tore gehen, ist eine Lösung gefunden.
        # die Strecke zwischen den Parallelen wird zurückgegeben
        if is_possible:
            trueShotPath = middle_line_between(shotPath, parallel_path)
            return trueShotPath

    return None


def midpoint(p, q):
    """Gibt den Mittelpunkt zwischen den zwei Punkten p und q zurück."""
    return ((p[0] + q[0]) / 2.0,
            (p[1] + q[1]) / 2.0)


def middle_line_between(lineA, lineB):
    """
    Erzeugt die Strecke zwischen zwei parallelen Linien aka der eigentliche Schusspfad
    lineA = (p1, p2) und lineB = (q1, q2),
    indem die Mittelpunkte der jeweiligen Endpunkte verbunden werden. Dafür ist die Reihenfolge der Pfosten wichtig.

    Rückgabe: (M1, M2) = die beiden Endpunkte der Mittellinie.
    """
    (p1, p2) = lineA
    (q1, q2) = lineB

    # M1 = Mittelpunkt von p1 und q1
    m1 = midpoint(p1, q1)
    # M2 = Mittelpunkt von p2 und q2
    m2 = midpoint(p2, q2)

    return m1, m2


def getParallel(p1, p2, p3):
    """
    Erzeugt die Parallele von der Strecke (p1, p2), welche durch den Punkt p3 verläuft.
    :param p1: 1. Punkt der Strecke
    :param p2: 2. Punkt der Strecke
    :param p3: Punkt durch den die Parallele läuft.
    :return: die Parallele (p3, p4)
    """
    # Richtungsvektor der Original-Linie
    vx = p2[0] - p1[0]
    vy = p2[1] - p1[1]

    # Falls p1 == p2, ist die Original-Linie degeneriert
    if vx == 0 and vy == 0:
        raise ValueError("Die Original-Linie hat Länge 0 (p1 == p2). Keine eindeutige Richtung!")

    # Bilden der parallelen Linie: p3 -> p4
    p4 = (p3[0] + vx, p3[1] + vy)

    return p3, p4


def getChokePoint(lines):
    """
    Findet den Pfosten mit dem größten Abstand
    :param lines: alle Pfosten mit ihrem Abstand
    :return: den Pfosten mit dem größten Abstand
    """
    maxValue, maxIndex = maxDistance(lines)

    if maxValue == 0:
        return None
    else:
        return lines[maxIndex]


def maxDistance(distances):
    # maxValue ist am Anfang null
    maxValue = 0
    maxIndex = None
    # für jede Linie/Abstand durchgehen
    for line in distances:
        # ist der Abstand größer als maxValue wird maxValue und maxIndex aktualisiert
        if line[2] > maxValue:
            maxValue = line[2]
            maxIndex = distances.index(line)

    return maxValue, maxIndex


def getDistances(list_posts, line, left):
    # die Liste mit Toren und deren Abstände
    post_distances = []

    # jeden Pfosten durchgehen
    for post in list_posts:
        # den Schnittpunkt von dem Pfosten und der Linie finden
        # die Linie von dem Pfosten und dem Schnittpunkt muss senkrecht zu der Linie verlaufen
        intersection = perpendicularIntersectionPoint(line, post)
        # die Länge von den zwei Punkten berechnen
        length = lengthVector([post, intersection])
        # die Richtung der Linie finden über ein crossProduct
        direction = crossProduct(line, post)

        if line[0][1] > line[1][1]:
            direction = direction * -1

        # wenn die Richtung negativ ist, dann muss die Länge negativ sein
        if left and direction < 0:
            length = length * -1
        elif not left and direction > 0:
            length = length * -1

        post_distances.append([post, intersection, length])

    return post_distances


def extend_line_linear(point1, point2, x_min, x_max):
    """
    Erstellt eine lineare Funktion aus einer Linie, die durch zwei Punkte definiert ist,
    und berechnet zwei neue Punkte anhand der vorgegebenen x-Werte (x_min und x_max).

    :param point1: Tuple (x1, y1) - erster Punkt
    :param point2: Tuple (x2, y2) - zweiter Punkt
    :param x_min: float - der kleinere x-Wert für die verlängerte Linie
    :param x_max: float - der größere x-Wert für die verlängerte Linie
    :return: Tuple ((x_min, y_min), (x_max, y_max)) - die neuen Endpunkte der verlängerten Linie
    """
    # Koordinaten der Punkte
    x1, y1 = point1
    x2, y2 = point2

    # Berechnung der Steigung m
    if x2 == x1:
        raise ValueError("Die Linie ist vertikal. Verwende eine andere Methode.")

    m = (y2 - y1) / (x2 - x1)

    # Berechnung des Achsenabschnitts b
    b = y1 - m * x1

    # Berechnung der neuen Punkte basierend auf x_min und x_max
    y_min = m * x_min + b
    y_max = m * x_max + b

    return (x_min, y_min), (x_max, y_max)
