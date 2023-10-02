# GUIWttrTextualApp
wttr.in Python Textual UX

# Local Set Up [aka Hacking it]
```bash 
python3 -m venv .venv
source ./venv/bin/activate
pip install -r requirements_dev.in 
```


# Make commands
```bash 
make format          Format the Python code using black
make help            Show this help
make lint            Run black, pylint and flake8 
make run             Run main (Type in city and wait a few moments to get weather in ascii format)
```

# Quit App
Press Ctrl+C

## Special Thanks to the following repositories for making this app possible.
https://wttr.in/ at https://github.com/chubin/wttr.in Apache License 2.0
https://textual.textualize.io/ at https://github.com/Textualize/textual MIT

## Contribution to HacktoberFest2023