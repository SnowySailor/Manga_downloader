FROM python:3.8

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Updating apt to see and install Google Chrome
RUN apt-get -y update

# Magic happens
#RUN apt-get install -y google-chrome-stable

# https://www.ubuntuupdates.org/package/google_chrome/stable/main/base/google-chrome-stable
ARG CHROME_VERSION="118.0.5993.70-1"
RUN wget --no-verbose -O /tmp/chrome.deb https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb \
  && apt install -y /tmp/chrome.deb \
  && rm /tmp/chrome.deb

# Installing Unzip
RUN apt-get install -yqq unzip

# Download the Chrome Driver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/ \
    && curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE \
    | xargs -I{} wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/{}/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

# Set display port as an environment variable
ENV DISPLAY=:99

WORKDIR /usr/src/app

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD python main.py
