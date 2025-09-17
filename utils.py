import sys
import re

def validate_command(cmd):
    warnings = []

    # Exemplo 1: alerta para uso do rm sem -i
    if re.match(r'^rm\s', cmd) and '-i' not in cmd:
        warnings.append("⚠️ Atenção: comando 'rm' sem '-i'. Considere usar para confirmação segura.")

    # Exemplo 2: sugestão para git push
    if cmd.startswith("git push") and "git pull" not in cmd:
        warnings.append("💡 Dica: use 'git pull' antes de 'git push' para evitar conflitos.")

    # Exemplo 3: alertar para uso de sudo sem necessidade
    if cmd.startswith("sudo") and "apt-get" not in cmd and "apt" not in cmd:
        warnings.append("⚠️ Você está usando sudo. Verifique se é realmente necessário.")

    return warnings

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python validate_command.py '<comando>'\n")
        sys.exit(1)

    command_input = sys.argv[1]
    result = validate_command(command_input)

    if result:
        print("\n".join(result))
    else:
        print("Comando OK.")