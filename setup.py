import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()



__version__ = "0.0.0"

REPO_NAME= "text_summariser"
Author_name = "Furqan JAved"
Author_email = "mfurqanjaved@gmail.com"
Description = "Text summarizer"
SRC_REPO = "text_summarization"



setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=Author_name,
    author_email=Author_email,
    description="A small package for nlp APP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/mfurqanjaved/text_summarization",
    project_urls={
        "Bug Tracker": f"https://github.com/mfurqanjaved/text_summarization/issues",
    },
    package_dir = {"": "src"},
    packages=setuptools.find_packages(where="src"),
)