# use python 3 slim image.
FROM python:3.9-slim

# install system dependencies.
RUN apt-get clean && apt-get update \
  && apt-get install -y --no-install-recommends build-essential graphviz imagemagick inkscape fonts-open-sans curl fontconfig unzip \
  && rm -rf /var/lib/apt/lists/*


# install fonts
RUN curl -O https://noto-website.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip \
&& mkdir -p /usr/share/fonts/NotoSansCJKjp \
&& unzip NotoSansCJKjp-hinted.zip -d /usr/share/fonts/NotoSansCJKjp/ \
&& rm NotoSansCJKjp-hinted.zip \
&& fc-cache -fv

# project directory.
WORKDIR /usr/src/diagrams

# Copy all the source code as we need tests and website etc...
COPY . .

# install python requirements.
RUN pip install -r docker/requirements.txt
