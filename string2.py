
# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.

def verbing(s):
  if len(s) >= 3:
        if s.endswith('ing'):
            return s + 'ly'
        else:
            return s + 'ing'
        
        # E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!

def not_bad(s):
    not_index = s.find('not')
    bad_index = s.find('bad')
    
    if not_index != -1 and bad_index != -1 and bad_index > not_index:
        return s[:not_index] + 'good' + s[bad_index + 3:]
    
    # F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

def front_back(a, b):
    # Helper function to split a string into two halves
    def split_string(s):
        mid = (len(s) + 1) // 2  # Extra char goes to the front half if length is odd
        return s[:mid], s[mid:]
    
    a_front, a_back = split_string(a)
    b_front, b_back = split_string(b)
    
    return a_front + b_front + a_back + b_back
