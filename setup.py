from setuptools import setup, find_packages

setup(
    name="consh",
    version="0.07",
    packages=find_packages(),
    install_requires=["prompt_toolkit>=3.0.0"],
    entry_points={
        "console_scripts": [
            "consh = consh.cli:main"
        ]
    },
    author="codewithzaqar",
    url="https://github.com/codewithzaqar/consh",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)