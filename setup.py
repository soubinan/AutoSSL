import os

from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))

# retrieve package information
about = {}
with open(os.path.join(HERE, 'autossl', '__version__.py'), 'rb') as f:
    exec(f.read().decode('utf-8'), about)

with open(os.path.join(HERE, 'README.rst'), 'rb') as readme_file:
    readme = readme_file.read().decode('utf-8')

install_requires = [
    'six',
    'cryptography',
    'pyyaml',
    'requests',
]

extras_require = {
    # acme
    'acme': ['acme'],
    # servers
    # tracking
    # storage
    'git': ['GitPython'],
}
# ability to install automatically all dependencies
extras_require['all'] = list(set(value for sublist in extras_require.values() for value in sublist))


setup(
    name=about['__title__'],
    version=about['__version__'],

    author=about['__author__'],
    author_email=about['__author_email__'],

    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    url=about['__url__'],
    license=about['__license__'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'autossl = autossl.__main__:main'
        ]
    },
    platforms='Unix; MacOS X',

    install_requires=install_requires,
    extras_require=extras_require,
)
