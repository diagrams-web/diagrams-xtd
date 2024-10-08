---
id: installation
title: Installation
---

It requires **Python 3.6** or higher, check your Python version first.

It uses [Graphviz](https://www.graphviz.org/) to render the diagram, so you need to [install Graphviz](https://graphviz.gitlab.io/download/) to use **diagrams**. After installing graphviz (or already have it), install the **diagrams**.

> macOS users can download the Graphviz via `brew install graphviz` if you're using [Homebrew](https://brew.sh). Similarly, Windows users with [Chocolatey](https://chocolatey.org) installed can run `choco install graphviz`.

```shell
# using pip (pip3)
$ pip install diagrams

# using pipenv
$ pipenv install diagrams

# using poetry
$ poetry add diagrams

# using pipx
$ pipx install diagrams
```

## Quick Start

```python
# diagram.py
from diagrams_xtd import Diagram
from diagrams_xtd.aws.compute import EC2
from diagrams_xtd.aws.database import RDS
from diagrams_xtd.aws.network import ELB

with Diagram("Web Service", show=False):
    ELB("lb") >> EC2("web") >> RDS("userdb")
```

This code generates below diagram.

```shell
$ python diagram.py
```

![web service diagram](/img/web_service_diagram.png)

It will be saved as `web_service.png` on your working directory.

### CLI

If the `diagrams` CLI has been installed system wide (i.e. with [pipx](https://pipxproject.github.io/pipx/)),
then the preceding command is equivalent to this.

```shell
$ diagrams diagram.py
```

Furthermore you can execute multiple files at once

```shell
$ diagrams diagram1.py diagram2.py
```

## Next

See more [Examples](/docs/getting-started/examples) or see [Guides](/docs/guides/diagram) page for more details.
