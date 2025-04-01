import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-End-Chicken-Disease-Image-Classification"
AUTHOR_USER_NAME = "IamMayur95"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "mayurharisangam10@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/IamMayur95/End-To-End-Chicken-Disease-Image-Classification.git",
    project_urls={
        "Bug Tracker": f"https://github.com/IamMayur95/End-To-End-Chicken-Disease-Image-Classification/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)