# DBtoCSV
write data from database into csv file

### Install
```bash
$ pip install dbtocsv
```

### Usage
```python
from dbtocsv import Dbtocsv
dbtocsv = Dbtocsv(host='', db_name='')
dbtocsv.authenticate()
dbtocsv.write_to_csv()
```
