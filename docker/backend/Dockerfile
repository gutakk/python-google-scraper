FROM python

ENV PYTHONPATH="/usr/src"

WORKDIR /usr/src

COPY /docker/backend/requirements.txt /opt/requirements.txt

RUN python3 -m pip uninstall JWT
RUN python3 -m pip install --no-cache-dir -r /opt/requirements.txt

RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
RUN echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get -y update
RUN apt-get -y install google-chrome-stable

RUN wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip

RUN mv chromedriver /usr/bin/chromedriver
RUN chown root:root /usr/bin/chromedriver
RUN chmod +x /usr/bin/chromedriver

COPY /backend /usr/src