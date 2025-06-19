# ✅ **ToDoPy | _Sua lista de tarefas no terminal_**

---

## 📌 **Descrição**

**ToDoPy** é um gerenciador de tarefas simples, escrito em **Python**, que roda direto no terminal.  
Ele salva tudo em um arquivo `tarefas.json`, permitindo que você:

* adicione tarefas com um nome de até 80 caracteres;  
* mova tarefas entre três estados (_a fazer_, _executando_, _pronta_);  
* limite, opcionalmente, a apenas **10** tarefas em “executando”;  
* marque como **Done** ou exclua tarefas definitivamente;  
* visualize a lista com IDs auto-incrementais e status coloridos.

É o jeito mais rápido de organizar seu dia sem sair da linha de comando.

---

## 🚀 **Funcionalidades**

- **CRUD completo de Tarefas:** criar, listar, atualizar (mover) e excluir.  
- **Persistência em JSON:** todos os dados ficam em `tarefas.json`, legível e fácil de versionar no Git.  
- **Sistema de Status:**  
  - `a fazer` → backlog inicial;  
  - `executando` → tarefas em progresso (máx. 10 simultâneas);  
  - `pronta` → concluídas.  
- **Menu interativo:** escolha ações digitando 1, 2, 3, 4 ou 0.  
- **Validações robustas:** evita nomes vazios, IDs inexistentes e status inválidos.  
- **Mensagens com emojis:** feedback claro e divertido para cada operação.

---

## 🛠️ **Tecnologias Utilizadas**

| Ferramenta | Função |
|------------|--------|
| **Python 3** 🐍 | Linguagem principal |
| **json** | Leitura/escrita do arquivo de tarefas |
| **os** | Verificar existência do arquivo |
| **typing** (type hints) | List[dict] para melhor legibilidade |

> *Não há dependências externas além da instalação padrão do Python.*

---

## 💻 **Como Instalar e Executar**

1. **Verifique se tem Python 3:**

```bash
python --version
```

2. **Clone o repositório:**

```bash
git clone https://github.com/GustavoSantosgcs/TodoList.git
```

3. **Entre na pasta do projeto:**

```bash
cd todoList
```

4. **Execute o programa:**

```bash
python to_do.py
```

5. **Pronto!** Use o menu para começar a adicionar tarefas. ✅

---

## 📸 **Exemplo de Uso**

```text
========= Menu =========
1. Adicionar tarefa
2. Mover tarefa
3. Excluir/Done tarefa
4. Listar tarefas
0. Sair
========================
Escolha uma opção: 1
Nome da tarefa (máx. 80 caracteres): Estudar algoritmos
✅  Tarefa adicionada com status 'a fazer'.
```

---

## 🌱 **Melhorias Futuras (Backlog)**

- 🖥️ Interface gráfica com **CustomTkinter**  
- 🔍 Filtro de busca por palavra-chave / status  
- 🗂️ Tags e categorias personalizadas  
- ⏰ Notificações de prazo (deadline)  

---

### ⚠️ **Aviso**

*Este projeto é didático e está em constante evolução.  
Sugestões, pull requests e _issues_ são muito bem-vindos!*
