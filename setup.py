from setuptools import setup

setup(
    name="fraud-detection",
    version="0.1.0",
    packages=["app", "data", "models"],  # Explicit list of packages
    install_requires=[
        "flask", 
        "gunicorn",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
