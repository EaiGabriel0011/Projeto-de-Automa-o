# Para começar a automação primeiro e preciso escrever o comando a baixo.
import pyautogui
import time

# pyautogui.click -> clicar em alugum lugar.
# pyautogui.press -> apertar uma tecla.
# pyautogui.write -> escrever um texto.
# pyautogui.hotkey -> apertar uma combinação de teclas.

# O comando a baixo é para colocar um tempo de resposta para cada comando, o número representa os segundos a cada comando.
# Esse é o tempo para cada comando.
pyautogui.PAUSE = 2


# Anotar passo a passo do que fazer!

# Passo 1: Entrar no sistema da empresa:https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Abrir o navegador.
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Digitar o site.
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Esperar 3 segundos.
# O comando a baixo é para esperar um certo tempo. 
# O código é para um momento especifico.
time.sleep(3)

# Passo 2: Fazer login.
# Preencher email.
pyautogui.click(x=530, y=372)
# escrever o seu email
pyautogui.write("gabsilva2408@gmail.com")
pyautogui.press("tab") # passando pro próximo campo

# Preencher senha.
# Tecla (tab) sempre irá pular para o proximo campo.    
pyautogui.write("avai2408")

# Botão logar.
pyautogui.press("tab")
pyautogui.press("enter")

# Espera de 3 segundos.
time.sleep(2.5)

# Passo 3: Importar a base de dados.
# Primeiro instalar e verificar se o pandas está instalado. Para instalar ir ao terminal e execurtar o codigo (pip install pandas)
# Para importar base de dados executar código a baixo.

import pandas

tabela = pandas.read_csv(r"C:\Users\User\Downloads\produtos.csv")   

print(tabela)

# Passo 4: Cadastras o produto.


for linha in tabela.index:


    pyautogui.press("tab")

    codigo = tabela.loc [linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab") # passar para o próximo campo.
    marca = tabela.loc [linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc [linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str (tabela.loc [linha, "categoria"]) # String = texto -> str()
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc [linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc [linha, "custo"])
    pyautogui.write(custo)   
    pyautogui.press("tab")
    obs = str(tabela.loc [linha, "obs"])

    if obs != "nan":          # (!=) = Diferente.
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)

# Passo 5: Repetir para todos os produtos.





# pyautogui -> Fazer automações com python. Permite usar mouse, tela e teclado.
# Para instalar a biblioteca (pyautogui)...Entrar no terminal e escrever (pip install pyautogui) e apertar enter.