from setuptools import setup

# Version info -- read without importing
_locals = {}
with open("fabenv/_version.py") as fp:
    exec(fp.read(), None, _locals)
version = _locals["__version__"]

setup(name='fabenv',
      version=version,
      description='',
      url='http://github.com/glitchcorp/fabenv',
      author='Mariusz Masztalerczuk',
      author_email='mariusz@glitchcorp.com',
      license='MIT',
      packages=['fabenv'],
      install_requires=[
          'patchwork'
      ],
      zip_safe=False)
