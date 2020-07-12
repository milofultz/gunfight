#Gunfight Game using Blessed v2

import json
import random
import string
from sys import exit as quit
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

def get_name():
	clear()
	name = input("What's yer name, traveler? --> ")
	print('')
	return name

def how_to_play():
	print("You aren't from around here, are you? This is a gun eat gun town. \
		Look, here comes someone now to challenge you. The way to win is by \
		pressing the displayed letter as fast as you can after you see the \
		word 'DRAW'. Got it? Good luck.\n")

def intro_to_badguy(name, info):
	print(f"That's {name}. {info} But watch out, they're fast. (Press any key)")
	press_any_key()

def gunfight(badguy_speed):
	button = random.choice(string.ascii_lowercase + string.digits)
	random_time = random.uniform(1.5, 2.5)
	win = False
	
	with TERM.hidden_cursor():
		clear()
		sleep(1.5)
		center_text('Get ready!')
		sleep(1.5)
		clear()
		sleep(random_time)
		center_text(f'DRAW! ---- {button}') 
	
	start_time = get_time()
	with TERM.cbreak():
		val = TERM.inkey(timeout=badguy_speed)
	end_time = get_time()
	gunshot_display()

	user_speed = 0

	if user_speed < badguy_speed and val == button:
		win = True
		user_speed = end_time - start_time

	return user_speed, win

def gunshot_display():
	color_list = [
		TERM.on_bright_white, 
		TERM.on_white, 
		TERM.on_bright_black, 
		TERM.on_black
		]
	for i in range(4):
		print(color_list[i], TERM.clear)
		sleep(.06)

def get_score(user_speed, badguy_speed, level):
	points = (1/badguy_speed * (badguy_speed + level)/user_speed) * 1000
	return round(points)


def you_win_but(name):
	print(f"I can't believe it! You killed {name}! This is good news, but be \
		careful. There's another bad dude right over there. ", end='')

def you_win(name, score):
	print(f'Wow! You really are fast! And everyone who lives here is dead!\n\
		All hail {name}, who scored {score} points!')

def you_lose(name, score):
	print(f'You died.\n"Here lies {name}, who scored {score} points."')

def want_to_play():
	print('Want to play another game?')
	with TERM.cbreak():
		val = ''
		val = TERM.inkey()
		if val.lower() != 'y':
			print("Yer a coward.")
			exit()

def list_high_scores(high_scores_list):
	print('--- HIGH SCORES ---')
	for num, (name, score) in enumerate(high_scores_list):
		print(f'{num+1}. {name} -- {score}')

def update_hs_list(high_scores_list, name, score):
	new_hs = False

	for rank, (old_name, old_high_score) in enumerate(high_scores_list):
		if score >= old_high_score and not new_hs:
			new_hs = True
			high_scores_list.insert(rank, [name, score])
			if len(high_scores_list) > 3:
				high_scores_list = high_scores_list[0:3]
	
	return high_scores_list

def save_config(fp, high_scores_list, badguy_list):
	config_dict = {
		'high_scores': high_scores_list,
		'bad_guys': badguy_list
		}
	with open(fp, 'w') as f:
		json.dump(config_dict, f, sort_keys=True, indent=4)

def press_any_key():
	with TERM.cbreak(), TERM.hidden_cursor():
		inp = TERM.inkey()

def center_text(strng):
	with TERM.location(y=height//2):
			print(TERM.center(
			TERM.bright_white + f'{strng}' + TERM.normal)) 

def clear():
	print(TERM.clear)


if __name__ == '__main__':
	config_fp = 'config.json'
	high_scores_list, badguy_list = config_loader(config_fp)
	max_level = len(badguy_list)

	name = get_name()
	how_to_play()

	level = 0
	score = 0

	while True:
		badguy_name, badguy_speed, badguy_text = badguy_list[level]

		intro_to_badguy(badguy_name, badguy_text)
		user_speed, win = gunfight(badguy_speed)

		if win:
			score += get_score(user_speed, badguy_speed, level)
			if level + 1 == max_level:
				you_win(name, score)
				high_scores_list = update_hs_list(
					high_scores_list, name, score)
				list_high_scores(high_scores_list)
				save_config(config_fp, high_scores_list, badguy_list)
				quit()
			else:
				you_win_but(badguy_name)
				level += 1
				continue
		else:
			you_lose(name, score)
			high_scores_list = update_hs_list(
				high_scores_list, name, score)
			list_high_scores(high_scores_list)
			want_to_play()
			level = 0