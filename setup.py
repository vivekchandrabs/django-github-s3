from setuptools import setup

import storages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='django-github-s3',
    version=v_01,
    packages=['storages_github', 'storages_github.backend'],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    install_requires=['Django>=2.11'],
    extras_require={
        'libcloud': ['apache-libcloud'],
        'sftp': ['paramiko'],
    },
    author='Vivek Chandra B S',
    author_email='vivek.chandra.301096@gmail.com',
    license='Mozilla Public License Version 2.0',
    description='Support for many storage backends in Django',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/vivekchandrabs/django-github-s3.git',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    zip_safe=False
)