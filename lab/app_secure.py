"""
Laboratório de Teste - DIO Agent (Cibersegurança & AppSec)
Arquivo: app_secure.py
Descrição: Versão corrigida e mitigada com Consultas Parametrizadas (Prepared Statements)
"""

import sqlite3

def init_db():
    """Inicializa o banco de dados em memória para simulação."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT,
            is_admin INTEGER DEFAULT 0
        )
    """)
    cursor.execute("INSERT INTO users (username, password, email, is_admin) VALUES ('admin', 'Sup3rS3cr3tP@ss', 'admin@empresa.com', 1)")
    cursor.execute("INSERT INTO users (username, password, email, is_admin) VALUES ('joao_silva', 'senha123', 'joao@empresa.com', 0)")
    cursor.execute("INSERT INTO users (username, password, email, is_admin) VALUES ('maria_dev', 'm@ri@2026', 'maria@empresa.com', 0)")
    conn.commit()
    return conn

def login_seguro(conn, username, password):
    """
    Função de autenticação SEGURA.
    MITIGAÇÃO: Uso de Prepared Statements / Consultas Parametrizadas.
    O motor do banco de dados trata a entrada do usuário estritamente como DADO, nunca como CÓDIGO executável.
    """
    cursor = conn.cursor()
    # QUERY PARAMETRIZADA:
    # Os placeholders '?' separam a instrução SQL dos valores inseridos pelo usuário.
    query = "SELECT id, username, email, is_admin FROM users WHERE username = ? AND password = ?"
    print(f"[DEBUG SQL Parametrizada]: {query} | Parâmetros: ('{username}', '{password}')")
    
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    return user

if __name__ == "__main__":
    db = init_db()
    print("=== Laboratório de Autenticação (Versão Segura Mitigada) ===")
    
    # 1. Tentativa de login legítimo
    print("\n[Teste 1] Tentativa de login legítimo com 'joao_silva':")
    resultado = login_seguro(db, "joao_silva", "senha123")
    if resultado:
        print(f"-> Login bem-sucedido! Usuário logado: {resultado[1]} (Admin: {resultado[3]})")
    else:
        print("-> Falha no login!")

    # 2. Tentativa de exploração com o mesmo payload SQL Injection
    print("\n[Teste 2] Simulação do mesmo ataque com payload SQL Injection (admin' --):")
    payload_user = "admin' --"
    payload_pass = "qualquer_senha"
    resultado_ataque = login_seguro(db, payload_user, payload_pass)
    if resultado_ataque:
        print(f"-> ALERTA: Login burlado como: {resultado_ataque[1]}!")
    else:
        print("-> SUCESSO DEFENSIVO: Tentativa de injeção neutralizada! Autenticação rejeitada.")
