def Available_letters(letter_storage):
    string=''
    count=0
    s='abcdefghijklmnopqrstuvwxyz'
    for letter in s:
        if letter in letter_storage:
            count+=1
        else:
            string+=letter
    return string

