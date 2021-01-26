import requests
from termcolor import colored

file1 = open('BTClist.txt', 'r')
Lines = file1.read().splitlines()
for line in Lines:
    print line
    data = {'address': {line}}
    response = requests.post('https://allprivatekeys.com/check_address.php', data)
    if response.text.__contains__("Congratulation!"):
        print colored("Not Leaked", "green")
    else:
        print colored("Leaked", "red")
file1.close()
