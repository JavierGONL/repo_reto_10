def promedio_arreglo_reales(cantidad_numeros): # pro,edio de un arreglo de numeros reales
    suma_del_promedio = 0
    for _ in range(cantidad_numeros):
        # se usa un for para recorrer la cantidad de numeros que se ingresaron e ir sumando los numeros para luego dividirlos por la cantidad de numeros
        numero = float(input("ingrese un numero: "))
        suma_del_promedio += numero
    promedio = suma_del_promedio / cantidad_numeros
    return promedio
if __name__ == "__main__":
    cantidad_numeros = int(input("ingrese la cantidad de numeros que desea promediar: "))
    print(f"el promedio es {promedio_arreglo_reales(cantidad_numeros)}")
        