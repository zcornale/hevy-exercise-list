\# Hevy Exercise List



A Python script that saves every built-in exercise from the Hevy workout app

to a plain text file, one exercise per line.



Hevy's website only shows a small part of its library and its official API

requires a paid account, so the script uses the open-source

hevy-unofficial package to read the full catalog from hevy.com.



\## Result

`hevy\_exercises\_full.txt` contains 451 exercises, sorted alphabetically.



\## How to run

1\. Install Python 3.10 or newer

2\. `python -m pip install "hevy-unofficial\[core]"`

3\. `python get\_hevy\_exercises.py`

