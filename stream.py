import re
for test_string in ['num', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print (test_string, 'is a valid local phone number')
    else:
        print (test_string, 'rejected')