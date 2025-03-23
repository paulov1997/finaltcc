import subprocess
import sys
import os
import json
import platform
import shutil
if sys.platform.startswith("linux"):
    import distro  # Pacote para identificar a distribuição Linux

from google.cloud import resourcemanager_v3
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.exceptions import DefaultCredentialsError


def instalar_pre_requisitos():
    """Verifica e instala os pré-requisitos necessários: PIP, Cloud CLI (gcloud) e pacotes Python."""

    # Verifica se o PIP está instalado
    print("Verificando se o PIP está instalado...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("PIP já está instalado.")
    except subprocess.CalledProcessError:
        print("PIP não encontrado. Instalando...")

        os_name = platform.system()

        if os_name == 'Linux':
            distro_name = distro.id()
            if distro_name in ['debian', 'ubuntu', 'linuxmint', 'mxlinux', 'devuan', 'deepin', 'elementary', 'zorin', 'pop']:
                print("Sistema Debian-based detectado. Instalando PIP com apt...")
                subprocess.check_call(['sudo', 'apt', 'update'])
                subprocess.check_call(['sudo', 'apt', 'install', 'python3-pip', '-y'])
                print("PIP instalado com sucesso em sistemas Debian-based.")
            else:
                print(f"Sistema Linux {distro_name} não suportado para instalação automática do PIP.")
                sys.exit(1)
        elif os_name == 'Windows':
            print("Sistema Windows detectado. Instalando PIP com o Python...")
            subprocess.check_call([sys.executable, "-m", "ensurepip", "--upgrade"])
            print("PIP instalado com sucesso em sistemas Windows.")
        else:
            print(f"Sistema operacional {os_name} não suportado para instalação do PIP.")
            sys.exit(1)

    # Verifica se o Cloud CLI (gcloud) está instalado
    print("Verificando se o Cloud CLI (gcloud) está instalado...")
    if shutil.which("gcloud"):
        print("Cloud CLI (gcloud) já está instalado.")
    else:
        print("Cloud CLI (gcloud) não encontrado. Instalando...")

        os_name = platform.system()

        if os_name == 'Linux':
            distro_name = distro.id()
            if distro_name in ['debian', 'ubuntu', 'linuxmint', 'mxlinux', 'devuan', 'deepin', 'elementary', 'zorin', 'pop']:
                print("Sistema Debian-based detectado. Instalando Cloud CLI com apt...")
                try:
                    # Atualizar repositórios e instalar dependências
                    subprocess.check_call(['sudo', 'apt-get', 'update'])
                    subprocess.check_call(['sudo', 'apt-get', 'install', 'apt-transport-https', 'ca-certificates', 'gnupg', 'curl', '-y'])

                    # Remover keyring existente, se houver
                    subprocess.check_call(['sudo', 'rm', '-f', '/usr/share/keyrings/cloud.google.gpg'])

                    # Baixar a chave GPG e convertê-la
                    subprocess.check_call(['curl', '-s', 'https://packages.cloud.google.com/apt/doc/apt-key.gpg', '-o', '/tmp/cloud.google.gpg'])
                    subprocess.check_call(['sudo', 'gpg', '--batch', '--yes', '--dearmor', '-o', '/usr/share/keyrings/cloud.google.gpg', '/tmp/cloud.google.gpg'])

                    # Adicionar o repositório ao sources.list
                    subprocess.check_call([
                        'sudo', 'bash', '-c',
                        'echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" > /etc/apt/sources.list.d/google-cloud-sdk.list'
                    ])

                    # Atualizar os repositórios e instalar o Cloud CLI
                    subprocess.check_call(['sudo', 'apt-get', 'update'])
                    subprocess.check_call(['sudo', 'apt-get', 'install', 'google-cloud-cli', '-y'])
                    print("Cloud CLI (gcloud) instalado com sucesso em sistemas Debian-based.")
                except subprocess.CalledProcessError as e:
                    print(f"Falha ao instalar o Cloud CLI (gcloud) em sistemas Debian-based. Erro: {e}")
                    sys.exit(1)
            else:
                print(f"Sistema Linux {distro_name} não suportado para instalação automática do Cloud CLI.")
                sys.exit(1)

        elif os_name == 'Windows':
            print("Sistema Windows detectado. Instalando Cloud CLI com o instalador...")
            try:
                # Comando para baixar e executar o instalador do gcloud no Windows
                subprocess.check_call([
                    "powershell",
                    "(New-Object Net.WebClient).DownloadFile(\"https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe\", \"$env:Temp\\GoogleCloudSDKInstaller.exe\")"
                ])
                subprocess.check_call([
                    "powershell",
                    "& $env:Temp\\GoogleCloudSDKInstaller.exe"
                ])
                print("Cloud CLI (gcloud) instalado com sucesso em sistemas Windows.")
            except subprocess.CalledProcessError as e:
                print(f"Falha ao instalar o Cloud CLI (gcloud) em sistemas Windows. Erro: {e}")
                sys.exit(1)
        else:
            print(f"Sistema operacional {os_name} não suportado para instalação do Cloud CLI.")
            sys.exit(1)

    # Lista de pacotes Python necessários
    required_packages = {
        'google-cloud-resource-manager': 'google.cloud',
        'google-api-python-client': 'googleapiclient',
        'google-auth': 'google.auth',
        'google-cloud-storage': 'google.cloud.storage',
    }

    # Verifica e instala os pacotes Python necessários
    for package, module in required_packages.items():
        try:
            __import__(module)
            print(f"Pacote {package} já está instalado.")
        except ImportError:
            print(f"Pacote {package} não encontrado. Instalando...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"Pacote {package} instalado com sucesso.")

    print("Todos os pré-requisitos foram instalados com sucesso.")




def configurar_gcp(credentials_file):
    """Função para configurar o GCP, habilitar APIs e criar os arquivos tfvars."""
    
    def authenticate_with_service_account(credentials_file):
        """Autentica usando a chave da conta de serviço."""
        try:
            if not os.path.exists(credentials_file):
                raise FileNotFoundError(f"O arquivo de credenciais não foi encontrado: {credentials_file}")
            
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_file
            print(f"Autenticado com sucesso usando a chave {credentials_file}.")
        except DefaultCredentialsError as e:
            print(f"Erro ao autenticar: {e}")
            sys.exit(1)
        except FileNotFoundError as e:
            print(e)
            sys.exit(1)

    def get_project_id_from_credentials(credentials_file):
        """Obtém o project_id do arquivo de credenciais da conta de serviço."""
        try:
            with open(credentials_file, 'r') as f:
                credentials_data = json.load(f)
                return credentials_data.get("project_id")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erro ao obter project_id das credenciais: {e}")
            sys.exit(1)

    def check_and_enable_api(project_id, api_name):
        """Verifica se uma API está habilitada no projeto e a habilita, se necessário."""
        try:
            print(f"Verificando se a API {api_name} está habilitada para o projeto {project_id}...")
            service = build('serviceusage', 'v1')
            request = service.services().get(name=f"projects/{project_id}/services/{api_name}")
            response = request.execute()

            if response.get('state') == 'ENABLED':
                print(f"A API {api_name} já está habilitada.")
                return True

            print(f"Habilitando a API {api_name}...")
            enable_request = service.services().enable(name=f"projects/{project_id}/services/{api_name}")
            enable_response = enable_request.execute()
            print(f"A API {api_name} foi habilitada com sucesso.")
            return enable_response
        except HttpError as e:
            print(f"Erro ao verificar ou habilitar a API {api_name}: {e}")
            return False

    def write_tfvars_from_env():
        """Gera o arquivo terraform.tfvars e salva nas pastas computeengine e gke."""
        tfvars_content = (
            f'project = "{os.environ["TF_VAR_project"]}"\n'
            f'region = "{os.environ["TF_VAR_region"]}"\n'
            f'zone = "{os.environ["TF_VAR_zone"]}"\n'
            f'credentials = "{os.environ["TF_VAR_credentials"]}"\n'
        )

        for folder in ["infraestrutura/computeengine", "infraestrutura/gke"]:
            os.makedirs(folder, exist_ok=True)  # Garante que as pastas existem
            tfvars_path = os.path.join(folder, "terraform.tfvars")
            with open(tfvars_path, "w") as f:
                f.write(tfvars_content)
            print(f'Arquivo {tfvars_path} criado com sucesso!')

    # Início da execução da configuração
    authenticate_with_service_account(credentials_file)

    project_id = get_project_id_from_credentials(credentials_file)
    if not project_id:
        print("Erro: Não foi possível obter o project_id das credenciais.")
        sys.exit(1)

    required_apis = [
        "cloudresourcemanager.googleapis.com",
        "compute.googleapis.com",
        "container.googleapis.com"
    ]

    for api in required_apis:
        check_and_enable_api(project_id, api)

    os.environ["TF_VAR_project"] = project_id
    os.environ["TF_VAR_region"] = "us-central1"
    os.environ["TF_VAR_zone"] = "us-central1-c"
    os.environ["TF_VAR_credentials"] = credentials_file

    print("Configuração concluída.")
    write_tfvars_from_env()

def conectar_vm():
    """Conecta à VM automaticamente via gcloud."""
    project = os.environ.get("TF_VAR_project")
    zone = os.environ.get("TF_VAR_zone")
    
    if not project or not zone:
        print("Erro: Variáveis de ambiente TF_VAR_project e TF_VAR_zone não estão definidas.")
        return
    
    comando = f"gcloud compute ssh flask-vm --zone={zone} --project={project}"
    subprocess.run(comando, shell=True, check=True)

def conectar_gke():
    """Obtém as credenciais do cluster GKE automaticamente via gcloud."""
    project = os.environ.get("TF_VAR_project")
    zone = os.environ.get("TF_VAR_zone")
    
    if not project or not zone:
        print("Erro: Variáveis de ambiente TF_VAR_project e TF_VAR_zone não estão definidas.")
        return
    
    comando = f"gcloud container clusters get-credentials gke-cluster --zone={zone} --project={project}"
    subprocess.run(comando, shell=True, check=True)

    