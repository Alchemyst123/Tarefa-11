#joao pedro garcia pereira
#Entrada de dados para iniciar o programa
n=0
n=float(input("digite um numero: "))
#Repeticao do programa enquanto n ser maior que zero
while n>0:
	#Declaracao de variaveis
	raiz=0.0
	cont=0
	#Processamento
	raiz=n/2
	#Repeticao do metodo de aproximacao por vinte vezes
	while cont<=20:
		cont=cont+1
		raiz=((raiz**2)+n)/(2*raiz)
	#Saida de dados
	print("n= %.0f raiz= %.7f" %(n,raiz))
	#Entrada de dados para parar ou continuar o programa
	n=float(input("digite um numero: "))
