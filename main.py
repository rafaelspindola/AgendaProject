from entities.Usuario import Usuario


def main():
    Usuario()


if __name__ == "__main__":
    main()


# Função responsável pelo menu, que roda em loop de acordo com o input inserido e executando as funções correspondentes
stop = False
while not stop:
    menu = input('''
  "Seja bem-vindo ao projeto de agenda de contatos em python, digite o número da operação desejada: \n
  1. Cadastrar novo contato 
  2. Cadastrar vários contatos 
  3. Buscar contato  
  4. Remover contato 
  5. Atualizar dados de contato  
  6. Gerar relatório de pessoas cadastradas 
  7. Salvar contatos  
  8. Sair \n
  ''')
    if "1" in menu:
        Usuario.cadastrar_usuario()
    if "2" in menu:
        Usuario.cadastrar_varios_usuarios()
    if "3" in menu:
        Usuario.buscar_usuario()
    if "4" in menu:
        Usuario.deletar_usuario()
    if "5" in menu:
        Usuario.atualizar_usuario()
    if "6" in menu:
        Usuario.gerar_relatorio()
    if "7" in menu:
        Usuario.salvar_contatos("contatos.csv")
    if "8" in menu:
        Usuario.sair()
        break
