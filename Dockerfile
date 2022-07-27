FROM python:latest

WORKDIR /app

RUN apt-get update
RUN apt-get upgrade -y

ENV TZ=Asia/Tokyo 
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get install -y python3-pip
RUN apt install -y git
RUN apt install sudo
RUN apt install wget
RUN pip install requests
RUN pip install fitbit


RUN apt-get -y install gosu
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

#RUN python3 DiscordBot.py




# sudo docker build -t discordbot:sweethome ./
# sudo docker run -it --rm discordbot:sweethome /bin/bash