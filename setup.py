from setuptools import setup

setup(
    name='QuakeCL',
    version='0.2.0',
    license='MIT',
    description='A command line tool that displays the recent earthquakes and aftershocks in Nepal.',
    long_description=open('README.md').read(),
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3'
    ],
    author='Amit Chaudhary',
    author_email='meamitkc@gmail.com',
    url='https://github.com/amitness/QuakeCL',
    install_requires=['requests'],
    download_url='https://github.com/amitness/QuakeCL/tarball/0.2.0',
    packages=['quakecl', ],
    test_suite='quakecl.tests',
    entry_points="""
    [console_scripts]
    earthquake=quakecl.earthquake:main
    """,
)
