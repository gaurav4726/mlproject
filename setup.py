from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'    # -e . helps to run setup.py file , need to add at the end of requirments.txt.
def get_requirements(file_path:str)->List[str]: # All package will convert into list
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() # Read one by one all pacakage
        requirements=[req.replace("\n","") for req in requirements] # After each package /n will come will need to replace by ""

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)  # "-e . added in requirements.txt which should not run as pacakage and need to remove from build"
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Gaurav',
author_email='gaurav4726@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt') # Here we can give package name also but package can be many , so best practice to define functions

)