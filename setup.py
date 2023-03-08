from setuptools import setup, find_packages
from typing import List

DONT_EXECUTE_E = '-e .'


def get_requirements(file_path: str) -> List[str]:
    '''this fuction will return the list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "")for req in requirements]

        if DONT_EXECUTE_E in requirements:
            requirements.remove(DONT_EXECUTE_E)
    return requirements


setup(
    name='mini ml project',
    version='1.0.0',
    author='Lalith',
    author_email='thomalalalithsai@gmail.com',
    description='A mini Python ML project',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
