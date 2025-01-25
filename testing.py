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

data = [((19, 3329), (6, 148)), [(40, 443), (119, 118)], ((13, 860), (138, 55)), ((105, 667), (294, 73)), ((19, 2458), (318, 221)), [(300, 358), (324, 310)], [(157, 1547), (333, 269)], [(365, 513), (374, 51)], [(738, 721), (401, 129)], ((410, 1237), (908, 550)), ((55, 2517), (961, 477)), ((246, 2397), (1085, 301)), ((732, 1355), (1150, 682)), ((948, 1132), (1626, 54)), [(72, 2913), (1632, 44)], ((933, 1439), (1674, 170)), ((185, 2756), (1725, 190)), ((126, 3069), (1584, 435)), ((487, 2467), (1471, 677)), ((111, 3220), (1810, 88)), ((1219, 1312), (1614, 494)), ((1365, 1014), (1578, 600)), ((1447, 1103), (2034, 1)), ((1280, 1472), (1880, 462)), [(25, 3465), (1968, 431)], ((1170, 1699), (1752, 938)), ((1039, 2198), (1840, 899)), ((1650, 1241), (2288, 293)), ((1765, 1121), (2290, 402)), ((1344, 1717), (2511, 135)), ((334, 3265), (2390, 470)), ((473, 3151), (2674, 91)), ((1699, 1491), (2774, 20)), ((1065, 2366), (2444, 486)), ((666, 2941), (2786, 29)), ((288, 3461), (2569, 353)), ((760, 2881), (2194, 902)), ((962, 2650), (2383, 753)), ((221, 3641), (2347, 830)), ((489, 3470), (2584, 616)), ((326, 3708), (3081, 95)), ((1140, 2671), (2960, 453)), ((1730, 1961), (2931, 515)), ((1384, 2413), (2611, 921)), ((568, 3504), (2569, 998)), ((1654, 2167), (3279, 147)), [(213, 3933), (3103, 511)], ((636, 3465), (3415, 148)), ((505, 3626), (2540, 1261)), ((1087, 3007), (2919, 852)), ((548, 3806), (2496, 1378)), ((1215, 3130), (2706, 1121)), ((1386, 2941), (3412, 280)), ((2226, 2017), (2745, 1272)), [(1207, 3222), (2731, 1466)], ((2311, 1980), (3863, 285)), ((2411, 1936), (3334, 905)), ((2533, 1834), (4076, 95)), ((95, 4656), (4073, 161)), ((1914, 2651), (4128, 196)), ((1639, 2967), (3043, 1417)), ((2687, 1917), (4363, 89)), ((56, 4802), (3202, 1382)), ((272, 4633), (4191, 336)), ((1484, 3354), (3715, 878)), ((1207, 3815), (3226, 1443)), ((2344, 2497), (3444, 1235)), ((2199, 2699), (3547, 1208)), ((2935, 1931), (3904, 904)), ((1000, 4040), (3303, 1549)), ((2985, 1948), (4237, 626)), ((815, 4248), (4030, 903)), ((1952, 3076), (4245, 682)), ((1779, 3314), (4349, 587)), ((287, 4982), (4233, 735)), ((1612, 3582), (4299, 716)), ((2342, 2851), (4219, 845)), ((738, 4617), (4278, 793)), ((2292, 2994), (4719, 356)), ((2221, 3093), (4447, 702)), ((690, 4760), (4977, 156)), ((2286, 3098), (4676, 582)), ((1807, 3647), (4652, 608)), ((2094, 3407), (3933, 1461)), ((1930, 3604), (4741, 612)), ((3061, 2413), (4803, 583)), ((3316, 2173), (3845, 1609)), ((1931, 3690), (3676, 1836)), [(3058, 2521), (4946, 467)], ((1997, 3658), (3993, 1577)), [(1080, 4649), (4895, 635)], ((620, 5328), (3767, 1852)), ((2719, 3069), (3672, 1974)), ((3438, 2266), (4653, 899)), ((3241, 2536), (5232, 338)), [(1312, 4655), (4572, 1093)], ((1946, 3971), (4243, 1466)), ((1242, 4814), (4376, 1334)), ((1407, 4632), (5424, 172)), ((2347, 3632), (4240, 1517)), ((1953, 4106), (4760, 938)), ((3431, 2447), (4826, 1120)), [(3266, 2676), (5733, 248)], ((3236, 2734), (4990, 1093)), ((3338, 2684), (4033, 2055)), [(2149, 3897), (4341, 1755)], [(1533, 4537), (5683, 478)], ((3773, 2367), (4345, 1791)), [(981, 5079), (4782, 1399)], [(869, 5191), (5601, 618)], [(394, 5681), (5559, 667)], ((1307, 4912), (4338, 1882)), ((2481, 3775), (6074, 175)), [(1554, 4677), (5144, 1241)], ((1623, 4652), (4143, 2213)), ((638, 5691), (4762, 1621)), [(2695, 3683), (5939, 449)], ((225, 6151), (6084, 423)), ((1018, 5436), (5073, 1417)), ((3694, 2794), (6301, 210)), ((1690, 4808), (5454, 1070)), ((2476, 4044), (5952, 609)), ((1101, 5433), (4833, 1715)), ((2232, 4307), (5133, 1463)), ((1193, 5379), (5380, 1233)), ((957, 5623), (6519, 107)), ((2205, 4397), (6151, 481)), [(1383, 5206), (6240, 478)], ((1980, 4656), (4612, 2095)), ((1024, 5612), (4923, 1815)), ((2912, 3788), (5669, 1092)), ((3971, 2753), (6418, 360)), ((4064, 2665), (5244, 1513)), ((2172, 4551), (5408, 1367)), [(1529, 5245), (6037, 744)], ((3860, 2938), (6388, 493)), ((3586, 3223), (4742, 2116)), [(1750, 5047), (6751, 155)], ((1041, 5792), (5799, 1109)), ((2308, 4579), (4913, 1993)), ((3046, 3870), (5388, 1542)), [(4287, 2702), (6191, 721)], ((4499, 2500), (6733, 228)), [(44, 6762), (5457, 1617)], [(965, 5934), (6774, 354)], [(3142, 3861), (4744, 2329)], ((4540, 2555), (6634, 512)), [(1379, 5601), (5049, 2141)], ((1994, 5042), (7158, 141)), ((3650, 3493), (5735, 1511)), ((3871, 3293), (6345, 950)), ((3450, 3703), (5707, 1560)), ((3203, 3940), (6305, 1014)), ((3218, 3942), (5348, 1948)), ((2013, 5089), (6386, 1003)), ((2615, 4534), (6247, 1169)), ((1515, 5611), (5949, 1456)), ((2788, 4470), (6158, 1284)), ((1773, 5503), (5549, 1862)), ((4746, 2664), (7082, 438)), ((3888, 3499), (7276, 263)), ((410, 6848), (5090, 2384)), ((3534, 3891), (5145, 2351)), [(4342, 3150), (6625, 935)], ((958, 6544), (5228, 2298)), ((2947, 4630), (6769, 814)), ((3012, 4613), (6583, 1004)), [(1286, 6567), (7383, 175)], ((1168, 6742), (6640, 965)), ((4231, 3559), (7289, 374)), [(2775, 5073), (6215, 1522)], ((4159, 3648), (6043, 1718)), ((2393, 5483), (7492, 257)), ((2581, 5300), (7452, 302)), ((2608, 5300), (5313, 2498)), ((4755, 3111), (5748, 2086)), ((3172, 4795), (6411, 1406)), ((3964, 3971), (6632, 1175)), ((4623, 3321), (7804, 12)), ((3445, 4584), (6914, 977)), ((1651, 6551), (5991, 2006)), ((2296, 5920), (5855, 2153)), ((2150, 6195), (6313, 1722)), ((2623, 5733), (6553, 1492)), ((3649, 4657), (6563, 1496)), ((2712, 5694), (5677, 2473)), [(3896, 4434), (6252, 1846)], ((3689, 4665), (6271, 1875)), ((3808, 4557), (7634, 411)), ((5277, 2967), (5938, 2257)), ((2357, 6139), (5510, 2718)), ((3103, 5357), (7085, 1032)), ((2557, 5952), (7355, 770)), ((2238, 6352), (7666, 441)), ((4175, 4254), (5767, 2522)), [(3194, 5321), (7930, 174)], ((2444, 6155), (5741, 2585)), ((3612, 4930), (6294, 2013)), ((2220, 6444), (7511, 734)), ((4932, 3532), (7320, 970)), ((2605, 6213), (5674, 2845)), ((4275, 4404), (6831, 1578)), ((3400, 5411), (6936, 1463)), ((5169, 3494), (7830, 475)), ((5339, 3309), (7181, 1230)), ((2880, 6218), (6190, 2376)), ((3638, 5352), (6539, 1977)), ((4923, 3888), (6720, 1830)), ((4607, 4258), (8080, 352)), ((3275, 5850), (6807, 1817)), ((3268, 5859), (7541, 1047)), ((5099, 3887), (7153, 1508)), ((3735, 5490), (6950, 1773)), ((3398, 5923), (6103, 2755)), ((5788, 3157), (8152, 386)), ((3816, 5474), (8409, 132)), ((3008, 6472), (6815, 2011)), ((5856, 3148), (6872, 1950)), [(4611, 4602), (6425, 2492)], ((4627, 4666), (6268, 2701)), ((4765, 4581), (6480, 2485)), ((4623, 4776), (8355, 198)), ((5368, 3944), (6763, 2235)), ((4168, 5427), (7918, 903)), ((4961, 4494), (6671, 2435)), ((4726, 4867), (7125, 1901)), ((5835, 3509), (8212, 740)), ((5176, 4314), (7406, 1704)), ((4314, 5389), (8095, 904)), ((4803, 4825), (6373, 2967)), ((3622, 6230), (7412, 1750)), ((4972, 4653), (8807, 126)), ((3720, 6237), (6494, 2898)), ((3155, 6985), (7636, 1530)), ((4480, 5402), (8270, 789)), ((4159, 5850), (7644, 1591)), ((4382, 5583), (7659, 1644)), ((3347, 6848), (7249, 2142)), ((3599, 6545), (8500, 640)), ((3653, 6483), (7094, 2376)), ((5619, 4138), (7404, 2007)), ((4236, 5811), (7316, 2117)), ((5411, 4426), (8927, 198)), ((4984, 4942), (7132, 2372)), [(6262, 3452), (8706, 476)], ((4407, 5731), (7828, 1572)), ((3816, 6455), (7527, 1957)), [(6222, 3597), (7998, 1369)], ((5229, 4868), (6709, 2989)), ((5808, 4193), (7144, 2480)), ((6408, 3429), (8201, 1146)), ((6119, 3815), (7041, 2629)), ((5368, 4833), (8796, 387)), ((6130, 3858), (8467, 835)), ((5218, 5041), (6503, 3396)), [(4120, 6564), (8941, 229)], ((4210, 6493), (7429, 2232)), ((4939, 5575), (6699, 3272)), [(4711, 6051), (6953, 2926)], [(4676, 6157), (7452, 2286)], [(5599, 4909), (8492, 906)], ((5708, 4759), (6774, 3286)), ((4197, 6921), (7549, 2228)), ((4956, 5877), (7407, 2447)), ((4975, 5881), (8203, 1395)), ((6630, 3591), (8691, 725)), ((4226, 6946), (8640, 798)), ((5180, 5671), (7291, 2695)), ((6554, 3791), (8500, 1008)), ((5232, 5835), (7052, 3139)), ((5180, 5930), (8383, 1189)), ((5272, 5817), (7571, 2403)), ((5745, 5202), (7170, 3033)), ((5416, 5724), (7467, 2594)), ((5312, 5951), (8261, 1395)), ((5781, 5286), (7112, 3211)), ((5179, 6253), (8936, 395)), ((5019, 6557), (7784, 2244)), ((5849, 5316), (7201, 3175)), ((4935, 6791), (8088, 1843)), ((5164, 6530), (7236, 3233)), ((6710, 4091), (8101, 1893)), ((6768, 4130), (7831, 2402)), [(6069, 5237), (8923, 731)], ((6434, 4750), (8479, 1495)), ((5749, 6023), (7767, 2640)), ((6474, 4838), (7738, 2731)), ((6394, 4985), (8618, 1293)), ((6595, 4685), (8959, 747)), ((6289, 5237), (8817, 1023)), ((6178, 5434), (8635, 1362)), ((5872, 6127), (7568, 3161)), ((7220, 3889), (8921, 976)), ((7212, 4033), (7882, 2894)), [(7005, 4546), (8629, 1529)], [(5897, 6576), (8831, 1264)], ((6034, 6342), (8216, 2474)), [(6649, 5362), (8843, 1345)], ((6959, 4860), (8830, 1445)), ((6759, 5249), (8753, 1604)), ((6940, 5059), (8669, 1866)), ((7127, 4780), (7935, 3279)), ((6727, 5678), (7977, 3346)), ((6933, 5301), (7930, 3465)), ((7104, 5115), (7720, 3893)), ((6640, 6203), (7939, 3544)), [(6878, 6152), (8737, 1789)], ((7140, 5569), (8733, 1920)), ((7594, 4554), (8399, 2687)), ((7541, 4769), (8036, 3602)), ((7459, 5233), (8170, 3402)), [(7050, 6240), (8222, 3418)], ((7230, 6102), (8499, 2679)), ((7288, 5969), (7980, 4104)), ((7655, 5333), (8079, 3901)), [(7439, 6027), (8270, 3368)], ((7322, 6514), (8397, 3011)), ((7740, 5441), (8352, 3233)), ((7765, 5382), (8584, 2448)), ((7324, 6996), (8253, 3694)), ((7384, 6994), (8327, 3502)), ((8009, 5483), (8407, 3449)), ((8175, 4729), (8806, 1608)), [(7915, 5986), (8352, 3960)], ((8116, 5272), (8620, 2793)), ((8045, 5859), (8972, 1119)), ((8311, 4682), (8949, 1814)), ((8166, 5357), (8962, 1853)), ((8032, 5960), (8782, 2752)), ((8055, 6175), (8739, 3041)), ((8066, 6220), (8798, 2870)), ((8033, 6634), (8593, 4017)), ((8154, 6246), (8638, 3935)), ((8208, 6245), (8866, 3107)), ((8304, 6106), (8714, 3934)), ((8715, 5513), (8816, 3716)), ((8704, 5935), (8845, 3556)), ((8736, 5687), (8816, 4322)), [(8722, 6159), (8903, 2631)], ((8775, 5412), (8950, 2307)), ((8811, 4901), (8866, 3970)), ((8786, 5930), (8852, 4542)), [(8927, 5772), (8981, 2731)]]


plt.figure(figsize=(10, 8))
for idx, (post1, post2) in enumerate(data):
    # Erster Pfosten (blau)
    plt.plot([post1[0], post2[0]], [post1[1], post2[1]], 'r-', label='Linie' if idx == 0 else "")  # Rote Linie
    plt.plot([post1[0]], [post1[1]], 'bo-', label='Erster Pfosten' if idx == 0 else "")  # Blaue Punkte

    # Zweiter Pfosten (grün)
    plt.plot([post2[0]], [post2[1]], 'go-', label='Zweiter Pfosten' if idx == 0 else "")  # Grüne Punkte


points_line1 = ((-181, 63.728234249323165), (9181, 4705.107650938998))
points_line2 = ((-181, 119.53562279131239), (9181, 4760.915039480987))
#points_line3 = [(30538, 6831), (30812, 10508)]

x_values_line1 = [point[0] for point in points_line1]
y_values_line1 = [point[1] for point in points_line1]

# Entpacke x- und y-Werte für Linie 2
x_values_line2 = [point[0] for point in points_line2]
y_values_line2 = [point[1] for point in points_line2]

#x_values_line3 = [point[0] for point in points_line3]
#y_values_line3 = [point[1] for point in points_line3]


# Linie 1
plt.plot(x_values_line1, y_values_line1, label='Linie 1', color='blue', marker='o')
# Linie 2
plt.plot(x_values_line2, y_values_line2, label='Linie 2', color='yellow', marker='x')
#plt.plot(x_values_line3, y_values_line3, label='Linie 2', color='green', marker='.')
plt.title("Pfosten Positionen")
plt.xlabel("X-Koordinate")
plt.ylabel("Y-Koordinate")
plt.legend()
plt.grid(True)
plt.show()
