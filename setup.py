from setuptools import find_packages,setup
from typing import List
#consider as meta data of the project
#whenever this package findpackges() is running it will see 
#in how many file __init__.py is present it will consider src folder as packages 
#it will try to build src folder as package

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
   '''this function will return the list of requirements
   '''

   requirements=[]
   with open (file_path) as file_obj:
      requirements=file_obj.readlines()
      requirements=[req.replace("\n","")for req in requirements]
      if HYPEN_E_DOT in requirements:
         requirements.remove(HYPEN_E_DOT)

   return requirements   
          
setup(
   names= 'mlproject',
   version='0.0.1',
   author='Basant',
   author_email='btirkey1208@gmail.com',
   packages=find_packages(),
   #install_requires=['pandas','numpy','seaborn'] #do this when we require small packages 
   install_requires=get_requirements('requirements.txt')#it will help to diffrent packages 
)
#-e. is used to trigger the setup.py when requirements.txtx is used 