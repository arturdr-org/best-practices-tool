import os
import yaml

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

    # Ignora validação se globalmente desativado
    if not is_validation_enabled():
        return []

    # Exemplo: validação para comando docker só se habilitado
    if cmd.startswith("docker") and not is_validation_enabled("docker"):
        return []

    # Exemplo 1: alerta para uso do rm sem -i (confirmar remoção)
    if cmd.startswith("rm ") and "-i" not in cmd:
        warnings.append("⚠️ Atenção: comando 'rm' sem opção '-i'. Use com cuidado!")

    # Exemplo 2: sugestão para usar git pull antes de git push
    if cmd.startswith("git push") and "git pull" not in cmd:
        warnings.append("💡 Dica: use 'git pull' antes de 'git push' para evitar conflitos.")

    # Exemplo 3: alerta para uso de sudo desnecessário
    if cmd.startswith("sudo") and not any(x in cmd for x in ["apt", "yum", "dnf", "pacman"]):
        warnings.append("⚠️ Aviso: você usou sudo. Verifique se é realmente necessário.")

    return warnings

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python validate_command.py '<comando>'")
        exit(1)

    command_input = sys.argv[1]
    results = validate_command(command_input)
    if results:
        print("\n".join(results))
    else:
        print("Comando OK.")
