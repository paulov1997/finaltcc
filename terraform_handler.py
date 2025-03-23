import subprocess
import os
import sys

BASE_DIR = os.path.dirname(__file__)
VM_DIR = os.path.join(BASE_DIR, "infraestrutura", "computeengine")
GKE_DIR = os.path.join(BASE_DIR, "infraestrutura", "gke")

def executar_terraform(diretorio):
    """Executa Terraform no diretório especificado."""
    try:
        print(f"\n🔄 Inicializando o Terraform no diretório: {diretorio} ...")
        subprocess.run(["terraform", "init"], cwd=diretorio, check=True)

        print("\n🚀 Aplicando a infraestrutura com Terraform...")
        subprocess.run(["terraform", "apply", "-auto-approve"], cwd=diretorio, check=True)

        print("\n✅ Infraestrutura criada com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Erro ao executar o Terraform: {e}")
        sys.exit(1)

def destruir_terraform(diretorio):
    """Executa Terraform no diretório especificado."""
    try:
        print(f"\n🔄Destruindo o Terraform no diretório: {diretorio} ...")
        subprocess.run(["terraform", "destroy", "-auto-approve"], cwd=diretorio, check=True)

        print("\n✅ Infraestrutura excluida com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Erro ao executar o Terraform: {e}")
        sys.exit(1)        

def criar_vm():
    """Executa Terraform para subir uma VM."""
    executar_terraform(VM_DIR)

def criar_gke():
    """Executa Terraform para subir um cluster GKE."""
    executar_terraform(GKE_DIR)

def destruir_vm():
    """Executa Terraform para destruir a VM."""
    destruir_terraform(VM_DIR)      

def destruir_gke():
    """Executa Terraform para destruir o cluster GKE."""
    destruir_terraform(GKE_DIR)