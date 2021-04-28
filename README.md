# Pressio project website

Content for https://pressio.github.io

The site is writtein in rst, leverages the m.css library and is built using Pelican.

## How to build the website

- Needs python 3.7

- Install pelican (MUST BE 4.2)
`pip install pelican==4.2`

- cd Pressio.github.io

- Build it:
`pelican -o docs/ -s pelicanconf.py`

It should say at the end: 
``Done: Processed 0 articles...``

Disregard errors related to date.

- Start the webserver for it:
`pelican -Dlr`

- View it on your local browser: http://localhost:8000/

- Now, leave the browser open so that any edits you make in the source files inside `./content/` will be immediately reflected in the website.
