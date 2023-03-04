import datetime
libros={}

while True:
    opcion=int(input(f'Seleccione alguna de las siguientes opciones: \n [1:Subir libro]\n [2:Consultas y Reportes]\n [3:Salir]\n '))
    if opcion==1:
        identificador=max(libros, default=0)+1
        titulo=input('Ingrese el titulo del libro: ').upper()
        autor=input('Ingrese el autor del libro: ').upper()
        genero=input('Ingrese el genero del libro: ').upper()
        año=input('Ingrese el año en que fue publicado el libro: ')
        isbn=input('Ingrese el ISBN del libro: ')
        fecha_adquisicion=input('Ingrese la fecha  en que fue adquirido el libro (dd/mm/aaaa): ')
        fecha_adq= datetime.datetime.strptime(fecha_adquisicion, "%d/%m/%Y").date()
        fecha = (fecha_adq.strftime("%d/%m/%Y"))
        libros[identificador]=[titulo,autor,genero,año,isbn,fecha]
        
    elif opcion==2:
        while True:
            menu=int(input(f'Seleccione alguna de las siguientes opciones:\n[1:Consulta de titulo]\n[2:Reportes]\n[3:Volver al menu]\n'))
            if menu==1:
                while True:
                    consulta=int(input(f'Seleccione alguna de las siguientes Consultas:\n[1:Por titulo]\n[2:Por ISBN]\n[3:Salir]\n'))
                    if consulta==1:
                        consulta_titulo=input('Ingrese el nombre del titulo a buscar: ').upper()
                        for titulos, autor, genero, año_publicacion, isbn, fecha in libros.values():
                            if titulos==consulta_titulo:
                                print(f"Datos del Libro\nTitulo={titulos}\nAutor={autor}\nGenero={genero}\nAño de publicacion={año_publicacion}\nISBN={isbn}\nFecha de aquisicion={fecha}")
                    elif consulta==2:
                        consulta_isbn=input('Ingrese el ISBN del libro a consultar')
                        for titulo, autor, genero, año_publicacion, isbns, fecha in libros.values():
                            if isbns==consulta_isbn:
                                print(f"Datos del Libro\nTitulo={titulo}\nAutor={autor}\nGenero{genero}\nAño de publicacion={año_publicacion}\nISBN={isbns}\nFecha de aquisicion={fecha}")
                    elif consulta==3:
                        break
                    else:
                        print('Opcion no valida')
                        continue

            elif menu==2:
                while True:
                    reportes=int(input(f"Seleccione por que medio desea realizar los reportes:\n[1:Ver catalogo completo]\n[2:Por autor]\n[3:Genero]\n[4:Año publicacion]\n[5:Salir]\n"))
                    if reportes==1:
                        diccionario = libros.values()
                        print("\n** Catálogo completo ** ")
                        print("Titulo \t\t\tAutor\t\t\tGenero\t\t\tAño de Publicación\t\t\tISBN\t\t\tFecha de Adquisición")
                        print("*" * 120)
                        for titulo, autor, genero, año_publicacion, isbn, fecha in diccionario:
                            print(f"{titulo: <15} | {autor: <15} | {genero: <15} | {año_publicacion: <15} | {isbn:<15} |  {fecha:<15}")

                    elif reportes==2:
                        print('Los autores disponibles son:')
                        lista_autores=[autor for titulo, autor, genero, año_publicacion, isbn, fecha in libros.values()]
                        set_autores=set(lista_autores)
                        print(set_autores)
                        autor_busqueda=input('Ingrese el nombre del autor: ').upper()
                        print("Titulo \t\t\tAutor\t\t\tGenero\t\t\tAño de Publicación\t\t\tISBN\t\t\tFecha de Adquisición")
                        for titulo, autor, genero, año_publicacion, isbn, fecha in libros.values():
                            if autor==autor_busqueda:
                                print(f"{titulo: <15} | {autor: <15} | {genero: <15} | {año_publicacion: <15} | {isbn:<15} |  {fecha:<15}")	
                        continue

                    elif reportes==3:
                        print('Los generos disponibles son:')
                        lista_generos=[genero for titulo, autor, genero, año_publicacion, isbn, fecha in libros.values()]
                        set_generos=set(lista_generos)
                        print(set_generos)
                        genero_busqueda=input('Ingrese el Genero: ').upper()
                        print("Titulo \t\t\tAutor\t\t\tGenero\t\t\tAño de Publicación\t\t\tISBN\t\t\tFecha de Adquisición")
                        for titulo, autor, genero, año_publicacion, isbn, fecha in libros.values():
                            if genero==genero_busqueda:
                                print(f"{titulo: <15} | {autor: <15} | {genero: <15} | {año_publicacion: <15} | {isbn:<15} |  {fecha:<15}")	
                        continue

                    elif reportes==4:
                        print('Los años disponibles son:')
                        lista_años=[año_publicacion for titulo, autor, genero, año_publicacion, isbn, fecha in libros.values()]
                        set_años=set(lista_años)
                        print(set_años)
                        año_busqueda=input('Ingrese el año: ')
                        print("Titulo \t\t\tAutor\t\t\tGenero\t\t\tAño de Publicación\t\t\tISBN\t\t\tFecha de Adquisición")
                        for titulo, autor, genero, año_publicacion, isbn, fecha in libros.values():
                            if año_publicacion==año_busqueda:
                                print(f"{titulo: <15} | {autor: <15} | {genero: <15} | {año_publicacion: <15} | {isbn:<15} |  {fecha:<15}")	
                        continue
                    elif reportes==5:
                        break
                    else:
                        print('Opcion no valida')
                        continue
            elif menu==3:
                break
            else:
                print('Opcion no valida')
                break
                
    elif opcion==3:
        break
    else:
        print('Opcion no valida')