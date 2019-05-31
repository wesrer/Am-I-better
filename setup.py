from setuptools import setup, find_namespace_packages

setup(
    name="amibetter",
    version="0.1",
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src'),
    include_package_data=True,
    install_requires=[
        'Click'
    ],
    scripts=[

    ]
)
