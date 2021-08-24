def calcular(texto):
    if texto == '':
        return 0
    else:
        texto_formatado = texto.replace('\n', ',')
        texto_formatado = texto_formatado.replace(';', ',')
        texto_formatado = texto_formatado.replace(' ', ',')
        numeros = texto_formatado.split(',')
        total = 0
        negativos = []
        for numero in numeros:
            numero_inteiro = int(numero)
            if numero_inteiro < 0:
                negativos.append(numero)
            else:
                total += numero_inteiro
        if len(negativos) > 0:
            negativos_formatados = ", ".join(negativos)
            raise Exception(f"numeros negativos nao permitidos: {negativos_formatados}")
        return total
