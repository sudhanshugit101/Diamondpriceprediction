from setuptools import setup, find_packages
from typing import List

HYPHENEDOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
        requirements.remove(HYPHENEDOT)
    return requirements



setup(
    name='Diamond_price_prediction',
    version='0.1',
    author='Sudhanshu',
    author_email='sudhanshu.vishnu73@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages(),
)
