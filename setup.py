import setuptools

long_description = """
# Jevis    
This package is very powerful.    
This has pointer, switch, etc.    
This package comply with MIT License.    
The author of this package is Jiang ChengJun.    
My email is jcj1947725596@hotmail.com.    
"""

setuptools.setup(
    name="Jevis",
    version="0.1.4",
    author="Jiang ChengJun",
    author_email="jcj1947725596@hotmail.com",
    description="A powerful package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
