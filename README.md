# ChatRPC
Um cliente teve a brilhante ideia de projetar um sistema de troca de mensagens (também conhecido como Chat) utilizando RPC. O cliente considera que existe uma sala de bate-papo com vários usuários trocando mensagens. Ele definiu que o sistema seria modularizado nos seguintes métodos:
Ingressar_no_sistema: esse método permite que um usuário (através de seu nome) solicite o credenciamento ao sistema. O método define uma identificação para o usuário;
Entrar_na_sala: esse método permite identificar que um usuário (através de sua identificação) ingresse na sala de bate-papo;
Sair_da_sala: esse método permite identificar que um usuário (através de sua identificação) saia da sala de bate-papo;
Enviar_mensagem: esse método permite que o usuário envie uma mensagem através de sua identificação;
Listar_mensagens: esse método permite que o usuário liste todas as mensagens publicadas no serviço;
Enviar_mensagem_usuário: esse método permite que o usuário envie uma mensagem para outro usuário específico. Apenas os dois usuários recebem e visualização a mensagem;
Listar_usuários: esse método permite que o usuário receba uma lista de usuários que estão ativos na sala;
