from setuptools import setup

setup(name='utils',
      version='0.1',
      description='general utilities',
      url='https://github.com/josmcg/utils',
      author='Josh McGrath',
      author_email='joshuawmcgrath@gmail.com',
      license='MIT',
      packages=['collect_files'],
      install_requires=[
          "click"
      ],
      entry_points ={
            "console_scripts":["collect_files=collect_files.collect_files:main"],
      },
      zip_safe=False)
