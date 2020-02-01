import setuptools
from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name='shtaklataqku',
        version='0.1.31',
        url='https://github.com/nu11secur1ty/shtaklataqku',
        author='Ventsislav Varbanovski @nu11secur1ty',
        author_email='venvaropt@gmail.com',
        description="HTTP Sniff Login Py",
        long_description=long_description,
        long_description_content_type="text/markdown",
        license='MIT',
        packages=['shtaklataqku'],
        zip_safe=False,
        classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
        python_requires='>=3.7',

        entry_points = {
          'console_scripts': ['cool-cmd=shtaklataqku.__main__:main'],
      }
)
