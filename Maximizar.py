"""
En este programa, la función maximize_number convierte el número en una cadena, luego crea una lista de caracteres a partir de la cadena, 
la ordena en orden descendente y luego une los caracteres nuevamente para formar el número máximo posible. 
Esto se logra al tener los dígitos más grandes en las posiciones más significativas.
"""
def maximize_number(num):
    num_str = str(num)
    num_list = list(num_str)
    num_list.sort(reverse=True)
    max_num = int(''.join(num_list))
    return max_num

# Ejemplo de uso
valor = 120
maximized_value = maximize_number(valor)
print(f"El número más grande posible al reorganizar los dígitos de {valor} es {maximized_value}.")
