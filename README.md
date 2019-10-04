# NBackend
Stands for Node-Backend.
The scaffolding tool to automatically create the node project modules with the standard followed in node-starter-kit distributed under pluginfactory.
The repository has missing description for now as this project is under development. You can watch this repository to keep yourself sync with the upcoming
changes and development.

## Setup
### Distributing a setuptools based project
Before you begin, make sure you have the latest versions of setuptools and wheel:
```
python3 -m pip install --user --upgrade setuptools wheel
```
To build a setuptools project, run this command from the same directory where setup.py is located:
```
python3 setup.py sdist bdist_wheel
```
This will generate distribution archives in the dist directory.

Before you upload the generated archives make sure you’re registered on https://test.pypi.org/account/register/. You will also need to verify your email to be able to upload any packages. You should install twine to be able to upload packages:
```
python3 -m pip install --user --upgrade setuptools wheel
```
Now, to upload these archives, run:
```
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
To install your newly uploaded package `nbackend-pluginfactory`, you can use pip:
```
python3 -m pip install --index-url https://upload.pypi.org/simple/ nbackend-pluginfactory
```