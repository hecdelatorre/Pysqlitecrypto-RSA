from setuptools import setup, find_packages

setup(
    name='Pysqlitecrypto-RSA',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'rsa'
    ],
    entry_points={
        'console_scripts': [
            'pysqlitecrypto-rsa = pysqlitecrypto_rsa.__main__:main'
        ]
    },
    license='GPL-3.0',
    author='hecdelatorre',
    author_email='hector982015@gmail.com',
    description='A package for RSA encryption and decryption using SQLite storage.',
    keywords='RSA encryption decryption SQLite cryptography',
    url='https://github.com/hecdelatorre/Pysqlitecrypto-RSA.git',
)
