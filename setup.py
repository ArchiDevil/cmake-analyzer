from setuptools import setup, find_packages

setup(
    name='cmake-analyzer',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'TatSu',
        'PyYAML'
    ],
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'cmana=cmake_analyzer.analyzer:entrypoint',
        ],
    },

    url='https://bitbucket.org/ArchiDevil/cmake-analyzer',
    author='Denis Bezykornov'
)
