
while True:
    cpf = input('Digite o CPF: ')  #  [1, 3, 5, 5, 5, 7, 4, 9, 7, 7, 0]
    novocpf = cpf[0:9]
    soma1 = 0
    soma2 = 0
    primeiro_final = ''
    segundo_final = ''
    for digitos, mult in enumerate(range(10, 1, -1)):
        soma1 = soma1 + int(cpf[digitos]) * mult
        contador = 11 - (soma1 % 11)
        if contador > 9:
            primeiro_final = '0'
        else:
            primeiro_final = str(contador)

    novocpf += primeiro_final

    for digitos, mult in enumerate(range(11, 1, -1)):
        soma2 = soma2 + int(cpf[digitos]) * mult
        contador = 11 - (soma2 % 11)
        if contador > 9:
            segundo_final = '0'
        else:
            segundo_final = str(contador)

    novocpf += segundo_final
    if novocpf == cpf:
        print('CPF valido')
    else:
        print('CPF invalido')

    cpffinal = ''
    for n, digicpf in enumerate(novocpf):
        digicpf = str(digicpf)
        cpffinal += digicpf
        if n == 2 or n == 5:
            cpffinal += '.'
        elif n == 8:
            cpffinal += '-'

    print(f'Os digitos finais gerados do CPF são: {primeiro_final} e {segundo_final} e o CPF final é: {cpffinal}')
