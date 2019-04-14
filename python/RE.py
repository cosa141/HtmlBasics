import re

patterns=['term1','term2']
text= 'this is a string with term1 and term2'
for pattern in patterns:
    print('im searching for: '+ pattern)
    if re.search(pattern,text):
        print('match!')
    else:
        print('no match..')
        #this time its missing the second pattern
text= 'this is a string with term1 and pies'
for pattern in patterns:
    print('im searching for: '+ pattern)
    if re.search(pattern,text):
        print('match!')
    else:
        print('no match..')
match = re.search('this', text)
#to get the start location of the term we are searching for
print(match.start())
#to get the start and end location of the term
print(match.span())
#to get back all the times a match appears use len() to get back int
print(re.findall('match', 'test phrase match with match more than once'))


def multi_re_find(patterns,phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print('Searching the phrase using the re check: {}'.format(pattern))
        print(re.findall(pattern,phrase))
        print('\n')
test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
test_patterns = [ 'sd*',        # s followed by zero or more d's dont use loool
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{1,3}',      # s followed by two to three d's
                's[sd]+'        # s followed by one or more s or d
                ]
multi_re_find(test_patterns,test_phrase)

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
testPat2 = ['[^!.?]+']
# Use [^!.? ] to check for matches that are not a !,.,?, or space. Add the +
# to check that the match appears at least once, this basically translate into
# finding the words.
multi_re_find(testPat2,test_phrase)
test_phrase2 = 'This is an example sentence. Lets see if we can find some letters.'
test_patterns2=[ '[a-z]+',     # sequences of lower case letters
                '[A-Z]+',      # sequences of upper case letters
                '[a-zA-Z]+',   # sequences of lower or upper case letters
                '[A-Z][a-z]+'] # one upper case letter followed by lower case letters

multi_re_find(test_patterns2,test_phrase2)

test_phrase3 = 'This is a string with some numbers 1233 and a symbol #hashtag'

test_patterns3=[r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ]

multi_re_find(test_patterns3,test_phrase3)
