def calcular_promedio(lista_numeros):
    """
    Purpose: Calcula el promedio de una lista de números
    """
    suma_total = sum(lista_numeros) 
    promedio = suma_total/len(lista_numeros)
    return promedio

# end def

if __name__ == "__main__":
    mis_calificaciones = [85, 90, 78, 92, 88]
    resultado = calcular_promedio(mis_calificaciones)
    print(f"El promedio es: {resultado:.2f}")

    for nota in mis_calificaciones:
        if (nota > 90):
            print(f"¡Excelente nota: {nota}!") 
        # end if
    # end for
    
# end main

