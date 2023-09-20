from setuptools import setup,find_packages

setup(
    name="DeepL_Translator",
    version="0.1",
    description="Library, That uses selenium, To translate, Using DeepL Translator, Without the usage of key.",
    author="Agoxu",
    packages=find_packages(),
    install_requires=[
        'selenium'
    ],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
