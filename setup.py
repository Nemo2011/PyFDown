from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="PyFDown", 
    version="0.0.6",
    description="A fast downloader with Python",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Nemo2011",
    author_email="yimoxia@outlook.com",
    packages=find_packages(exclude=["test.py"]),
    install_requires=['requests', 'tqdm', 'multitasking', 'retry'],
    url = "https://github.com/Nemo2011/PyFDown", 
)
