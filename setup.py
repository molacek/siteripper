import setuptools

setuptools.setup(
    name="siteripper",
    version="0.0.1",
    packages=setuptools.find_packages(),
    install_requires=["bs4", "requests", "xdg"],
    entry_points={
        "console_scripts": [
            #"scan = girlsreleased:scan",
        ]
    }
)