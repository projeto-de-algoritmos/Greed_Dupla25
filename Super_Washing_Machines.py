# Problema Super Washing Machines, do LeetCode
# link: https://leetcode.com/problems/super-washing-machines/

def findMinMoves(machines):

    soma = 0
    tam = len(machines)

    for i in range(tam):
        soma += machines[i]

    # caso em que o print é -1, no sentido que é impossível dividir em pares o números total de roupas
    if soma % tam != 0:
        return -1

    limite = soma / tam
    trocas = 0
    saldo_geral = 0

    for i in range(tam):

        # falta esse valor para a máquina atual ficar no limite
        saldo_atual = machines[i] - limite

        # saldo geral nas máquinas que já conferimos
        saldo_geral += saldo_atual

        # se o saldo da atual é maior que o saldo geral, então o saldo que importa é o atual
        # considerando o valor absoluto porque o saldo geral pode estar negativo ou positivo
        # porem isso não importa no efeito de comparação, já que as trocas podem ser de saída ou entrada de roupas

        # nessa condição, meu saldo atual passa a ser o mais importante, que influencia de forma direta no meu número de trocas
        if saldo_atual > abs(saldo_geral):
            if saldo_atual > trocas:
                trocas = saldo_atual
        else:
            if abs(saldo_geral) > trocas:
                trocas = abs(saldo_geral)

    return int(trocas)


machines = [1, 0, 5]
print(findMinMoves(machines))
machines = [0, 3, 0]
print(findMinMoves(machines))
machines = [0, 2, 0]
print(findMinMoves(machines))
machines = [4, 0, 0, 4]
print(findMinMoves(machines))
machines = [0, 0, 11, 5]
print(findMinMoves(machines))
