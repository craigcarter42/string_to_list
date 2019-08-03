#/usr/bin/env python

path = '/Users/admin/Projects/tmp/schedule.conf'
expected = ['monday', 'tuesday', 'wednesday']
found = {}
unexpected = {}
new_list = []

try:
    fh = open(path, mode='r')
    data = fh.readlines()
    fh.close()
except Exception, error_msg:
    print('error:\n{}'.format(error_msg)); quit()

head = 4
tail = 0
count = 0

def convert_to_int(data):
    try:
        data = int(data)
    except:
        print('could not convert to int:\n -> {}'.format(data))
        quit()
    return(data)

for d in data:
    if ':' in d and '#' not in d:
        new_key = d.split(':')[0].rstrip('\n').lstrip()
        new_value = d.split(':')[1].rstrip('\n').lstrip()
        if new_key in expected:
            if new_value.startswith('[') and new_value.endswith(']'):
                new_value = new_value.replace('[', '')
                new_value = new_value.replace(']', '')
                total = len(new_value)
                new_list.append(convert_to_int(new_value[tail:head]))
                while(count <= total):
                    shift = head - 1
                    if new_value[tail:head] == ', ':
                        tail = head
                        head = head + 4
                        new_list.append(convert_to_int(new_value[tail:head]))
                        
                    elif new_value[tail:shift] == ',':
                        tail = head - 1
                        head = head + 3
                        new_list.append(convert_to_int(new_value[tail:head]))

                    else:
                        tail = head
                        head = head + 2
                    count = count + 2
                found.update({new_key : new_list})
            else:
                found.update({new_key : new_value})
        else:
            unexpected.update({new_key : new_value})

for key, value in found.items() :
    print('  > {} = {}'.format(key, value))

mon = found['monday']
for m in  mon:
    print(' > {}'.format(m))
