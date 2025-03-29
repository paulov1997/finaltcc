Primeiro, vá ao Google Cloud Console.

Abra o Google Cloud Console: Acesse https://console.cloud.google.com/ no seu navegador.
Inicie sessão: Utilize as informações da sua conta Google para aceder ao Console, se ainda não o fez.
Passo 2: Escolha um projeto ou crie um
Certifique-se de que tem um projeto no GCP antes de criar a conta de serviço.
Escolha um projeto ou comece um novo:
No topo da página, clique no seletor de projetos.
Para iniciar um projeto novo:
Selecione "Novo Projeto."
Dê um nome ao seu projeto e um ID de projeto distinto.
Clique em "Criar".

Etapa 3: vá para contas de serviço.
No menu à esquerda, selecione IAM & Admin.
Clique em contas de serviço no IAM & Admin.

Etapa 4: estabeleça uma nova conta para serviços
Clique no botão "Criar conta de serviço" na página Contas de Serviço.

Preencha as informações da conta de serviço:

Nome da conta de serviço: um nome como "serviço-conta-my-project" ou "my-service-conta" seria descritivo.
ID da conta de serviço: Usando o nome que você fornece, o GCP criará automaticamente um ID especial. Nas APIs do GCP, esse ID será usado para identificar a conta de serviço.
(Opcional) Descrição: Uma descrição opcional (como "Conta de Automação Terraform") para sua conta de serviço.
Clique em "Criar".

Etapa 5: Dê as funções da conta de serviço
Você será solicitado a dar funções à conta de serviço na próxima tela.

Escolha funções: para atribuir a esta conta, você pode escolher em uma lista de funções predefinidas.
Editor: fornece acesso de leitura a gravação a todos os recursos do projeto para a conta de serviço.
Proprietário: fornece autoridade completa sobre todos os recursos do projeto.
Custom: Você pode fazer uma função personalizada que conceda permissões específicas, se necessário.
Clique em continuar depois de escolher uma função que atenda às suas necessidades.

Um exemplo de uma função automatizada é:

Dependendo do grau de acesso que você deseja conceder, você pode selecionar o editor ou a função do visualizador ao criar uma conta de serviço para automação (para Terraform ou scripts, por exemplo).
Dê um passo


# TCC
