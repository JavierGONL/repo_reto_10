<div align='center'>
<figure> <img src="https://res.cloudinary.com/dm0p2ljin/image/upload/v1714416338/error-418_dtb3ak.png" alt="" width="300" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>


# repo_reto_10

Desarrolle la mayoría de ejercicios en clase. Para cada punto cree un programa individual. Al finalizar suba todo a un repo y subalo al canal reto_10 en slack.

1. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales. 
```python
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
```
2. Desarrollar un algoritmo que calcule el [producto punto](https://www.cuemath.com/algebra/dot-product/) de dos arreglos de números enteros (reales) de igual tamaño.
```python
def producto_punto(arreglo1, arreglo2):
    producto = 0
    for n in range(len(arreglo1)):
        producto += arreglo1[n] * arreglo2[n]
    return producto
if __name__ == "__main__":
    arreglo1 = [2, 4, 6]
    arreglo2 = [3, 6, 9]
    print(f"el producto punto de los arreglos es {producto_punto(arreglo1, arreglo2)}")
```
3. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
```python
def numeros_de_ceros(arreglo_1):
    cantidad_0s = 0
    for n in arreglo_1:
        if n / 10 == n // 10: #se comprueba que si n/10 y n // 10 son iguales es que hay un 0 en el numero
            cantidad_0s += 1
    return cantidad_0s
if __name__ =="__main__":
    arreglo_1 = [10,20,23,89,180,90,23,0,12]# a vista hay 4 0s
    print(numeros_de_ceros(arreglo_1))
```
4. Revisar que son los algoritmos de *sorting*, entender *bubble-sort* ([enlace](https://www.geeksforgeeks.org/bubble-sort/) a implementación).
