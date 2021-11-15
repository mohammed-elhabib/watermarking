def get_watermark():
    text = input("enter a string to convert into ascii values:")
    ascii_values = []
    for character in text:
        ascii_values.append(ord(character))
    print(ascii_values)
    return ascii_values
