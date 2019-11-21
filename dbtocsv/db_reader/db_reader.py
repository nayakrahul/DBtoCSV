import MySQLdb


class Database:
    def __init__(self, host, db_name):
        self.host = host
        self.db_name = db_name
        self.cursor = None

    def make_connection(self, username, password):
        db = MySQLdb.connect(self.host, username,
                             password, self.db_name)
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
                            AND TABLE_NAME='{}'".format(self.db_name, table)
        columns = self.query(sql_query)
        columns = list(map(lambda x: x[0], columns))
        return columns

    def fetch_all_rows(self, table, spinner):
        count_query = "SELECT COUNT(*) FROM {}".format(table)
        count = self.query(count_query, first=True)
        i = 0
        spinner.text = "Writing table {} ({}/{})".format(
            table, i, count)
        updated_rows = []
        length = 10000
        start = 0
        while start < count:
            sql_query = "SELECT * FROM {} LIMIT {}, {}".format(
                table, start, length)
            rows = self.query(sql_query)
            for row in rows:
                row = list(map(lambda x: int.from_bytes(
                    x, 'little') if isinstance(x, bytes) else x, row))
                updated_rows.append(row)
                i += 1
                spinner.text = "Writing table {} ({}/{})".format(
                    table, i, count)

            start += length

        return updated_rows

    def query(self, sql_query, first=False):
        if self.cursor is None:
            raise Exception("Connection is not made")
        if sql_query is None:
            raise ValueError("Cannot process null query")
        try:
            self.cursor.execute(sql_query)
            if first:
                return self.cursor.fetchone()[0]
            rows = self.cursor.fetchall()
            return rows
        except:
            return None
