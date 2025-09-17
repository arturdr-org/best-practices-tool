import os
from pathlib import Path
import subprocess
import requests # Added for update_practices.py
from update_practices import update_best_practices_docs # Import the new function name

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

def install_git_hooks():
    print("Instalando Git hooks...")
    # Find all git repositories in the home directory
    home = Path.home()
    for git_dir in home.glob('**/.git'):
        if git_dir.is_dir():
            repo_root = git_dir.parent
            print(f"Configurando hooks para o repositório: {repo_root}")

            # Create pre-commit hook
            pre_commit_hook_path = git_dir / "hooks" / "pre-commit"
            our_pre_commit_script = Path(__file__).parent / "hooks" / "git_hook_pre_commit"
            our_pre_commit_script = our_pre_commit_script.resolve()

            with open(pre_commit_hook_path, "w") as f:
                f.write(f"#!/bin/bash\n{our_pre_commit_script}\n")
            os.chmod(pre_commit_hook_path, 0o755)
            print(f"  - pre-commit hook instalado em {pre_commit_hook_path}")

            # Create pre-push hook
            pre_push_hook_path = git_dir / "hooks" / "pre-push"
            our_pre_push_script = Path(__file__).parent / "hooks" / "git_hook_pre_push"
            our_pre_push_script = our_pre_push_script.resolve()

            with open(pre_push_hook_path, "w") as f:
                f.write(f"#!/bin/bash\n{our_pre_push_script}\n")
            os.chmod(pre_push_hook_path, 0o755)
            print(f"  - pre-push hook instalado em {pre_push_hook_path}")
    print("Instalação de Git hooks concluída.")

def install_wrapper():
    home = Path.home()
    wrapper_path = Path(__file__).parent / "wrapper.sh"
    destination = home / "bin" / "run_validated_command.sh"
    os.makedirs(destination.parent, exist_ok=True)
    if not destination.exists():
        with open(wrapper_path, "r") as src, open(destination, "w") as dst:
            dst.write(src.read())
        os.chmod(destination, 0o755)
        print(f"Wrapper instalado em {destination}")
    else:
        print("Wrapper já está instalado.")

    # Seta alias no bashrc
    bashrc = home / ".bashrc"
    alias_line = "alias run_validated_command='$HOME/bin/run_validated_command.sh'\n"
    with open(bashrc, "r") as f:
        content = f.read()
    if alias_line not in content:
        with open(bashrc, "a") as f:
            f.write(f"\n# Alias para comando validado\n{alias_line}")
        print(f"Alias adicionado no {bashrc}")

def main():
    install_practices_docs()
    install_shell_hook()
    install_git_hooks()
    install_wrapper()
    update_best_practices_docs() # Call the new function name
    print("Instalação completa. Reabra o terminal para aplicar.")

if __name__ == "__main__":
    main()
