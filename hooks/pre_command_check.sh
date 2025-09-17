#!/bin/bash

validate_command_with_python() {
  # Get the full command string
  local cmd="${BASH_COMMAND}"

  # Path to the Python validator script
  local python_validator_script="$(dirname "$0")"/../utils.py

  # Run the Python validator and capture its output
  local validation_output=$(python3 "$python_validator_script" "$cmd")

  # If the Python script returned warnings, display them
  if [[ -n "$validation_output" && "$validation_output" != "Comando OK." ]]; then
    echo "$validation_output"
    # Optionally, you could ask for user confirmation here before proceeding
    # read -p "Continuar mesmo assim? (s/N): " -n 1 -r
    # echo
    # if [[ ! $REPLY =~ ^[Ss]$ ]]; then
    #   return 1 # Abort command execution
    # fi
  fi
  return 0 # Allow command execution
}

PROMPT_COMMAND=validate_command_with_python