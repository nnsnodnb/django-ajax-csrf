from setuptools import setup, find_packages

setup(
    name='django-ajax-csrf',
    version='1.0.0',
    description='Django app - bundle csrf token additioner for JavaScript',
    long_description=open('README.rst', 'r').read(),
    author='nnsnodnb',
    author_email='ahr63_gej@me.com',
    url='https://github.com/nnsnodnb/django-ajax-csrf',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    keywords='django csrf staticfiles',
    platforms=['any'],
)

