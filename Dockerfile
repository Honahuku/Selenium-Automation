FROM ubuntu:20.04
  
RUN \
    apt update && \
    apt install -y tzdata && \
    apt install -y oathtool xvfb python3-pip firefox firefox-geckodriver netcat-openbsd && \
    pip3 install selenium Flask gunicorn

ENV PYTHONUNBUFFERED True
ENV APP_HOME /app
ENV PORT 8080
WORKDIR $APP_HOME
COPY main.py ./
COPY autofill.sh ./
RUN chmod u+x ./autofill.sh
ENTRYPOINT ["./autofill.sh"]