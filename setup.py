from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return a list of requirements from the given file.
    """
    requirements = []
    try:
        with open(file_path, 'r') as file_obj:
            requirements = file_obj.readlines()
            # Clean up any extraneous whitespace/newline characters
            requirements = [req.strip() for req in requirements]
            
            # Remove the development mode package if it exists
            if hyphen_e_dot in requirements:
                requirements.remove(hyphen_e_dot)
    except FileNotFoundError:
        print(f"Warning: The requirements file {file_path} was not found.")
    except IOError as e:
        print(f"Error reading {file_path}: {e}")
    
    return requirements

setup(
    name="laptop-price-prediction",
    version="0.0.1",
    author='Prashant J',
    author_email='p@p.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)