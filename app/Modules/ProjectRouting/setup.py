from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="ProjectRouting",
    version="1.0.0",
    author="Chris Oberdalhoff",
    author_email="n/a",
    description="Perform operations on network prefix-list",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="n/a",
    packages=find_packages(),
    install_requires=("ipaddress", "sqlite3", "collections", "netmiko", "time", "os", "openpyxl"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
