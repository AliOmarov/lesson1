def get_summ(one, two, delimiter='&'):
	return str(one).upper() + str(delimiter).upper() + str(two).upper()

my_string = get_summ('learn', 'python')
print(my_string)
