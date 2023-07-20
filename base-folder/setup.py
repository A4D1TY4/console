from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Console.log package.'

# Setting up
setup(
    name="console",
    version=VERSION,
    author="Aaditya Sangroula",
    author_email="aadityasangroula099@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords=['python', 'javascript', 'print', 'hello world', 'package', 'console', 'terminal'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
