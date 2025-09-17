import os
import shutil
import requests

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
    os.makedirs("practices/auto", exist_ok=True)
    for tool_name, info in TOOLS_BEST_PRACTICES.items():
        if is_tool_installed(info["command"]):
            print(f"Detectado {tool_name}, atualizando boas práticas...")
            dest_file = os.path.join("practices", "auto", info["filename"])
            download_file(info["url"], dest_file)
        else:
            print(f"{tool_name} não detectado, pulando.")

if __name__ == "__main__":
    update_best_practices_docs()