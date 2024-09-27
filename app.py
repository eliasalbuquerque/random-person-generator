# title: 'app'
# author: 'Elias Albuquerque'
# version: '0.1'
# created: '2024-09-27'
# update: '2024-09-27'


from faker import Faker
import re
import json
import pandas as pd

class Pessoa:
    def __init__(self):
        self.fake = Faker('pt_BR')

    def gerar_dados_pessoa(self):
        """Gera dados fictícios de uma pessoa."""

        nome = self.fake.name()
        cpf = self.gerar_cpf_valido()
        email = self.fake.email()
        endereco = self.fake.address()
        telefone = self.fake.phone_number()
        
        return {
            'nome': nome,
            'cpf': cpf,
            'email': email,
            'endereco': endereco,
            'telefone': telefone
        }

    def gerar_cpf_valido(self):
        """Gera um CPF válido, mas falso, utilizando a biblioteca Faker e verificações de dígitos."""

        cpf_base = self.fake.numerify('#########')  # Gera uma string de 9 dígitos aleatórios

        # Calcula o primeiro dígito verificador
        soma = sum([int(digito) * (10 - i) for i, digito in enumerate(cpf_base)])
        resto = 11 - (soma % 11)
        digito1 = resto if resto <= 9 else 0

        # Calcula o segundo dígito verificador
        soma = sum([int(digito) * (11 - i) for i, digito in enumerate(cpf_base + str(digito1))])
        resto = 11 - (soma % 11)
        digito2 = resto if resto <= 9 else 0

        cpf_completo = cpf_base + str(digito1) + str(digito2)

        # Formata o CPF
        cpf_formatado = re.sub(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', cpf_completo)

        return cpf_formatado

def gerar_pessoas(quantidade):
    """Gera uma lista de dicionários com dados de pessoas."""
    pessoas = []
    for _ in range(quantidade):
        pessoa = Pessoa().gerar_dados_pessoa()
        pessoas.append(pessoa)
    return pessoas

def salvar_dados(pessoas, formato):
    """Salva os dados gerados no formato escolhido."""

    if formato == "json":
        with open("pessoas.json", "w", encoding='utf-8') as f:
            json.dump(pessoas, f, indent=4)
        print("Dados salvos em pessoas.json")
    elif formato == "xlsx":
        df = pd.DataFrame(pessoas)
        df.to_excel("pessoas.xlsx", index=False)
        print("Dados salvos em pessoas.xlsx")
    elif formato == "txt":
        with open("pessoas.txt", "w", encoding='utf-8') as f:
            for pessoa in pessoas:
                f.write(f"Nome: {pessoa['nome']}\n")
                f.write(f"CPF: {pessoa['cpf']}\n")
                f.write(f"Email: {pessoa['email']}\n")
                f.write(f"Endereço: {pessoa['endereco']}\n")
                f.write(f"Telefone: {pessoa['telefone']}\n\n")
        print("Dados salvos em pessoas.txt")
    else:
        print("Formato inválido!")

if __name__ == "__main__":
    quantidade = int(input("Digite a quantidade de pessoas a serem geradas: "))
    formato = input("Digite o formato de saída (json, xlsx, txt): ")
    pessoas = gerar_pessoas(quantidade)
    salvar_dados(pessoas, formato)