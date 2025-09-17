#!/bin/bash

VALIDATOR_PATH="$HOME/path/to/validate_command.py"

run_validated_command() {
  cmd="$*"
  warnings=$(python3 "$VALIDATOR_PATH" "$cmd")
  echo "$warnings"
  if [[ "$warnings" != "Comando OK." ]]; then
    read -p "Deseja continuar a execução? (s/n) " resp
    if [[ "$resp" != [Ss] ]]; then
      echo "Execução cancelada pelo usuário."
      return 1
    fi
  fi
  eval "$cmd"
}

alias run='run_validated_command'

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  if [ $# -eq 0 ]; then
    echo "Uso: $0 <comando>"
    exit 1
  fi
  run_validated_command "$@"
fi