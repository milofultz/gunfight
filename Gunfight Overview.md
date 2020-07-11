# Gunfight! Overview
---

**Stay in abstract thinking as long as possible. The longer you take to implement your concepts, the better.**

* Describe what your program will do in abstract terms, as if it was a person doing it, not a computer.

Program will open and prompt you to get ready. In a randomized amount of time, the screen will say 'Draw!'. Then you will have to press space before the Program reaches their time. How fast you do it will be displayed and you will be shown if you won or lost. You will progress in levels against different "opponents".

* From there, describe how your program will handle data. Start BIG as possible.

The program will take in a list of opponents and their unique properties, along with any high scores. The program will output any changes to the high scores.

* Break down the process further in abstract terms. What are the distinct actions it will need to take? What would a random stupid guy need if you wanted him to do it?

Program will start by loading up any config files and high score files and storing them in local memory.
Program will write out the rules and ask if you want to play. If no, it will quit the program and heckle you.
Program will ask for your name and will save your name to be used while you play and for the high scores.
Program will then start the game. They will ask you to press a button as quickly as you can after seeing the word 'draw' displayed. 
When draw is displayed, Program will start a stopwatch and if you hit the button in time, you will win and progress to the next round. This will repeat until you can't hit your button in time.
Once you lose, Program will put your name on a gravestone along with some heckling words. 
Program will check the high scores and see if you were better than the top 3 players it has recorded there. If you were, it will place you in the list and remove the lowest person.
Program will ask if you want to play again, and if so, it will start all over again.

* Determine the biggest distinct functions you can perceive in the description you just created.

Loader - Find any config files and load them into memory
Display - Display what you want on screen
Namer - Get user's name and save it
Timer - Sees you beat the computer in time
Draw - The program that runs when the game starts against the computer
Leveler - Ups the level when you beat that level
Score Saver - Checks the last score and if it's good enough, saves it to the high score file
Play again - Asks the user if they want to play again

* What data types would be best to transfer in between these functions?

Loader - Find any config files and load them into memory
	IN: file
	OUT: dictionary
Display - Display what you want on screen
	IN: string, text
	OUT: none (display)
Namer - Get user's name and save it
	IN: none
	OUT: string
Timer - Sees if you beat the computer in time
	IN: none
	OUT: float, time
Draw - The program that runs when the game starts against the computer
	IN: none
	OUT: float, time in seconds
Checker - Compares your time vs. the computer
	IN: float(s), time in seconds
	OUT: bool
Leveler - Ups the level when you beat that level
	IN: none
	OUT: str, name; float, time
Score Saver - Checks the last score and if it's good enough, saves it to the high score file
	IN: str, name; float, time
	OUT: file
Play again - Asks the user if they want to play again
	IN: str
	OUT: bool

* Make a very rough outline of the program using information from chunking steps. Include only necessary in/out information.
	
* Write out overview for each function as if you were telling a random stupid guy to do it.	

* Do this for all functions and see how you can break down the process into atomistic functions. The more that functions can be used and reused all around the whole program, the better.

* Once the program has been broken down into its most atomistic functions, start writing pseudocode into them to have an idea of what you're going to do.

* Look for similarities in between functions and see if there is any process the functions could share. If so, then take that and break it down into it's own function.

* When you feel it has been broken down fully and the flow of data makes sense, make a basic way to test it as it goes. In Python, this is by adding an ```if __name__ == '__main__':``` section. Start with more pseudocode and continue with it until you feel that you can correctly write out the flow using the functions you've already created.

* Figure out what is the easiest thing to program and test. Go with the pseudocode you've written and start fleshing it out with real functionality. Test each part as you go in the terminal.

* Repeat this process with each element of your code, ensuring that it works exactly as you expect. You don't have to go in a linear fashion, if it is easier or more sensible to jump around.

** Don't be afraid to go back to previous steps if you realize further possibilities of chunking or other revisions.** 