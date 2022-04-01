
#!/usr/bin/env python

from setuptools import setup, find_packages


def load_requirements(f):
    retval = [str(k.strip()) for k in open(f, "rt")]
    print("done")
    return [k for k in retval if k and k[0] not in ("#", "-")]


setup(
    name="cc2",
    version="1.0.0",
    description="Example of classification using regression",
    url="https://github.com/imenbenmhd/MiniProject",
    license="BSD",
    author="Imen Ben Mahmoud & Teodora Glamocanin",
    author_email="",
    long_description=open("README.md").read(),
    #long_description_content_type="text/x-rst",
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['Data/*.csv']}
    install_requires=load_requirements("./requirements.txt"),
    entry_points={"console_scripts": ["cc2-analysis = cc2.analysis:main"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)