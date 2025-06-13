from setuptools import setup, find_packages

setup(
    name="lexgen",
    version="0.1.0",
    packages=find_packages(),
    entry_points={"console_scripts": ["lexgen=lexgen.cli:main"]},
    install_requires=[],
)
