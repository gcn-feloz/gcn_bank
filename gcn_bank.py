
from time import sleep

opções = ['Sair','Extrato','Saque','Deposito']

saldo = 0
extrato = []

## operações de saque
limite_saques_diario = 3
limite_valor_saque = 500

def transição(txt='', tempo=.9, qnt=1):
    for y in range(2):
        for x in range(qnt):
            print()
            sleep(tempo)
        if y == 0:
            print(txt)
    
def deposito(valor):
    valor = float(valor)
    transição(f'  💰  [+R${valor:.2f}]  💰  ')
    print(f"Foi depositado na sua conta: R${valor:.2f}")
    extrato.append(valor)
    define_saldo()

  


def saque(valor):
    valor = float(valor)
    global limite_saques_diario
    transição(f'  💸  [-R${valor:.2f}]  💸  ')
    print(f"Foi sacado da sua conta: R${valor:.2f}")
    extrato.append(valor*(-1))
    define_saldo()
    limite_saques_diario -= 1


def valida(valor):
    try:
        valor = float(valor)
        if valor > 0:
            return True
    except:
        return False

def define_saldo():
    global saldo
    saldo = 0
    for x in extrato:
        saldo += x

def valida_operação(valor):
    global saldo
    transição(" 📝 [Validando transação...] 📝")
    if valida(valor):
        valor = float(valor)
    else:
        transição(f"⛔ [Você digitou um valor inválido: {valor}] ⛔")
        transição("⚠️ [Digite um valor válido.] ⚠️")
        return False
    if limite_saques_diario == 0:
        transição("⛔ [Você excedeu o limite de [3] saques diarios.] ⛔")
        transição("⚠️ [Tente novamente amanhã.] ⚠️")
        return False
    elif valor > limite_valor_saque:
        transição(f"⛔ [O valor que está tentando sacar ultrapassa o limite de R${limite_valor_saque:.2f}] ⛔")
        transição(f"⚠️ [Tente novamente com um valor abaixo de R${limite_valor_saque:.2f}] ⚠️")
        return False
    elif valor > saldo:
        transição(f"⛔ [O Valor que está tentando sacar [R${valor:.2f}] é maior que seu saldo disponivel [R${saldo:.2f}].] ⛔")
        transição(f"⚠️ [Tente novamente com um valor igual ou abaixo do seu saldo atual.] ⚠️")
    else:
        transição("✅ [Transação Autorizada] ✅")
        return True

def cabeçalho(txt, sep = '-', esp = 5):
    print(sep*(len(txt)+esp))
    print(txt.center(len(txt)+esp))
    print(sep*(len(txt)+esp))

def limpa_tela(intervalo=0.5):
    print('\n'*25)
    sleep(intervalo)

transição(" 🔐 [Entrando na conta...] 🔐")
transição("🔓 Seja bem-vindo ao gcn_Bank! 🔓")

while True:
    cabeçalho("_.gcn_Bank!", esp=12)
    sleep(.5)
    cabeçalho(f"[Saldo]: R${saldo:.2f}")
    sleep(.5)
    for pos, val in enumerate(opções):
        print(f'[{pos}] - {val}')
        sleep(.5)
    print('-'*20)

    entrada = input("Digite uma opção: ")
    
    if entrada == '0':
        print(opções[0])
        print("saindo...")
        sleep(1)
        print("Obrigado por usar nossos serviços.")
        sleep(1)
        print("Volte sempre!")
        sleep(1)
        for x in range(3,0,-1):
            print(f'{x}...')
            sleep(1)
        break

    if entrada == '1':
        transição("Extrato selecionado...")
        cabeçalho(f'🧾 {opções[1]} 🧾', esp=16)
        if len(extrato) > 0:
            print("|op.| ------ | valor |")
            for pos, val in enumerate(extrato):
                print(f'[{pos:^3}] ------ R${val:<8.2f}')
                sleep(.5)
            cabeçalho(f"Saldo: R${saldo:.2f}", esp = 12)
        else:
            print("Não há movimentações".center(27))
            print("para exibir no extrato.".center(27))
            print('-'*27)
        print()
        print("Pressione [Enter] para sair do extrato:")
        while True:
            if input() == '':
                break
       ## transição()

    if entrada == '2':
        transição("Opção de Saque Selecionado...")
        cabeçalho(('💸 '+opções[2]+' 💸'),esp=35)
        print(f"Saques rest.: [{limite_saques_diario}]      R$-max/saque: [{limite_valor_saque}]")
        print('-'*44)
        sleep(.5)
        entrada = input("Digite o valor a ser sacado: R$")
        if valida_operação(entrada):
            saque(entrada)

    if entrada == '3':
        transição("Opção de Deposito Selecionado...")
        cabeçalho((f"💰 {opções[3]} 💰"),esp=30)
        entrada = input("Digite o valor a ser depositado: R$")
        if valida(entrada):
            deposito(entrada)
            


