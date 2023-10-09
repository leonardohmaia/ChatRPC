from xmlrpc.server import SimpleXMLRPCServer

# Cria um servidor XML-RPC
server = SimpleXMLRPCServer(('localhost', 8000))

# Dicionário para armazenar mensagens e usuários
messages = []
user = {}
active_users = {}
user_messages = [[],[],[],[],[],[],[],[],[]]
# Métodos do servidor

def Ingressar_no_sistema(username):
    for user_id, existing_username in user.items():
        if existing_username == username:
            return user_id 

    user_id = len(active_users) + 1
    user[user_id] = username
    return user_id

def Entrar_na_sala(user_id):
    if user_id in user:
        active_users[user_id]=user[user_id]
        return f"{active_users[user_id]} entrou na sala."

def Sair_da_sala(user_id):
    if user_id in active_users:
        username = active_users.pop(user_id)
        return f"{username} saiu da sala."

def Enviar_mensagem(user_id, message):
    if user_id in user:
        username = user[user_id]
        messages.append(f"{username}: {message}")
        return "Mensagem enviada com sucesso."

def Listar_mensagens(user_id):
    messages_user=[]
    messages_user.extend(messages)
    messages_user.extend(user_messages[user_id])
    return messages_user

def Enviar_mensagem_usuário(sender_id, recipient_name, message):
    recipient_id = ""
    for user_id in user:
        if user[user_id] == recipient_name:
            recipient_id = user_id
    if not recipient_id=="":
        sender_name = user[sender_id]
        private_message = f"{sender_name} para {recipient_name}: {message}"
        user_messages[sender_id].append(private_message)
        user_messages[recipient_id].append(private_message)

        return "Mensagem enviada com sucesso."
    else:
        return "Usuário não encontrado."


def Listar_usuarios():
    return list(active_users.values())

server.register_function(Ingressar_no_sistema, 'Ingressar_no_sistema')
server.register_function(Entrar_na_sala, 'Entrar_na_sala')
server.register_function(Sair_da_sala, 'Sair_da_sala')
server.register_function(Enviar_mensagem, 'Enviar_mensagem')
server.register_function(Listar_mensagens, 'Listar_mensagens')
server.register_function(Enviar_mensagem_usuário, 'Enviar_mensagem_usuário')
server.register_function(Listar_usuarios, 'Listar_usuarios')

print("Servidor RPC iniciado na porta 8000...")
server.serve_forever()
