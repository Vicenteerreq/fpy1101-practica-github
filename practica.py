# ============================================================
# Registro simple de productos
# FPY1101 - Fundamentos de Programación
# Metodología E.P.S. = Entrada - Proceso - Salida
# ============================================================
# ENTRADA
lista_productos = []
producto_1 = input("Ingrese el primer producto: ")
producto_2 = input("Ingrese el segundo producto: ")
producto_3 = input("Ingrese el tercer producto: ")
# PROCESO
lista_productos.append(producto_1)
lista_productos.append(producto_2)
lista_productos.append(producto_3)
# SALIDA
print("Productos registrados:")
print(lista_productos)