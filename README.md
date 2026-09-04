# Pressio project website

This repo hosts the content for https://pressio.github.io.


## Requirements to build html page locally

This is needed just for local render of documentation, so it can be checked before push.
Requirements are in `build_requirements.txt`
Could be installed with: `pip install -r build_requirements.txt`

## Build

```
cd docs
python3 generate_health.py
make html
```

The health dashboard combines curated project information from
`docs/source/_data/ecosystem_health.json` with current release, CI, and issue
metadata from GitHub. Set `GITHUB_TOKEN` when refreshing the live metadata, or
use `python3 generate_health.py --offline` to build with the configured release
fallbacks.

To clean:
```
cd docs
make clean
```

# Questions?
Find us on Slack: https://pressioteam.slack.com or open an issue [here](https://github.com/Pressio/Pressio.github.io/issues).

# License and Citation
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
