def control_digit(ID):
	""" compute the check digit in an Israeli ID number,
	given as a string """
	total = 0
	print ("xxx here we go xxx")
	for i in range(8):
		print ("current i: " + str(i))
		print ("current ID[i]: " + str(ID[i]))
		val = int(ID[i]) #converts a char to its numeric integer value
		print ("current val : " + str(val))
		if i % 2 == 0:
			total = total+val
		else:
			if val < 5:
				total += 2*val
			else:
				total += (2*val % 10) + 1 # sum of digits in 2*val
		print ("current total: " + str(total))
		print ("xxxxxxx end of loop xxxxxxx")
	total = total % 10
	check_digit= (10 - total) % 10 # the complement mod 10 of sum

	return str(check_digit)

x=control_digit("31629677")
print (x)








