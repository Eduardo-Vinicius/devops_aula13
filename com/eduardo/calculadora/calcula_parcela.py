'''
Calcula a parcela e tem a função do valor do pagamento com juros ou não.
'''


def valor_pagamento(valor, dias_atraso):
    '''
    Função que verifica os valores, e vê se a multa é aplicavel ou não,
    conforme cada caso
    '''
    if valor < 0:
        return None
    if dias_atraso > 0:
        multa = valor * 0.03
        adicional_atraso = valor * (dias_atraso * 0.01)
        return valor + multa + adicional_atraso
    return valor
