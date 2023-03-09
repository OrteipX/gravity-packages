import setuptools

setuptools.setup(
    name="gravity-packages",
    version="0.0.3",
    author="Stratus",
    description="a description for gravity packages",
    url="https://github.com/OrteipX/gravity-packages",
    license="MIT",
    packages=[
        "math_gravity",
        "print_beauty",
        "gravity_device"
    ],
    install_requires=["spacy"]
)
