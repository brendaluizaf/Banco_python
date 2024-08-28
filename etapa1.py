menu="""

[d] depositar
[s] sacar
[e] extrato
[q] sair

=>"""

saldo=0
limite= 500
extrato= ""
numero_saque= 0
LIMITE_SAQUE = 3

while True:
   
   opcao = input(menu)
   
   if opcao == "d":
       valor = float(input("informe o valor do depósito: "))
       
       if valor > 0:
           saldo += valor
           extrato += f"Depósito: R$ {valor:.2f}"
           
       else:
           print("A operação falhou! O valor informado é inválido.")     

   elif opcao == "s":
        valor = float(input("informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saque = numero_saque >= LIMITE_SAQUE
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo.")
            
        elif excedeu_limite:
            print("Operação falhou! Limite insuficiente.")
        
        elif excedeu_saque:
            print("Operação falhou! Número")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}"
            numero_saque += 1
            
        else:
            print("A operação falhou! O valor informado é inválido.")
            
   elif opcao == "e":
        print("\n=============== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n saldo: R$ {saldo:.2f}")
        print("========================================")
        
   elif opcao == "q":
       break
   
   else:
       ("Opção inválida, por favor selecione novamente a opção desejada.")