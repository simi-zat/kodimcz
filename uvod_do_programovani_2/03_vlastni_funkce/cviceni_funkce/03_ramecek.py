def udelej_ramecek(text):
    print("*" * (len(text) + 4))
    print("* " + text + " *")
    print("*" * (len(text) + 4))


def udelej_ramecek_bonus(text, symbol):
    print(symbol * (len(text) + 4))
    print(symbol + " " + text + " " + symbol)
    print(symbol * (len(text) + 4))


udelej_ramecek("ahoj")
udelej_ramecek_bonus("ahoj", "#")
