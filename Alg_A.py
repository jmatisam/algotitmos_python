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

def heuristica(nodo, destino):
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
    return heuristica_avion[nodo]

def astar(G, origen, destino):
    abiertos = {origen}
    cerrados = set()
    camino = []

    while abiertos:
        nodo_actual = min(abiertos, key=lambda nodo: G.nodes[nodo]['weight'] + heuristica(nodo, destino))
        abiertos.remove(nodo_actual)
        cerrados.add(nodo_actual)

        for nodo_adyacente, peso in G[nodo_actual].items():
            if nodo_adyacente in cerrados:
                continue

            distancia_estimada = G.nodes[nodo_actual]['weight'] + peso['weight']

            # Imprime los pasos
            print(f"{nodo_actual} -> {nodo_adyacente} ({peso['weight']})")

            if distancia_estimada < G.nodes[nodo_adyacente]['weight']:
                G.nodes[nodo_adyacente]['weight'] = distancia_estimada
                abiertos.add(nodo_adyacente)

                # Mover la condición del destino aquí
                if nodo_adyacente == destino:
                    break

        camino.append(nodo_actual)

       # Visualización del grafo
        plt.figure(figsize=(8, 6))

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')
        
        # Resaltar el camino recorrido
        edge_colors = ['red' if edge in zip(camino, camino[1:]) else 'black' for edge in G.edges]
        node_colors = ['red' if node in camino else 'skyblue' for node in G.nodes]

        nx.draw(G, pos, with_labels=True, node_size=700, node_color=node_colors, font_size=8, font_color='black', edge_color=edge_colors)

        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')
        plt.title(f"Paso actual: {nodo_actual}")
        plt.show()

        # Verificar la condición del destino aquí
        if nodo_adyacente == destino:
            camino.append(destino)
            break

    return camino


# Crear grafo de NetworkX
G = nx.Graph()

# Agregar nodos y aristas al grafo
for nodo, conexiones in distancias.items():
    G.add_node(nodo, weight=float('inf'))  # Inicializar pesos a infinito
    for destino, peso in conexiones.items():
        G.add_edge(nodo, destino, weight=peso)

# Asegurar que el origen y el destino estén en el grafo
origen = "J"
destino = "F"
G.add_node(origen, weight=float('inf'))
G.add_node(destino, weight=float('inf'))

# Inicializar el peso del nodo de origen a 0
G.nodes[origen]["weight"] = 0

# Ejecutar A*
camino = astar(G, origen, destino)

# Mostrar resultados
print(f"Distancia: {G.nodes[destino]['weight']}")
