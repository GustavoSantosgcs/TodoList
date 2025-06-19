# Atividade To-do list

import json, os

ARQUIVO = "tarefas.json"
tarefas: list[dict] = []
STATUS_VALIDOS = ("a fazer", "executando", "pronta")

#Carregar arquivo com as tarefas se existir ou criar um novo json:
def carregar():
    global tarefas
    if os.path.exists(ARQUIVO):
          try:     
               with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
                    tarefas = json.load(arquivo)
          except (json.JSONDecodeError, IOError):
            print("⚠️  Erro ao ler usuários. Criando arquivo novo.")
    else:
        tarefas = []


def salvar():
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=2)


def proximo_id():
    return max((i["id"] for i in tarefas), default=0) + 1


# ---------- utilidades ----------
def listar():
    if not tarefas:
        print("\n📭  Nenhuma tarefa cadastrada.\n")
        return
    print("\n📋  Tarefas:")
    print("=" * 60)
    for i in tarefas:
        print(f"[{i['id']:03}] {i['name']:<42} → {i['status']}")
    print("-" * 60 + "\n")


def input_nao_vazio(msg: str):
    entrada = input(msg).strip()
    while not entrada:
        entrada = input("Entrada vazia. Tente novamente: ").strip()
    return entrada


def contar_exec():
    return sum(i["status"] == "executando" for i in tarefas)


# ---------- operações ----------
def adicionar():
    while True:
        nome = input_nao_vazio("Nome da tarefa (máx. 80 caracteres): ")
        if len(nome) <= 80:
            break
        print("⚠️  Máximo de 80 caracteres! Digite novamente.\n")

    tarefas.append({"id": proximo_id(), "name": nome, "status": "a fazer"})
    salvar()
    print("✅  Tarefa adicionada com status 'a fazer'.\n")


def mover():
    if not tarefas:
        print("⚠️  Não há tarefas para mover.\n")
        return

    listar()
    try:
        tid = int(input("ID da tarefa a mover: "))
    except ValueError:
        print("⚠️  ID inválido.\n")
        return

    tarefa = next((t for t in tarefas if t["id"] == tid), None)
    if not tarefa:
        print("⚠️  Tarefa não encontrada.\n")
        return

    destino = input("Novo status (a fazer / executando / pronta): ").strip().lower()
    if destino not in STATUS_VALIDOS:
        print("⚠️  Status inválido.\n")
        return

    if destino == "executando" and contar_exec() >= 10:
        print("🚫  Limite de 10 tarefas 'executando' atingido!\n")
        return

    tarefa["status"] = destino
    salvar()
    print(f"🔀  Tarefa [{tid}] movida para '{destino}'.\n")


def done_ou_excluir():
    if not tarefas:
        print("⚠️  Não há tarefas para processar.\n")
        return

    listar()
    try:
        tid = int(input("ID da tarefa: "))
    except ValueError:
        print("⚠️  ID inválido.\n")
        return

    idx = next((i for i, t in enumerate(tarefas) if t["id"] == tid), None)
    if idx is None:
        print("⚠️  Tarefa não encontrada.\n")
        return

    escolha = input("Digite D para marcar como Done (pronta) ou E para Excluir: ").strip().upper()
    if escolha == "D":
        tarefas[idx]["status"] = "pronta"
        salvar()
        print(f"✅  Tarefa [{tid}] marcada como 'pronta'.\n")
    elif escolha == "E":
        tarefas.pop(idx)
        salvar()
        print(f"🗑️  Tarefa [{tid}] excluída.\n")
    else:
        print("⚠️  Opção cancelada.\n")


# ---------- programa principal ----------
def main():
    carregar()

    menu = """
========= Menu =========
1. Adicionar tarefa
2. Mover tarefa
3. Excluir/Done tarefa
4. Listar tarefas
0. Sair
========================
"""
    while True:
        print(menu)
        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1":
                adicionar()
            case "2":
                mover()
            case "3":
                done_ou_excluir()
            case "4":
                listar()
            case "0":
                print("👋  Até mais!")
                break
            case _:
                print("Opção inválida.\n")


if __name__ == "__main__":
    main()
