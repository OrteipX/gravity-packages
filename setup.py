import setuptools

setuptools.setup(
    name="gravity-packages",
    version="0.0.1",
    author="Stratus",
    description="a description for gravity packages",
    url="https://github.com/OrteipX/gravity-packages",
    license="MIT",
    packages=[
        "math",
        "print_beauty"
    ],
    requires=["spacy"]
)
