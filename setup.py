#usr/bin/env python
from setuptools import setup

setup(
    name="tap-dynamics-365",
    python_requires=">=3.8.5",
    version="0.0.1",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_dynamics_365"],
    install_requires=[
        'singer-python==5.9.0',
    ],
    extras_require={
        'dev': [
            'ipdb',
            'pylint',
            'nose'
        ]
    },
    entry_points="""
    [console_scripts]
    tap-dynamics-365=tap_dynamics_365:main
    """,
    packages=["tap_dynamics_365"],
    package_data = {
    },
    include_package_data=True,
)
