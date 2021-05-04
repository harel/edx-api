import os
from setuptools import find_packages, setup


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='edx-api',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='Proprietary',
    description='Adds missing api endpoints to edx',
    long_description="",
    url='https://',
    author='Harel Malka',
    author_email='harel@harelmalka.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'djangorestframework',
    ],
    entry_points={
        "lms.djangoapp": [
            "edxapi = lms.djangoapp.edxapi.apps:EdxapiConfig",
        ],
    }
)