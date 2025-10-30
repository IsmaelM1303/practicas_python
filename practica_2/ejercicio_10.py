personas = [("Juan", 25), ("Ana", 20), ("Luis", 30)]

personas_ordenadas = sorted(personas, key=lambda persona: persona[1])

print("Lista original:")
print(personas)

print("\nLista ordenada por edad:")
print(personas_ordenadas)
