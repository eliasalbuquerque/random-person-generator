# Gerador de Dados Fictícios de Pessoas

Um gerador de dados fictícios de pessoas em Python, utilizando a biblioteca 
Faker para criar nomes, CPFs, e-mails, endereços e telefones falsos, mas 
válidos, para testes e desenvolvimento.

## Funcionalidades

* Gera dados fictícios de pessoas, incluindo:
    * Nome completo
    * CPF válido
    * Email personalizado
    * Endereço completo formatado como o Google Maps
    * Número de contato no padrão brasileiro
* Permite definir a quantidade de pessoas a serem geradas.
* Permite escolher o formato de saída dos dados: JSON, XLSX ou TXT.

## Requisitos

* Python 3.6+
* Bibliotecas:
    * `faker`
    * `pandas`
    * `XlsxWriter`

## Como usar

1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Execute o script `app.py`:**
   ```bash
   python app.py
   ```
3. **Insira a quantidade de pessoas a serem geradas:**
   ```
   Digite a quantidade de pessoas a serem geradas: 
   ```
4. **Escolha o formato de saída:**
   ```
   Digite o formato de saída ([j] json, [x] xlsx, [t] txt): 
   ```
5. **Os dados serão gerados e salvos no formato escolhido.**

## Exemplo de uso

```
Digite a quantidade de pessoas a serem geradas: 3
Digite o formato de saída ([j] json, [x] xlsx, [t] txt): j
Dados salvos em pessoas.json
```

Arquivo salvo `pessoas.json` na raiz do projeto:

```json
[
    {
        "nome": "Cauê Dias",
        "cpf": "569.834.217-28",
        "email": "cauê_dias@yahoo.com.br",
        "endereco": "Av. Kaique Mendonça, 62 - Vila Cloris, Andrade - DF, 08029-713",
        "contato": "(31) 99561-6594"
    },
    {
        "nome": "Diego da Luz",
        "cpf": "340.895.627-83",
        "email": "diego.luz@bol.com.br",
        "endereco": "R. Freitas, 835 - Santo Agostinho, Gonçalves - PE, 18884-066",
        "contato": "(21) 99778-0276"
    },
    {
        "nome": "Maria Luiza Brito",
        "cpf": "478.526.301-62",
        "email": "maria.brito@ig.com.br",
        "endereco": "Av. Ana Aparecida, 29 - Santa Rita, da Paz de Rios - RJ, 26512-677",
        "contato": "(31) 93198-9292"
    }
]
```

##  Notas

* A geração de CPFs é realizada com a validação de dígitos, garantindo a 
  geração de CPFs válidos.
* A geração de emails é personalizada para combinar o nome da pessoa com um 
  domínio fictício.
* O endereço é formatado de forma semelhante ao Google Maps, com rua, número, 
  bairro, cidade, estado e CEP.
* O número de contato é formatado no padrão brasileiro (XX) XXXXX-XXXX.

