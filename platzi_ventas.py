print("Bienvenido al sistema de ventas de clientes")
print("Elige la opcion que deseas")
print("**C CREAR CLIENTES")
print("**R LISTAR CLIENTES")
print("**U ACTUALIZAR CLIENTES")
print("**D BORRAR CLIENTES")
clients="Sergio,Erick"
opcion=input("Escribe la opcion")

def get_name():
    client_name=input("Ingresa el nombre del cliente")
    return client_name

if opcion.upper()=='C':
    client_name=get_name()
    clients+=','+client_name
    print(clients)
else:
    print("Lo lamento esa opcion no existe")

