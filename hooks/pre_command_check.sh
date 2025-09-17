#!/bin/bash

# Antes de executar qualquer comando, exibe um lembrete rápido de boas práticas

check_best_practices() {
  echo "🔔 Lembre-se de seguir as boas práticas para comandos no terminal! Consulte './practices/' para dicas."
}

PROMPT_COMMAND=check_best_practices