from setuptools import find_packages,setup
from typing import List

ramesh = '-e .'

def get_requirements(file_path : str) -> List[str]:
    requirements=[]
    with open(file_path) as file_obj :
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if ramesh in requirements :
            requirements.remove(ramesh)
    return requirements

setup(
    name='Project-1',
    version='0.0.1',
    author='Rishikesh',
    author_email='rishikesh.bhatt24@spit.ac.in',
    packages =find_packages(),
    install_requires =get_requirements('requirements.txt')
    
    
)