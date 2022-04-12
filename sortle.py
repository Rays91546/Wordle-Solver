"""
This class takes care of reading in lists from text files and sorting them.
Sorts are done alphabetically 
"""
class Sortle:
    def __init__(self):
        self.list = []

    """ returns the frequency of each letter in the english alphabet for the given list """
    def count_frequencies(self, list):
        return None

    """ loads a list from the txt file if it's in the format of
        word
        word
        word
        ... and so on """
    def LoadList(self, txtfile):
        list = []
        with open(txtfile) as f:
            for line in f:
                list.append(line.lower())
        return sorted(list)

    """ gets the list from the medium website and strips it of everything but the solution word list
    for site put 1 if the medium website or put 2 if from the source code off New York Times Wordle """
    def convert_to_clean_solution_list(self, writeTo, openFile, site):

        # open a file to write the cleaned up word list to
        with open(writeTo, 'w') as w:

            # open the file with the uncleaned up version of the world solution list
            with open(openFile) as f:
                list = []
                if (site == 1): # if word list taken from Medium website
                    for line in f:

                        # split each line by spaces
                        split_string = line.split(' ')

                        # get the last entry which is the word we want
                        word = split_string[len(split_string-1)]

                        # get rid of the new lines
                        if (word[:-2] == '\n'):
                            word = word[:-2]
                        
                        # only append the word if its of length 5
                        if (len(word) == 5):
                            list.append(word.lower())

                else: # if word list taken from New York Times source code
                    word = ""
                    while True:
                        # reading a single character from the file
                        ch = f.read(1)

                        if not ch:
                            # end of file
                            break
                        else:
                            # check if character is alphabet discard if not
                            if (ch.isalpha()):
                                word += ch
                            else:
                                # only append the word to the list if of length 5
                                if len(word) == 5:
                                    list.append(word.lower() + "\n")
                                    word = ""
                
                # sort the list
                list = sorted(list)
                # write to the file
                for word in list:
                    w.write(word)

                f.close() # close the file we're reading from
            w.close() # close the file we're writing to

    """ returns if lists are identical or not """
    def compare_lists(self, list1, list2):
        if len(list1) != len(list2):
            print('Lists not of equal size!')
            print('list1 is size -> ' + str(len(list1)))
            print('list2 is size -> ' + str(len(list2)))
            #return False
        else:
            print('Lists are both size -> ' + str(len(list1)))
        
        for i in range(len(list1)):
            # get the items from both lists
            word1 = list1[i]
            word2 = list2[i]

            # get rid of the newlines from them if there are any
            if (word1[:-2] == '\n'):
                word1 = word1[:-2]
            if (word2[:-2] == '\n'):
                word2 = word2[:-2]
            
            # compare the two items
            if (word1 != word2):
                print('items at ' + str(i) + " are not the same!")
                print('list1 item is -> ' + list1[i])
                print('list2 item is -> ' + list2[i])
                return False
        
        print('Lists are identical!')
        return True