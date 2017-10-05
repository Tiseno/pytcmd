from setuptools import setup

setup(name='pytcmd',
      version='0.1',
      description='A command',
      url='http://github.com/tiseno/pytcmd',
      author='ML',
      license='MIT',
      packages=['pytcmd'],
      entry_points = {
          'console_scripts': [
              'pytcmd-main=pytcmd',
              'pytcmd-hello=pytcmd:hello_world',
              'pytcmd-something=pytcmd.something:hello',
              ]
      },
      zip_safe=False)
