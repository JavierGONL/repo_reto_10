def numeros_de_ceros(arreglo_1):
    cantidad_0s = 0
    for n in arreglo_1:
        if n / 10 == n // 10: #se comprueba que si n/10 y n // 10 son iguales es que hay un 0 en el numero
            cantidad_0s += 1
    return cantidad_0s
if __name__ =="__main__":
    arreglo_1 = [10,20,23,89,180,90,23,0,12]# a vista hay 4 0s
    print(numeros_de_ceros(arreglo_1))