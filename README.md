# Sistema Bancário - Desafio DIO

Este projeto é uma solução para o desafio de criar um sistema bancário básico utilizando Python, proposto pela DIO (Digital Innovation One). O sistema implementa funcionalidades essenciais de um banco, como depósitos, saques e a geração de um extrato, seguindo regras específicas para garantir a segurança e a simplicidade das operações.

## Funcionalidades

- **Depósito**: Permite realizar depósitos de valores positivos, que são refletidos no saldo e no extrato.
- **Saque**: Limita a quantidade de saques a 3 por dia, com um valor máximo de R$ 500 por saque. O saldo disponível é atualizado automaticamente.
- **Extrato**: Lista todas as operações (depósitos e saques) realizadas, mostrando o saldo final ao final do extrato.

## Requisitos

- Python 3.8+
- Visual Studio Code

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/dayviddouglas/sistema_bancario_desafio_dio.git
    ```

2. Entre no diretório do projeto:
    ```bash
    cd sistema_bancario_desafio_dio
    ```

## Uso

Para executar o sistema bancário, utilize o seguinte comando:
```bash
python main.py
