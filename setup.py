import setuptools
import os


with open("readme.md", "r") as fh:
    long_description = fh.read()



setuptools.setup(
    name="pexls_graber",  # Replace with your own username
    version="1.0.1",
    author="Manoj A.P",
    author_email="manojap@outlook.com",
    description="pexels bot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/manojap/pexelsbot",
    packages=setuptools.find_packages(),
    install_requires=[
        'selenium', 'webdriver-manager'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
