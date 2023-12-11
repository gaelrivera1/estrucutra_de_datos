def invertir_frase(frase):
    palabras = frase.split()  
    palabras_invertidas = palabras[::-1]  
    frase_invertida = ' '.join(palabras_invertidas)  

    return frase_invertida


frase_original = input("Ingrese una frase: ")


frase_resultante = invertir_frase(frase_original)
print("Frase invertida:", frase_resultante)
