def reverse_list(ihavethehighground):
	if len(ihavethehighground) == 1:
		return ihavethehighground
	else:
		return ihavethehighground[-1] + power(ihavethehighground[-1] -1 )