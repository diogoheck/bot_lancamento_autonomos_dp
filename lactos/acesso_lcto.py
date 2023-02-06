import pyautogui
from time import sleep


def acesso_aba_lancamento_autonomos():
    sleep(5)
    # acessar a guia lancamentos
    pyautogui.hotkey('alt', 'l')
    sleep(5)
    # guia -> lancamento para apuracao de impostos
    pyautogui.hotkey('n')
    sleep(2)
    # guia -> servicos(RPA)
    pyautogui.hotkey('s')
    sleep(5)


if __name__ == '__main__':
    acesso_aba_lancamento_autonomos()
