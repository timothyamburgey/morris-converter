from morris_converter import MorrisCodeConverter as Converter

continue_app = True

while continue_app:
    user_text = input("Enter the text to convert:")
    print(Converter.convert_text(user_text))
    if input("Convert another text (y/n):") == 'n':
        break
