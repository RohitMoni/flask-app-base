import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="basic-flask-app-scaffold",
    version="1.0.0",
    author="Rohit Moni",
    author_email="rohitmdxb@gmail.com",
    description="A scaffold so I can start new flask projects easily",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "Flask"
    ],
    extras_require={
        'dev': [
            "pylint"
        ]
    }
)

requires: (For later)
Flask

dev / test:
pylint
