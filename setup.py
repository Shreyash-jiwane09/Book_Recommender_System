from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


REPO_NAME = "Book_Recommender_System"
AUTHOR_USER_NAME = "Shreyash-jiwane09"
SRC_REPO = "books_recommender"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Shreyash-jiwane09",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Shreyash-jiwane09/Book_Recommender_System",
    author_email="shrey.jiwane09@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires="==3.9",
    install_requires=LIST_OF_REQUIREMENTS
)
