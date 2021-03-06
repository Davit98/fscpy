from setuptools import setup

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
	name='fscpy',
	version='0.1.0',    
	description='Python package for Field State Classification',
	url='https://github.com/Davit98/fscpy',
	author='Davit Martirosyan',
	author_email='dvmartirosyan@gmail.com',
	license='BSD 2-clause',
	packages=['fscpy'],
	install_requires=requirements
)
