from setuptools import setup, find_packages

setup(
    name="yourname-wf-basic",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pyyaml",
        "typer"
    ],
    entry_points={
        "console_scripts": [
            "yourname-wf-basic=commands:app",
        ],
    },
)
