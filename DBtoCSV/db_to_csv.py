from db_reader import Database
from csv_writer import CSV

host = ""
username = ""
password = ""
db = ""

db = Database(host, username, password, db)
db.make_conection()

tables = db.fetch_tables()

for table in tables:
    columns = db.fetch_columns(table)
    rows = db.fetch_all_rows(table)
    csv = CSV(file='{}.csv'.format(table))
    csv.write(rows, columns)
