from random import randint


def valida():
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]  # Elimina os dois últimos digitos do CPF
    reverso = 10  # Contador reverso
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:  # Primeiro índice vai de 0 a 9,
            index -= 9  # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        reverso -= 1  # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:  # Se o digito for > que 9 o valor é 0
                d = 0
            total = 0  # Zera o total
            novo_cpf += str(d)  # Concatena o digito gerado no novo cpf

    # Evita sequencias. Ex.: 11111111111, 00000000000...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # Descobri que sequências avaliavam como verdadeiro, então também
    # adicionei essa checagem aqui
    if cpf == novo_cpf and not sequencia:
        return True
    else:
        return False


def gera():
    numero = str(randint(100000000, 999999999))
    novocpf = numero
    soma1 = 0
    soma2 = 0
    primeiro_final = ''
    segundo_final = ''
    for digitos, mult in enumerate(range(10, 1, -1)):
        soma1 = soma1 + int((novocpf[digitos])) * mult
        contador = 11 - (soma1 % 11)
        if contador > 9:
            primeiro_final = '0'
        else:
            primeiro_final = str(contador)

    novocpf += primeiro_final

    for digitos, mult in enumerate(range(11, 1, -1)):
        soma2 = soma2 + int(novocpf[digitos]) * mult
        contador = 11 - (soma2 % 11)
        if contador > 9:
            segundo_final = '0'
        else:
            segundo_final = str(contador)

    novocpf += segundo_final

    cpffinal = ''
    for n, digicpf in enumerate(novocpf):
        digicpf = str(digicpf)
        cpffinal += digicpf
        if n == 2 or n == 5:
            cpffinal += '.'
        elif n == 8:
            cpffinal += '-'

    return cpffinal


opcao = input('Digite 1 para validar um CPF ou 2 para gerar um CPF valido: ')

if opcao == '1':
    if valida():
        print('Valido')
    else:
        print('Invalido')

elif opcao == '2':
    cpffilnal = gera()
    print(f'O CPF valido gerado é: {cpffilnal}')

else:
    print('Digite somente as opções 1 ou 2')
