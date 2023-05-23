import csv

class Usuario:
    # Inicializa o dicionário, que pode ser usado em qualquer função da classe
    data_dict = {}

    # Função que inicializa as propriedades de objetos que serão instanciados
    def __init__(self):
        self.name = None
        self.phone = None
        self.email = None
        self.twitter = None
        self.instagram = None

    # Função responsável por receber os dados de cadastro, salvá-los no dicionário e instanciar o objeto do contato
    @classmethod
    def cadastrar_usuario(cls):
        name = input("\n Digite o nome do contato: ")
        phone = input("Digite o telefone do contato: ")
        email = input("Digite o e-mail do contato: ")
        twitter = input("Digite o nome de usuário do twitter: ")
        instagram = input("Digite o nome de usuário do instagram: ")
        print("Contato cadastrado com sucesso! \n")

        user_data = {
            "name": name,
            "phone": phone,
            "email": email,
            "twitter": twitter,
            "instagram": instagram,
        }

        cls.data_dict[name] = user_data

    # Função responsável por cadastrar vários contatos, baseado no número inserido no terminal
    @classmethod
    def cadastrar_varios_usuarios(cls):
        numero_usuarios = int(input("Digite quantos contatos gostaria de adicionar: "))
        for _ in range(numero_usuarios):
            usuario = cls()
            usuario.cadastrar_usuario()

    # Função responsável por buscar todos os dados do contato baseado no nome inserido no terminal
    @classmethod
    def buscar_usuario(cls):
        name = input("\n Digite o nome do contato: ")
        if name in cls.data_dict:
            user_data = cls.data_dict[name]
            print("\n Name: ", user_data["name"])
            print("Phone: ", user_data["phone"])
            print("Email: ", user_data["email"])
            print("Twitter: ", user_data["twitter"])
            print("Instagram: ", user_data["instagram"], "\n")
        else:
            return print("\n Contato não encontrado. \n")

    # Função responsável por deletar todos os dados de um contato baseado no nome inserido no terminal
    @classmethod
    def deletar_usuario(cls):
        name = input("\n Digite o nome do contato a ser deletado: ")
        if name in cls.data_dict:
            del cls.data_dict[name]
            print("\n Contato deletado com sucesso! \n")
        else:
            print("\n Contato não encontrado. \n")

    # Função responsável por atualizar dos dados de um contato baseado no nome inserido no termimal
    @classmethod
    def atualizar_usuario(cls):
        name = input("\n Digite o nome do contato a ser atualizado: ")
        if name in cls.data_dict:
            user_data = cls.data_dict[name]
            user_data["name"] = input("Digite o nome atualizado do contato: ")
            user_data["phone"] = input("Digite o telefone atualizado do contato: ")
            user_data["email"] = input("Digite o e-mail atualizado do contato: ")
            user_data["twitter"] = input("Digite o twitter atualizado do contato: ")
            user_data["instagram"] = input("Digite o instagram atualizado do contato: ")
            print("\n Contato atualizado com sucesso! \n")
        else:
            print("\n Contato não encontrado. \n")

    # Função responsável por gerar um relatório dos contatos cadastrados
    @classmethod
    def gerar_relatorio(cls):
        if not cls.data_dict:
            print("\n Nenhum contato cadastrado. \n")
        else:
            print("\n Relatório de Contatos: \n \n")
            print("Nro\tNome\tTelefone\tE-mail\t\t\t\t\tTwitter\t\tInstagram")
            for i, user_data in enumerate(cls.data_dict.values(), 1):
                name = user_data["name"]
                phone = user_data["phone"]
                email = user_data["email"]
                twitter = user_data["twitter"]
                instagram = user_data["instagram"]
                print(f"{i}\t{name}\t{phone}\t{email}\t{twitter}\t{instagram}")

    # Função responsável por salvar contatos em arquivo
    @classmethod
    def salvar_contatos(cls, nome_arquivo):
        if not cls.data_dict:
            print("Nenhum contato cadastrado. ")
        else:
            with open(nome_arquivo, 'w', newline='') as arquivo:
                writer = csv.writer(arquivo)
                writer.writerow(["Nome", "Telefone", "Email", "Twitter", "Instagram"])
                for user_data in cls.data_dict.values():
                    writer.writerow([
                        user_data["name"],
                        user_data["phone"],
                        user_data["email"],
                        user_data["twitter"],
                        user_data["instagram"]
                    ])
            print("Contatos salvos com sucesso! ")

    # Função responsável por terminar o while loop do menu
    @classmethod
    def sair(cls):
        print("\n Obrigado por utilizar nossos serviços!")