def GuessedWord(secret_word,letter_storage):
    guess_word=''
    for char in secret_word:
        if char in letter_storage:
            guess_word+=char
        else:
            guess_word+='_ '
    return guess_word

