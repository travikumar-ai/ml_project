from setuptools import find_packages, setup


HYPEN_e = '-e .'
def get_rewuirements(file_name):
    
    with open(file_name, 'r') as f:
        
        packages = [ line.strip().replace('\n', '') for line in f.readlines() if HYPEN_e not in line ]
    return packages

setup(
    name='ML Project',
    version="0.0.1",
    author="T Ravi Kumar",
    maintainer="T Ravi Kumar",
    maintainer_email='thotakuriravi@gmail.com',
    packages=find_packages(),
    install_requires=get_rewuirements('requirements.txt')
)