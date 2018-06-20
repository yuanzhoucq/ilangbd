from setuptools import setup, find_packages

setup(
    name="ilangbd",
    version='0.3.0',
    description="A console application of speaking made with Baidu Yuyin",
    long_description="speak",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    author="joyuer",
    author_email="yuanzhou.cq@gmail.com",
    url="https://github.com/yuanzhoucq/ilangbd",
    license='MIT',
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        ilang=ilangbd.main:read
    ''',
)