#!/bin/bash
validate_command() {
  cmd="${BASH_COMMAND}"

  if [[ "$cmd" =~ ^rm\  && ! "$cmd" =~ -i ]]; then
    echo "⚠️ Atenção: 'rm' está sem opção '-i' para confirmação. Use com cuidado!"
  fi

  if [[ "$cmd" == git\ push* ]]; then
    echo "💡 Dica: use 'git pull' para atualizar branch antes de 'git push'."
  fi

  if [[ "$cmd" == sudo* && ! "$cmd" =~ apt ]]; then
    echo "⚠️ Você está usando sudo. Verifique se é realmente necessário."
  fi
}
PROMPT_COMMAND=validate_command