from docgluemend.helpers import languages, parameter_handler

FOOT = "    - <sub> This doc-view was created by [docglueMenD](https://github.com/roteRakete66/docglueMenD)</sub>\n"
WRONG_USAGE = "Usage: docgluemend <code_file> <comment_file> <doc_file> [language en_comment_out_file]"


def together(code_file_path, comment_file_path, glued_file_path):
    if not parameter_handler.permission(glued_file_path):
        return
    try:
        with (
            open(code_file_path, "r", encoding="utf-8") as code_file,
            open(comment_file_path, "r", encoding="utf-8") as comment_file,
            open(glued_file_path, "w", encoding="utf-8") as out_file,
        ):
            code_lines_count = lines_count(code_file)
            comment_lines_count = lines_count(comment_file)
            if code_lines_count < comment_lines_count:
                print(
                    "Your comment_file must have at most as many lines as your code_file."
                )
                print(WRONG_USAGE)
                return
            language = languages.get_string(code_file_path)
            both(
                code_file,
                language,
                code_lines_count,
                comment_file,
                comment_lines_count,
                out_file,
            )
            out_file.write(FOOT)
    except OSError as e:
        print(f"An error occurred: {e}")


def both(
    code_file, language, code_lines_count, comment_file, comment_lines_count, glued_file
):
    for line_count, (code_line, comment_line) in enumerate(
        zip(code_file, comment_file), start=1
    ):
        glued_file.write(line(line_count, code_line, language, comment_line))
    if code_lines_count == comment_lines_count:
        return
    to_position(code_file, comment_lines_count)
    for line_count, code_line in enumerate(code_file, start=comment_lines_count + 1):
        glued_file.write(line(line_count, code_line, language, "\n"))


def line(line_count, code_line, language, comment_line):
    line = body_line(line_count, code_line, language)
    if comment_line == "\n":
        return line
    return line + body_comment_line(line_count, code_line, comment_line)


def lines_count(file):
    count = sum(1 for _ in file)
    file.seek(0)
    return count


def to_position(file, line_count):
    file.seek(0)
    for _ in range(line_count):
        file.readline()


def body_line(line_count, line, language):
    return f"{line_count}. ```{language}\n    {line}    ```\n"


def body_comment_line(line_count, code_line, comment_line):
    return f"    > {comment_line}"
