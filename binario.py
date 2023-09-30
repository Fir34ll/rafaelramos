import pickle
def criar_contato():
    name = input("Nome: ")
    phone_number = input("Número de telefone: ")
    email = input("E-mail: ")
    contato = {
        "name": name,
        "phone_number": phone_number,
        "email": email
    }
    return contato
def salvar_contatos(contatos):
    with open("contatos.bin", "wb") as f:
        pickle.dump(contatos, f)
def main():
    contatos = []
    while True:
        contato = criar_contato()
        contatos.append(contato)
        escolha = input("Deseja continuar? (S/N) ")
        if escolha == "N":
            break
    salvar_contatos(contatos)
if __name__ == "__main__":
    main()
