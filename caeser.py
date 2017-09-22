
def alphabet_position(letter):
    value = ""

    value = ord(letter.lower())-97

    return value

def rotate_character(char, rot):
    value = ""
    is_uppercase = False
    if 64<ord(char)<91 or 96<ord(char)<123:
        if 64<ord(char)<91:
            is_uppercase = True

        value = chr(((alphabet_position(char)+rot)%26)+97)
        
        if is_uppercase: 
            value = value.upper()
    else:
        value = char

    return value

def rotate_string(text, rot):
    value = ""
    for char in text:
        value += rotate_character(char, rot)
    return value


def main():
    text = input("Type a message:")
    rot = input("Rotate by:")

    print(encrypt(text, rot))

if __name__ == "__main__":
    main()

