# docglueMenD

> **🚧 Work in Progress (WIP):** This project is currently under active development and refactoring. Core single-file merging and translation work as described below, while automated project-wide workflows and CLI improvements are actively being built.

**docglueMenD** is a Python-based CLI tool designed to create Markdown files with syntax-highlighted code lines and associated comments. It keeps inline explanations separate from your actual source code so your codebase stays clean and readable.

## Features

- **Syntax Highlighting**: Automatically detects the programming language based on file extensions and applies syntax highlighting in Markdown.
- **Separate Comment Files**: Keeps comments in a separate file, ensuring your code remains clean and uncluttered.
- **Translation Support**: Integrates with [deep_translator](https://github.com/nidhaloff/deep-translator) to translate comments from your chosen language into English.
- **Cross-Platform**: Works on Windows, macOS, and Linux.
- **Easy to Use**: Simple command-line interface for generating Markdown files.

## Roadmap & Planned Features

The following features are currently planned and in progress:

- **Mirror Directory Generation (`create_structure`)**: Run `docgluemend create_structure [target_dir]` to automatically generate a mirrored directory tree of empty comment files inside `comments/` (defaults to the current directory if no path is provided).
- **Ignore Rules (`.glueignore`)**: Support a `.glueignore` file (similar to `.gitignore`) to exclude specific folders, files, or patterns when generating the comment structure.
- **Zero-Config Project Aggregation (`docgluemend`)**: Running `docgluemend` without arguments will automatically detect a `comments/` directory (including language subdirectories like `en/`, `ger/`, etc.) and generate all corresponding Markdown outputs into `gluements/`.
- **Simplified Single-File Mode**: Run `docgluemend <code_file>` to automatically resolve the matching file in `comments/` and output the merged result to `gluements/` without manually specifying all file paths.

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
