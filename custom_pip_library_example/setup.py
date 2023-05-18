from setuptools import setup, find_packages

setup(
    name="custom_pip_library_example",
    version="0.1",
    packages=find_packages(),
    author="Pedro Pacheco",
    description="A simple example package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'pandas',
    ],
)
