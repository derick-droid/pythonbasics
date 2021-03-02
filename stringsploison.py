# Given a non-empty string like "Code" return a string like "CCoCodCode".
#
# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'

def string_splosion(str):
    result = ""
    for itmes in str:
        if len(str) <= 1:
            print(str)
        elif len(str) > 1:
            print((str[0] * 2) + str[1] + str[-1])



pop = string_splosion("abc")