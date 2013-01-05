from distutils.core import setup

setup(
    name='sparkl',
    version='0.0.1',
    author='Phil Adams',
    author_email='phil@philadams.net',
    packages=['sparkl', 'sparkl.test'],
    scripts=['bin/sparkl'],
    url='http://github.com/philadams/sparkl',
    license='LICENSE.txt',
    description='sparklines. on the command line.',
    long_description=open('README.txt').read(),
    install_requires=[],
)
