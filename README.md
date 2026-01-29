# Gerenciador de tarefas (Task Manager)

## Objetivo
Este projeto marca minha transição de scripts isolados (como calculadoras e exercícios simples) para o desenvolvimento de **sistemas integrados com banco de dados**. O foco aqui é resolver o problema real de persistência de dados e relacionamento entre entidades (Usuários e Tarefas).

## O que este projeto resolve?
Diferente de projetos básicos, este sistema foca em:
- **Persistência Real:** Os dados não se perdem ao fechar o programa.
- **Relacionamento (SQL):** Implementação de chaves estrangeiras para ligar tarefas a usuários específicos.
- **Escalabilidade:** Estrutura preparada para crescer e receber novas funcionalidades.

## Tecnologias Utilizadas
- **Python 3**
- **SQLite3**

## Estrutura do Banco de Dados
O sistema utiliza duas tabelas principais:
1.  **Usuários**: Armazena `nome` e `email`.
2.  **Tarefas**: Armazena `titulo`, `status` e a referência ao usuário dono da tarefa.

## Evolução Contínua (Roadmap)
Este projeto está em desenvolvimento constante. Minha meta é aplicar melhorias incrementais conforme avanço nos estudos:
- [x] Criar estrutura básica do banco de dados.
- [ ] Implementar CRUD de usuários e tarefas.
- [ ] Adicionar tratamento de erros e gerenciamento de contexto (Context Managers).
- [ ] Aplicar Clean Code e padrões de projeto (Repository Pattern).

## Como rodar o projeto
1. Certifique-se de ter o Python instalado.
2. Clone o repositório:
   ```bash
   git clone [https://github.com/Andreyn873-ux/Gerenciador_de_Tarefas.git]
4. Execute o arquivo que inicializa o banco:
   ```bash
   main.py
