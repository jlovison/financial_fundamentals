from setuptools import setup, find_packages

version = '0.3.1'
desc = '''\
FinancialFundamentals
=========================
:Authors: Josh Lovison, Andrew Kittredge
:Version: $Revision: {}
:Copyright: Josh Lovison, Andrew Kittredge
:License: Apache Version 2


FinancialFundamentals is designed around pulling filings from the SEC's EDGAR system and extracting defined metrics from the filings.

FinancialFundamentals is under active development, comments, suggestions, and bug reports are appreciated.

'''.format(version)

setup(name='FinancialFundamentals',
      version=version,
      description='Extraction of financial data from the SEC EDGAR database.',
      long_description=desc,
      author='Josh Lovison',
      author_email='jlovison@gmail.com',
      license='Apache 2.0',
      packages=find_packages(),
      classifiers=[
	'Development Status :: 4 - Beta',
	'License :: OSI Approved :: Apache Software License',
	'Natural Language :: English',
	'Programming Language :: Python',
	'Programming Language :: Python :: 2.7',
	'Operating System :: OS Independent',
	'Intended Audience :: Science/Research',
	'Topic :: Office/Business :: Financial',
     	],	
      install_requires=[
	'numpy',
	'pytz',
	'requests_cache',
	'requests',
	'BeautifulSoup',
	'mock',
	'xmltodict',
	'blist',
	'python-dateutil==1.5',
	],
      url='https://github.com/jlovison/financial_fundamentals',
)
