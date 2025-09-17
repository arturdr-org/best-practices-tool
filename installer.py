import getpass
import os
import shutil
import subprocess
from pathlib import Path
import yaml

def create_default_config():
    config_file = "config.yaml"
    if not os.path.exists(config_file):
        config = {
            "enabled": True,
            "disabled_tools": []
        }
        with open(config_file, "w") as f:
            yaml.dump(config, f)
        print("Arquivo config.yaml criado com configuração padrão.")
    else:
        print("Arquivo config.yaml já existe.")

def load_config(config_file="config.yaml"):
    if not os.path.exists(config_file):
        return {"enabled": True, "disabled_tools": []}
    with open(config_file, "r") as f:
        return yaml.safe_load(f)

config = load_config()

def is_validation_enabled(tool=None):
    if not config.get("enabled", True):
        return False
    if tool and tool in config.get("disabled_tools", []):
        return False
    return True

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

    bashrc = home / ".bashrc"
    alias_line = "alias run_validated_command='$HOME/bin/run_validated_command.sh'\n"
    with open(bashrc, "r") as f:
        content = f.read()
    if alias_line not in content:
        with open(bashrc, "a") as f:
            f.write(f"\n# Alias para comando validado\n{alias_line}")
        print(f"Alias adicionado no {bashrc}")

def schedule_cron_update():
    user = getpass.getuser()
    python_path = shutil.which("python3") or "/usr/bin/python3"
    script_path = str(Path(__file__).parent / "update_practices_cron.py")

    cron_job = f"0 3 * * * {python_path} {script_path} >> /tmp/update_practices.log 2>&1\n"

    try:
        existing_crontab = subprocess.check_output(["crontab", "-l"], text=True)
    except subprocess.CalledProcessError:
        existing_crontab = ""

    if cron_job not in existing_crontab:
        new_crontab = existing_crontab + cron_job
        proc = subprocess.Popen(["crontab", "-"], stdin=subprocess.PIPE, text=True)
        proc.communicate(input=new_crontab)
        print("Cron job para atualização de boas práticas agendado para 03:00 AM diariamente.")
    else:
        print("Cron job de atualização já está agendado.")

def main():
    create_default_config()
    install_practices_docs()
    install_shell_hook()
    install_wrapper()
    schedule_cron_update()
    print("Instalação completa. Reabra o terminal para aplicar.")

if __name__ == "__main__":
    main()
