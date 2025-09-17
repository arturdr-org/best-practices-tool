import shutil
import subprocess
import os
import requests

def check_installed(tool):
    return shutil.which(tool) is not None

def download_url(url, output_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            file.write(response.content)
        print(f"Arquivo baixado: {output_path}")
    else:
        print(f"Falha ao baixar {url} - Status: {response.status_code}")

def update_best_practices():
    tools = {
        "docker": "https://raw.githubusercontent.com/docker/docker.github.io/main/best-practices.md",
        "ansible": "https://raw.githubusercontent.com/ansible/community/devel/CONTRIBUTING.md",
        "terraform": "https://raw.githubusercontent.com/hashicorp/terraform-guides/master/best-practices.md",
        # Adicione mais links oficiais pertinentes
    }

    os.makedirs("practices/auto", exist_ok=True)

    for tool, url in tools.items():
        if check_installed(tool):
            output_file = f"practices/auto/{tool}_best_practices.md"
            print(f"{tool} detectado, baixando boas práticas...")
            download_url(url, output_file)
        else:
            print(f"{tool} não encontrado, ignorando.")

if __name__ == "__main__":
    update_best_practices()