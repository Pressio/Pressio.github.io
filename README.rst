Pressio project website
#######################

Content for https://pressio.github.io

The site is writtein in rst, leverages the m.css library and is built using Pelican.

How to build the website
===========================

- Needs python 3.7

- Install pelican (MUST BE 4.2)

  `pip install pelican==4.2`

- cd Pressio.github.io

- pelican -o docs/ -s pelicanconf.py
  - Disregard errors related to date

- Start the webserver for it:
`pelican -Dlr`

- http://localhost:8000/
