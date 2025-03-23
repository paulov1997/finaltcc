import os
from funcoes import instalar_pre_requisitos, configurar_gcp ,conectar_vm, conectar_gke 
from terraform_handler import criar_vm, criar_gke , destruir_vm , destruir_gke # Importa a função que vai rodar o terraform

def executar_menu():
    # Variável para controlar o estado do menu
    pre_requisitos_instalados = False
    gcp_configurado = False

    while True:
        print("\nMenu:")
        print("1 - Instalar pré-requisitos")
        print("2 - Configurar GCP")
        print("3 - Criar uma VM")
        print("4 - Criar um cluster GKE")
        print("5 - Destruir a VM criada")
        print("6 - Destruir o cluster criado")
        print("7 - Conectar-se a VM criada")
        print("8 - Conectar-se ao cluster criado")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            instalar_pre_requisitos()
            pre_requisitos_instalados = True
        elif opcao == "2":
            if not pre_requisitos_instalados:
                print("Você precisa instalar os pré-requisitos antes de configurar o GCP.")
            else:
                credentials_file = input("Digite o caminho da chave de autenticação: ")
                configurar_gcp(credentials_file)                
                gcp_configurado = True
        elif opcao == "3":
            # Chama a função para construir uma VM usando o Terraform na pasta computeengine
            criar_vm()
        elif opcao == "4":
            # Chama a função para construir o cluster Kubernetes usando o Terraform na pasta gke
            criar_gke()
        elif opcao == "5":
            # Chama a função para destruir uma VM usando o Terraform na pasta computeengine
            destruir_vm()
        elif opcao == "6":
            # Chama a função para destruir o cluster Kubernetes usando o Terraform na pasta gke
            destruir_gke()
        elif opcao == "7":
            # Chama a função para conectar a VM criada
            conectar_vm()   
        elif opcao == "8":
            # Chama a função para conectar o cluster Kubernets
            conectar_gke()                                
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
