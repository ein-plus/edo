from setuptools import setup, find_packages

install_requires = [
    'flask',
    'pyhash',
]

tests_require = [
    'pytest',
]

setup(
    name='edo',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
)
