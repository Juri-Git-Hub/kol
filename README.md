Krocket:

beliebige Anzahl, größe und Position von Toren. Tore dürfen sich nicht überschneiden.

Ziel: Es muss überprüft werden, ob man mit einem Schuss durch alle Tore schießen kann. Dabei muss die Reihenfolge der Tore beachtet werden. 

Linearer Ansatz:

Reihenfolge der Tore (Winkeltest) und Orientierungstest:
Wenn man durch ein Tor schießt, gibt es immer einen Pfosten, der links vom Schusspfad ist, und einen der rechts ist.
... fehlt noch



Eine Lösung ist ein Vektor, bestehend aus einem Startpunkt und einer Richtung. Die Menge aller Lösungen kann als Polygon dargestellt werden. 
Jeder Vektor/jede Strecke, die durch dieses Polygon führt ist eine mögliche Lösung. 
Das Polygon stellt einen Kanal vom ersten bis zum letzten Tor dar, da jede Lösung durch das erste und letzte Tor gehen muss. 
Folgend geht dieses Kanalpolygon durch alle Tore in der richtigen Reihenfolge. 
Da dieses Kanalpolygon alle Lösungen darstellt, muss es begrenzt sein. Jede Anordnung von Toren hat, wenn sie lösbar ist, ein Kanalpolygon.
Es wird immer durch Pfosten begrenzt. Mindestens vier und maximal acht Pfosten begrenzen ein Kanalpolygon. -> Begründung ???
Das Polygon hat also immer mindestens 4 Seiten. Zwei Seiten sind immer Anfang/Ende des Polygons, diese Seiten ignorieren wir.
Im folgenden wird angenommen, dass ein Schuss genau durch einen Pfosten möglich ist. Die zwei Punkte eines Tores markieren die Torlinie.
Die restlichen Seiten sind Lösungen, da sie im Polygon liegen. Sie sind Extremlösungen. 
Jedes Kanalpolygon hat solche Extremlösungen, da jedes Polygon laut seiner Definition Seiten hat. Diese Seiten müssen mindestens zwei Pfosten berühren.

Wenn es eine Lösung gibt, gibt es eine Lösung, welche zwei Pfosten berührt.

-> 1. Lösungsansatz: Brute Force.
Mit diesem Wissen kann man schlussfolgern, dass ein Überprüfen der Verbindung von jedem Pfosten mit jedem anderen Pfosten zu einer Lösung führen MUSS.
Wenn es keine Verbindung gibt, dessen verlängerte Linie durch alle Tore führt, kann es keine Lösung geben, da es kein Kanalypolgon geben kann.
Dieser Ansatz ist jedoch sehr ineffizient. (O(n) = n⁴)


Mithilfe des Orientierungstests lässt sich zuordnen, welches Tor links und welche rechts sein muss.















