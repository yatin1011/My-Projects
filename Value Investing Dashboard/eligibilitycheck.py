def eligibilitycheck(ticker, dfformatted):

	legiblestock = True
	reasonlist = []

	# print (dfformatted)
	# EPS increases over the year (consistent)
	for growth in dfformatted.epsgrowth:
		if growth < 0:
			legiblestock = False
			reasonlist.append('There is negative growth ' + str(growth))
			break

	# ROE > 0.15
	if dfformatted.roe.mean() < 0.13:
		legiblestock = False
		reasonlist.append('ROE mean is less than 0.13 ' + str(dfformatted.roe.mean()))

	# ROA > 0.07 (also consider debt to equity cause Assets = liabilities + equity)
	if dfformatted.roa.mean() < 0.07:
		legiblestock = False
		reasonlist.append('ROA mean is less than 0.07 ' + str(dfformatted.roa.mean()))

	# Long term debt < 5 * income
	if dfformatted.Longtermdebt.tail(1).values[0] > 5 * dfformatted.netincome.tail(1).values[0]:
		legiblestock = False
		reasonlist.append('Longtermdebt is 5 times the net income ')

	# Interst Coverage Ratio > 3
	if dfformatted.interestcoverageratio.tail(1).values[0] < 3:
		legiblestock = False
		reasonlist.append('Interest Coverage Ratio is less than 3 ')

	# print ticker, legiblestock, reasonlist
	return reasonlist