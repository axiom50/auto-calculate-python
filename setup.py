from setuptools import setup, find_packages

setup(
    name='auto-calculate-python',
    version='0.1.0',
    author='exiom50',
    author_email='exiom50@gmail.com',
    description='A brief description of the package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/axiom50/auto-calculate-python',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',

)
