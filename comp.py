#!/bin/python3
import os
import json
import subprocess
import requests
root_passwd = ''
users = {}
username = 'root'
hostname = ''
cwd = '/'
new_user = True
dir = os.getcwd()
ask_cmd = True
while True:
    new = input('Is this your first time? (Y/n): ')
    if new == '':
        new_user = True
        break
    elif new == 'y' or new == 'Y':
        new_user = True
        break
    elif new == 'n' or new == 'N':
        if os.path.exists('./comp'):
            new_user = False
            break
        else:
            print('Error: saved filesystem not found.  Setting up new user.')
            new_user = True
            break
    else:
        print('Error: Input invalid.  Please try again.')
if new_user:
    print('Welcome, user.')
    print('First, let\'s set up your root account.')
    print('Please type your root password.')
    while True:
        new_root_passwd = input()
        print('Now repeat that password.')
        if input() == new_root_passwd:
            root_passwd = new_root_passwd
            print('Root password set succesfully.')
            break
        else:
            print('Failure, please try again.')
    print('Now let\'s set up your hostname')
    print('Type your hostname.')
    hostname = input()
    users['root'] = root_passwd
    for x in ['./comp', './comp/bin', './comp/home', './comp/home/root', './comp/etc']:
        if not os.path.exists(x):
            os.makedirs(x)
    file = 'install.py'
    url = 'https://raw.githubusercontent.com/fantasia-wizard/comp-repo/main/' + file
    r = requests.get(url, allow_redirects=True)
    open('./comp/bin/' + file, 'wb').write(r.content)
    with open('./comp/etc/passwords.json', 'w') as outfile:
        json.dump(users, outfile)
    file = dir + '/comp/etc/hostname.txt'
    file = open(file, 'w')
    file.write(hostname)
    file.close()
    file = open('./comp/etc/dir.txt', 'w')
    file.write(dir)
    file.close()
else:
    print('Welcome back.')
    with open('./comp/etc/passwords.json') as file:
        users = json.load(file)
    with open('./comp/etc/hostname.txt', 'r') as file:
        for x in file.readlines():
            hostname = x
        file.close()
        file.close()
os.chdir('./comp')

while True:
    if not os.getcwd().startswith(dir):
        os.chdir(dir)
    old_dir = os.getcwd()
    os.chdir(dir + '/comp')
    for x in ['./comp', './comp/bin', './comp/home', './comp/home/root', './comp/etc']:
        if not os.path.exists(x):
            os.makedirs(x)
    os.chdir(old_dir)
    for x in users:
        if not os.path.exists(dir + '/comp/home/' + x):
            os.makedirs(dir + '/comp/home/' + x)
    cwd = os.getcwd().removeprefix(dir + '/comp') + '/'
    if ask_cmd:
        cmd = input('[' + username + '@' + hostname + ' ' + cwd + ' : ] ')
    else:
        ask_cmd = True
    if cmd == 'mkdir':
        new_directory = input('Name: ')
        new_directory = './' + new_directory
        if not os.path.exists(new_directory):
            os.mkdir(new_directory)
        else:
            print('Error: directory exists.')
#    elif cmd == 'install':
#        file = input('Name: ')
#        url = 'https://raw.githubusercontent.com/fantasia-wizard/comp-repo/main/' + file
#        r = requests.get(url, allow_redirects=True)
#        open(dir + '/comp/bin/' + file, 'wb').write(r.content)
    elif cmd == 'touch':
        new_file = input('Name: ')
        new_file = './' + new_file
        file = open(new_file, 'w')
        file.close()
    elif cmd == 'cd':
        file = input('Name: ')
        file = './' + file
        if os.path.exists(file) and not (os.getcwd().endswith('comp') and file.startswith('./..')):
           os.chdir(file)
        else:
            print('Error: Folder not found.')
    elif cmd == 'cat':
        file = input('Name: ')
        file = './' + file
        if os.path.exists(file):
            file = open(file, 'r')
            for x in file.readlines():
                print(x)
            file.close()
        else:
            print('Error: File not found.')
    elif cmd == 'ls':
        for x in os.listdir():
            print(x)
    elif cmd == 'rm':
        file = input('Name: ')
        if os.path.exists('./' + file):
            os.remove(file)
            print('Removed ' + file + '.')
        else:
            print('Error: File not found.')
    elif cmd == 'rm -r':
        file = input('Name: ')
        if os.path.exists('./' + file):
            os.rmdir(file)
            print('Removed ' + file + '.')
        else:
            print('Error: Folder not found.')
    elif cmd == 'useradd':
        user = input('Name: ')
        if not os.path.exists(dir + '/comp/home/' + user):
            os.mkdir(dir + '/comp/home/' + user)
        pass_set = False
        while not pass_set:
            user_password = input('Password: ')
            if input('Please repeat the password: ') == user_password:
                users[user] = user_password
                with open(dir + '/comp/etc/passwords.json', 'w') as outfile:
                    json.dump(users, outfile)
                pass_set = True
            else:
                input_pass = input('Error: Passwords do not match. Try again? (Y/n) ')
                if input_pass == '' or input_pass == 'Y' or input_pass == 'y':
                    print('Try again.')
                else:
                    print('Exiting.')
                    pass_set = True
    elif cmd == 'su':
        user = input('Name: ')
        if user in users:
            input_pass = input('Password for ' + user + ' ')
            if input_pass == users[user]:
                username = user
                os.chdir(dir + '/comp/home/' + username)
            else:
                print('Error: Incorrect password for ' + user)
        else:
            print('Error: User not found.')
    elif cmd == 'exit':
        exit()
    else:
        if cmd.endswith('.py'):
            cmd.removesuffix('.py')
        cmd += '.py'
        if os.path.exists(dir + '/comp/bin/' + cmd):
            prev_location = os.getcwd()
            os.chdir(dir + '/comp/bin/')
            subprocess.call(['python3', dir + '/comp/bin/' + cmd])
            os.chdir(prev_location)
        else:
            print('Error: Command not found.')
            print('Check for typos, or install the command.')
