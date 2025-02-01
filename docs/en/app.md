1. ```python
    import sys
    ```
2. ```python
    
    ```
3. ```python
    from helpers import glue, languages, translator
    ```
4. ```python
    
    ```
5. ```python
    
    ```
6. ```python
    def main():
    ```
7. ```python
        params = sys.argv[1:]
    ```
8. ```python
        match len(params):
    ```
    > A match case for the different numbers of input parameters.
9. ```python
            case 3:
    ```
    > If there are 3 parameters it will not be translated.
10. ```python
                languages.sync()
    ```
    > The file extensions and associated programming languages ​​are synced.
11. ```python
                glue.together(*params)
    ```
    > Then create the Markdown file.
12. ```python
            case 5:
    ```
    > If there are 5 parameters it will be translated.
13. ```python
                languages.sync()
    ```
    > The file extensions and associated programming languages ​​are synced.
14. ```python
                translate_params = [params[1], params[4], params[3]]
    ```
15. ```python
                if not translator.translate(*translate_params):
    ```
    > Translate at the same time and check whether it worked.
16. ```python
                    return
    ```
17. ```python
                glue_params = [params[0], params[4], params[2]]
    ```
18. ```python
                glue.together(*glue_params)
    ```
    > Then create the Markdown file.
19. ```python
            case _:
    ```
    > Otherwise the tool was called incorrectly.20. ```python
                print(glue.WRONG_USAGE)
    ```
21. ```python
    
    ```
22. ```python
    
    ```
23. ```python
    if __name__ == "__main__":
    ```
24. ```python
        main()
    ```
    - <sub> This doc-view was created by [docglueMenD](https://github.com/roteRakete66/docglueMenD)</sub>
