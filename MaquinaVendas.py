#DEF PAGAMENTO / TROCO

#função que percorre o vetor dos trocos, e vai fazendo divisões inteiras até não sobrar nada
def calcularTroco(troco):
    for i in range(len(possiveisTrocos)):
        trocoRecebido = int(troco//possiveisTrocos[i])
        if (trocoRecebido) >= 1:
            if possiveisTrocos[i] > 0:
                print((trocoRecebido), "nota(s) ou moeda(s) de", possiveisTrocos[i])
        troco -= ((trocoRecebido) * possiveisTrocos[i])

#MATRIZ E VETOR DA MAQUINA

#matriz que mostra a tabela de produtos para o usuario
matrizEstoque = [['   ''PRODUTO     ''PREÇO ''ESTOQUE'],
           [1, 'Coca-Cola', 3.75, 2],
           [2, 'Pepsi    ', 3.67, 5],
           [3, 'Monster  ', 9.96, 1],
           [4, 'Café     ', 1.25, 100],
           [5, 'Redbull  ', 13.99, 2]]

#vetor que contem todas as notas e moedas que o usuario pode receber depois de efetuar o pagamento
possiveisTrocos = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]

#INICIO PROGRAMA
while True:

#TELA DAS OPÇÕES DO USUARIO

#percorre a matriz para simular uma tela de compras
    for contador in range(6):
        print(str(matrizEstoque[contador]))

#ESCOLHA DO USUARIO

#usuario escolhe o produto e é informado caso não exista mais tal produto ou se ele digitou errado
    opcao = int(input("Selecione o Produto desejado: "))
    while opcao < 1 or opcao > 5:
        print("Codigo Invalido")
        opcao= int(input("Selecione o Produto desejado: "))
    if matrizEstoque[opcao][3] < 1:
        print("Produto fora de estoque")
        opcao = int(input("Selecione outro produto: "))

#PAGAMENTO DO USUARIO

#percorre a matriz e informa o preço do produto ao usuario
    precoProduto = matrizEstoque[opcao][2]
    print("Preço a pagar: ", precoProduto)

#recebe o pagamento do usuario e informa caso a quantidade não for suficiente
    precoPago = 0
    dinheiroPago = float(input("Insira um valor valido para pagar: "))
    precoPago += dinheiroPago
    while precoPago < precoProduto:
        print("Ainda falta dinheiro para terminar de pagar o produto, insira um novo monte: ")
        dinheiroPago = float(input())
        precoPago += dinheiroPago

#Ativa a função do troco e o entrega
    trocoFinal = precoPago - precoProduto
    print("Valor recebido, seu troco é de: ")
    calcularTroco(trocoFinal)

#DECREMENTAÇAO DO ESTOQUE :

#percorre a matriz até encontrar a opção escolhida e retira uma unidade do estoque
    matrizEstoque[opcao][3] -= 1

#reinicia o programa depois de 3 segundos
    from time import sleep
    sleep(3)
