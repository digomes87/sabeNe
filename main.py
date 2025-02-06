import os
import time
from datetime import datetime

# Configurações
REPO_DIR = "/home/birudin/projetos/sabeNe"  # Altere para o caminho do seu repositório local
BRANCH = "main"  # Altere se estiver em outra branch

def atualizar_arquivo():
    """Modifica um arquivo para gerar um commit."""
    file_path = os.path.join(REPO_DIR, "log.txt")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(file_path, "a") as f:
        f.write(f"Update at {timestamp}\n")

def fazer_commit_e_push():
    """Faz commit e push das alterações."""
    os.system(f"cd {REPO_DIR} && git add .")
    os.system(f'cd {REPO_DIR} && git commit -m "Atualização automática {datetime.now()}"')
    os.system(f"cd {REPO_DIR} && git push origin {BRANCH}")

if __name__ == "__main__":
    atualizar_arquivo()
    fazer_commit_e_push()

