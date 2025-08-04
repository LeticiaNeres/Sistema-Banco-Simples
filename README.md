# Sistema Bancário Simples em Python

Este projeto simula um sistema bancário básico desenvolvido em Python. O objetivo foi implementar funcionalidades essenciais de uma conta bancária, permitindo a realização de depósitos, saques e a visualização do extrato de movimentações.

## 💡 Objetivo

Criar um sistema funcional simples para um banco fictício, aplicando conceitos fundamentais da linguagem Python. A proposta simula as principais operações bancárias para um único usuário, com armazenamento em variáveis e exibição por terminal.

## ⚙️ Funcionalidades

### ✅ Operação de Depósito
- Permite depósitos de valores positivos.
- Não há necessidade de número de conta ou agência, pois o sistema trabalha com um único usuário.
- Todos os depósitos são registrados e exibidos na operação de extrato.

### ✅ Operação de Saque
- Permite até 3 saques diários.
- Limite máximo de R$ 500,00 por saque.
- Saques não são permitidos caso o saldo seja insuficiente.
- Todas as operações de saque são registradas e exibidas na operação de extrato.

### ✅ Operação de Extrato
- Lista todas as movimentações realizadas (depósitos e saques).
- Exibe o saldo atual da conta.
- Caso nenhuma movimentação tenha sido realizada, exibe a mensagem:
  

