#Gunfight Game using Blessed

# Loader - Find any config files and load them into memory
# 	IN: file
# 	OUT: dictionary
def loader(fp):
	# look for config file at filepath
	# open file at file path
	# dump file into a dictionary of it's contents
	# return the new dictionary
	return hs_list, badguy_list

# Draw - the program that initiates game sequence
# 	IN: 
# 	OUT: 
def draw():
	# get current time when program starts
	# wait for user to press button
	# get time of when user presses button
	# subtract start time from button press time
	# return the time
	return user_speed

# Timer - Sees if you beat the computer in time
# 	IN: none
# 	OUT: float, time
def get_time():
	# get current time in seconds since epoch
	# return that time
	return current_time

# Gunshot display - show a blink on the screen like a gunshot after game is over
# 	IN: none
# 	OUT: none (display)
def gunshot_display():
	pass

# Checker - Compares your time vs. the computer
# 	IN: float(s), time in seconds
# 	OUT: bool
def checker(user_speed, comp_speed):
	# check to see if user's speed is less than computer speed
	win = True
	# return the result
	return win

# Leveler - Ups the level when you beat that level
# 	IN: int, list index
# 	OUT: str, name; float, time
def leveler(opp_list, prev_level):
	# check list for index
	# unpack values of tuple found at next element in sequence
	# return new values
	return new_name, new_time

# Score Saver - Checks the last score and if it's good enough, saves it to the high score file
# 	IN: str, name; float, time
# 	OUT: dict
def score_saver(name, time, hs_list):
	# compare time input against each element other in high score list
	# If user score is worse than current, insert it after current
	# Remove last element in high score list
	new_hs_list = []
	# Return new list
	return new_hs_list