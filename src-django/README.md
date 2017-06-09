# To setup a new environment:
1. Install python : [Windows](https://www.python.org/ftp/python/3.6.1/python-3.6.1.exe)
2. Use virtual environment if you don't want to mess up your existing python environment:
   - Pick any directory outside this repo, for example c:\Temp\venv\
   - Create: `python -m venv env`
   - Activate: `c:\Temp\venv\env\Scripts\activate.bat`
   - Deactivate: `deactivate`
3. Install packages
   - (In 'src-django' dir) `python -m pip install -r requirements.txt`

# Run a clean app:
In 'myproj' dir

```
del db.sqlite3
python manage.py migrate
python manage.py collectstatic
python manage.py runserver [port]
```


Explain of each command:
- `del db.sqlite3` To remove existing database file
- `python manage.py migrate` To create a new database file
- `python manage.py collectstatic` To prepare static files (for nginx)
- `python manage.py runserver [port]` To run the server at given port or 8000 default.

