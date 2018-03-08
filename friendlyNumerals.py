def FriendlyNumber(number, region):
	# Inputs:
	# Number: an int, string, or float of the number to convert
	# Region: USA, EUR, or IND

	#Makes the input friendly
	number = str(number)
	region = region.lower()

	# Split the input into number and decimal portion
	part = number.split(".")
	# Reverses the string
	part[0] = part[0][::-1]
	final = ""

	# Ternary to decide if it should use , or .
	dec  = "." if region == "usa" or region == "ind" else ","
	sep  = "," if region == "usa" or region == "ind" else "."

	counter = 0
	places = 3

	round1 = False
	once = False

	# Iterate through first part of string
	for l in part[0]:
		final += l
		counter += 1

		# If first round is complete then change to 2 places
		if round1 and region == "ind":
			places = 2
			once = True

		# If it is time for a separator character, add it
		if counter == places:
			final += sep
			counter = 0
			round1 = True

	# Rereverses the string
	final = final[::-1]

	# If a sep is first, remove it
	if final[0] == sep:
		final = final[1:]

	# If it had a decimal, re add it
	if len(part) > 1:
		final += dec + part[1]

	# Return the Friendly number
	return final

def RomanNumerals(number):
	# Deals with the input
	number = int(number)

	if (number <= 0 or number > 5000):
		return "This cannot be converted"

	# Database of Roman Numerals
	numerals = [
		[1000, "M"],
		[500, "D"],
		[100, "C"],
		[50, "L"],
		[10, "X"],
		[5, "V"],
		[1, "I"]
	]

	final = ""
	places = [0]*4
	l = 0

	# Seperates numbers by place ex:
	# 2000
	# 300
	# 50
	# 7
	while number > 0:
		for i in range(len(numerals)):
			if ("5" not in str(numerals[i])):
				while number >= numerals[i][0]:
					number -= numerals[i][0]
					places[l] += numerals[i][0]
				l += 1

	found = False
	for i in range(len(places)):
		t = str(places[i])

		if "9" in t or "4" in t:
			# If it is a 9 or 4 use subtraction numerals
			for n in numerals:
				for j in numerals:
					if n[0] - j[0] == places[i] and not found:
						final += j[1] + n[1]
						found = True
		else:
			# Append other numbers to the string
			while places[i] > 0:
				for n in numerals:
					while n[0] <= places[i]:
						places[i] -= n[0]
						final += n[1] 

		found = False
	return final