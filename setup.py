from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name="pyini",
    version="0.1",
    description="Simple INI shell parser",
    long_description=readme(),
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities'
        ],
    keywords='pyini ini shell parsing',
    python_requires=">=3",
    url="http://github.com/adriengentil/pyini",
    author="Adrien Gentil",
    author_email="adg-gh@pm.me",
    license="MIT",
    packages=["pyini"],
    zip_safe=False,
    entry_points={"console_scripts": ["pyini=pyini.pyini:main"]},
)
