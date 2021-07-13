
numero1 = int(input('Insira o primeiro número: '));
numero2 = int(input('Insira o segundo número: '));

operacao = int(input('Selecione a operação:\nDigite:\n 1-Soma\n 2-Subtração\n 3-Divisão\n 4-Multiplicação\n '));

resultado = 0;


if operacao==1:

	resultado = numero1+numero2;

	print('O resultado é: ' + str(resultado));

elif operacao==2:
	
	resultado = numero1-numero2;

	print('O resultado é: ' + str(resultado));

elif operacao==3:

	resultado = numero1/numero2;

	print('O resultado é: ' + str(resultado));

elif operacao==4:

	resultado = numero1*numero2;

	print('O resultado é: ' + str(resultado));

else: print('Reinicie e digite um número válido');