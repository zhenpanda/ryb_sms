def clean_table(arr_, max_col):
	for row in arr_:
		while len(row) < max_col:
			row.append('')