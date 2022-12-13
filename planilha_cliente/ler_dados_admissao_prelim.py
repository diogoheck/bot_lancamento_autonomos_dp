import datetime
from enum import auto
from openpyxl import load_workbook
import os
CAMINHO = 'planilha_cliente'


def configurar_data(data_servico):

    data_servico = str(data_servico)[0:10].split('-')
    data_servico = data_servico[2] + data_servico[1] + data_servico[0]
    return data_servico


def ler_excel(nome_arquivo):
    dados_cliente_excel = load_workbook(nome_arquivo)
    plan_clientes_excel = dados_cliente_excel.active
    cabecalho = True
    lista = []

    for linha in plan_clientes_excel.values:
        if not cabecalho:
            empresa = str(linha[0])
            autonomo = str(linha[1])
            ordem = str(linha[2])
            documento = str(linha[3])
            data_servico = str(linha[4])
            # print(data_servico)
            hora = str(linha[5])
            data_pagto = str(linha[6])
            # data_pagto = datetime.strftime(linha[6], '$%d$m$y')
            valor = str(linha[7])
            centro = str(linha[8])
            cidade = str(linha[9])
            lista.append([empresa, autonomo, ordem, documento,
                         data_servico, hora, data_pagto, valor, centro, cidade])
        cabecalho = False

    # print(lista)
    return lista


def ler_pasta():
    dicionario_admissoes = []
    for diretorio, subpastas, arquivos in os.walk(CAMINHO):

        for arquivo in arquivos:

            formato = os.path.join(diretorio, arquivo).split('.')[-1]
            if formato == 'xlsx' or formato == 'xls':
                # nome_arquivo = os.path.join(diretorio, arquivo).split('\\')[-1]

                nome_arquivo = os.path.join(diretorio, arquivo)
                # print(nome_arquivo)
                dicionario_admissoes = ler_excel(
                    nome_arquivo)
    return dicionario_admissoes


if __name__ == '__main__':
    dados_lancamento_autonomo = ler_pasta()
