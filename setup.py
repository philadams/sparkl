from distutils.core import setup


with open('README.txt') as f:
    readme = f.read()

setup(
    name='sparkl',
    version='0.0.2',
    author='Phil Adams',
    author_email='phil@philadams.net',
    url='http://github.com/philadams/sparkl',
    license='LICENSE.txt',
    description='sparklines. on the command line.',
    long_description=readme,
    packages=['sparkl'],
    scripts=['bin/sparkl'],
)
