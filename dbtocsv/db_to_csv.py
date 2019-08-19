from .db_reader import Database
from .csv_writer import CSV


class DBtoCSV:
    def __init__(self, host, username, password, db_name):
        """
        Parameters
        ----------
        host : str, required
            database hostname.
        username : str, required
            username to access database.
        password : str, required
            password to access database.
        db_name : str, required
            name of the database.
        """
        self.host = host
        self.username = username
        self.password = password
        self.db_name = db_name
        self.db = Database(host, username, password, db_name)
        try:
            self.db.make_conection()
        except:
            raise Exception("Error while making database connection.")

    def write_to_csv(self):
        try:
            tables = self.db.fetch_tables()
        except:
            raise Exception("Error while fetching tables.")

        for table in tables:
            try:
                columns = self.db.fetch_columns(table)
                rows = self.db.fetch_all_rows(table)
            except:
                raise Exception("Error while fetching data from tables.")
            try:
                csv = CSV(file='{}.csv'.format(table))
                csv.write(rows, columns)
            except:
                raise Exception("Error while writing data to csv file.")
