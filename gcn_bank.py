from time import sleep

opções = ['Sair','Extrato','Saque','Deposito']

saldo = 0
extrato = []

delay = 0.2 # ALTERE O DELAY DE IMPRESSÃO PARA MAIOR CONFORTO VISUAL, TEMPO EXPRESSO EM FRAÇÃO DE SEGUNDOS. ex.: 1= 1 segundo, 0.5= meio segundo.

## operações de saque
limite_saques_diario = 3
limite_valor_saque = 500

def transição(txt='', tempo=delay, qnt=1):
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

"""def valida(valor):
    global entrada
    try:
        valor = round(float(valor), 2)
        if valor > 0:
            entrada = valor
            return True
        else:
            transição(f"⛔ [Você digitou um valor inválido: {valor:.2f}] ⛔")
            transição("⚠️ [Digite um valor MAIOR QUE ZERO.] ⚠️")
    except:
        transição(f"⛔ [Você digitou um valor inválido: {valor}] ⛔")
        transição("⚠️ [Digite um valor válido.] ⚠️")
        return False"""

def recebe_e_verifica(txt, valida):
    ## recebe_e_verifica(txt, função_sem_argumentos) Não coloque o argumento pois o mesmo será preenchido pela função, quando verificar a condição.
    while True:
        entrada = input(f"{txt}")
        retorno =  valida(entrada)
        if retorno[0]:
            return True, retorno[1]
            

def valida_int(entrada): ## Verifica se a entrada é uma int Valida.
     try:
          entrada = int(entrada)
          return True, int(entrada)
     except:
          print(" ⛔ Digite um valor inteiro válido. ⛔ ")
          return False, 0

def valida_float(entrada): ## Verifica se a entrada é uma float valida.
    try:
        entrada = float(entrada)
        if entrada > 0:
            return True, float(entrada)
        else:
            transição(f"⛔ [Você digitou um valor inválido: {entrada:.2f}] ⛔")
            transição("⚠️ [Digite um valor MAIOR QUE ZERO.] ⚠️")
            raise Exception
    except:
        transição(f"⛔ [Você digitou um valor inválido: {entrada}] ⛔")
        transição("⚠️ [Digite um valor válido.] ⚠️")
        return False, 0

def valida_nome(entrada): ## vai validar qualquer entrada que seja Letras e Espaços, qualquer coisa fora disso é retorna False.
    try:
        for x in entrada[:]:
            if not (x.isalpha() or x.isspace()):
                raise Exception
        return True, entrada
    except:
        print(" ⛔ Digite um nome válido. ⛔")
        return False, 0



def define_saldo():
    global saldo
    saldo = 0
    for x in extrato:
        saldo += x

def valida_operação(valor):
    global saldo
    transição(" 📝 [Validando transação...] 📝")
    
    
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
    sleep(delay)
    print(txt.center(len(txt)+esp))
    sleep(delay)
    print(sep*(len(txt)+esp))
    sleep(delay)

def exibe_extrato():
    transição("Extrato selecionado...")
    cabeçalho(f'🧾 {opções[1]} 🧾', esp=16)
    if len(extrato) > 0:
        print("|op.| - |tipo| -- | valor |")
        for pos, val in enumerate(extrato):
            if val < 0:
                dep_ou_saq = "Saq."
            else:
                dep_ou_saq = "Dep."
            print(f'|{pos:^3}| - |{dep_ou_saq:^4}| -- R$ {val:<10.2f}')
            sleep(delay)
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

cliente = [{'nome':'s','data_nascimento':'a','cpf':'654654654654','endereço':'Endereço completo'},]

logradouro = str()
numero_residencia = str()
bairro = str()
cidade = str()
unidade_federativa = str()
endereço_completo = f"{logradouro}, {numero_residencia}, {bairro} - {cidade}-{unidade_federativa}"


def cadastra_usuario():
    novo_user = {}
    
    while True:
        entrada = input("Digite apenas o primeiro nome:").upper().strip()
        if entrada.isalpha():
            novo_user['nome'] = entrada
            break
    
    while True:
        entrada = input("Digite o sobrenome:").upper().strip()





transição(" 🔐 [Entrando na conta...] 🔐")
transição("🔓 Seja bem-vindo ao gcn_Bank! 🔓")

while True:
    cabeçalho("_.gcn_Bank!", esp=12)    
    cabeçalho(f"[Saldo]: R${saldo:.2f}")
    
    for pos, val in enumerate(opções):
        print(f'[{pos}] - {val}')
        sleep(delay)
    print('-'*30)

    retorno = recebe_e_verifica("Digite uma opção: ", valida_int)
    

    if retorno[1] == 0:
        print(opções[0])
        print("saindo...")
        sleep(delay)
        print("Obrigado por usar nossos serviços.")
        sleep(delay)
        print("Volte sempre!")
        sleep(delay)
        for x in range(3,0,-1):
            print(f'{x}...')
            sleep(delay)
        break

    if retorno[1] == 1:
        exibe_extrato()

    if retorno[1] == 2:
        transição("Opção de Saque Selecionado...")
        cabeçalho(('💸 '+opções[2]+' 💸'),esp=35)
        print(f"Saques rest.: [{limite_saques_diario}]      R$-max/saque: [{limite_valor_saque:.2f}]")
        print('-'*44)
        sleep(delay)
        ##entrada = input("Digite o valor a ser sacado: R$")
        retorno = recebe_e_verifica("Digite o valor a ser sacado: R$", valida_float)
        if retorno[0]:
            if valida_operação(retorno[1]):
                saque(retorno[1])
        
        
        ##if valida_operação(entrada):
           ## saque(entrada)

    if retorno[1] == 3:
        transição("Opção de Deposito Selecionado...")
        cabeçalho((f"💰 {opções[3]} 💰"),esp=30)
        retorno = recebe_e_verifica("Digite o valor a ser depositado: R$", valida_float)
        if retorno[0]:
            deposito(retorno[1])
            


