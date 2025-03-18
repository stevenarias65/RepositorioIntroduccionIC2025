Algoritmo sin_titulo
	//Crea dos arrays o arreglos unidimensionales que tengan el mismo tamaño 
	//(lo pedir? por
	//teclado), en uno de ellos almacenaras nom?res de personas como cadenas, en 
	//el otro array o
	//arreglo ira almacenando la longitud de los nom?res, para ello puedes usar la 
	//#unci$n
	//LONGITUD(cadena) que viene en 'se-nt. Muestra por pantalla el nom?re y la 
	//longitud que
	//&ene. 'uedes usar #unciones si lo deseas.
	
	
	definir arregloNombre Como Caracter
	definir arregloLogitud,logitud Como Entero
	
	Escribir "Digite el tamaño que desea ingresar"
	leer logitud
	
	Dimension arregloNombre[logitud]
	Dimension arregloLogitud[logitud]
	
	para i=0 hasta logitud-1 Hacer
		Escribir "Digite el nombre"
		leer arregloNombre[i]
		arregloLogitud[i] = Longitud(arregloNombre[i])
	FinPara
	
	//Para i=0 hasta logitud-1 Hacer
	//	arregloLogitud[i] = Longitud(arregloNombre[i])
	//FinPara
	
	para i= 0 hasta logitud-1 Hacer
		Escribir "el nombre ",arregloNombre[i], " tiene un tamaño de ",arregloLogitud[i]
	FinPara
	
	
	
	
FinAlgoritmo
