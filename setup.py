
#!/usr/bin/env python

from setuptools import setup, find_packages


with open('./requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name="tgibm",
    version="1.1.0",
    description="Example of a fully reproducible project !",
    url="https://github.com/imenbenmhd/MiniProject",
    license="MIT license",
    author="Imen Ben Mahmoud & Teodora Glamocanin",
    author_email="imen.benmhd@gmail.com",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    packages=find_packages(),
    include_package_data=True,
    package_data={'tgibm': ['data/*']},
    install_requires=required,
    entry_points={"console_scripts": ["tgibm-result = tgibm.result:main"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Bsd License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)