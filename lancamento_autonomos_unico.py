from Login.login_unico import logar_unico
from modulo_DP.selecionar_mod_DP import acessar_modulo_folha
from lactos.acesso_lcto import acesso_aba_lancamento_autonomos as acesso_lctos_autonomos
from planilha_cliente.ler_dados_admissao_prelim import ler_pasta as ler_dados_excel
from tela_lctos_autonomos.lcto_de_autonomos import preencher_tela_autonomos
import pyautogui
import os


if __name__ == '__main__':
    dados_autonomos = ler_dados_excel()
    logar_unico()
    acessar_modulo_folha()
    primeiro_cadastro = True

    acesso_lctos_autonomos()
    for autonomo in dados_autonomos:
        preencher_tela_autonomos(autonomo, primeiro_cadastro)

        print(autonomo)
        primeiro_cadastro = False

    pyautogui.alert(text='Fim da Automação',
                    title='Automacao de Lctos de Autônomos', button='ok')

