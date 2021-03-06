"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path)
    text_string = ""

    for line in file:
    	line = line.strip(" ")
    	text_string += line 
    # print(text_string)

    return text_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two 
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}
    text_string = text_string.split()


    for word in range(len(text_string)-2):
    	#making tuples out of each  pair of consecutive words in the string
    	word_key = (text_string[word],text_string[word+1])

    	#values in the dictionary will be lists of possible consecutive words
    	if word_key in chains:
    		chains[word_key] += [text_string[word+2]]
    	else:
    		chains[word_key] = [text_string[word+2]]

    return chains

def make_chains_n(text_string,n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two 
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}
    text_string = text_string.split()


    for word in range(len(text_string)-n):
    	#making tuples out of each  pair of consecutive words in the string
    	#word_key = (text_string[word],text_string[word+1])
    	word_key = ()

    	# make tuple out of 2 consecutive words using loop
    	# need to make it so that each time it takes 2 DIFFERENT indexes

    	for index in range(word, word+n):
    	    word_key = word_key + (text_string[index],)

    	#values in the dictionary will be lists of possible consecutive words
    	if word_key in chains:
    		chains[word_key] += [text_string[word+n]]
    	else:
    		chains[word_key] = [text_string[word+n]]

    return chains







def make_text(chains):
    """Return text from chains.
    The function gets the dictionary "chains" as an input, 
    and returns a text as a string of randomized words as output. 
    The text is built in a way that every 2 consecutive words fit together.
    (bigrams) 
		
    """

    words = []

    key = choice(list(chains.keys()))
    word1 = key[0]
    word2 = key[1]

    words.append(word1)
    words.append(word2)
    
    while key in chains:
    	value = chains[key]
    	word3 = choice(value)

    	words.append(word3)
    	key = (word2, word3)
    	word2 = word3
    

    return " ".join(words)


def make_text_n(chains):
    """Return text from chains.
    The function gets the dictionary "chains" as an input, 
    and returns a text as a string of randomized words as output. 
    The text is built in a way that every n consecutive words fit together. 
    (n-grams)
		
    """

    words = []

    key = choice(list(chains.keys()))
    words.extend(key)

    while key in chains:
    	value = chains[key]
    	new_word = choice(value)
    	# adding new randomized word to our output list
    	words.append(new_word)
    	# making new key, without the first item in old key and adding the new word
    	new_key = ()
    	for word in range(1, len(key)):
    		new_key += (key[word],)
    	key = new_key
    	key += (new_word,)
    	
    

    output_text = " ".join(words)
    return output_text.capitalize()


#input_path = "gettysburg.txt"
input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

#print(random_text)
chains_n = make_chains_n(input_text,5)

random_text_n = make_text_n(chains_n)
print(random_text_n)


