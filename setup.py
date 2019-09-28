import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="image_fetcher",
    version="1.0.0",
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
    python_requires='>=3.6',
)