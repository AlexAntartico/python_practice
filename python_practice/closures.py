# Hola 3 -> HolaHolaHola
# Facundo 2 -> FacundoFacundo
# Platzi 4 -> PlatziPlatziPlatziPlatzi


from timeit import repeat


def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utiliazar cadenas"
        return string * n
    return repeater


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola"))
    repeat_5 = make_repeater_of(10)
    print(repeat_5("Platzi"))


if __name__ == '__main__':
    run()