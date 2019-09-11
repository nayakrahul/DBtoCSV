# DBtoCSV
write data from database into csv file

### Install
```bash
$ pip install dbtocsv
```

### Usage
```python
from dbtocsv import Dbtocsv
dbtocsv = Dbtocsv(host='', username='', password='', db_name='')
dbtocsv.write_to_csv()
```
