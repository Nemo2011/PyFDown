from setuptools import setup, find_packages

setup(
    name="PyFDown", 
    version="0.0.3",
    description="A fast downloader with Python",
    license="MIT",
    long_description=open("README.md").read(),
    author="Nemo2011",
    author_email="yimoxia@outlook.com",
    packages=find_packages("PyFDown", exclude=["test.py"]),
    install_requires=['requests', 'tqdm', 'multitasking', 'retry'],
    url = "https://github.com/Nemo2011/PyFDown", 
)
