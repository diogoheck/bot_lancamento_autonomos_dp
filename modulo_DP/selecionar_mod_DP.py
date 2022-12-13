import pyautogui
from time import sleep


def acessar_modulo_folha():

    # clicar no unico contabil para abrir opcoes
    pyautogui.click(1174, 58, duration=1)
    sleep(2)
    # mover ate opcao unico folha
    pyautogui.move(0, 38, duration=1)
    sleep(2)
    # clicar unico folha para mudar o modulo
    pyautogui.click()
    sleep(10)


if __name__ == '__main__':
    acessar_modulo_folha()
