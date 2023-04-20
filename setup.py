from setuptools import setup, find_packages

setup(name='cogstat',
      version='2.3',
      description='Simple statistics for researchers.',
      url='https://www.cogstat.org',
      author='Attila Krajcsi',
      author_email='krajcsi@gmail.com',
      packages=find_packages(),
      include_package_data=True,
      license='GNU GPL 3',
      install_requires=['numpy', 'scipy >=1.9', 'matplotlib >=1.5.0, !=2.0.1, !=2.0.2, !=3.6.*',
                        'pandas >=1.1.0', 'statsmodels >=0.12.2', 'pingouin >=0.3.8', 'scikit-posthocs',
                        'pyreadstat', 'odfpy', 'xlrd', 'openpyxl', 'pyreadr',
                        'appdirs', 'python-bidi', 'IPython', 'Jupyter', 'sklearn', 'svgutils'],
      python_requires='>=3.6',
      entry_points={'console_scripts': ['cogstat=cogstat.cogstat_gui:main']},
      extras_requires={'GUI': ['PyQt5']}
)
