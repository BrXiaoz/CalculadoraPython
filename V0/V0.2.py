retorno = 0;
while retorno==0:
	
	numero1 = int(input('Insira o primeiro número: '));
	numero2 = int(input('Insira o segundo número: '));

	operacao = int(input('Selecione a operação:\nDigite:\n 1-Soma\n 2-Subtração\n 3-Divisão\n 4-Multiplicação\n '));




	while (operacao>4) or (operacao<1):
		
		operacao = int(input('Selecione uma operação válida:\nDigite:\n 1-Soma\n 2-Subtração\n 3-Divisão\n 4-Multiplicação\n '));


	resultado = 0;


	if operacao==1:

		resultado = numero1+numero2;

		print('O resultado é: ' + str(resultado)+'\n');

	elif operacao==2:
		
		resultado = numero1-numero2;

		print('O resultado é: ' + str(resultado)+'\n');

	elif operacao==3:

		resultado = numero1/numero2;

		pprint('O resultado é: ' + str(resultado)+'\n');

	elif operacao==4:

		resultado = numero1*numero2;

		print('O resultado é: ' + str(resultado)+'\n');

	retorno = int(input('Insira 0 para continuar e 1 para finalizar:\n\n- '));
	while retorno!=1 and retorno!=0:
		retorno = int(input('Número Inválido\nInsira 0 para continuar e 1 para finalizar:\n\n- '));
