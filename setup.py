from setuptools import setup


setup(
    name = 'crawl',
    version = '0.0.2',
    packages = ['crawl'],
    install_requires = [
        'requests',
        'pandas',
        'matplotlib',
        'selenium',
        'selenium-wire',
    ],
    author = 'overxus',
    description = 'web scrapy, data processing & visualization',
    python_requires='>=3.8',
)
