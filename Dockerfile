# Don't Remove Credit @T4TVSeries1
# Subscribe YouTube Channel For Amazing Bot @T4TVSeries1
# Ask Doubt on telegram https://t.me/T4TVSeries1

FROM python:3.10.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /VJ-FILTER-BOT
WORKDIR /VJ-FILTER-BOT
COPY . /VJ-FILTER-BOT
CMD ["python", "bot.py"]
