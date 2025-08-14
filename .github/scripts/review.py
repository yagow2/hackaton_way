import os
import requests
import subprocess
import json

# --- Configurações ---
HUGGINGFACE_API_URL = os.getenv("HUGGINGFACE_API_URL") or '' # ex.: https://api-inference.huggingface.co/models/<modelo>
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
PR_NUMBER = os.getenv("PR_NUMBER")
REPO = os.getenv("GITHUB_REPOSITORY")

headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

# --- 1. Obter arquivos modificados no PR ---
result = subprocess.run(
    ["git", "diff", "--name-only", "origin/main...HEAD"],
    stdout=subprocess.PIPE,
    text=True
)

changed_files = [f for f in result.stdout.split("\n") if f.endswith(".ts")]
if not changed_files:
    print("Nenhum arquivo TypeScript alterado.")
    exit(0)

# --- 2. Ler conteúdo dos arquivos ---
diffs = []
for file in changed_files:
    try:
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        diffs.append(f"Arquivo: {file}\n\n{code}")
    except Exception as e:
        print(f"Erro ao ler {file}: {e}")

# --- 3. Enviar para Hugging Face ---
payload = {
    "inputs": "\n\n".join(diffs),
    "parameters": {"max_new_tokens": 512}
}
response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=payload)
review = response.json()

# --- 4. Postar comentário no PR ---
comment_body = f"### 🤖 Code Review com IA\n\n{review}"
requests.post(
    f"https://api.github.com/repos/{REPO}/issues/{PR_NUMBER}/comments",
    headers={
        "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
        "Accept": "application/vnd.github.v3+json"
    },
    json={"body": comment_body}
)
