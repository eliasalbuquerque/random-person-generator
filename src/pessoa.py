# title: 'pessoa'
# author: 'Elias Albuquerque'
# version: '0.1'
# created: '2024-09-28'
# update: '2024-09-28'


from faker import Faker
from faker.providers.person import Provider
import random
import re


class Pessoa:
    def __init__(self):
        self.fake = Faker('pt_BR')

    def gerar_dados_pessoa(self):
        """Gera dados fictícios de uma pessoa."""

        nome = self.__gerar_nome_sem_prefixos()
        cpf = self.__gerar_cpf_valido()
        email = self.__gerar_email_personalizado(nome) 
        endereco = self.__gerar_endereco_customizado()
        contato = self.__gerar_numero_de_contato()
        
        return {
            'nome': nome,
            'cpf': cpf,
            'email': email,
            'endereco': endereco,
            'contato': contato
        }

    def __gerar_nome_sem_prefixos(self):
        """Gera um nome fictício sem prefixos como 'Dr.' ou 'Dra.'."""

        nome_completo = self.fake.name()
        nome = re.sub(r"^(Dr\.|Dra\.|Sra\.|Sr\.|Srta\.)\s*", "", nome_completo)      

        return nome
        

    def __gerar_cpf_valido(self):
        """Gera um CPF válido, mas falso, utilizando um provider da biblioteca Faker."""

        return self.fake.cpf()

    def __gerar_email_personalizado(self, nome):
        """Gera um e-mail fictício usando parte do nome da pessoa com separadores variados."""

        partes_nome = nome.split()
        primeiro_nome = partes_nome[0]
        ultimo_nome = partes_nome[-1]

        separadores = ['.', '_', '']
        separador = random.choice(separadores)

        dominio = self.fake.free_email_domain()
        email = f"{primeiro_nome.lower()}{separador}{ultimo_nome.lower()}@{dominio}"

        return email

    def __gerar_endereco_customizado(self):
        """Gera um endereço no formato do Google Maps."""


        # Demais partes do endereço
        numero = self.fake.building_number()    # Número do prédio
        rua = self.__gerar_nome_rua()           # Endereço
        bairro = self.fake.bairro()             # Bairro
        cidade = self.fake.city()               # Cidade
        estado = self.fake.estado_sigla()       # Sigla do estado (SP, RJ, etc.)

        # Gerar e formatar o CEP no padrão brasileiro
        cep_cru = self.fake.postcode(formatted=False)
        cep = re.sub(r"(\d{5})(\d{3})", r"\1-\2", cep_cru)

        # Construir o endereço completo
        endereco_formatado = f"{rua}, {numero} - {bairro}, {cidade} - {estado}, {cep}"

        return endereco_formatado


    def __gerar_nome_rua(self):
        """Gera um nome de rua formatado conforme regras definidas."""

        # NOTE: O método street_name() gera nomes de lugares como Largo, 
        # Vereda, Sítio, etc. Nesse caso, esse método visa inserir Rua e 
        # Avenida, trabalhando com o resultado do método street_name(), usando 
        # probabilidade e adequando o resultado do nome da rua para um endereço 
        # final coerente.

        rua = self.fake.street_name()
        chance_alteracao = random.random()

        # 80% de chance de alterar o nome
        if chance_alteracao < 0.8:  
            primeira_palavra = rua.split()[0]

            # Escolher entre 'R.' ou 'Av.' com igual probabilidade
            if random.choice([True, False]):
                rua = rua.replace(primeira_palavra, 'R.', 1)
            else:
                rua = rua.replace(primeira_palavra, 'Av.', 1)

            # Verificar a segunda palavra e corrigir se necessário:
            # Se a próxima palavra tiver apenas 2 caracteres substituir por um 
            # nome de pessoa
            palavras = rua.split()
            
            if len(palavras) > 1 and len(palavras[1]) == 2:  
                novo_nome = self.fake.first_name()  
                palavras[1] = novo_nome
                rua = " ".join(palavras)

        return rua


    def __gerar_numero_de_contato(self):
        """Gera um número de contato formatado no padrão brasileiro (XX) XXXXX-XXXX."""

        # Gera um número de celular bruto usando msisdn()
        numero_completo = self.fake.msisdn()
        
        # Remove o código do país (55)
        numero_bruto = numero_completo[2:]

        # Separa o DDD, os primeiros 5 dígitos e os últimos 4 dígitos
        ddd = numero_bruto[:2]
        parte1 = numero_bruto[2:7]
        parte2 = numero_bruto[7:]

        # Formata o número no padrão brasileiro: (XX) XXXXX-XXXX
        contato = f"({ddd}) {parte1}-{parte2}"
        
        return contato
