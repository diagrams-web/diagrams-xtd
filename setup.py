# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

packages = \
['diagrams',
 'diagrams.alibabacloud',
 'diagrams.aws',
 'diagrams.azure',
 'diagrams.base',
 'diagrams.c4',
 'diagrams.custom',
 'diagrams.digitalocean',
 'diagrams.elastic',
 'diagrams.firebase',
 'diagrams.gcp',
 'diagrams.generic',
 'diagrams.ibm',
 'diagrams.k8s',
 'diagrams.oci',
 'diagrams.onprem',
 'diagrams.openstack',
 'diagrams.outscale',
 'diagrams.programming',
 'diagrams.saas'
]

package_data = \
{'': ['*']}

install_requires = \
['graphviz>=0.13.2,<0.21.0', 'jinja2>=2.10,<4.0', 'typed-ast>=1.5.4,<2.0.0']

setup_kwargs = {
    'name': 'diagrams_xtd',
    'version': '0.23.4.15',
    'url': 'https://github.com/diagrams-web/diagrams-xtd',
    'license': 'MIT',
    'author': ["Diagrams-web <no_spam@nowhere.mail>"],
    'description': 'Extended version of diagrams',
    'long_description_content_type': "text/markdown",
    'packages': find_packages(exclude=["tests"]),
    'long_description': open('README.md').read(),
    'zip_safe': False,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'classifiers': [
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
}

setup(**setup_kwargs)
