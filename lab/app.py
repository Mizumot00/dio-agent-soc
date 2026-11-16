"""
Laboratório de Teste - DIO Agent (Cibersegurança & AppSec)
Arquivo: app.py
Descrição: Demonstração de uma aplicação com vulnerabilidade crítica de SQL Injection (SQLi)
ATENÇÃO: Código intencionalmente vulnerável para fins estritamente educacionais em laboratório.
"""

import sqlite3

def init_db():
    """Inicializa o banco de dados em memória para simulação."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    # Cria tabela de usuários
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT,
            is_admin INTEGER DEFAULT 0
        )
    """)
    # Insere dados de teste
    cursor.execute("INSERT INTO users (username, password, email, is_admin) VALUES ('admin', 'Sup3rS3cr3tP@ss', 'admin@empresa.com', 1)")
    cursor.execute("INSERT INTO users (username, password, email, is_admin) VALUES ('joao_silva', 'senha123', 'joao@empresa.com', 0)")
    cursor.execute("INSERT INTO users (username, password, email, is_admin) VALUES ('maria_dev', 'm@ri@2026', 'maria@empresa.com', 0)")
    conn.commit()
    return conn

def login_vulneravel(conn, username, password):
    """
    Função de autenticação VULNERÁVEL.
    FALHA: Concatenação direta de strings na query SQL (SQL Injection).
    """
    cursor = conn.cursor()
    # VULNERABILIDADE CRÍTICA AQUI:
    # A entrada do usuário é concatenada diretamente na query SQL sem sanitização ou parametrização.
    query = f"SELECT id, username, email, is_admin FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"[DEBUG SQL Executada]: {query}")
    
    cursor.execute(query)
    user = cursor.fetchone()
    return user

if __name__ == "__main__":
    db = init_db()
    print("=== Laboratório de Autenticação (Versão Vulnerável) ===")
    
    # 1. Tentativa de login legítimo
    print("\n[Teste 1] Tentativa de login legítimo com 'joao_silva':")
    resultado = login_vulneravel(db, "joao_silva", "senha123")
    if resultado:
        print(f"-> Login bem-sucedido! Usuário logado: {resultado[1]} (Admin: {resultado[3]})")
    else:
        print("-> Falha no login!")

    # 2. Tentativa de exploração com SQL Injection (Bypass de autenticação)
    # Payload clássico: admin' --
    print("\n[Teste 2] Simulação de exploração com payload SQL Injection (admin' --):")
    payload_user = "admin' --"
    payload_pass = "qualquer_senha"
    resultado_ataque = login_vulneravel(db, payload_user, payload_pass)
    if resultado_ataque:
        print(f"-> ALERTA DE SEGURANÇA: Login burlado com sucesso como: {resultado_ataque[1]} (Admin: {resultado_ataque[3]})!")
    else:
        print("-> Autenticação rejeitada.")
