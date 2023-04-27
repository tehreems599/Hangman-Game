import GuessWord
import AvailableLetters
letter_storage=[]
def hangman(secret_word):
    length=len(secret_word)
    print("I have chosen a word which is", length, 'letters long.')
    print('You have 3 warnings left')
    print(secret_word)
    guess,warning=6,3
    while guess>0:
        print('******************')
        if secret_word!= GuessWord.GuessedWord(secret_word,letter_storage):
            print('You have',guess,'guesses left')
            print('Available Letters are:', AvailableLetters.Available_letters(letter_storage))
            guess_taken=input('Please guess a letter:').lower()

            if not guess_taken.isalpha(): 
                 print('Oops! that is an invalid letter')
                 if warning==0:
                   guess-=1
                   print('Sadly, you have no warnings left so you lose one guess:',GuessedWord(secret_word,letter_storage))
                 else:
                   warning-=1
                   print('You have ',warning,'warnings left:',GuessWord.GuessedWord(secret_word,letter_storage))
            elif guess_taken in letter_storage:
                  print("Oops! You\'ve already guessed that letter")
                  if warning==0:
                        guess-=1
                        print('You have no warnings left so you lose one guess:',GuessWord.GuessedWord(secret_word,letter_storage))
                  else:
                        warning-=1
                        print('You have',warning,'warnings left:',GuessWord.GuessedWord(secret_word,letter_storage))
            
            elif guess_taken not in secret_word:
                letter_storage.append(guess_taken)
                print('Oops! That letter is not in my word',GuessWord.GuessedWord(secret_word,letter_storage))
                if guess_taken not in 'aeiou':
                    guess-=1
                elif guess_taken in 'aeiou':
                    guess-=2
            else:
                  letter_storage.append(guess_taken)
                  print('Good guess:', GuessWord.GuessedWord(secret_word,letter_storage))
        elif secret_word==GuessWord.GuessedWord(secret_word,letter_storage):
               print('Congratulations you won!')
               print('Your score is:',guess*len(set(secret_word)))
               break
    else:
         print('******************')
         print('Sorry! You ran out of guesses')
         print ('The correct word was', secret_word)
