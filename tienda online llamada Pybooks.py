#Caso de Una tienda online llamada Pybooks

#listas
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}


stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}


def menu():
    while True:
        print("\n* MENU PRINCIPAL *")
        print("1. Stock marca")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case '1':
                marca = input("Ingrese marca a consultar: ")
                stock_marca(marca)

            case '2':
                while True:
                    try:
                        p_min = int(input("Ingrese precio mínimo: "))
                        p_max = int(input("Ingrese precio máximo: "))
                        break
                    except ValueError:
                        print("Debe ingresar valores enteros!!")
                busqueda_precio(p_min, p_max)

            case '3':
                while True:
                    codigo = input("Ingrese modelo a actualizar: ").upper()
                    try:
                        nuevo_precio = int(input("Ingrese el nuevo precio: "))
                    except ValueError:
                        print("Debe ingresar un precio válido (entero)!!")
                        continue

                    if actualizar_precio(codigo, nuevo_precio):
                        print("Precio actualizado!!")
                    else:
                        print("El modelo no existe!!")

                    continuar = input("¿Desea actualizar otro precio (s/n)?: ").lower()
                    if continuar != 's':
                        break

            case '4':
                print("Programa finalizado.")
                break

            case _:
                print("Debe seleccionar una opción válida!!")
                


#Opcion 1 
def stock_marca(marca):
    total = 0
    marca = marca.lower()
    for codigo, datos in stock.items():
        if datos[1].lower() == marca:
            total += productos[codigo][1]
    print(f"El stock es: '{marca}': {total}")

#Opcion 2
def busqueda_precio(p_min, p_max):
    disponibles = []
    for codigo, datos in stock.items():
        precio = datos[0]
        
        if p_min <= precio <= p_max :
            productos = productos[codigo][0]
            disponibles.append(f"{productos} -- {codigo}")
    if disponibles:
        disponibles.sort()
        print("\nLos notebooks entre los precios consultas son:")
        for producto in disponibles:
            print(producto)
    else:
        print("No hay notebooks en ese rango de precios.")


#Opcion 3   
def actualizar_precio(codigo, nuevo_precio):
    if codigo in stock:
        stock[codigo][0] = nuevo_precio
        return True
    else:
        return False

                
menu()
