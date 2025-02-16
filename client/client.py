import socket

def enviar_mensagem(mensagem):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('server', 12345)) 
        client_socket.send(mensagem.encode())
        response = client_socket.recv(1024).decode()
        client_socket.close()
        return response
    except:
        return "Erro ao decodificar mensagem"

def main():
    print("Cliente iniciado. Conectando ao servidor...")

    while True:
        print("\nEscolha uma opção:")
        print("1. Criptografar mensagem")
        print("2. Descriptografar mensagem")
        print("3. Sair")
        escolha = input("Digite o número da opção: ")

        if escolha == "1":
            mensagem = input("Digite a mensagem para criptografar: ")
            response = enviar_mensagem(f"ENCRYPT:{mensagem}")
            print(f"Token recebido: {response}")

        elif escolha == "2":
            token = input("Digite o token para descriptografar: ")
            response = enviar_mensagem(f"DECRYPT:{token}")
            print(f"Mensagem descriptografada: {response}")

        elif escolha == "3":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()