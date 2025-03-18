Algoritmo sin_titulo
	
	definir cantidad Como Entero
	definir vector,nombre Como Caracter
	
	Escribir "Digite el tamaño del arreglo"
	leer cantidad
	
	Dimension vector[cantidad]
	
	para i=0 hasta cantidad-1 Con Paso 1 Hacer
		Escribir "Digite el nombre ", i+1
		leer nombre
		vector[i]=nombre
	FinPara
	
	para i=0 Hasta cantidad-1 Hacer
		
		Escribir vector[i]
		
	FinPara
	
	
	
	
	
FinAlgoritmo
