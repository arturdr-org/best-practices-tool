import os
import shutil
from pathlib import Path

def install_practices():
    print("Instalando arquivos de boas práticas...")
    os.makedirs("practices", exist_ok=True)
    # Exemplos simples - criar arquivos markdown de boas práticas
    with open("practices/git_practices.md", "w") as f:
        f.write("# Boas Práticas Git\n- Commit mensagens claras\n- Branch protection\n")
    with open("practices/bash_practices.md", "w") as f:
        f.write("# Boas Práticas Bash\n- Use set -e para abortar em erro\n- Evite variáveis globais\n")
    print("Arquivos de boas práticas criados em ./practices/")

def install_hooks():
    print("Configurando hooks e wrappers...")
    home = str(Path.home())
    bashrc = os.path.join(home, ".bashrc")

    hook_script = os.path.abspath("hooks/pre_command_check.sh")
    if not os.path.isfile(hook_script):
        print(f"Script de hook {hook_script} não encontrado!")
        return

    line = f"source {hook_script}\n"
    with open(bashrc, "r") as f:
        content = f.read()
    if line not in content:
        with open(bashrc, "a") as f:
            f.write(f"\n# Hook de boas práticas\n{line}")
        print(f"Hook adicionado ao {bashrc}")
    else:
        print("Hook já está configurado no .bashrc")

def main():
    install_practices()
    install_hooks()
    print("Instalação concluída! Abra um novo terminal para as alterações terem efeito.")

if __name__ == "__main__":
    main()
