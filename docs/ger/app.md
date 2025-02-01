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
    > Ein Match-Case für die verschiedenen Anzahlen der Eingabe Parameter.
9. ```python
            case 3:
    ```
    > Wenn es 3 Parameter sind wird nicht übersetzt.
10. ```python
                languages.sync()
    ```
    > Die Dateiendungen und dazugehörigen Programmiersprachen werden gesynct.
11. ```python
                glue.together(*params)
    ```
    > Dann die Markdown Datei erstellen.
12. ```python
            case 5:
    ```
    > Wenn es 5 Parameter sind wird übersetzt.
13. ```python
                languages.sync()
    ```
    > Die Dateiendungen und dazugehörigen Programmiersprachen werden gesynct.
14. ```python
                translate_params = [params[1], params[4], params[3]]
    ```
15. ```python
                if not translator.translate(*translate_params):
    ```
    > Gleichzeitiges Übersetzen und checken ob das geklappt hat.
16. ```python
                    return
    ```
17. ```python
                glue_params = [params[0], params[4], params[2]]
    ```
18. ```python
                glue.together(*glue_params)
    ```
    > Dann die Markdown Datei erstellen.
19. ```python
            case _:
    ```
    > Sonst wurde das Tool falsch aufgerufen.
20. ```python
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
