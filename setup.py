from distutils.core import setup
from setuptools import find_packages

with open("README", "r") as f:
  long_description = f.read()

setup(name='pysrec',  # 包名
      version='1.0.0',  # 版本号
      description='A package to handle Motolora s-record file',
      long_description=long_description,
      author='sgnes',
      author_email='sgnes0514@gmail.com',
      url='https://github.com/sgnes/pysrec',
      install_requires=[],
      license='BSD License',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries'
      ],
      )