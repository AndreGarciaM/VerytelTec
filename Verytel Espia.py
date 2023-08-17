"""
Funcion find_spy_id:
Entrada: Lista de ID´s
Retorno: ID del espia
"""
def find_spy_id(id_list):
    even_count = 0
    odd_count = 0
    spy_id = None

    for num in id_list:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            spy_id = num

    if even_count == 1:
        return spy_id

    if odd_count == 1:
        return spy_id

# Ejemplo de uso
lista_ids = [10, 8, 66, 124, 12, 11, 2602, 36]
# Este es un bloque de codigo en el cual se ingresan los valores del Array
"""
cantidad = int(input("Ingrese la cantidad de elementos en el array: "))
        array = []

        for i in range(cantidad):
            num = float(input(f"Ingrese el número para la posición {i}: "))
            array.append(num)
lista_ids = array
"""
spy_id = find_spy_id(lista_ids)
print(f"El espía tiene la identificación: {spy_id}")