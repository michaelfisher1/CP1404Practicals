from Prac07.programminglanguage import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby","Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1995)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(ruby)
    print(python)
    print(vb)
    languages = [ruby,python,vb]
    print(["{}".format(language.name) for language in languages if language.is_dynamic()])
    print("The dynamically typed languages are: ")
    for language in languages:
        if language.is_dynamic():
            print("{}".format(language.name))
main()