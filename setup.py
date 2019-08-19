from setuptools import setup
from os import path

current_path = path.abspath(path.dirname(__file__))

with open(path.join(current_path, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '')
                    for x in all_reqs
                    if x.startswith('git+')]

setup(
     name='dbtocsv',
     version='0.1',
     description="Python Script to put data from MySQL database into csv files",
     url="https://github.com/nayakrahul/DBtoCSV",
     keywords='mysql database csv',
     include_package_data=True,
     author='Rahul Nayak',
     install_requires=install_requires,
     dependency_links=dependency_links,
     author_email='rahulnk521@gmail.com',
 )
