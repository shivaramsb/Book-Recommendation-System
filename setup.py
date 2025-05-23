from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Edit Below variables as per ypur requirements

REPO_NAME = "Book Recommendation System"
AUTHOR_USER_NAME = "Shivaram Babar"
SRC_REPO = "bookrecommondedsystem"
LIST_OF_REQUIREMENTS = []

setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url= "https://github.com/shivaramsb/Book-Recommendation-System",
    author_email="shivaramb1702@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires = LIST_OF_REQUIREMENTS
)