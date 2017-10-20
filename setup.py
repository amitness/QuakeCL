from setuptools import setup

requirements = [pkg.split('=')[0] for pkg in open('requirements.txt')]

setup(
    name='QuakeCL',
    version='0.1.7',
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
    install_requires=requirements,
    download_url='https://github.com/amitness/QuakeCL/tarball/0.1.7',
    packages=['quakecl', ],
    test_suite='quakecl.tests',
    entry_points="""
    [console_scripts]
    earthquake=quakecl.earthquake:main
    """,
)
