
def create_mafia(num_types):
    if num_types is None or num_types < 1 or num_types > 255:
        return "( O_o)"

    if num_types % 2 == 0:
        return "( O_o)"

    if num_types == 1:
        return "(-_-)"

    if num_types <= 7:
        return "(- " + "(-_- " * (num_types - 2) + "_-) " * (num_types - 1) + "-)"

    mafia = "(- " + "(-_- " * ((num_types - 1) // 3) + "(-_ " + "(-_- " * (((num_types - 1) // 3) - 2) + "_-) " * ((num_types - 1) // 3) + "_-) " * (((num_types - 1) // 3) + 1) + "_-) " * (num_types // 3) + "-)"
    return mafia

# Ejemplos de uso
print(create_mafia(11))
print(create_mafia(14))
print(create_mafia(6))
print(create_mafia(256))  # Esto devolverá "( O_o)"