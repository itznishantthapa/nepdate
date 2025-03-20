from setuptools import setup, find_packages

setup(
    name="nepdate",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "nepali-datetime",
    ],
    entry_points={
        "console_scripts": [
            "nepdate=nepdate_cli.cli:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A command-line tool to display Nepali dates",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/nepdate",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 