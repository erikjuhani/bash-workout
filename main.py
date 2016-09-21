import sys
import time

def clear_window():
    for i in range(40):
        print('')

def read(fn):
    pass

def read_file(fn):
    file = open(fn, 'r')
    return file.read().split('\n')

def write_file(fn, w):
    file = open(fn, 'w')
    file.write(w)

def write(fn, w):
    lines = read_file(fn)
    lines.append(w)
    for i in range(len(lines)-1):
        lines[i] += '\n'
    file = open(fn, 'w')
    file.writelines(lines)

def get_day(fn):
    file = read_file(fn)
    return int(file[0].replace(' ','').split(':').pop())

now      = time.strftime('%c')
filetype = '.txt'
filepath = '/'
logpath  = '/logs/'
fn = 'w' + filetype
fe = False
config = 'conf' + filetype
record = 'record' + filetype
day    = get_day(config)

# Checks for config file
try:
    file = open(config, 'r')
except IOError:
    print('Error, cannot find \'config.txt\' file.')
    print('Quitting program.')
    sys.exit()

# Creates record file if it does not exist
try:
    file = open(record, 'r')
except IOError:
    file = open(record, 'w')
    file.write('')

default_workout = [
                ['Pushups', 10],
                ['Squats', 20],
                ['Inverted pushups', 10],
                ['Plank', 30],
                ['Chin ups', 2],
                ['Pull ups', 1],
           ]

user_workout = []

def load_workouts():
    file_exists = False
    fn = 'workouts' + filetype
    try:
        file = open(fn, 'r')
        #print(fn + ' exists, opening file...')
        file_exists = True
    except IOError:
        print('Error, ' + fn + ' does not exist.')
        file_exists = False

    if file_exists:
        lines = file.read().split('\n')
        i = len(lines)
        print('\nLoading workouts...')
        for n in lines:
            i -= 1
            if i > 0:
                user_workout.append(n.replace(' ', '').split('-'))

    if not file_exists:
        i = input('Create default \'workouts.txt\'? (y/n)\n').lower()

        if 'y' in i:
            print('\nCreating a new default \'workouts.txt\' file...')
            file = open(fn, 'w');
            for w in default_workout:
                file.write(w[0] + ' - ' + str(w[1]) + '\n')
                print('+ ' + w[0] + ' - ' + str(w[1]))
        else:
            'Quitting program.'
            return

def start_workout(day):
    print('Current time is: ' + now)
    a = input('Start workout? (y/n)\n')
    if 'y' in a:

        write(record, '\nDAY ' + str(day) + ' --- ' + now)
        clear_window()

        base_mult = 1.05
        mult = 1.0
        i = 0;

        for i in range(day):
            mult *= base_mult

        for w in user_workout:
            i += 1
            tabs = ''
            string_size = len(w[0])
            if string_size > 6 and string_size < 14:
                tabs = '\t\t'
            elif string_size > 14:
                tabs = '\t'
            else:
                tabs = '\t\t\t'
            workout = round(float(w[1]) * mult)
            if workout < 10:
                workout = ' ' + str(workout)
            print(' ' + w[0] + tabs + str(workout))
            input('---------------------------')
            write(record, w[0] + ' - ' + str(workout))
            print('-----------DONE------------')
            print('---------------------------')
            print('')
        day += 1
        write_file(config, 'Day: ' + str(day))
    return;

'''
def make_record():
    pass

def add_workout():
    pass
def delete_workout():
    pass
def change_workout():
    pass
'''

load_workouts()
start_workout(day)

'''
def write_file():
    pass

try:
    file = open(fn, 'r')
    print(fn + ' exists, opening file...')
    fe = True
except IOError:
    file = open(fn, 'w')
    print(fn + ' does not exist, creating file...')

if fe and not file.read() == '':
    print('File was found')
else:
    print('Writing workouts to file...')
    file = open(fn, 'w')

    for w in default_workout:
        file.write(w[0] + ' - ' + str(w[1]) + '\n')
        print('+ ' + w[0] + ' - ' + str(w[1]))
'''
