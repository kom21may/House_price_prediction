from setuptools import find_packages,setup


from typing import List

HYPEN_E_DT=OT='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
    if HYPEN_E_DT in requirements:
        requirements.remove(HYPEN_E_DT)
    return requirements
setup(name='Regressor project',
      version='0.0.1',
      author='komal',
      author_email='komalkumari199905@gmail.com',
      install_requires=get_requirements('requirements.txt'),
      packages=find_packages()
      
      )