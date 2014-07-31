financial_fundamentals
======================

Note: Planning on revamping dependencies and changing the project slightly now that original author abandoned. Stay tuned. -jlovison


Find XBRL filings on the SEC's edgar and extract accounting metrics.

	# Get the filings
	import financial_fundamentals.edgar as edgar
	filings = edgar.get_filings(symbol='MSFT', filing_type='10-K)
	
	# Get the Metrics
	import financial_fundamentals.accounting_metrics EPS
	eps_values = []
	for filing in filings:
	    eps_values.append(filing.first_tradable_date, EPS.value_from_filing(filing))
