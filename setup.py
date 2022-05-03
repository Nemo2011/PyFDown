from setuptools import setup, find_packages

setup(
    name="PyFDown", 
    version="0.0.1",
    description="A fast downloader with Python",
    license="MIT",
    long_description="""
        This library is a fast downloader that like Aria2. But it doesn't need to compile. It is easy to use. 
    """,
    author="Nemo2011",
    author_email="yimoxia@outlook.com",
    packages=find_packages("PyFDown", exclude=["test.py"]),
    install_requires=['requests', 'tqdm', 'multitasking', 'retry'],
    url = "https://github.com/Nemo2011/PyFDown"
)
