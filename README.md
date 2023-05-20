# freelancing!!

# پروژه فریلنسری

این پروژه به درخواست شرکت میدکو و بر اساس طراحی های مورد نیاز طراحی و پیاده شده است

## Anlayses cod by pylint

Pylint is a static code analyser for Python.
Pylint analyses your code without actually running it. It checks for errors, enforces a coding standard, looks for code smells, and can make suggestions about how the code could be refactored.

```sh
cd backend
pylint --load-plugins pylint_django --fail-under=9 --django-settings-module=midlancer.settings <MODULENAME>
```

Please edit .pylintrc for ignoring folder.

## Create Fixture

```sh
python -Xutf8 manage.py dumpdata > fixture.json
```

## Test Api

For test api use this command

```sh
python manage.py test user/tests/
python manage.py test user.tests.test_user
```
