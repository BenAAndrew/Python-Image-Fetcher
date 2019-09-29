import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="image_fetcher",
    version="1.0.2",
    author="Ben Andrew",
    author_email="benandrew89@gmail.com",
    description="Package for downloading images from google",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BenAAndrew/Python-Image-Fetcher",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "beautifulsoup4>=4.8.0",
        "bs4>=0.0.1",
        "certifi>=2019.9.11",
        "chardet>=3.0.4",
        "func-timeout>=4.3.5",
        "idna>=2.8",
        "selenium>=3.141.0",
        "soupsieve>=1.9.3",
        "tqdm>=4.36.1",
        "urllib3>=1.25.5",
        "wincertstore>=0.2",
    ],
    python_requires='>=3.6',
)