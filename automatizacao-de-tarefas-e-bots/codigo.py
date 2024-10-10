# pip install pyautogui (ferramenta para automatizar)
from re import S
import pyautogui
import time

# pyautogui.write --> Escrever alguma coisa
# pyautogui.press --> Apertar alguma tecla
# pyautogui.click --> Clicar com o mouse
# pyautogui.hotkey -> apertar um atalho de teclado


# Passo 1 : Entrar no menu do pc
pyautogui.PAUSE = 2

pyautogui.press("win")

# Passo 2 :  Abrir o navegador e entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(" https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#Quero dar uma pausa de 2 segundos
time.sleep(3)
pyautogui.click(x=340, y=476)
pyautogui.write("cadastrodeclientes@gmail.com")
pyautogui.press("tab")
pyautogui.write("@3287f5dA")

# Passo 3 : Fazer o login
pyautogui.click(x=671, y=671)
time.sleep(2)


# Passo 4: Importar a base de dados
# pip install pandas
import pandas
tabela = pandas.read_csv("C:/Users/lelia/Documents/python-treino/automatizacao-de-tarefas-e-bots/produtos.csv")
print(tabela)


linha = 0
# para cada linha da minha tabela
for linha in tabela.index:
    # Selecionar o 1° campo
    pyautogui.click(x=309, y=331)
    time.sleep(1)

    #Código do Produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #Marca do Produto
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #Tipo do Produto
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #Categoria do Produto
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #Preço Unitário do Produto
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #Custo do Produto
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #OBS
    obs = tabela.loc[linha, "obs"]
    # se a obs não estiver vazia, preencha, se estiver, pule
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    #Enviar
    pyautogui.press("enter")
    pyautogui.scroll(2000)

    # Passo 6 : Repetir até acabar


