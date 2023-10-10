import hashlib
import re

class Usuario:
    def __init__(self, nome, senha, role = "usuario normal"):
        if self.nome_valido(nome):
            self.nome = nome
        else:
            raise ValueError("Nome de usuário contém caracteres especiais.")
        
        self.senha_hash = self.hash_senha(senha)
        self.role = role

    def hash_senha(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()
    
    def nome_valido(self, nome):
        return re.match("^[a-zA-Z0-9_]+$", nome) is not None
    
    def __str__(self):
        return f"Nome: {self.nome}\nRole: {self.role}"

# Lista de usuários com diferentes níveis de acesso
usuarios = [
    Usuario("Pedro", "Para_de_ser_burro"),
    Usuario("Joao", "cheio_de_ideia_errada"),
    Usuario("Thiago", "vive_de_forro", "boss"),
    Usuario("Israel", "vive_tranquilo", "administrador"),
    Usuario("Bruno", "Topus_Embraer")
]
    
# Verificação de login
def fazer_login(nome_usuario, senha_digitada):
    for usuario in usuarios:
        if usuario.nome == nome_usuario:
            senha_digitada_hash = usuario.hash_senha(senha_digitada)
            if senha_digitada_hash == usuario.senha_hash:
                print(f"{usuario.nome} fez login com sucesso como {usuario.role}.")
                return
    print("Nome de usuario ou senha incorretos. Tente novamente.")

# Exemplo de uso da função de login

if __name__ == "__main__":
    fazer_login("Joao", "cheio_de_ideia_errada")
    fazer_login("Pedro", "muito_inteligente")
    fazer_login("Thiago", "vive_de_forro")
    fazer_login("Israel", "nao_vive_tranks")
    fazer_login("Bruno", "Topus_Embraer")
