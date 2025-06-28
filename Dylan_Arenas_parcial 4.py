


def menu_inicial():
    while True:
        print("1.- Reservar zapatillas”.")
        print("2.- Buscar zapatilla reservada”.")
        print("3.- Ver stock de reservas.")
        print("4.- Salir.")
        opcion=input("Ingrese su opción: ")
        
        match opcion:
            case "1":
                reserva_zapatilla()
                
            case "2":
                buscar_reserva()
              
            case "3":
                stock_reserva()
               
            case "4":
                print("Programa terminado")
                break
            case _:
                print("debe ingresar una opcion valida")
                
def reserva_zapatilla():
    while True:
        nombre_valido=True
        nombre=input("Ingrese su nombre: ").lower()
        
        for idx in reservas:
            if nombre == idx["nombre"]:
                print("Este nombre ya está repetido")
                nombre_valido = False
                break

        if nombre_valido:
            validacion_de_reserva=input("¿Estas en lista de reserva?, de ser asi introduce la palabra secreta: ")
            if validacion_de_reserva == "EstoyEnListaDeReserva":
                
                reservas.append(nombre)
                print("Reserva exitosa! ")
                i -1
                break
                
            else:
                print("No estas en lista de reserva")

def buscar_reserva():
    while True:
        buscar_reserva = input("Con que nombre reservaste tus zapatillas: ")
        if buscar_reserva in reservas:
            input("¿Desea pagara adicional por la reserva VIP?").lower
            if "si":
                i-1
            else:
                break
        else:
            print("su nombre no esta en la lista ")
            break
            
            
def stock_reserva():
    total=reservas - i
    print(f"Quedan un total de: {total}")

i = 20   
reservas = []
menu_inicial()             
            



                
            







