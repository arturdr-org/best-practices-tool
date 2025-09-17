import sys
import re
import yaml # Added
import os # Added

def load_config(config_file="config.yaml"):
    script_dir = os.path.dirname(__file__)
    config_path = os.path.join(script_dir, config_file)
    if not os.path.exists(config_path):
        return {"enabled": True, "disabled_tools": []}
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

config = load_config()

def is_validation_enabled(tool=None):
    if not config.get("enabled", True):
        return False
    if tool and tool in config.get("disabled_tools", []):
        return False
    return True

def validate_command(cmd):
    warnings = []

    if not is_validation_enabled():
        return warnings # Global validation disabled

    # Exemplo 1: alerta para uso do rm sem -i (confirmar remoção)
    if is_validation_enabled(tool="rm") and re.match(r'^rm\s', cmd) and '-i' not in cmd:
        warnings.append("⚠️ Atenção: comando 'rm' sem opção '-i'. Considere usar para confirmação segura.")

    # Sugestão para usar git pull antes de git push
    if is_validation_enabled(tool="git") and cmd.startswith("git push") and "git pull" not in cmd:
        warnings.append("💡 Dica: use 'git pull' antes de 'git push' para evitar conflitos.")

    # Alerta para uso de sudo desnecessário
    if is_validation_enabled(tool="sudo") and cmd.startswith("sudo") and not re.search(r'apt|yum|dnf|pacman', cmd):
        warnings.append("⚠️ Aviso: você usou sudo. Verifique se é realmente necessário.")

    return warnings

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python validate_command.py '<comando>'\n")
        sys.exit(1)

    command_input = sys.argv[1]
    results = validate_command(command_input)

    if results:
        print("\n".join(results))
    else:
        print("Comando OK.")