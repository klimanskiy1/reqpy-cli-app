from setuptools import setup, find_packages

setup(
    name="reqpy",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click==8.3.2",
        "requests==2.33.1",
        "tabulate==0.10.0",
        "colorama==0.4.6",
        "PyYAML==6.0.3",
        "charset-normalizer==3.4.7",
        "urllib3==2.6.3",
        "certifi==2023.7.22"  # последняя стабильная версия
    ],
    entry_points={
        "console_scripts": [
            "reqpy=app.cli:main",
        ],
    },
)