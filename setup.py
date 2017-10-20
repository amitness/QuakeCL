from setuptools import setup


setup(
    name='QuakeCL',
    version='0.1.dev0',
    license='MIT',
    description='A command line tool that displays the recent earthquakes and aftershocks in Nepal.',
    long_description=open('README.md').read(),
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    author='Amit Chaudhary',
    author_email='',  # TO DO
    url='https://github.com/amitness/QuakeCL',
    packages=['quakecl', ],
    test_suite='quakecl.tests',
    entry_points="""
    [console_scripts]
    earthquake=quakecl.earthquake:main
    """,
)
