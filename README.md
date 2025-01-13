Krocket:

beliebige Anzahl, größe und Position von Toren. Tore dürfen sich nicht überschneiden.

Ziel: Es muss überprüft werden, ob man mit einem Schuss durch alle Tore schießen kann. Dabei muss die Reihenfolge der Tore beachtet werden. 

Linearer Ansatz:

Reihenfolge der Tore (Winkeltest) und Orientierungstest:
Wenn man durch ein Tor schießt, gibt es immer einen Pfosten, der links vom Schusspfad ist, und einen der rechts ist.
... fehlt noch


Der Ballradius wird zunächst nicht beachtet.


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


Chokepoints:
Es wird im folgenden davon ausgegangen, dass es möglich ist die Aufgabe zu lösen.
Ein Kanalypolygon, welches durch mehr als 4 Pfosten eingegrenzt wird, hat Pfosten, die das Polygon weiter nach innen eingrenzen. Diese Pfosten sind Chokepoints.
Da alle Linien des Kanalpolygons (außer die zwei Seiten am Anfang und am Ende des Kanalpolygons) diese Chokepoints berühren und eine der Linien eine Lösung sein muss, muss eine Lösung einen Chokepoint berühren. Wenn man also diese Chokepoints kennt, kann man die Suche nach Verbindungen deutlich verkürzen.

Wie findet man die Chokepoints?
Die gleiche Frage anders gestellt: Was haben Chokepoints für eine Eigenschafft, die andere Pfosten nicht haben?

Chokepoints grenzen das Polygon, die Menge an Lösungen, ein. Wenn man ein Viereck aus dem ersten und letzten Tor macht, sind sie die Pfosten, welche am weitesten in dieses Viereck eindringen. Wenn man also die Entfernung von allen Pfosten zu den Verbindungen zwischen erstem und letzten Tor misst, kann man die Chokepoints finden, indem man die längste Entfernung sucht. 
Dafür muss man aber wissen welcher Pfosten links und welcher rechts vom Schuss verläuft. -> siehe Orientierungstest

-> 2. Lösungsansatz: Brute Force, aber nur noch so halb :)
Wenn man die Chokepoints kennt, muss man nur noch alle Verbindungen zwischen einem Chokepoint und jedem anderen Tor überprüfen.
n bisschen schneller, aber das geht doch noch besser!


Für die Lösung der Aufgabe braucht nicht ein Kanalpolygon, sondern eine einzige Lösung.
Ist es möglich NUR mit den Chokepoints eine Lösung zu finden?

Es gibt verschiedene Fälle:
1. Es gibt keine Chokepoints: Man überprüft, ob die engste Stelle des Polygon aus erstem und letztem Tor größer als der Balldurchmesser ist.
2. Es gibt einen Chokepoint: Man überprüft, ob die Distanz von dem einen Chokepoint zur anderen Verbindungslinie größer als der Balldurchmesser ist.

3. Es gibt zwei Chokepoints:
Dieser Fall ist komplizierter:
Wenn man versucht das Polygon zu finden, kommt man aber auf die Lösung.
Um ein vollständiges Kanalpolygon zu finden, braucht man noch die eingrenzenden Pfosten auf jeder Seite, da sie die Seiten des Polygons mit eingrenzen. (Skizze notwendig) (diese Pfosten kann es, muss es aber nicht, geben)

Eingrenzende Pfosten:
Diese eingrenzenden Pfosten müssen nicht zwingend die höchsten Pfosten sein (Skizze notwendig). Wie findet man also schnell diese Pfosten?
Nun, wenn man sich die Linie zwischen dem höchsten Pfosten und einem eingrenzenden Pfosten vorstellt, dann liegt kein Pfosten von diesem Abschnitt mehr über der Linie. 
Eine Lösung ist es, eine waagerechte Linie, die den höchsten Pfosten berührt, zu ziehen und diese zu "drehen" bis sie den ersten Pfosten berührt. Dieser Pfosten muss ein eingrenzender Pfosten sein, da kein Pfosten über der waagerechten Linie liegt.
Also berechnet man für jeden Pfosten einen Winkel (Skizze notwendig) und der Pfosten mit dem kleinsten Winkel für jede Seite ist der einschränkende Pfosten.

Wenn man diese waagerechten Linien für beide Chokepoints einzeichnet, ähnelt das einem Schusspfad. Dafür muss man sie natürlich parallel zueinander zeichnen.















