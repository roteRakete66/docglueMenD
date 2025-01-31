import sys

from helpers import glue, languages, translator


def main():
    params = sys.argv[1:]
    match len(params):
        case 3:
            languages.sync()
            glue.together(*params)
        case 5:
            languages.sync()
            translate_params = [params[1], params[4], params[3]]
            if not translator.translate(*translate_params):
                return
            glue_params = [params[0], params[4], params[2]]
            glue.together(*glue_params)
        case _:
            print(glue.WRONG_USAGE)


if __name__ == "__main__":
    main()
