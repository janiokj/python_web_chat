#flet - É um framework para Python que permite construir aplicativos, Sites, softwares e afins

#Principais caras para criar sites no Python: Flask, Django, Fast Api, Tornado e Flet


import flet as ft

#Função Principal (main) do Código
def main(pagina): #def cria uma função, no caso de site ou App obrigatoriamente a Função principal tem que receber sua página como paramentro

    #A regra é : Cria o componente e depois coloca na página
    titulo = ft.Text("Chat Linshalm") #Cria o componente 
    pagina.add(titulo) #Coloca na página

    titulo_janela = ft.Text("Seja Bem Vindo ao Chat Linshalm")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no Chat")

    texto_mensagem = ft.TextField(label="Digite a sua mensagem:")

    #socket = tunel de comunicação - sempre que quiser que algo aconteça para mais do que um usuário simultaneamente
    def enviar_mensagem_tunel(mensagem):
        print(mensagem)

    pagina.pubsub.subscribe(enviar_mensagem_tunel) #Comando para CRIAR o socket/Tunel de comunicação
    

    #Funcao para Enviar a Mensagem
    def enviar_mensagem(evento):
        #enviar a mensagem do usuário
        texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"
        chat.controls.append(ft.Text(texto))

        #Enviar uma mensagem no Tunel
        pagina.pubsub.send_all("É Nóis...")   

        #limpar o campo de mensagem
        texto_mensagem.value = ""
        pagina.update()


    botao_enviar = ft.ElevatedButton("Enviar",on_click=enviar_mensagem)

    #Criar CHAT
    chat = ft.Column()

    #Colunas e Linahs
    linha_mensagem = ft.Row([texto_mensagem,botao_enviar])

    #Funcao para o Botao entrar no chat
    def entrar_chat(evento):
        #tirar o titulo
        pagina.remove(titulo)
        #tirar o botao iniciar
        pagina.remove(botao_iniciar)
        #fechar o popup
        janela.open = False
        #criar o chat
        pagina.add(chat)
        #criar o campo de texto que envia mensagem e criar o botao para enviar mensagem        
        pagina.add(linha_mensagem)

        #Escrever: Usuario entrou no site
        texto_entrou_chat = f"{campo_nome_usuario.value} entrou no Chat"
        chat.controls.append(ft.Text(texto_entrou_chat)) #Append: Adicionar um item a lista

        pagina.update()

    
    botao_entrar = ft.ElevatedButton("Entrar no Chat",on_click=entrar_chat)

    #Criar o Popup/Modal/Alert
    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome_usuario,
        actions=[botao_entrar]
        
    ) 

    #Funcão Abrir Popup/Modal
    def abrir_popup(evento): #Toda função para botão DEVE receber um evento como parâmetro
        pagina.dialog = janela
        janela.open = True
        pagina.update() #Sempre que fizer uma alteração visual na página tem que rodar um atualizar

    botao_iniciar = ft.ElevatedButton("Iniciar Chat",on_click=abrir_popup)
    pagina.add(botao_iniciar)



#Executar o Sistema
#ft.app(main, view=ft.WEB_BROWSER) #Esse cara defini também se a saída(view) vai ser Um navegador(WEB_BROWSER), um app ou um programa
ft.app(main)