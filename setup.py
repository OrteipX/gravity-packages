import setuptools

setuptools.setup(
    name="gravity-packages",
    version="0.0.6",
    author="Stratus_Test",
    description="a description for gravity packages",
    url="https://github.com/OrteipX/gravity-packages",
    license="MIT",
    packages=[
        "math_gravity",
        "print_beauty",
        "gravity_device",
        "gravity_features"
    ],
    install_requires=["spacy", "numpy"]
)
