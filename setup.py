import setuptools
import os


def read(f_name):
    return open(os.path.join(os.path.dirname(__file__), f_name)).read()


long_description = read('readme.md')

setuptools.setup(
    name="pexlsbot",  # Replace with your own username
    version="1.0.1",
    author="Manoj A.P",
    author_email="manojap@outlook.com",
    description="pexels bot",
    long_description="A selenium bots for automate stock free image downloading from pexels.com",
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
