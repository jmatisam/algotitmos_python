import matplotlib.pyplot as plt
import networkx as nx

distancias = {
    "A": {"C": 63, "D": 75, "F": 44},
    "B": {"C": 61, "D": 77, "G": 64},
    "C": {"A": 63, "B": 61, "D": 29},
    "D": {"A": 75, "B": 77, "C": 29, "E": 38, "H": 56, "K": 34},
    "E": {"D": 38, "F": 58, "K": 59},
    "F": {"A": 44, "E": 58},
    "G": {"B": 64, "H": 27, "J": 55},
    "H": {"D": 56, "G": 27, "I": 35, "K": 44},
    "I": {"H": 35, "J": 40},
    "J": {"G": 55, "I": 40},
    "K": {"D": 34, "E": 59, "H": 44}
}
heuristica_avion = {
        "A": 38,
        "B": 97,
        "C": 59,
        "D": 62,
        "E": 46,
        "F": 0,
        "G": 111,
        "H": 112,
        "I": 139,
        "J": 158,
        "K": 87,
    }
def a_star(Inicio, destino, distancias, heuristica_avion):
    open_set = [(0, Inicio)]
    closed_set = set()
    came_from = {}

    g_score = {node: float('inf') for node in distancias}
    g_score[Inicio] = 0

    f_score = {node: float('inf') for node in distancias}
    f_score[Inicio] = heuristica_avion[Inicio]

    while open_set:
        current = min(open_set, key=lambda x: x[0])[1]

        if current == destino:
            path = reconstruct_path(came_from, current)
            return path

        open_set = [(fs, node) for fs, node in open_set if node != current]
        closed_set.add(current)

        for neighbor in distancias[current]:
            if neighbor in closed_set:
                continue

            tentative_g_score = g_score[current] + distancias[current][neighbor]

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristica_avion[neighbor]

                if neighbor not in [node for _, node in open_set]:
                    open_set.append((f_score[neighbor], neighbor))

    return None


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

origen = "J"
destino = "F"

destino_node = 'F'
path =a_star(origen, destino , distancias, heuristica_avion)

if path:
    print("Camino:", path)
    print("Distancia:", sum(distancias[path[i]][path[i + 1]] for i in range(len(path) - 1)))
else:
    print("No se encontró un camino.")

def draw_graph(distancias, path):
    G = nx.Graph()

    for nodo, vecinos in distancias.items():
        G.add_node(nodo)
        for vecino, peso in vecinos.items():
            G.add_edge(nodo, vecino, weight=peso)

    pos = nx.spring_layout(G)  # Puedes cambiar el diseño según tus preferencias

    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)

    # Resaltar el camino en color diferente
    edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    edge_colors = ['red' if edge in edges else 'gray' for edge in G.edges()]
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color=edge_colors, width=2)

    plt.show()


