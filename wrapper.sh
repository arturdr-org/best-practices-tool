#!/bin/bash

# Caminho para o validador Python
VALIDATOR_PATH="$(dirname "$0")"/utils.py

run_validated_command() {
  # Junta todos os argumentos como um comando string
  cmd="$*"

  # Chama o validador Python e captura as mensagens
  warnings=$(python3 "$VALIDATOR_PATH" "$cmd")

  # Mostra o resultado do validador
  echo "$warnings"

  # Se houver alertas, pedir confirmação para continuar
  if [[ "$warnings" != "Comando OK." ]]; then
    read -p "Deseja continuar a execução? (s/n) " resp
    if [[ "$resp" != [Ss] ]]; then
      echo "Execução cancelada pelo usuário."
      return 1
    fi
  fi

  # Executa o comando real
  eval "$cmd"
}

# Alias para usar no lugar do bash normal
alias run='run_validated_command'

# Para uso direto: rodar ./wrapper.sh ls -l
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  if [ $# -eq 0 ]; then
    echo "Uso: $0 <comando>"
    exit 1
  fi

  run_validated_command "$@"
fi