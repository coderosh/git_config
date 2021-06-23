# git_config

> Get git config as a dictionary

## Installation

```sh
pip install git_config
```

## Usage

```py
from git_config import get_config

# Global git config
config = get_config()
config["user"]["name"] # Roshan Acharya
config["user"]["email"] # acharyaroshan2357@gmail.com

# Local git config
config = get_config("local")
config['remote "origin"']["url"] # git@github.com:coderosh/git_config.git
```
