'''
Modified on July 31st, 2014
Modified by jlovison

Created on Jan 26, 2013
@original_author: akittredge
'''

from financial_fundamentals.xbrl import XBRLMetricParams, DurationContext,\
    InstantContext
from financial_fundamentals.exceptions import ValueNotInFilingDocument
import numpy as np
                      
                      
class AccountingMetric(object):
    '''Parent class for accounting metrics.'''
    def __init__(self, filing_type, name):
        self.filing_type = filing_type
        self.name = name
        
    @classmethod
    def _build_xbrl_params(cls, possible_tags):
        return XBRLMetricParams(possible_tags=possible_tags,
                                context_type=cls._context)
        
    @classmethod
    def _value_from_filing(cls, filing, possible_tags):
        xbrl_params = cls._build_xbrl_params(possible_tags)
        metric_value = filing.latest_metric_value(xbrl_params)
        return metric_value


class EPS(AccountingMetric):
    _name_template = '{}_eps'
    _possible_tags=['us-gaap:EarningsPerShareDiluted',
                    'us-gaap:EarningsPerShareBasicAndDiluted']
    _context = DurationContext
    @classmethod
    def value_from_filing(cls, filing):
        return cls._value_from_filing(filing, possible_tags=cls._possible_tags)


class BookValuePerShare(AccountingMetric):
    _name_template = '{}_book_value_per_share'
    _context = InstantContext
    _assets_tags = ['us-gaap:Assets']
    _liabilities_tags = ['us-gaap:Liabilities']
    _shares_outstanding_tags = ['dei:EntityCommonStockSharesOutstanding']
    _stockholders_equity_tags = ['us-gaap:StockholdersEquity']
    @classmethod
    def value_from_filing(cls, filing):
        try:
            assets = cls._value_from_filing(filing, possible_tags=cls._assets_tags)
            liabilities = cls._value_from_filing(filing, possible_tags=cls._liabilities_tags)
        except ValueNotInFilingDocument:
            book_value = cls._value_from_filing(filing, possible_tags=cls._stockholders_equity_tags)
        else:
            book_value = assets - liabilities
        shares_outstanding = cls._value_from_filing(filing, possible_tags=cls._shares_outstanding_tags)
        try:               
            return book_value / shares_outstanding
        except ZeroDivisionError:
            return np.NaN
