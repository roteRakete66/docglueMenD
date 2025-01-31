# docglueMenD

**docglueMenD** is a Python-based tool designed to create Markdown files with syntax-highlighted code lines and associated comments. It is particularly useful for developers who want to document their code in a clean and organized way.

## Features

- **Syntax Highlighting**: Automatically detects the programming language based on file extensions and applies syntax highlighting in Markdown.
- **Separate Comment Files**: Keeps comments in a separate file, ensuring your code remains clean and uncluttered.
- **Translation Support**: Integrates with [deep_translator](https://github.com/nidhaloff/deep-translator) to translate comments from your chosen language into english.
- **Cross-Platform**: Works on Windows, macOS, and Linux.
- **Easy to Use**: Simple command-line interface for generating Markdown files.

## Agenda

### Planned Feature(s)
- Automatically generate a doc folder with the same tree as the project and create all doc files with one command.

## Installation

To use **docglueMenD**, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/roteRakete66/docglueMenD.git
   cd docglueMenD
   ```
2. **Install Dependencies**:

   Make sure you have [Poetry](https://python-poetry.org/) installed. Then run:
   ```bash
   poetry install
   ```

## Usage

To generate a Markdown file from your code and your comment, run the following command:
```bash
poetry run python docgluemend\app.py <code_file> <comment_file> <doc_file> [language en_comment_out_file]
```
If you do not specify a language, the files are simply merged (glued).

If you specify a language, this must be the language in which your comments are written. Because these will be translated into English. An English commentary file is also created for this purpose. The doc file here is then also the markdown with English comments.

### Characteristic

The comment files may have at most as many lines as the code file they comment on, but they may be smaller.

**Each respective line comments the corresponding line in the code file.**

It is therefore normal to have several empty lines. Ensure that your IDE does not automatically format the comment file type, as this may disrupt the line-by-line correspondence with the code file.Speaking of comment file type, you can choose it freely. I also use markdown files here (i.e. .md extension), but that doesn't matter.

## Examples

### Usage

```bash
poetry run python docgluemend\app.py code.py comments.md doc.md 
```
For just *glue*

```bash
poetry run python docgluemend\app.py code.py comments.md en_doc.md german en_comments.md
```
To create the translated files from German .

### Output

Just look at the [docs](docs/) folder in this repo to see examples.

## Supported Languages

**docglueMenD** supports syntax highlighting for a wide range of programming languages. The supported languages are based on the [GitHub Linguist](https://github.com/github/linguist) library.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [deep_translator](https://github.com/nidhaloff/deep-translator) for providing translation support.
- Inspired by the need for better code documentation tools.

---

**Enjoy using docglueMenD!** 🚀
