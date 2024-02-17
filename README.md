# djangolancer!!


## Anlayses cod by pylint

Pylint is a static code analyser for Python.
Pylint analyses your code without actually running it. It checks for errors, enforces a coding standard, looks for code smells, and can make suggestions about how the code could be refactored.

```sh
cd backend
pylint --load-plugins pylint_django --fail-under=9 --django-settings-module=midlancer.settings <MODULENAME>
```

Please edit .pylintrc for ignoring folder.

