from setuptools import setup, find_packages

setup(
    name='EdApiConnector',
    version='v0.0.1',
    packages=find_packages(),
    package_dir={'': 'src/EDApiConnector'},
    url='https://github.com/preinboth/EdApiConnector',
    license='MIT',
    author='preinboth',
    author_email='',
    description='Elite Dangerous Api Connector',
    install_requires=['requests']
)
