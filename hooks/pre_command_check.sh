#!/bin/bash

validate_command() {
  cmd="${BASH_COMMAND}"

  # Exemplo: alertar se usar 'rm' sem opções seguras
  if [[ "$cmd" =~ ^rm\  && ! "$cmd" =~ -i ]]; then
    echo "⚠️ Atenção: 'rm' está sem opção '-i' para confirmação. Use com cuidado!"
  fi

  # Exemplo: sugerir uso de git pull antes de push
  if [[ "$cmd" == git\ push* ]]; then
    echo "💡 Dica: use 'git pull' para atualizar branch antes de 'git push'."
  fi

  # Outras regras podem ser inseridas aqui...
}

PROMPT_COMMAND=validate_command