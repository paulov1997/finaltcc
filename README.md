Guia para Criação de Chave de Acesso aos Recursos Computacionais do Google Cloud
Para permitir que aplicações automatizadas criem e gerenciem recursos computacionais na nuvem do Google Cloud, é necessário criar uma conta de serviço e gerar uma chave de autenticação no formato JSON. A seguir, apresenta-se um passo a passo completo para realizar esse processo:

Etapa 1: Acesse o Console do Google Cloud
Abra o navegador e acesse: https://console.cloud.google.com/

Faça login com sua conta Google.

Etapa 2: Crie ou selecione um projeto
No topo da tela, clique no seletor de projetos.

Se você já possui um projeto, selecione-o. Caso contrário:

Clique em “Novo Projeto”.

Defina um nome e um ID de projeto (único).

Clique em “Criar”.

![image](https://github.com/user-attachments/assets/aab10bc9-b8d9-41d4-b1ab-1143ff1f0fe0)
Etapa 3: Acesse a aba de contas de serviço
Acesse diretamente:
https://console.cloud.google.com/projectselector2/iam-admin/serviceaccounts

No menu lateral esquerdo, clique em IAM e administrador > Contas de serviço.
![image](https://github.com/user-attachments/assets/9032a1dc-65cc-4358-91ea-4088087081f7)


Etapa 4: Crie a conta de serviço
Clique em “Criar conta de serviço”.

Preencha os campos:

Nome da conta de serviço: use algo descritivo, como conta-servico-projeto.

ID da conta de serviço: será preenchido automaticamente.

Descrição (opcional): exemplo: “Conta para automação via Terraform”.

Clique em “Criar e continuar”.

Etapa 5: Atribua permissões à conta de serviço
Na etapa de permissões, selecione o papel “Proprietário” na aba Básico.

Clique em “Continuar” e depois em “Concluído”.
![image](https://github.com/user-attachments/assets/aba7cd7b-c2f0-492c-82bb-e320a6768706)
Etapa 6: Gere a chave de autenticação
Após criada, clique sobre a conta de serviço listada.

Vá até a aba “Chaves”.

Clique em “Adicionar chave” > “Criar nova chave”.

Escolha o formato JSON e clique em “Criar”.

Salve o arquivo .json em um local seguro — ele será usado para autenticação nos scripts e ferramentas de automação.

Importante: Essa chave permite que sistemas automatizados, como o Terraform ou scripts Python, acessem a infraestrutura do GCP. Não compartilhe esse arquivo com terceiros.
![image](https://github.com/user-attachments/assets/f446b6e9-b69a-4a0e-91b0-940ea5b5c640)
Etapa 7: Conceda permissões específicas na aba IAM
No menu lateral, acesse IAM e administrador > IAM.

Localize a conta de serviço criada e clique em “Conceder acesso”.

Em “Novos principais”, insira o e-mail da conta de serviço.

Adicione o papel “Administrador da API Management”.

Clique em “Salvar”.

Esse papel é necessário para permitir a criação de recursos computacionais por meio de APIs do Google Cloud.
![image](https://github.com/user-attachments/assets/af82d2cd-4a34-4a9a-af50-3c80607876b7)




# TCC
