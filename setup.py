from setuptools import setup, find_packages

setup(
    name='python color manager',
    version='0.2',
    license='MIT',
    author="murjo06",
    author_email='markvlogs228@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/murjo06/PCM',
    long_description_content_type="text/markdown",
    long_description="README.md"
)