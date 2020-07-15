from halo import Halo
import getpass

from .db_reader import Database
from .csv_writer import CSV

spinner = Halo(spinner='arrow3')


class Dbtocsv:
    def __init__(self, host, db_name):
        """
        Parameters
        ----------
        host : str, required
            database hostname.
        db_name : str, required
            name of the database.
        """
        self.db = Database(host, db_name)

    def authenticate():
        username = raw_input("username : ")
        try:
            self.db.make_connection(username, getpass.getpass(prompt="password : "))
        except:
            raise Exception("Error while making database connection.")

    def write_to_csv(self, only_tables=[], exclude_tables=[]):
        """
        Parameters
        ----------
        only_tables : list(str), optional
            fetch for only these tables.
        exclude_tables : list(str), optional
            exclude these tables.
        """
        try:
            if len(only_tables) > 0:
                tables = only_tables
            else:
                tables = self.db.fetch_tables()
        except:
            raise Exception("Error while fetching tables.")
        tables = list(set(tables) - set(exclude_tables))

        for table in tables:
            spinner.text = "Writing table {}".format(table)
            spinner.start()
            try:
                columns = self.db.fetch_columns(table)
                rows = self.db.fetch_all_rows(table, spinner)
            except:
                raise Exception(
                    "Error while fetching data from tables.")
                spinner.fail(
                    "Writing to table {} failed".format(table))
                continue
            try:
                csv = CSV(file='{}.csv'.format(table))
                csv.write(rows, columns)
                spinner.succeed("Wrote table {}".format(table))
            except:
                raise Exception(
                    "Error while writing data to csv file.")
                spinner.fail(
                    "Writing to table {} failed".format(table))
