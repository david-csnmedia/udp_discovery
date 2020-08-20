import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="udp_discovery-dnewmon", # Replace with your own username
    version="0.0.1",
    author="David Newmon",
    author_email="dnewmon@gmail.com",
    description="A simple broadcast UDP discovery module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/david-csnmeda/udp_discovery",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
