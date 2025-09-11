OB:ESTE PROJETO TEM DUAS VERSÕES UMA SIMPLES COM FUNCIONALIDADES BÁSICAS , E UMA OUTRA COM INTEGRAÇÃO DE OUTRAS FUNCIONALIDADES BÁSICAS PERTINENTES AO SISTEMA DE CAIXA ELETRÔNICO.
 
 
 
 
 
 Sistema Bancário em Python
Este projeto é um sistema bancário simples desenvolvido em Python como parte da trilha de aprendizado da DIO. Ele simula operações básicas de uma conta corrente, como depósitos, saques e emissão de extrato, com regras de negócio aplicadas para controle de limite e segurança.

 Funcionalidades
Depósito: Permite adicionar valores positivos ao saldo da conta.

Saque:

Limite de R$ 500,00 por saque

Máximo de 3 saques diários

Verificação de saldo antes da operação

Extrato: Exibe todas as movimentações realizadas e o saldo atual.

Menu interativo: Interface simples via terminal para navegação entre opções.
 Regras de Negócio
Apenas valores positivos são aceitos para depósito e saque.

O sistema impede saques acima do saldo ou do limite por operação.

O número de saques diários é limitado a três.

Todas as transações são registradas no extrato.

 Estrutura do Código
menu: Exibe as opções disponíveis para o usuário.

saldo: Armazena o valor atual da conta.

limite: Define o valor máximo por saque.

extrato: Registra todas as transações.

numero_saques: Controla a quantidade de saques realizados.

LIMITE_SAQUES: Constante que define o limite diário de saques.

while True: Loop principal que mantém o sistema em execução até o usuário sair.

 Tecnologias Utilizadas
Python 3.x

Lógica de programação

Manipulação de strings e estruturas condicionais

