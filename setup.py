from setuptools import setup

setup(
    name="package-name",
    version="0.1",
    packages=["package_name"],
    install_requires=[],
    extras_require={
        "dev": [
            "black",
            "pytest",
        ],
    }
)
