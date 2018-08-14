from setuptools import setup

setup(
    name='insights_publisher',
    description="A package to streamline publication workflows for Knowledge Repo and tie published work to GitHub commits.",
    url='https://github.com/CPapadim/insights_publisher',
    version='0.1.0',
    author='Charalampos Papadimitriou',
    author_email='papadimitriou.c@gmail.com',
    license='MIT',
    packages=['insights_publisher'],
    zip_safe=False,
    scripts=['insights_publisher/publisher'],
)
