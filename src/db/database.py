import sys
sys.dont_write_bytecode = True

import sqlite3

class TokenManager:
    def __init__(self, db_name='database.db'):
        self.db_name = db_name
        self._criar_tabela()

    def _criar_tabela(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tokens (
                    name TEXT PRIMARY KEY,
                    access_token TEXT,
                    validade TEXT
                )
            ''')
            conn.commit()

    def obter_token(self, name):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT access_token FROM tokens WHERE name = ?", (name,))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None

    def atualizar_token(self, name, novo_token):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO tokens (name, access_token) 
                VALUES (?, ?)
                ON CONFLICT(name) DO UPDATE SET access_token = excluded.access_token
            ''', (name, novo_token))
            conn.commit()

    def obter_validade(self, name):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT validade FROM tokens WHERE name = ?", (name,))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None
        
    def atualizar_validade(self, name, nova_validade):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE tokens
                SET validade = ?
                WHERE name = ?
            ''', (nova_validade, name))
            conn.commit()