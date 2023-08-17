"""
Este algoritmo utiliza la programación dinámica para calcular la cantidad de formas en que la rana puede cruzar el río. 
"""
def count_frog_ways(rocks):
    if rocks <= 0:
        return 0
    elif rocks == 1:
        return 1
    elif rocks == 2:
        return 2
    elif rocks == 3:
        return 4

    ways = [0] * (rocks + 1)
    ways[1] = 1
    ways[2] = 2
    ways[3] = 4

    for i in range(4, rocks + 1):
        ways[i] = ways[i - 1] + ways[i - 2] + ways[i - 3]

    return ways[rocks]

# Ejemplo de uso

num_rocks = 3
# Este es un bloque de codigo en el cual se peude ingresar la cantidad de rocas
"""
numrocks = input()
"""
total_ways = count_frog_ways(num_rocks)
print(f"La rana puede cruzar el río de {num_rocks} rocas de {total_ways} formas distintas.")