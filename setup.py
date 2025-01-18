from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(filepath: str) -> List[str]:
    '''
    This function will return the list of required packages
    '''

    requirements = []
    with open(filepath) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Ritayan',
    author_email='ritayanpatra98@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)