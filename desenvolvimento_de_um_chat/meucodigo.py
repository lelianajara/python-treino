# Título: Pythonchat
# Botão: Iniciar Chat
    # quando clicar no botão:
    # abrir um popup/modal/alerta
        # Título: Bem vindo ao Hashzap
        # Caixa de Texto: Escreva seu nome no chat
        # Botão: Entrar no chat
            # quando clicar no botão
            # sumir com o título
            # sumir com o botão iniciar
                # carregar o chat
                # carregar o campo de enviar mensagem: "Digite sua mensagem"
                #botão Enviar
                    # quando clicar no botão enviar
                    # enviar a mensagem
                    # limpar a caixa de mensagem

#Flet
# importar o flet

import flet as ft

# criar uma função principal para rodar o seu aplicativo

def main(pagina):

    #título
    titulo = ft.Text("chatlu")

    def enviar_mensagem(evento):
        texto = ft.Text(campo_enviar_mensagem.value)
        chat.controls.append(texto)
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem,botao_enviar])

    chat = ft.Column()
    
    def entrar_chat(evento):
        #fechar o popup
        popup.open = False
        #sumir com o titulo
        pagina.remove(titulo)
        #sumir com o botao iniciar chat
        pagina.remove(botao)
        #carregar o chat
        pagina.add(chat)
        #carregar campo de envio de msg
        pagina.add(campo_enviar_mensagem)
        #carregar botao enviar
        pagina.add(botao_enviar)
        
        pagina.update()
    
    #criar popup
    titulo_popup = ft.Text("Bem vind@ ao chatlu")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)

    popup = ft.AlertDialog(title=titulo_popup,content=caixa_nome,actions=[botao_popup])


    # botao inicial
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        
    botao = ft.ElevatedButton("Iniciar chat", on_click=abrir_popup)

    # colocar os elementos na página
    pagina.add(titulo)
    pagina.add(botao)


# executar essa função com o flet
ft.app(main, view=ft.AppView.WEB_BROWSER)

