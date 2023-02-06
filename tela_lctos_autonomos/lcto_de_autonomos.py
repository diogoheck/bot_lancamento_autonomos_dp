from enum import auto
import pyautogui
from time import sleep
from planilha_cliente.ler_dados_admissao_prelim import ler_pasta


def preencher_tela_autonomos(autonomo, primeiro_cadastro):

    if primeiro_cadastro:
        pyautogui.write(autonomo[0])  # empresa
        sleep(1)
        pyautogui.press('enter')
        sleep(1)
        pyautogui.write(autonomo[1])  # autonomo
        sleep(1)
        pyautogui.press('enter')
        sleep(1)
    else:
        pyautogui.doubleClick(213, 191)
        sleep(3)
        pyautogui.write(autonomo[1])  # autonomo
        sleep(1)
        pyautogui.press('enter')
        sleep(1)
    pyautogui.write(autonomo[2])  # ordem
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.write(autonomo[3])  # documento
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.write(autonomo[4])  # data servico
    sleep(1)
    pyautogui.write(autonomo[5])  # hora
    sleep(1)
    pyautogui.write(autonomo[6])  # data pagto
    sleep(1)
    pyautogui.write(autonomo[7])  # valor
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.write(autonomo[8])  # centro
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.write(autonomo[9])  # cidade
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('pagedown')
    sleep(10)

    # Nome
if __name__ == '__main__':
    dados_funcionario = ler_pasta()
