from setuptools import setup, find_packages

setup(
    name="UCMigrantFinder",
    version="1.0.0",
    author="Tosin Kuye",
    description="A Hackathon project focused on finding and provided resources for new immigrants and refugees.",
    url="https://github.com/tkuye/UCMigrantFinder",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.9",
    entry_points={"console_scripts": ["ucmfinder = src.api.main:main"]},
    packages=find_packages(),
)