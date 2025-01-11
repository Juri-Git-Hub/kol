from utility import crossProduct, perpendicularIntersectionPoint, lengthVector, intersection


def solveTask(configurations, first_goal, last_goal):
    # within these two lines is the solution, if there is one
    # ll and rr are the boundaries of the shot
    ll_line = (first_goal[0], last_goal[0])
    rr_line = (first_goal[1], last_goal[1])

    # jede mögliche Konfiguration durchgehen
    for configuration in configurations:
        # linke und rechte Pfosten aufteilen
        left_posts = [goal[0] for goal in configuration]
        right_posts = [goal[1] for goal in configuration]

        # Entfernung von den Pfosten zu jeweils einer Linie
        left_distances = getDistances(left_posts, ll_line, left=True)
        right_distances = getDistances(right_posts, rr_line, left=False)

        # die Begrenzenden Linen bekommen
        left_chokepoints = chokepoints(left_distances, first_goal, last_goal, left=True)
        right_chokepoints = chokepoints(right_distances, first_goal, last_goal, left=False)

        # überprüfen, ob es mögliche mit dieser Konfiguration
        is_possible = possible(left_chokepoints, right_chokepoints)
        if is_possible:
            return left_chokepoints, right_chokepoints

    return None, None


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

        # wenn die Richtung negativ ist, dann muss die Länge negativ sein
        if left and direction < 0:
            length = length * -1
        elif not left and direction > 0:
            length = length * -1

        post_distances.append([post, intersection, length])

    return post_distances


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
