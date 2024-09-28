# title: 'app'
# author: 'Elias Albuquerque'
# version: '0.1'
# created: '2024-09-27'
# update: '2024-09-28'


from src.pessoa import Pessoa
import json
import pandas as pd


def obter_quantidade():
    """Solicita e valida a entrada para a quantidade de pessoas a serem geradas."""

    while True:
        try:
            quantidade = int(input("Digite a quantidade de pessoas a serem geradas: "))
            if quantidade <= 0:
                print("Erro: A quantidade deve ser um número positivo.\n")
            else:
                return quantidade
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.\n")


def obter_formato():
    """Solicita e valida o formato de saída (json , xlsx, txt)."""

    formatos_validos = ["json", "xlsx", "txt", "j", "x", "t"]

    while True:
        formato = input("Digite o formato de saída ([j] json, [x] xlsx, [t] txt): ").lower()
        if formato not in formatos_validos:
            print(f"Erro: Formato inválido! Os formatos aceitos são: json, xls, txt.\n")
        else:
            return formato

def gerar_pessoas(quantidade):
    """Gera uma lista de dicionários com dados de pessoas."""

    pessoas = []

    for _ in range(quantidade):
        pessoa = Pessoa().gerar_dados_pessoa()
        pessoas.append(pessoa)

    return pessoas


def salvar_dados(pessoas, formato):
    """Salva os dados gerados no formato escolhido."""

    if formato == "json" or formato == "j":
        with open("pessoas.json", "w", encoding='utf-8') as f:
            json.dump(pessoas, f, indent=4, ensure_ascii=False)
        print("Dados salvos em pessoas.json")

    elif formato == "xlsx" or formato == "x":
        # Criar DataFrame e salvar em Excel
        df = pd.DataFrame(pessoas)
        with pd.ExcelWriter("pessoas.xlsx", engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Dados', index=False)

            # Pegar o objeto worksheet para ajustar colunas
            worksheet = writer.sheets['Dados']
            
            # Ajustar a largura das colunas com base nos conteúdos
            for idx, col in enumerate(df.columns):
                max_len = max(df[col].astype(str).map(len).max(), len(col))
                worksheet.set_column(idx, idx, max_len)

        print("Dados salvos em pessoas.xlsx")

    elif formato == "txt" or formato == "t":
        with open("pessoas.txt", "w", encoding='utf-8') as f:
            for pessoa in pessoas:
                f.write(f"Nome: {pessoa['nome']}\n")
                f.write(f"CPF: {pessoa['cpf']}\n")
                f.write(f"Email: {pessoa['email']}\n")
                f.write(f"Endereço: {pessoa['endereco']}\n")
                f.write(f"Contato: {pessoa['contato']}\n")
        print("Dados salvos em pessoas.txt")

    else:
        print("Formato inválido!\n")


if __name__ == "__main__":
    try:
        # Input usuário
        quantidade = obter_quantidade()
        formato = obter_formato()

        # Gera e salva os dados conforme entradas validadas
        pessoas = gerar_pessoas(quantidade)
        salvar_dados(pessoas, formato)

    except KeyboardInterrupt:
        print("\nExecução interrompida pelo usuário. Finalizando o programa...\n")