from setuptools import setup, find_packages

setup(
    name='new-cpp',
    description='Create new cpp project',
    version='2.0',
    packages=find_packages(),
    install_requires=[
        'click'
    ],
    entry_points={
        'console_scripts': [
            'new-cpp = new_cpp.cli:main'
        ]
    }
)
