import re


def find_name(line):

    # multiple initials + names, not really working well
    # pattern = r"(([A-Z][a-z]+)(?:\s[A-Z][a-z]+)+)|((?:[A-Z]\.)+)\s[A-Z]\w+"

    # multiple capitals together, ie. Billy Kid 
    pattern = r"([A-Z][a-z]+(?=\s[A-Z])(?:\s[A-Z][a-z]+)+)"
    result = re.findall(pattern,line)

    # add more lookups?
    # pattern=r'(October|Oct|November|Nov)( [0-9]{1,2}, [0-9]{4})'
    # result = result + re.findall(pattern,line)

    return result


f = open("little_women.txt")

names = []

for line in f.readlines():
    # print(line)
    # print("name", find_name(line)) 
    result = find_name(line)
    if (len(result)>0):
    #     print(result)
        names.append(result)
         
print(names)

# REGEX TESTS
# working, but won't capture Dr. Adam Driggers
# ((Ms|Mrs|Mr|Colonel|Dr|Miss|Reverend|Professor|Prof)(\.\s|\s))\w+|([A-Z][a-z]+\s[A-Z][a-z]+)

# multiple capitals together, will get Dr Adam Driggers, but not working with Dr.
# ([A-Z][a-z]+(?=\s[A-Z])(?:\s[A-Z][a-z]+)+)

# (((Mr|Ms|Mrs|Mr|Colonel|Dr|Miss|Reverend|Professor|Prof)(\.\s|\s))|[A-Z][a-z]+)(?=\s[A-Z])(?:\s[A-Z][a-z]+)

# get 0 to 1 of the perfixes, with or without the period
# ((Mr|Ms|Mrs|Mr|Colonel|Dr|Miss|Reverend|Professor|Prof)(\.|\s)+?)*

# an initial
# ([A-Z]\.\s)*

# best so far? Doesnt capture Dr. S. Howard
# ((Mr|Ms|Mrs|Mr|Colonel|Dr|Miss|Reverend|Professor|Prof)(\.|\s)+?)*([A-Z]\w+)(?:\s[A-Z][a-z]+)*

#two names or an initial followed by a name
# (([A-Z][a-z]+)(?:\s[A-Z][a-z]+)+)|([A-Z]\.\s[A-Z]\w+)

# prefix only or prefix and initial, or iniital only
# ((((Mr|Ms|Mrs|Mr|Colonel|Dr|Miss|Reverend|Professor|Prof)(\.\s|\s))|([A-Z]\.)){0,2})

# full name, or multiple intials plus a name
# (([A-Z][a-z]+)(?:\s[A-Z][a-z]+)+)|((?:[A-Z]\.)+)\s[A-Z]\w+

# referenced this...
# https://stackoverflow.com/questions/9525993/get-consecutive-capitalized-words-using-regex
