rm -rf dist
python3 setup.py sdist
venv/bin/python3 -m twine upload dist/*

