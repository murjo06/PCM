from setuptools import setup, find_packages

setup(
    name='PCM',
    version='0.2',
    license='MIT',
    author="murjo06",
    author_email='markvlogs228@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/murjo06/PCM',
    keywords='Python Color Manager',
    install_requires=[
          'PCM',
    ]
)