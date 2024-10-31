
nome = input('digite seu nome:')
senha = int(input('digite uma senha:'))
print('usuario cadastrado')
print('-digite os seus dados para acessar sua conta-')
meu_nome = input('digite o nome do usuario:')
minha_senha = int(input('digite sua senha:'))

for n in range(2,-1, -1):
    if minha_senha == senha and nome:
        print('bem-vindo', nome)
        
        print('saldo disponivel: R$4000')

        acesso = int(input('''
        escolha o que deseja
        
        1 - ver extrato
        2 - fazer deposito
        3 - fazer saque
        4 - sair do sistema
        
        '''))
        
        if acesso == 1:
            print('''
            mostra extrato:
            transação do dia 12/10
            deposito do dia 02/10
            ''')
        elif acesso == 2:
            fazer_deposito = input('digite o valor do deposito:')
            print('deposito efetuado de R$', fazer_deposito)
        elif acesso == 3:
            fazer_saque = int(input('digite o valor que deseja sacar:'))
            if fazer_saque > 4000:
                print('saldo insuficiente')
            else:
                print('saque realizado com sucesso')
        elif acesso == 4:
            pass
            print("saiu do sistema")
            
    
        
        else:
                print('digite algo valido') 
           
                   
else:
    print('algo deu errado, tente novamente')       
    



                
             


      

    
  



