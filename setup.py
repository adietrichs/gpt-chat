from setuptools import setup

setup(
    name="gpt-chat",
    version="0.1",
    packages=["gpt_chat"],
    install_requires=[],
    extras_require={
        "dev": [
            "black",
            "pytest",
        ],
    }
)
