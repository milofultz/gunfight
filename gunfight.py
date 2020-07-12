#Gunfight Game using Blessed

import json
import random
import string
from sys import exit
from time import time as get_time
from time import sleep

from blessed import Terminal

TERM = Terminal()

width = TERM.width
height = TERM.height

def config_loader(fp):
	with open(fp, 'r') as f:
		config_dict = json.load(f)
	hs_list = config_dict['high_scores']
	badguy_list = config_dict['bad_guys']
	return hs_list, badguy_list


def press_any_key():
	with TERM.cbreak(), TERM.hidden_cursor():
		inp = TERM.inkey()


def speed_test(comp_speed):
	alph = random.choice(string.ascii_lowercase)
	with TERM.hidden_cursor():
		print(TERM.clear)
		random_time = random.uniform(1.5, 2.5)
		sleep(1.5)
		center_text('Get ready!')

		sleep(1.5)
			
		print(TERM.clear)
		sleep(random_time)

		center_text(f'DRAW! ---- {alph}') 
	
	start_time = get_time()
	
	with TERM.cbreak():
		val = ''
		while val != alph:
			val = TERM.inkey(timeout=comp_speed)
			if not val:
				return comp_speed

	end_time = get_time()
	user_speed = end_time - start_time

	return user_speed


def center_text(strng):
	with TERM.location(y=height//2):
			print(TERM.center(
			TERM.bright_white + f'{strng}' + TERM.normal)) 

def gunshot_display():
	color_list = [TERM.on_bright_white, TERM.on_white, TERM.on_bright_black, TERM.on_black]
	for i in range(4):
		print(color_list[i], TERM.clear)
		sleep(.06)
	pass


# Checker - Compares your time vs. the computer
def checker(user_speed, comp_speed):
	win = False
	if user_speed < comp_speed:
		win = True
	return win


def points(user_speed, comp_speed, level):
	points = (1/comp_speed * (comp_speed + level)/user_speed) * 1000
	return round(points)


# Score Saver - Checks the last score and if it's good enough, saves it to the high score file
def high_score_saver(fp, hs_list, badguy_list, name, score):
	new_hs = False

	for rank, (old_name, old_high_score) in enumerate(hs_list):
		if score >= old_high_score:
			new_hs = True
			hs_list.insert(rank, [name, score])
			if len(hs_list) > 3:
				hs_list = hs_list[0:2]
			break

	if new_hs:
		print('Congratulations! You got a high score!')
		for rank, (new_name, new_high_score) in enumerate(hs_list):
			print(f'{rank}. {new_name} - {new_high_score}')

	config_dict = {}
	config_dict['high_scores'] = hs_list
	config_dict['bad_guys'] = badguy_list

	save_dict_to_json(fp, config_dict)

	return hs_list


def save_dict_to_json(fp, dic):
	with open(fp, 'w') as f:
		json.dump(dic, f, sort_keys=True, indent=4)


if __name__ == '__main__':
	print(TERM.clear)

	player_name = input("What's yer name, traveler? --> ")
	print("You aren't from around here, are you? This is a gun eat gun town.")
	print("Are you ready to put your speed to the test? (y/n)")

	with TERM.cbreak():
		val = ''
		val = TERM.inkey()
		if val.lower() != 'y':
			print("Yer too cowardly to even try? Get outta my bar.")
			exit()

	print("Good, because here comes someone now to challenge you. The way "
			+ "to win is by\npressing the displayed letter as fast as you can " 
			+ "after you see the word 'DRAW'.\nGot it? Good luck. (Press any "
			+ "key)")
	
	config_fp = 'config.json'
	hs_list, badguy_list = config_loader(config_fp)
	
	level = 0
	score = 0

	press_any_key()

	last_badguy = False

	while True:
		if len(badguy_list) == level+1:
				last_badguy = True

		badguy_info = badguy_list[level]
		print(f"That's {badguy_info[0]}. {badguy_info[2]} But watch out, "
			+ "they're fast.\n(Press any key) ")

		press_any_key()
		
		user_speed = speed_test(badguy_info[1])
		win = checker(user_speed, badguy_info[1])
		gunshot_display()

		if win and last_badguy == True:
			print('Wow! You really are fast! And everyone who lives here is '
				+ 'dead!')
			hs_list = high_score_saver(
				config_fp, hs_list, badguy_list, player_name, score)
			exit()

		elif win and last_badguy == False:
			# Blessed press any key thing
			score += points(user_speed, badguy_info[1], level)
			print(score)
			print('Wow! You really are fast! But wait until you see the next '
				+ 'guy...')
			
			level += 1

			press_any_key()
		elif not win:
			print('You died.\n')
			hs_list = high_score_saver(
				config_fp, hs_list, badguy_list, player_name, score)
			# blessed y/n
			print("Want to play again?")
			with TERM.cbreak():
				val = ''
				val = TERM.inkey()
				if val.lower() != 'y':
					exit()