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