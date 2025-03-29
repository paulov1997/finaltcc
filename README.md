Abra o Google Cloud Console: Acesse https://console.cloud.google.com/ no seu navegador.

Inicie sessão: Utilize as informações da sua conta Googl

Passo 2: Escolha um projeto ou crie um caso não tenha. 

![image](https://github.com/user-attachments/assets/aab10bc9-b8d9-41d4-b1ab-1143ff1f0fe0)

Caso não tenha selecione "Novo Projeto."
Dê um nome ao seu projeto e um ID de projeto distinto.
Clique em "Criar".

Etapa 3: Vá  para aba contas de serviço. https://console.cloud.google.com/projectselector2/iam-admin/serviceaccounts?authuser=2&invt=AbtVEg&supportedpurview=project&allowsmanagementprojects=true
No menu à esquerda, selecione IAM & Admin.
Clique em contas de serviço no IAM & Admin.
![image](https://github.com/user-attachments/assets/9032a1dc-65cc-4358-91ea-4088087081f7)


Etapa 4: Clique no botão "Criar conta de serviço" na página Contas de Serviço.

Preencha as informações da conta de serviço:

Nome da conta de serviço: um nome como "serviço-conta-my-project" ou "my-service-conta" seria descritivo.
ID da conta de serviço: Usando o nome que você fornece, o GCP criará automaticamente um ID especial. Nas APIs do GCP, esse ID será usado para identificar a conta de serviço.
(Opcional) Descrição: Uma descrição opcional (como "Conta de Automação Terraform") para sua conta de serviço.
Clique em "Criar".

Etapa 5: Dê as funções da conta de serviço
Primeiro na aba Basico e selecione o Papel de propietario (print abaixo)

![image](https://github.com/user-attachments/assets/9c21a2aa-0b90-49f4-bd2a-13852f41c5b1)

Clique em Continuar e depois concluir.


Etapa 6: Após criação da conta de serviço vocé irá clicar sobre ela e selecionar a opção chaves
Dentro da aba Chaves você irá clicar em "Adicionar chave"  selecionar a opção JSON e salvar num local de sua segurança
OBS : Essa chave e oque dara permissão ao codigo criar recursos na Nuvem de Dados.
![image](https://github.com/user-attachments/assets/aba7cd7b-c2f0-492c-82bb-e320a6768706)


Etapa 7:
Após isso vamos na ABA IAM, clicar na chave que acabou de criar 
![image](https://github.com/user-attachments/assets/f446b6e9-b69a-4a0e-91b0-940ea5b5c640)

Voce irá clicar em conceder acesso e irá adicionar em novos princiapis a chave que vc criou  o papel a sua conta Administrador da API Management (Esse papel e responsavel por liberar a criação de recursos computacionais via API) depois disso clique em salvar.
![image](https://github.com/user-attachments/assets/af82d2cd-4a34-4a9a-af50-3c80607876b7)




# TCC
