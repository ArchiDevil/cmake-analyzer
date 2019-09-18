from setuptools import setup, find_packages

setup(
    name='cmake-analyzer',
    version='0.1-rc2',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'TatSu==4.4.0'
    ],
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'cmana=cmake_analyzer.analyzer:entrypoint',
        ],
    },

    project_urls={
        "Homepage": "https://bitbucket.org/ArchiDevil/cmake-analyzer",
        "Bug Tracker": "https://bitbucket.org/ArchiDevil/cmake-analyzer/issues",
        "Source Code": "https://bitbucket.org/ArchiDevil/cmake-analyzer/src",
    },

    author='Denis Bezykornov',
    keywords='cmake lint analyzer',
    classifiers=[
        'Topic :: Software Development :: Build Tools',
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License'
    ]
)
