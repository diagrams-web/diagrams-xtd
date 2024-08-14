from setuptools import setup, find_packages

setup(
    name='diagrams_xtd',
    version='0.23.4.14',
    url='https://github.com/diagrams-web/diagrams-xtd',
    license='MIT',
    author=["Diagrams-web <no_spam@nowhere.mail>"],
    description='Extended version of diagrams',
    long_description_content_type="text/markdown",
    packages=find_packages(),
    long_description=open('README.md').read(),
    zip_safe=False,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ]
)