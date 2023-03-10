import setuptools

setuptools.setup(
    name="gravity-device",
    version="0.0.1",
    author="Stratus_Test",
    description="a description for gravity device",
    url="https://github.com/OrteipX/gravity-packages/tree/main/gravity_device",
    license="MIT",
    packages=[
        "gravity_device",
    ],
    install_requires=["spacy", "numpy"]
)
