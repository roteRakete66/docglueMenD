from helpers import languages, parameter_handler

FOOT = "    - <sub> This doc-view was created by [docglueMenD](https://github.com/roteRakete66/docglueMenD)</sub>\n"
WRONG_USAGE = (
    "Usage: python app.py <code_file> <doc_file> <out_file> [language en_doc_out_file]"
)


def together(code_file_path, doc_file_path, out_file_path):
    if not parameter_handler.permission(out_file_path):
        return
    try:
        with (
            open(code_file_path, "r") as code_file,
            open(doc_file_path, "r") as doc_file,
            open(out_file_path, "w") as out_file,
        ):
            code_lines_count = lines_count(code_file)
            doc_lines_count = lines_count(doc_file)
            if code_lines_count < doc_lines_count:
                print(
                    "Your doc_file must have at most as many lines as your code_file."
                )
                print(WRONG_USAGE)
                return
            language = languages.get_string(code_file_path)
            both(
                code_file,
                language,
                code_lines_count,
                doc_file,
                doc_lines_count,
                out_file,
            )
            out_file.write(FOOT)
    except IOError as e:
        print(f"An error occurred: {e}")


def both(code_file, language, code_lines_count, doc_file, doc_lines_count, out_file):
    for line_count, (code_line, doc_line) in enumerate(
        zip(code_file, doc_file), start=1
    ):
        out_file.write(line(line_count, code_line, language, doc_line))
    if code_lines_count == doc_lines_count:
        return
    to_position(code_file, doc_lines_count)
    for line_count, code_line in enumerate(code_file, start=doc_lines_count + 1):
        out_file.write(line(line_count, code_line, "\n"))


def line(line_count, code_line, language, doc_line):
    line = body_line(line_count, code_line, language)
    if doc_line == "\n":
        return line
    return line + body_doc_line(line_count, code_line, doc_line)


def lines_count(file):
    count = sum(1 for _ in file)
    file.seek(0)
    return count


def to_position(file, line_count):
    file.seek(0)
    for _ in range(line_count):
        file.readline()


def body_line(line_count, line, language):
    return f"{line_count}. ```{language}\n    {line}\n    ```\n"


def body_doc_line(line_count, code_line, doc_line):
    return f"    > {doc_line}\n"
