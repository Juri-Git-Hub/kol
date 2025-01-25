import math


def constructShotPath(p1, p2, b, above_line=True):
    """
    Konstruiert ein rechtwinkliges Dreieck, in dem:
      - p1, p2 die Hypotenuse (Länge a) ist,
      - p1, p3 eine Kathete (Länge b),
      - p2, p3 die zweite Kathete (Länge c = sqrt(a^2 - b^2)),
      - Der rechte Winkel liegt bei p3.

    Parameter
    ---------
    p1, p2 : (float, float)
        Koordinaten der gegebenen Hypotenuse
    b : float
        Länge einer Kathete (p1, p3)
    above_line : bool
        Legt fest, ob p3 'oberhalb' (True) oder 'unterhalb' (False)
        der Linie p1, p2 konstruiert wird.

    Returns
    p3
    """
    # Hypotenuse a = |p1->p2|
    vx = p2[0] - p1[0]
    vy = p2[1] - p1[1]
    a = math.hypot(vx, vy)

    if a == 0:
        raise ValueError("p1 und p2 sind identisch es gibt also keine gültige Hypotenuse.")

    # Prüfe, ob b < a:
    if b >= a:
        raise ValueError(f"Kein rechtwinkliges Dreieck möglich, da b >= a (b={b}, a={a}).")

    # c = sqrt(a^2 - b^2)
    c = math.sqrt(a*a - b*b)

    # Wir arbeiten in einem lokalen Koordinatensystem, in dem:
    #    p1' = (0,0), p2' = (a,0).
    #    Also muss man 'v' erst normalisieren, um die Drehung zu bekommen.
    #    theta = Winkel von p1->p2 relativ zur x-Achse
    theta = math.atan2(vy, vx)  # Winkel in [ -pi, +pi ]

    # Im lokalen System: p3' = (x', y')
    #    x' = b^2 / a
    #    y' = ±(b*c / a)
    x_ = (b*b) / a
    y_ = (b*c) / a
    if not above_line:
        y_ = -y_

    # Transformiere p3' zurück in das globale Koordinatensystem:
    #    p3 = p1 + R(theta) * (x_, y_)
    #    R(theta) = [[cosθ, -sinθ],[sinθ, cosθ]]
    cosT = math.cos(theta)
    sinT = math.sin(theta)

    x3 = p1[0] + x_*cosT - y_*sinT
    y3 = p1[1] + x_*sinT + y_*cosT
    p3 = (x3, y3)

    return p3

