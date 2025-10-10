from setuptools import setup, find_packages

setup(
	name="functions",
	version="0.1",
	author="Alex Chertikhin",
	author_email="a.chertikhin0072@mail.ru",
	description="There are function will be use ti complete 6th work.",
	packages=find_packages(),
	install_requires=[],
	entry_points={
		"console_scripts": [
			"function=function.main:main"
		]
	}
)