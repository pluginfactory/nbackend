import setuptools

# open the readme file for description of plugin
with open("README.md", "r") as fileHead:
	description = fileHead.read()

setuptools.setup(
	name="nbackend-pluginfactory",
	version="0.0.1",
	scripts=["nbackend"],
	author="gaurav sharma",
	author_email="sharma02gaurav@gmail.com",
	description="A node backend scaffolder based on node-starter-kit",
	long_description=description,
	long_description_content_type="text/markdown",
	url="https://github.com/pluginfactory/nbackend",
	packages=setuptools.find_packages(),
	classifiers=[
		
	],
)