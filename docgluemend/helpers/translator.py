from deep_translator import GoogleTranslator
from helpers import glue, parameter_handler


def translate(source_file_path, out_file_path, source_lang):
    if not parameter_handler.permission(out_file_path):
        return False
    try:
        with (
            open(source_file_path, "r") as source_file,
            open(out_file_path, "w") as out_file,
        ):
            lines_count = glue.lines_count(source_file)
            for line_count, comment in enumerate(source_file, start=1):
                translated_content = GoogleTranslator(
                    source=source_lang, target="en"
                ).translate(comment)
                out_file.write(translated_content)
                if lines_count > line_count:
                    out_file.write("\n")

    except IOError as e:
        print(f"An error occurred: {e}")
    return True
