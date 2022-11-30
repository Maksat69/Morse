from alphabets import Morse

morse = Morse()
ask = input('Please write text! ')
to_morse = morse.morse_generator(ask)
print(f'This is morse: {to_morse}')
print(f'This is decoder: {morse.morse_decoder(to_morse)}')
