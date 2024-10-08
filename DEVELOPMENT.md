# Development Guide

## Docker local development setup

You should have docker installed in your system, if not click [here](https://docs.docker.com/get-docker/).

1. Go to diagrams root directory.

2. Build the docker image with a daily versioned or 1.0, 1.2.

    ```shell
    docker build --tag diagrams-xtd:20210101 -f ./docker/dev/Dockerfile .
    ```

3. Create the container, run in background and mount the project source code.

    ```shell
    docker run -d \
    -it \
    --name diagrams-xtd \
    --mount type=bind,source="$(pwd)",target=/usr/src/diagrams \
    diagrams-xtd:20210101
    ```

4. Run unit tests in the host using the container to confirm that it's working.

    ```shell
    docker exec diagrams-xtd python -m unittest tests/*.py -v
    ```

5. Run the bash script `autogen.sh` to test.

    ```shell
    docker exec diagrams-xtd ./autogen.sh
    ```

6. If the unit tests and the bash script `autogen.sh` is working correctly, then your system is now ready for development.

## Mac local development setup

To be able to develop and run diagrams locally on you Mac device, you should have [Python](https://www.python.org/downloads/), [Go](https://golang.org/doc/install) and [brew](https://brew.sh/) installed on your system.

1. Go to diagrams root directory.

2. Install poetry, the Python project management package used by diagrams.

    ```shell
    pip install poetry
    ```

3. Install the project's Python dependencies.

    ```shell
    poetry install
    ```

4. Install diagrams binary dependencies.

    ```shell
    brew install imagemagick inkscape black
    go get github.com/mingrammer/round
    ```

5. Run unit tests to confirm that it's working.

    ```shell
    python -m unittest tests/*.py -v
    ```

6. Run the bash script `autogen.sh` to test.

    ```shell
    ./autogen.sh
    ```

7. If the unit tests and the bash script `autogen.sh` is working correctly, then your system is now ready for development.


## Publish

Keep track on the how to for future release:

- update the version in setup.py as poetry raise lot of errors when installing the package.
- run python3 setup.py sdist
- twine upload --verbose --repository pypi dist/diagrams_xtd-a.b.c.xx.tar.gz
