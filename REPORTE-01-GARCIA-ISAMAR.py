
import os
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_products
from lifestore_file import lifestore_searches

lista_a=['lala', 'lolo','stemen']
lista_b=['123','456','789']
lista_c=['admin','user','user']
name = input('Ingrese su usuario: ')
pw = input('Ingrese su contraseña: ')

correcto = 0
correcta = 0
correcto1 = 1
while correcta != 1:
  while correcto != 1:
    if name in lista_a and pw in lista_b:
        correcto = 1
        if lista_a.index(name) == lista_b.index(pw):
          if lista_c[lista_a.index(name)] == 'admin':
            os.system("clear")
            print('Bienvenido administrador')
            input("Presiona enter para continuar")
            os.system("clear")  
            while correcta != 1:
              if correcto1 == 1:
                print("\tBienvenid@ al reporte anual de Lifestore\n")
                print("\t               Edición 2020\n")
                print("A continuación se presenta el menú de reportes a generar, selecciona la letra correspondiente:\n")
                print("a) Productos más  y menos vendidos y productos con mayores y menores búsquedas.\nb) Productos por reseña de clientes y las devoluciones.\nc) Total de ingresos y ventas promedio mensuales.\nd) Salir del reporte anual\n")
                opcion = input('Escribe la letra (en minúscula) del reporte que desees consultar: ')
              if opcion == "a":
                os.system("clear") 
                #print("Seleccionaste a")
                while True:
                  #os.system("clear")
                  print("\tSelecciona el reporte a visualizar\n")
                  print("1.-Top 50 mayores ventas")
                  print("2.-Productos con mayores búsquedas")
                  print("3.-Productos con menores ventas")
                  print("4.-Productos con menores búsquedas")
                  print("5.-Regresar al menú inicial") 
                  option=input("Ingresa una opción: ") 
                  if option == "1":
                    #correcta = 1
                    os.system("clear")
                    print("#####TOP 50 MAYORES VENTAS#####")
                #correcta = 1
                    contador = 0
                    total_ventas = [] ##[[id,nombre,contador], [id2,contador2]]
                    for producto in lifestore_products:
                      for venta in lifestore_sales:
                        categoria = producto[3]
                        if producto[0] == venta[1]:
                          contador += 1
                      formato_ideal = [producto[0],producto[1],contador,categoria]
                      total_ventas.append(formato_ideal)
                      contador = 0

                    aux = None
                    for i in range (0,len(total_ventas)):
                      for j in range (0,len(total_ventas)):
                        if(total_ventas[i][2] > total_ventas[j][2]):
                          aux = total_ventas[i]
                          total_ventas[i] = total_ventas[j]
                          total_ventas[j] = aux 

                    counter = 1
                    for i in range(0,len(total_ventas)):
                      if total_ventas[i][2] != 0: ##Omite las busquedas 0
                        print(counter,'.- El producto: ', total_ventas[i][0], '\n Se vendió: ', total_ventas[i][2],'veces', '\n Pertenece a la categoría: ', total_ventas[i][3])
                        counter += 1
                #correcta = 1
                    print(".")
                    returns = input(print("Da enter para regresar al menú anterior"))
                    os.system("clear")
                    continue
                  elif option == "2":
                    #correcta = 1
                    os.system("clear")
                    print("#####PRODUCTOS CON MAYORES BÚSQUEDAS#####")
                    contador = 0
                    total_busquedas = [] ##[[id,nombre,contador], [id2,contador2]]

                    for producto2 in lifestore_products:
                      for busqueda in lifestore_searches:
                        categoria = producto2[3]
                        if producto2[0] == busqueda[1]:
                          contador += 1
                      formato_ideal2 = [producto2[0],producto2[1],contador,categoria]
                      total_busquedas.append(formato_ideal2)
                      contador = 0

                    aux = None
                    for i in range (0,len(total_busquedas)):
                      for j in range (0,len(total_busquedas)):
                        if(total_busquedas[i][2] > total_busquedas[j][2]):
                          aux = total_busquedas[i]
                          total_busquedas[i] = total_busquedas[j]
                          total_busquedas[j] = aux

                    counter = 1
                    for i in range(0,len(total_busquedas)):
                      print(counter,'.- El producto: ', total_busquedas[i][1], '\n Se buscó: ', total_busquedas[i][2],'veces', '\n Pertenece a la categoría: ', total_busquedas[i][3])
                      counter += 1
                #correcta = 1    
                    print(".")
                    returns = input(print("Da enter para regresar al menú anterior"))
                    os.system("clear")
                    continue   
                  elif option == "3":
                    #correcta = 1
                    os.system("clear")
                    print("#####PRODUCTOS CON MENORES VENTAS#####")
                    contador = 0
                    total_ventas = [] ##[[id,nombre,contador], [id2,contador2]]

                    for producto in lifestore_products:
                      for venta in lifestore_sales:
                        categoria = producto[3]
                        if producto[0] == venta[1]:
                          contador += 1
                      formato_ideal = [producto[0],producto[1],contador,categoria]
                      total_ventas.append(formato_ideal)
                      contador = 0

                    aux = None
                    for i in range (0,len(total_ventas)):
                      for j in range (0,len(total_ventas)):
                        if(total_ventas[i][2] < total_ventas[j][2]):
                          aux = total_ventas[i]
                          total_ventas[i] = total_ventas[j]
                          total_ventas[j] = aux 

                    counter = 1
                    for i in range(0,55): ##son 54 con venta cero
                      print(counter,'.- El producto: ', total_ventas[i][1], '\n Se vendió: ', total_ventas[i][2],'veces', '\n Pertenece a la categoría: ', total_ventas[i][3])
                      counter += 1 
                    #correcta = 1    
                    print(".")
                    returns = input(print("Da enter para regresar al menú anterior"))
                    os.system("clear")
                    continue   
                  elif option == "4":
                    #correcta = 1
                    os.system("clear")
                    print("#####PRODUCTOS CON MENORES BÚSQUEDAS#####")
                    contador = 0
                    total_busquedas = [] ##[[id,nombre,contador], [id2,contador2]]

                    for producto2 in lifestore_products:
                      for busqueda in lifestore_searches:
                        categoria = producto2[3]
                        if producto2[0] == busqueda[1]:
                          contador += 1
                      formato_ideal2 = [producto2[0],producto2[1],contador,categoria]
                      total_busquedas.append(formato_ideal2)
                      contador = 0

                    aux = None
                    for i in range (0,len(total_busquedas)):
                      for j in range (0,len(total_busquedas)):
                        if(total_busquedas[i][2] < total_busquedas[j][2]):
                          aux = total_busquedas[i]
                          total_busquedas[i] = total_busquedas[j]
                          total_busquedas[j] = aux

                    counter = 1
                    for i in range(0,len(total_busquedas)):
                      print(counter,'.- El producto: ', total_busquedas[i][1], '\n Se buscó: ', total_busquedas[i][2],'veces', '\n Pertenece a la categoría: ', total_busquedas[i][3])
                      counter += 1
                    #correcta = 1    
                    print(".")
                    returns = input(print("Da enter para regresar al menú anterior"))
                    os.system("clear")
                    continue
                  elif option == "5":
                    os.system("clear")
                    break
              elif opcion == "b":
                os.system("clear")
                print("A continuación se muestran dos listas: \nTop 20 productos con mejores reseñas \nTop 20 productos con peores reseñas \n\nPosteriormente se muestran las devoluciones: \n")
                print("#####TOP 20 PRODUCTOS CON MEJORES RESEÑAS#####")
                ranked_products  = []
                product_stars = [ [] for i in range(len(lifestore_products)) ]
                   
                for sale in lifestore_sales:
                  product_stars[sale[1] - 1].append(sale[2])

                for product in lifestore_products:
                  category = product[3]
                  if(len(product_stars[product[0]-1])):
                      ranked_products.append( (sum(product_stars[product[0] - 1]) / len(product_stars[product[0] - 1]), product[1], category) )
                  else:
                      ranked_products.append( (0.0, product[0], category) )

                ordered_ranking = sorted(ranked_products, reverse=True)
##extra
                counter = 1
                for i in range(0,20):
                  if ordered_ranking[i][0] != 0.0: 
                    print(counter,'.- El producto: ', ordered_ranking[i][1], '\n Tiene una reseña de: ', ordered_ranking[i][0], '\n Pertenece a la categoría: ', ranked_products[i][2])
                    counter += 1

                print("\n#####TOP 20 PRODUCTOS CON PEORES RESEÑAS#####")
                ranked_products  = []
                product_stars = [ [] for i in range(len(lifestore_products)) ]
             
                for sale in lifestore_sales:
                  product_stars[sale[1] - 1].append(sale[2])

                for product in lifestore_products:
                  category = product[3]
                  if(len(product_stars[product[0]-1])):
                      ranked_products.append( (sum(product_stars[product[0] - 1]) / len(product_stars[product[0] - 1]), product[1], category) )
                  else:
                      ranked_products.append( (0.0, product[0], category) )

                ordered_ranking = sorted(ranked_products, reverse=False)

                counter = 1
                for i in range(0,74):##top 20 excluyendo los no calificados
                  if ordered_ranking[i][0] != 0.0: 
                    print(counter,'.- El producto: ', ordered_ranking[i][1], '\n Tiene una reseña de: ', ordered_ranking[i][0], '\n Pertenece a la categoría: ', ranked_products[i][2])
                    counter += 1

                print("\n#####DEVOLUCIONES#####")

                devoluciones = []
                contador = 0

                for productodev in lifestore_products:
                  for productovend in lifestore_sales:
                    catego = productodev[3]
                    if productodev[0] == productovend[1]: 
                      if productovend[4] == 1: ##1 es que fue devuelto
                        contador += 1
                  if contador != 0: ##omite los 0 que no fueron devueltos
                    formato_ideal3 = [productodev[1], contador, catego]
                    devoluciones.append(formato_ideal3)
                    contador = 0

                aux = None
                for i in range (0,len(devoluciones)):
                  for j in range (0,len(devoluciones)):
                    if(devoluciones[i][1] > devoluciones[j][1]):
                      aux = devoluciones[i]
                      devoluciones[i] = devoluciones[j]
                      devoluciones[j] = aux

                counter = 1
                for i in range(0,len(devoluciones)):
                  if devoluciones[i][0] != 0: 
                    print(counter,'.- El producto: ', devoluciones[i][0], '\n Se devolvió: ', devoluciones[i][1],'veces', '\n Pertenece a la categoría: ', devoluciones[i][2])
                    counter += 1
                print(".")
                print(input("Da enter para regresar al menú inicial"))
                os.system("clear")
                #correcta = 1
                continue
                #break
              elif opcion == "c":
                os.system("clear")
                print("#####TOTAL DE INGRESOS POR MES#####")
                precio = []
                mes = []
                for i in range(0,len(lifestore_products)):##Se hace una lista con los precios pero se itera muchas veces
                  precio.append(lifestore_products[i][2])
                for i in range(0,len(lifestore_sales)):
                  venta2 = lifestore_sales[i][1]-1 ##Se saca el id
                  fechav = lifestore_sales[i][3].split("/")[1]##se saca el mes
                  if len(mes) == 0:
                    mes.append([precio[venta2], fechav])

                  else:
                    bandera = False
                    for m in mes:
                      if m[1] == fechav: 
                        m[0] += precio[venta2]
                        bandera = True 
                    if bandera == False:
                      mes.append([precio[venta2], fechav])        
                aux=[0,0]
                for i in range (0,len(mes)):
                  for j in range (0,len(mes)):
                    if(mes[i][1] < mes[j][1]):
                      aux[0] = mes[i]
                      mes[i] = mes[j]
                      mes[j] = aux[0]

                bigtotal = 0
                for i in range (0,len(mes)):
                  aux = mes[i][0]
                  bigtotal += + aux
                promedio = bigtotal/12

                for i in range(0,len(mes)):
                  print("El mes:",mes[i][1],"tuvo ingresos por: $"+str(mes[i][0]))
                print("\nLos meses 10 y 12 no tuvieron ventas\n\nTotal de ingresos en 2020 fue de: $",str(bigtotal))
                print("Promedio mensual: $",str(promedio))
                print(".")
                print(input("Da enter para regresar al menú inicial"))
                os.system("clear")
                #correcta = 1
                continue  #os.system("clear")
              elif opcion == "d":
                os.system("clear")  
                print("Gracias por consultar el reporte anual de Lifestore, vuelva pronto")
                break
              else:
                print("Opción incorrecta \n")
                correcto1 = 0
                opcion = input("Intenta con una opción del menú: ")
            break
          else:
              print('Bienvenido usuario\nUsted no puede acceder a los reportes anuales de la empresa Lifestore')
    else:
        os.system("clear")
        print ('Usuario o contraseña invalido, intentalo de nuevo:')
        name = input('Ingrese su usuario: ')
        pw = input('Ingrese su contraseña: ')
  break


