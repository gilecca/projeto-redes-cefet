import socket
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

token_store = {}

def criptografar_mensagem(mensagem):

    mensagem_criptografada = cipher_suite.encrypt(mensagem.encode())
    token = cipher_suite.encrypt(b"token")
    token_store[token] = mensagem_criptografada
    return token

def descriptografar_mensagem(token):
    if token in token_store:
        mensagem_criptografada = token_store[token]
        mensagem_descriptografada = cipher_suite.decrypt(mensagem_criptografada).decode()
        return mensagem_descriptografada
    return None

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(5)
    print("Servidor aguardando conexões...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Conexão estabelecida com {addr}")
        try:
            data = client_socket.recv(1024).decode()
            if data:
                print(f"Mensagem recebida: {data}")
                if data.startswith("ENCRYPT:"):
                    mensagem = data.split("ENCRYPT:")[1].strip()
                    token = criptografar_mensagem(mensagem)
                    client_socket.send(token)
                elif data.startswith("DECRYPT:"):
                    token = data.split("DECRYPT:")[1].encode()
                    mensagem_descriptografada = descriptografar_mensagem(token)
                    if mensagem_descriptografada:
                        client_socket.send(mensagem_descriptografada.strip().encode())
                    else:
                        client_socket.send(b"Token invalido")
            else:
                    client_socket.send(b"Comando invalido")
        except Exception as e:
            print(f"Erro ao processar a mensagem: {e}")
            client_socket.send(b"Erro interno no servidor")  # Envia bytes
        finally:
            client_socket.close()

if __name__ == "__main__":
    start_server()