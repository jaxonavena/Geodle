def compare_letter(self, guess):
    guess_letter = guess.get_name()[0]
    secret_letter = self.secretguess.get_name()[0]

    alphabet = list(string.ascii_uppercase)
    letter_index = 0
    if guess_letter == secret_letter:
        return 'green'
    elif guess_letter in alphabet:
        for letter in alphabet:
            if guess_letter == letter:
                letter_index = alphabet.index(letter)
        if letter_index < 4:
            for letter in alphabet[0:letter_index + 5:1]:
                if secret_letter == letter:
                    return 'yellow'
        elif letter_index > 20:
            for letter in alphabet[(letter_index - 5):25:1]:
                if secret_letter == letter:
                    return 'yellow'
        else:
            for letter in alphabet[(letter_index - 5):(letter_index + 5):1]:
                if secret_letter == letter:
                    return 'yellow'
    else:
        return 'gray'


