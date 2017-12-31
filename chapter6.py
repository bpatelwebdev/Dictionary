"""Let’s continue to concentrate on Sarah’s data for now. You were to strike
out the code that you no longer needed and replace it with new code that uses
a dictionary to hold and process Sarah’s data."""

def sanitize(time_string):
    if'-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins,secs) = time_string.split(splitter)
    return (mins +':'+ secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
# 1)Create a temporary list to hold the data BEFORE creating
# the dictionary all in one go

        templ = data.strip().split(',')
# 2)The dictionary creation code is now part of the function

        return ({'Name':templ.pop(0),
                 'DOB':templ.pop(0),
# 3)The code that determine the top three scored is part of the function,too
                 'Times': str(sorted(set([sanitize(t) for t in templ]))[0:3])

        })
    except IOError as ioerr:
        print('File error: '+ str(ioerr))
        return(None)
# Use the function to turn sarah's data file into a list,
# and then assign it to the "sarah" variable.
james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')
# 4) Call the function for an athlete and adjust the 'print()' statement as needed
print(james['Name'] + "'s fastest times are: " + james['Times'])
print(julie['Name'] + "'s fastest times are: " + julie['Times'])
print(mikey['Name'] + "'s fastest times are: " + mikey['Times'])
print(sarah['Name'] + "'s fastest times are: " + sarah['Times'])
# # The pop() call returns and data from the front of a list. Two calls to "pop(0)"
# # remove the first two data values and assigns them to the named variables.
# (sarah_name,sarah_dob) = (sarah.pop(0),sarah.pop(0))

# # A custom message within the call to "print()" is used to display the results
# # you're after.
# print(sarah_name + 's fastest times are: ' +
#       str(sorted(set([sanitize(t) for t in sarah]))[0:3]))

# sarah_data = {}
# sarah_data['Name'] = sarah.pop(0)
# sarah_data['DOB'] = sarah.pop(0)
# sarah_data['Times'] = sarah
#
# print(sarah_data['Name'] + "'s fastest times are: "+
#       str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))
