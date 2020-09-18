from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

with open('LICENSE', 'r') as f:
    license = f.read()

setup(
    name='type_assist',
    version='0.0.1',
    description='Model training and serving for predictive text completion',
    long_description=long_description,
    license=license,
    author='Eric Yates',
    author_email='eric@medleyagency.com',
    url='https://github.com/MedleyLabs/TypeAssist',
    packages=['type_assist'],
)
