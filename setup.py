
import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="example_python_package",
    version="0.0.1",
    author="billingsley-john",
    description="Example python package",
    long_description=long_description,
    url="https://github.com/billingsley-john/example_python_package",
    packages=["example_python_package"]   # can also use setuptools.find_packages()
)
