# Trabajo Sobre Algotimos del Módulo sobre Modelos de I.A. En cada Rama habrá un Trabajo diferente para dicho Módulo.

## 1º Rama main, el código implementa el algoritmo A* para encontrar el camino más corto entre dos puntos en un gráfico

##  [2º Rama satisfacción_de_restricciones-_II. Trabajo Sobre Algotimos del Módulo sobre Modelos de I.A. Satisfacción_de_restricciones: Se desea seleccionar cuatro números diferentes del 2 al 9 (ambos incluidos) que cumplan unas condiciones determinadas.](https://github.com/jmatisam/algotitmos_python/tree/satisfacción_de_restricciones-_II)

## [3º Rama satisf_III. Trabajo Sobre Algotimos del Módulo sobre Modelos de I.A. Colorear Mapas: Sea un mapa con los países A,B,C,D y E. Las fronteras entre los países son : (A,B), (A,C), (B,C),(B,D),(C,D),(C,E)y(D,E).](https://github.com/jmatisam/algotitmos_python/tree/satisf_III)

## --------------------------------------------------------------------------------------------------------

# 1º Rama main:
Este código implementa el algoritmo A* para encontrar el camino más corto entre dos puntos en un gráfico, utilizando tanto el costo real para llegar a cada nodo (conocido como el costo g) como una heurística que estima el costo de llegar al nodo final desde un nodo dado (el costo h). La suma de estos dos costos se conoce como el costo f.

## Enunciado del problema.
* [Documentación al proyecto:](https://drive.google.com/file/d/1tJZh2kpwup6iN4nhEL8Y-L12d95i40Wd/view?usp=drive_link)
![Enuciado](enucniado.png)


El código define dos diccionarios: distancias, que contiene las distancias entre los nodos, y heuristica_avion, que contiene las estimaciones heurísticas de la distancia al nodo objetivo F desde cada nodo.

La función a_star es la implementación del algoritmo A*. Inicia con el conjunto abierto open_set que contiene el nodo de inicio con un costo estimado de 0. El closed_set es un conjunto que almacenará los nodos ya evaluados.

La función utiliza dos diccionarios, g_score y f_score, para llevar la cuenta de los costos actuales y estimados, respectivamente. Inicialmente, todos los nodos tienen un costo infinito, excepto el nodo de inicio.

El bucle principal continúa mientras haya nodos en open_set. Selecciona el nodo con el menor costo f y lo evalúa. Si el nodo actual es el destino, reconstruye el camino utilizando la función reconstruct_path y lo devuelve.

Si no es el destino, el algoritmo actualiza los costos de los vecinos del nodo actual y los agrega al open_set si no están en el closed_set y si el nuevo camino es mejor que cualquier camino previo encontrado.

La función reconstruct_path construye el camino recorriendo hacia atrás desde el nodo destino hasta el nodo de inicio, utilizando el diccionario came_from que mantiene un registro de cómo se llegó a cada nodo.

Finalmente, la función draw_graph utiliza la biblioteca networkx para dibujar el gráfico y resaltar el camino encontrado. Utiliza matplotlib para mostrar el gráfico.

Aquí hay un ejemplo de cómo podría verse un gráfico simple con los nodos y caminos:

![Grafico](https://github.com/jmatisam/algotitmos_python/blob/main/Esquema_camino.png)


