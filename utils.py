import sys
import re

def validate_command(cmd):
    warnings = []

    # Alerta para uso do rm sem -i (confirmar remoção)
    if re.match(r'^rm\s', cmd) and '-i' not in cmd:
        warnings.append("⚠️ Atenção: comando 'rm' sem opção '-i'. Considere usar para confirmação segura.")

    # Sugestão para usar git pull antes de git push
    if cmd.startswith("git push") and "git pull" not in cmd:
        warnings.append("💡 Dica: use 'git pull' antes de 'git push' para evitar conflitos.")

    # Alerta para uso de sudo desnecessário
    if cmd.startswith("sudo") and not re.search(r'apt|yum|dnf|pacman', cmd):
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
