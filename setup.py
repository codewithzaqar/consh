from setuptools import setup, find_packages

setup(
    name="consh",
    version="0.01",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "consh = consh.cli:main"
        ]
    }
)