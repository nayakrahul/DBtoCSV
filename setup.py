from setuptools import setup, find_packages
from os import path
import io

current_path = path.abspath(path.dirname(__file__))

with open(path.join(current_path, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

with io.open("README.md", encoding='utf-8') as infile:
    long_description = infile.read()

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '')
                    for x in all_reqs
                    if x.startswith('git+')]

setup(
     name='dbtocsv',
     version='0.1.5',
     description="Python Script to put data from MySQL database into csv files",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/nayakrahul/DBtoCSV",
     keywords='mysql database csv',
     packages=find_packages(),
     include_package_data=True,
     author='Rahul Nayak',
     install_requires=install_requires,
     dependency_links=dependency_links,
     author_email='rahulnk521@gmail.com',
 )
