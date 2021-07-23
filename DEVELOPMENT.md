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
