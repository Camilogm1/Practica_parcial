#prduccion lechera con listas
#Diversificación de producción lechera

#Teniendo presente los cambiantes gustos del mercado, la finca Lácteos Gratavista
#ha decidido diversificar su producción lechera diaria. La finca tiene tres tipos
# de animales productores: vacas, cabras y búfalas, de las cuales puede obtener
# producción de leche que va entre 0.5 y 1.5 litros en cada ordeño.

#Es necesario conseguir la meta de producción mínima de 10 litros diarios, como
# una combinación de producción de cada una de las especies previamente indicadas.

#Para ello, los trabajadores de la finca indicarán cual tipo de animal se ordeñó y
# cuanto obtuvo de su producción. Solo si el volumen obtenido está en el rango de
# 0.5 y 1.5 litros se considerará válido. Si no es válido, este contenido no será
# tenido en cuenta y no se actualizarán los totalizadores de producción ni los
# contadores de animales ordeñados.

#Cuando la producción iguale o sobrepase la meta mínima de producción, se terminará
# el proceso de registro y se procede a visualizar los resultados.

#Se debe indicar por cada tipo de animal, cuánta producción se obtuvo y cuántos animales
# se ordeñaron. Finalmente se debe indicar cuanto fue la producción total obtenida de
# todos los procesos de ordeño válidos que fueron registrados.

def calcular_promedio_leche(leche, animal):
    if animal!=0:
        promedio=leche/animal 
        return promedio
    else:
        return 0.0

Animales=['vaca','cabra','bufala']
Total_leche=[0,0,0]
Ordeño_animal=[0,0,0]

carga_min=0.5
carga_max=1.5

Leche_actual =0
Meta_leche =10
Numero_ordeño=1
while Leche_actual<Meta_leche:
    try:
        Animal_ordeñado =input(F'\nEn el ordeño No.{Numero_ordeño} , ingrese el animal(Cabra,vaca,bufala):  ').lower()
        if Animal_ordeñado not in Animales:
            print('El animal ingresado no es valido')
            continue
        Ordeño=float(input(f'Ingrese la cantidad de leche ordeñada (Min 0.5L - Max 1.5L) se lleva {Leche_actual}L:  '))
        if Ordeño<carga_min or carga_max<Ordeño:
            print('El ordeño debe estar dentro del rango permitido')
            continue

        for indice in range(len(Animales)):
            if Animales[indice]==Animal_ordeñado:
                Total_leche[indice]+=Ordeño
                Ordeño_animal[indice]+=1
    except ValueError:
        print('Los datos ingresados no son validos ')
        continue
    Leche_actual+=Ordeño
    Numero_ordeño+=1


promedios=[0,0,0]
for indice in range(len(Animales)):
    promedios[indice]=calcular_promedio_leche(Total_leche[indice], Ordeño_animal[indice])

print ('Resultados ')
for indice in range (len(Animales)):
    print(f'Animal: {Animales [indice]:.2f},leche total {Total_leche[indice]:.2f}, Veces ordeñado {Ordeño_animal[indice]:.2f} ')
