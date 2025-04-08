#produccion lechera con diccionarios 

def calcular_promedio_efectividad(leche,ordeños):
    try:
        promedio = leche /ordeños
        return promedio
    except ZeroDivisionError:
        return 0
    
diccionario_animales={
'vaca':{'Ordeños':0,'Leche':0 ,'promedio':0},
'cabra':{'Ordeños':0,'Leche':0,'promedio':0},
'bufala':{'Ordeños':0,'Leche':0,'promedio':0}
}

Leche_min=0.5
leche_max=1.5

leche_actual=1
leche_meta=10
print('Los animales son ')
for llave in diccionario_animales.keys():
    print(f'-{llave}')

while leche_actual<= leche_meta:
    animal=input(f'\nEn el ordeño No.{leche_actual} escoja el animal: ').lower()
    if animal not in diccionario_animales.keys():
        print('El animal seleccionado no es valido ')
        continue
    try:
        leche=float(input(f'Ingrese la cantida de leche ordeñada (Debe de estar en el rango entre {Leche_min}L y {leche_max}): '))
        if leche<Leche_min or leche_max<leche:
            print(f'la cantidad de leche ingresada debe de estar en el rango entre {Leche_min}L y {leche_max}')
            continue
        
        diccionario_animales[animal]['Leche']+=leche
        diccionario_animales[animal]['Ordeños']+=1

    except ValueError:
        print('Los datos ingresados no son validos ')
        continue
    leche_actual+=1

for llave in diccionario_animales.keys():
    diccionario_animales[llave]['promedio']= calcular_promedio_efectividad(
        diccionario_animales[llave]['Leche'], diccionario_animales[llave]['Ordeños']    )

print(f' \nResultados ')
for llave in diccionario_animales.keys():
    print(f'- Animal: {llave}', end="")
    print(f'- Leche total: {diccionario_animales[llave]['Leche']}',end="")
    print(f'- Ordeños: {diccionario_animales[llave]['Ordeños']}', end="")
    print(f'- Promedio: {diccionario_animales[llave]['promedio']:.2f}')
