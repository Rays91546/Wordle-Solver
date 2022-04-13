import sys

from numpy import sort
sys.path.append('Final Project')

from search import *
from sortle import *

class Wordle:
    def __init__(self):
        self.word = "" # the word currently being solved for
        self.list = [] # all the guessable words minus the solution words
        self.solution_list = [] # all the words that are part of the solution list
        self.start_words = ["soare, asier, roast"]

    """ gives the word a score """
    def score(self, word):
        return 0

    """ solves for the word using self.list """
    def solve(self, word):
        return None

    """ solves for each word in self.solution_list """
    def solve_list(self):
        return None

def main():
    # make a new Wordle class
    wordle = Wordle()
    # make a new Sortle class
    sortle = Sortle()
    # convert the new york times solution list to just the words 
    sortle.convert_to_clean_solution_list('wordle_lists/nyt_wordle_solution_list.txt', 'wordle_lists/sources/new_york_times.txt', 2)
    # compare the new york times list with the one from medium
    list1 = sortle.LoadList('wordle_lists/nyt_wordle_solution_list.txt')
    list2 = sortle.LoadList('wordle_lists/medium_wordle_solution_list.txt')
    print(sortle.compare_lists(list1, list2))
    sortle.CountFrequencies(list1)


if __name__ == '__main__':
    main()