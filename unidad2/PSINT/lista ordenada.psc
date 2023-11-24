Algoritmo ordenalista
	Dimensionar lista(200)
	Escribir 'ingrese los nombres (enter en blanco para terminar):'
	cant <- 0
	Leer nombre
	Mientras nombre<>'' Hacer
		cant <- cant+1
		lista[cant] <- nombre
		Repetir
			Leer nombre
			se_repite <- Falso
			Para i<-1 Hasta cant Hacer
				Si nombre=lista[1] Entonces
					se_repite <- Verdadero
				FinSi
			FinPara
		Hasta Que  NO se_repite
	FinMientras
	Para i<-1 Hasta cant-1 Hacer
		pos_menor <- 1
		Para j<-i+1 Hasta cant Hacer
			Si lista[j]<lista[pos_menor] Entonces
				pos_menor <- j
			FinSi
		FinPara
		aux <- lista[i]
		lista[i] <- lista[pos_menor]
		lista[pos_menor] <- aux
	FinPara
	Escribir 'la lista esta ordenada:'
	Para i<--1 Hasta cant Hacer
		Escribir '  ', lista[i]
	FinPara
FinAlgoritmo
