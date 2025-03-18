Algoritmo sin_titulo
	definir notas,totalNotas,notamaxima Como Real
	Dimension notas[2,2]
	totalNotas = 0
	notamaxima = 0
	
	
	para i=0 hasta 1 Hacer
		
		para j=0 hasta 1 Hacer
			
			Escribir "Digite las notas"
			leer notas[i,j]
			
		FinPara
	FinPara
	
	para i=0 hasta 1 Hacer
		para j=0 hasta 1 Hacer
			
			totalNotas = totalNotas + notas[i,j]
			si notamaxima < notas[i,j]
				notamaxima = notas[i,j]
			FinSi
		FinPara
	FinPara
	
	Escribir "el total de notas es: ", totalNotas
	Escribir "la nota maxima es: ", notamaxima
	
FinAlgoritmo
