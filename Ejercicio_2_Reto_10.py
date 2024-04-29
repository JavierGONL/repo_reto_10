def producto_punto(arreglo1, arreglo2):
    producto = 0
    for n in range(len(arreglo1)):
        producto += arreglo1[n] * arreglo2[n]
    return producto
if __name__ == "__main__":
    arreglo1 = [2, 4, 6]
    arreglo2 = [3, 6, 9]
    print(f"el producto punto de los arreglos es {producto_punto(arreglo1, arreglo2)}")