lista_libros=[]
generos=("Ficción","No ficción","Ciencia")
registro_venta=[]


def selecciona_genero():
    print("1. Ficción\n2. No Ficción\n3. Ciencia")
    genero=int(input("Seleccione un género: "))
    if genero==1:
        return generos[0]
    elif genero==2:
        return generos[1]
    elif genero==3:
        return generos[2]
    else:
        print("Opción no valida")



def registro():
    
    titulo=input("Ingrese título del libro: ")
    titulo=titulo.upper()
    autor=input("Ingrese autor del libro: ")
    autor=autor.upper()

    genero=selecciona_genero()
    try:    
        precio=int(input("ingrese precio del libro: "))
        stock=int(input("Ingrese stock disponible: "))
    except ValueError:
        print("valor inválido")
    nuevo_libro=[titulo,autor,genero,precio,stock]
    lista_libros.append(nuevo_libro)

def listar():
    print("Título\t\t Autor\t\t Género\t\t Precio\t\t Stock\n")
    for libro in lista_libros:
        print(f"{libro[0]}\t{libro[1]}\t{libro[2]}\t\t{libro[3]}\t{libro[4]} \n")

def venta():
    libro=input("Ingrese título del libro a vender: ")
    libro=libro.upper()
    for i in lista_libros:
        if i[0]==libro:
            cantidad=int(input("Ingrese cantidad a vender: "))
            total=cantidad*i[3]
            i[4]-=cantidad
            genero=i[2]
            print(f"Detalle:\nItem: {libro}\nPrecio unitario: {i[3]}\nCantidad: {cantidad}\nTotal: {total} ")
            nueva_venta=[libro,genero,cantidad]
            registro_venta.append(nueva_venta)


def reporte():
    print("1. Reporte completo\n2. Reporte por género")
    tipo=int(input("Ingrese una opción: "))
    if tipo==1:
        print("Titulo\t\t Género \t\t Cantidad vendida")
        for venta in registro_venta:
            print(f"{venta[0]}\t\t{venta[1]}\t\t{venta[2]}")
    elif tipo==2:
        genero=selecciona_genero()
        print("Titulo\t\t Género \t\t Cantidad vendida")
        for venta in registro_venta:
            if venta[1]==genero:
              print(f"{venta[0]}\t\t{venta[1]}\t\t{venta[2]}")
    else:
        print("opción inválida, intente nuevamente")
            
def documento():
    print("1. Reporte completo\n2. Reporte por género")
    op=int(input("Ingrese opción para impresión de reporte"))
    with open("registro_ventas.txt","w") as archivo:
        if op==1:
            archivo.write("Titulo\t\t Género \t\t Cantidad vendida\n") 
            for venta in registro_venta:
                archivo.write(f"{venta[0]}\t\t{venta[1]}\t\t{venta[2]}\n")
            print("ARCHIVO GENERADO EXITOSAMENTE")
        elif op==2:
            genero=selecciona_genero()
            for venta in registro_venta:
                archivo.write("Titulo\t\t Género \t\t Cantidad vendida\n")
                if venta[1]==genero:
                    archivo.write(f"{venta[0]}\t\t{venta[1]}\t\t{venta[2]}\n")
            print("ARCHIVO GENERADO EXITOSAMENTE")

        else:
            print("Opción inválida, Intente nuevamente")


while True:
    print("1. Registrar Libro\n2. Listar todos los libros\n3. Registrar venta\n4. Mostrar ventas por pantalla\n5. Generar documento\n6. Salir ")
    try:
        op=int(input("Ingrese opción: "))
    except ValueError:
        print("MENU INVÁLIDO")
    if op==1:
        registro()
    elif op==2:
        listar()
    elif op==3:
        venta()
    elif op==4:
        reporte()
    elif op==5:
        documento()
    elif op==6:
        break
    else:
        print("Opción inválida, intente nuevamente")

