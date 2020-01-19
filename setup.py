#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

with open('requirements.txt') as req_file:
    requirements = req_file.read().split("\n")

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="sourcepirate",
    author_email='sourcepirate@codelantics.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Report generator",
    entry_points={
        'console_scripts': [
            'raptor=raptor.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='raptor',
    name='raptor',
    packages=find_packages(include=['raptor', 'raptor.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/sourcepirate/raptor',
    version='0.1.0',
    zip_safe=False,
)
