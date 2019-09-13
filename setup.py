from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='cmpx',
    version='0.6',
    description='Complex class for different operations on complex numbers',
    long_description_content_type='text/markdown',
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Omar Belghaouti',
    maintainer='Omar Belghaouti',
    author_email='bel_omar18@yahoo.com',
    maintainer_email='bel_omar18@yahoo.com',
    keywords=['Complex', 'ComplexOperations', 'ComplexNumbers'],
    url='https://github.com/Omar-Belghaouti/PythonComplex',
    download_url='https://pypi.org/project/cmpx/',
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ]
)

if __name__ == '__main__':
    setup(**setup_args)