import MySQLdb


class Database:
    def __init__(self, host, username, password, db):
        self.host = host
        self.username = username
        self.password = password
        self.db = db
        self.cursor = None

    def make_conection(self):
        db = MySQLdb.connect(self.host, self.username, self.password, self.db)
        self.cursor = db.cursor()

    def fetch_tables(self):
        sql_query = "SHOW TABLES"
        tables = self.query(sql_query)
        tables = list(map(lambda x: x[0], tables))
        return tables

    def fetch_columns(self, table):
        sql_query = "SELECT COLUMN_NAME \
                        FROM INFORMATION_SCHEMA.COLUMNS \
                        WHERE TABLE_SCHEMA='{}' \
                            AND TABLE_NAME='{}'".format(self.db, table)
        columns = self.query(sql_query)
        columns = list(map(lambda x: x[0], columns))
        return columns

    def fetch_all_rows(self, table):
        sql_query = "SELECT * FROM {}".format(table)
        rows = self.query(sql_query)
        updated_rows = []
        for row in rows:
            row = list(map(lambda x: int.from_bytes(x, 'little') if isinstance(x, bytes) else x, row))
            updated_rows.append(row)
        return updated_rows

    def query(self, sql_query):
        if self.cursor is None:
            raise Exception("Connection is not made")
        if sql_query is None:
            raise ValueError("Cannot process null query")
        try:
            self.cursor.execute(sql_query)
            rows = self.cursor.fetchall()
            return rows
        except:
            return None
