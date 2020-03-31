import csv   # İmport Comma Seperated Values Module

with open("states_us.csv", "r") as states:  # Read the file
	csv_read = csv.DictReader(states)

	with open("new_states.csv", "w") as new_states:	 # Create a file to write
		fieldnames = ["State","Abbreviation"]

		csv_write = csv.DictWriter(new_states, fieldnames=fieldnames, delimiter="\t") # Seperate the file with tab

		csv_write.writeheader()

		for line in csv_read:	# Write the readed lines row by row
			csv_write.writerow(line)
