from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="image_fetcher",
    version="2.0.0",
    author="Ben Andrew",
    author_email="benandrew89@gmail.com",
    description="A simple lightweight library to download images (and other files)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BenAAndrew/Python-Image-Fetcher",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "func-timeout==4.3.5",
        "tqdm==4.62.0",
        "urllib3==1.26.6",
    ],
    python_requires=">=3.5",
)
