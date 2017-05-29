from setuptools import setup, find_packages


install_requires = [
    "PyYAML",
    "ts3"
]

setup(
    name="ts3proxy",
    version='0.1',
    author="Karl-Martin Minkner",
    author_email="support@kandru.de",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "ts3proxy = ts3proxy.ts3proxy:main",
        ],
    },
)
