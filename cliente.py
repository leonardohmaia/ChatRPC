import os
import xmlrpc.client

server = xmlrpc.client.ServerProxy('http://localhost:8000/')
na_sala = False
username = input("Digite seu nome de usuário, para ingressar na sala: ")
user_id = server.Ingressar_no_sistema(username)
print("Usuário ID:", user_id)

while True:
    print("\n\nOpções:")
    if not na_sala:
        print("1. Entrar na sala")
    if na_sala:
        print("2. Enviar mensagem")
        print("3. Listar mensagens")
        print("4. Enviar mensagem para usuário específico")
        print("5. Listar usuários")
        print("6. Sair da sala")
    print("7. Sair do programa")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        print(server.Entrar_na_sala(user_id))
        na_sala = True
    elif opcao == '2':
        mensagem = input("Digite a mensagem: ")
        print(server.Enviar_mensagem(user_id, mensagem))
    elif opcao == '3':
        mensagens = server.Listar_mensagens(user_id)
        for mensagem in mensagens:
            print(mensagem)
    elif opcao == '4':
        recipient_username = input("Digite o nome de usuário do destinatário: ")
        mensagem = input("Digite a mensagem: ")

        resultado = server.Enviar_mensagem_usuário(user_id, recipient_username, mensagem)
        print(resultado)
    elif opcao == '5':
        usuarios = server.Listar_usuarios()
        for name in usuarios:
            print(f"{name}")
    elif opcao == '6':
        na_sala = False
        print(server.Sair_da_sala(user_id))
    elif opcao == '7':
        break
    else:
        print("Opção inválida. Tente novamente.")
