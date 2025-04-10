mode = int(input('Escolha um modo de operação:\n1)Adição\n2)Subtração\n3)Multiplicação\n4)Divisão\nSua escolha:'))
val1 = int(input('Digite o primeiro valor:'))
val2 = int(input('Digite o segundo valo:'))
if mode == 1:
    print('A soma dos valores é {}'.format(val1+val2))
elif mode == 2:
    print('A subtração dos valores é {}'.format(val1-val2))
elif mode == 3:
    print('A multiplicação dos valores é {}'.format(val1*val2))
elif mode == 4:
    print('A divisão dos valores é {}'.format(int(val1/val2)))
else:
    print('Tente Novamente')