import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="allogate",
    version="1.0.0",
    author="Ignis",
    author_email="me@ignis.wtf",
    description="A logging package but very pretty and has stacks and stuff",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FlameOfIgnis/allogate",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)