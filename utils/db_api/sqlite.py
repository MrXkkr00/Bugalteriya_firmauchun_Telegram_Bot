import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            nomer varchar(255) NOT NULL,
            sorov varchar(255) NOT NULL,
            bugalter varchar(255),
            jarayon varchar(255),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, nomer: str, sorov: str, bugalter: str = None, jarayon: str = None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, Name, nomer,  sorov, bugalter, jarayon) VALUES(?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, nomer, sorov, bugalter, jarayon), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_nomer(self, nomer, id):

        sql = f"""
        UPDATE Users SET nomer=? WHERE id=?
        """
        return self.execute(sql, parameters=(nomer, id), commit=True)

    def update_user_sorov(self, sorov, id):

        sql = f"""
        UPDATE Users SET sorov=? WHERE id=?
        """
        return self.execute(sql, parameters=(sorov, id), commit=True)

    def update_user_bugalter(self, bugalter, id):

        sql = f"""
        UPDATE Users SET bugalter=? WHERE id=?
        """
        return self.execute(sql, parameters=(bugalter, id), commit=True)

    def update_user_jarayon(self, jarayon, id):

        sql = f"""
        UPDATE Users SET jarayon=? WHERE id=?
        """
        return self.execute(sql, parameters=(jarayon, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
