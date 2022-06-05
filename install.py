import requests
import shutil
import os
file = input('Name: ')
url = 'https://raw.githubusercontent.com/fantasia-wizard/comp-repo/main/' + file
print('Searching...')
r = requests.get(url, allow_redirects=True)
if not (r.content == b'404: Not Found'
 or r.content == b'400: Invalid request'):
    print('Installing...')
    open('./' + file, 'wb').write(r.content)
    print(r.content)
else:
    if file == 'magic_stick':
        print('Downloading...')
        url = 'https://github.com/surajsinghbisht054/MagicStick_Editor/archive/refs/heads/master.zip'
        r = requests.get(url, allow_redirects=True)
        print('Installing...')
        open('./' + file + '.zip', 'wb').write(r.content)
        shutil.unpack_archive('./' + file + '.zip', './')
        os.chdir('MagicStick_Editor-master')
        for x in os.listdir():
            shutil.move(x, "../")
        os.chdir('..')
        os.rename('./main.py', './magic_stick.py')
        os.remove('./magic_stick.zip')
        os.remove('.gitignore')
        os.rmdir('./MagicStick_Editor-master')
    else:
        print('Error: package not found.')
print('Finished!')
