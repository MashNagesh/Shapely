import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ShapelyValues", 
    version="0.0.1",
    author="Mahalakshmi Nageswaran",
    author_email="mashrajiv@gmail.com",
    description="Implementation of the Shapely Owen decomposition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MashNagesh/Shapely",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)