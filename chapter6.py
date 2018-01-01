"""Let’s continue to concentrate on Sarah’s data for now. You were to strike
out the code that you no longer needed and replace it with new code that uses
a dictionary to hold and process Sarah’s data."""

class Athlete:
    def __init__(self,a_name,a_dob=None,a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
    def top3(self):
        return (sorted(set([sanitize(t) for t in self.times]))[0:3])
    def add_time(self,time_value):
        self.times.append(time_value)
    def add_times(self,list_of_times):
        self.times.extend(list_of_times)

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
        templ = data.strip().split(',')
        return (Athlete(templ.pop(0),templ.pop(0),templ))
    except IOError as ioerr:
        print('File error: '+ str(ioerr))
        return(None)
# Use the function to turn sarah's data file into a list,
# and then assign it to the "sarah" variable.
vera = Athlete('Vera Vi')
vera.add_time('1.31')
print(vera.top3())
vera.add_times(['2.22','1-21','2:22'])
print(vera.top3())

james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')
# 4) Call the function for an athlete and adjust the 'print()' statement as needed
print(james.name + "'s fastest times are: " + str(james.top3()))
print(julie.name + "'s fastest times are: " + str(julie.top3()))
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))
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
