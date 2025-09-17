import os
from pathlib import Path

def install_practices_docs():
    os.makedirs("practices", exist_ok=True)
    docs = {
        "git_practices.md": "# Boas Práticas Git\n- Mensagens claras\n- Branch protection\n",
        "bash_practices.md": "# Boas Práticas Bash\n- Use set -e\n- Variáveis locais\n",
        "security_practices.md": "# Segurança\n- Permissões mínimas\n- SSH seguro\n",
        "automation_practices.md": "# Automação\n- Versionar código IaC\n- Testar playbooks\n"
    }
    for filename, content in docs.items():
        with open(f"practices/{filename}", "w") as f:
            f.write(content)
    print("Docs de boas práticas instaladas em ./practices")

def install_shell_hook():
    home = Path.home()
    bashrc = home / ".bashrc"
    hook_path = Path(__file__).parent / "hooks" / "pre_command_check.sh"
    hook_path = hook_path.resolve()

    hook_line = f"source {hook_path}\n"
    if bashrc.exists():
        with open(bashrc, "r") as f:
            content = f.read()
        if hook_line not in content:
            with open(bashrc, "a") as f:
                f.write(f"\n# Hook de boas práticas\n{hook_line}")
            print(f"Hook instalado no {bashrc}")
        else:
            print("Hook já está instalado.")
    else:
        print(f"{bashrc} não encontrado, crie manualmente para habilitar hooks.")

def main():
    install_practices_docs()
    install_shell_hook()
    print("Instalação inicial completa. Abra novo terminal para aplicar.")

if __name__ == "__main__":
    main()