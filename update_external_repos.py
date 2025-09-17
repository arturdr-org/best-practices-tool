import os
import json
import requests

def load_config(config_file="external_repos.json"):
    script_dir = os.path.dirname(__file__)
    config_path = os.path.join(script_dir, config_file)
    with open(config_path, "r") as f:
        return json.load(f)

def download_and_save(url, path):
    script_dir = os.path.dirname(__file__)
    full_path = os.path.join(script_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    try:
        r = requests.get(url)
        r.raise_for_status()
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(r.text)
        print(f"Atualizado: {full_path}")
    except Exception as e:
        print(f"Erro ao baixar {url}: {e}")

def update_external_repos():
    config = load_config()
    for repo in config.get("repos", []):
        download_and_save(repo["url"], repo["local_path"])

if __name__ == "__main__":
    update_external_repos()