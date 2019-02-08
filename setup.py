from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="stepwise-regression",
    version="1.0.2",
    description="A Python package to implement stepwise regression",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/AakkashVijayakumar/stepwise-regression",
    author="Aakkash Vijayakumar",
    author_email="aakkashvijayakumar@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["stepwise_regression"],
    include_package_data=True,
    install_requires=["statsmodels","pandas"]
)