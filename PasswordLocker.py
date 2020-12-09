import pickle,pyperclip
import os.path

file_exists = os.path.isfile("PasswordLockersave.txt")  #returns a boolean value
if not file_exists:
    with open("PasswordLockersave.txt",'w'):
        pass

account=input("Please enter the account name")
with open("PasswordLockersave.txt", 'rb') as rfp: #file handling object

    objs = {}
    while 1:
        try:
            objs.update(pickle.load(rfp))
        except EOFError:
            break
if account in objs:
    pyperclip.copy(objs[account])
    print('Password for ' + account + ' copied to clipboard.')

else:
    new_dict={}
    print('There is no account named ' + account)
    password1=input('please enter password for' + account)
    new_dict={account:password1}
    with open("PasswordLockersave.txt", 'ab') as rfp1:
        pickle.dump(new_dict, rfp1)
        rfp1.close()

    pyperclip.copy(new_dict[account])
    print('Password for ' + account + ' copied to clipboard.')
