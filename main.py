import os
import subprocess
import sys
from menu import executar_menu  # Importando a função menu do menu.py

def run_command(command_list):
    """Executa um comando no terminal e exibe a saída em tempo real."""
    try:
        process = subprocess.Popen(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in process.stdout:
            print(line, end="")  # Exibe a saída em tempo real
        process.wait()
        if process.returncode != 0:
            print(f"Erro ao executar o comando: {' '.join(command_list)}\nErro: {process.stderr.read()}")
            sys.exit(1)
    except Exception as e:
        print(f"Erro ao executar o comando: {' '.join(command_list)}\nDetalhes: {e}")
        sys.exit(1)

# Função para rodar o código
if __name__ == "__main__":
    executar_menu()  # Chama a função menu que vai controlar o fluxo de escolhas do usuário
