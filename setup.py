from setuptools import setup, find_packages

setup(
    name='cmake-analyzer',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'TatSu'
    ],
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'cmake_analyzer=cmake_analyzer.analyzer:main',
        ],
    },

    url='https://bitbucket.org/ArchiDevil/cmake-analyzer',
    author='Denis Bezykornov'
)
