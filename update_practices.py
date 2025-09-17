import os
import shutil
import requests
import yaml # Added
from utils import load_config, is_validation_enabled # Added

TOOLS_BEST_PRACTICES = {
    "docker": {
        "command": "docker",
        "url": "https://raw.githubusercontent.com/docker/docker.github.io/main/best-practices.md",
        "filename": "docker_best_practices.md",
    },
    "ansible": {
        "command": "ansible",
        "url": "https://raw.githubusercontent.com/ansible/community/devel/CONTRIBUTING.md",
        "filename": "ansible_best_practices.md",
    },
    "terraform": {
        "command": "terraform",
        "url": "https://raw.githubusercontent.com/hashicorp/terraform-guides/master/best-practices.md",
        "filename": "terraform_best_practices.md",
    }
}

def is_tool_installed(tool_command):
    return shutil.which(tool_command) is not None

def download_file(url, dest_path):
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        with open(dest_path, 'wb') as f:
            f.write(resp.content)
        print(f"Baixado: {dest_path}")
    except Exception as e:
        print(f"Erro baixando {url}: {e}")

def update_best_practices_docs():
    config = load_config() # Load config
    os.makedirs("practices/auto", exist_ok=True)
    for tool_name, info in TOOLS_BEST_PRACTICES.items():
        if is_validation_enabled(tool=tool_name) and is_tool_installed(info["command"]): # Check if enabled and installed
            print(f"Detectado {tool_name}, atualizando boas práticas...")
            dest_file = os.path.join("practices", "auto", info["filename"])
            download_file(info["url"], dest_file)
        else:
            print(f"{tool_name} não detectado ou desativado, pulando.")
    
    update_external_practices() # Call the new function

def update_external_practices():
    config = load_config() # Load config
    if not is_validation_enabled(): # Check global validation
        print("Atualização de práticas externas desativada globalmente.")
        return

    print("Atualizando práticas externas...")
    config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
    if not os.path.exists(config_path):
        print("config.yaml não encontrado. Pulando atualização de práticas externas.")
        return

    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    if 'external_practices' in config:
        os.makedirs("practices/external", exist_ok=True)
        for practice in config['external_practices']:
            name = practice.get('name', 'unknown')
            url = practice.get('url')
            destination = practice.get('destination')
            
            if url and destination:
                dest_path = os.path.join("practices", "external", destination)
                print(f"Baixando prática externa: {name} de {url}...")
                download_file(url, dest_path)
            else:
                print(f"Configuração inválida para prática externa: {practice}")
    print("Atualização de práticas externas concluída.")

if __name__ == "__main__":
    update_best_practices_docs()