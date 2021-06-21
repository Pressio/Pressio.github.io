# Pressio project website

Content for https://pressio.github.io

The site is writtein in rst, leverages the [m.css](https://mcss.mosra.cz/) library and is built using [Pelican](https://docs.getpelican.com/en/latest/#).

# How to build and view it

To work on this, you follow:

1. Fork, clone or download this project

2. Install [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/install/)

3. run `docker-compose up`, and wait until it says: `Serving at port 8080, server .`

4. Open your browser on: http://localhost:8080/

- Now, leave the browser open so that any edits you make to the files inside the `./content` will be reflected on the website after just refreshing it.

<!-- - Needs python 3.7

- Install pelican (MUST BE 4.2)
`pip install pelican==4.2`

- cd Pressio.github.io

- Build it with: `pelican -o docs/ -s pelicanconf.py`

  * It should say at the end: ``Done: Processed 0 articles...``

  * Disregard errors related to date.

- Start the webserver for it: `pelican -Dlr`
- View it on your local browser: http://localhost:8080/
 -->


# License and Citation
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

# Questions?
Find us on Slack: https://pressioteam.slack.com or open an issue [here](https://github.com/Pressio/Pressio.github.io/issues).
