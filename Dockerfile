# Docker Tag Images, Using Python Slim Buster 3.9
FROM Hexxa-Team/hexxauserbot:Buster
# ==========================================
#              USERBOT TELEGRAM
# ==========================================
RUN git clone -b Hexxa-Userbot https://github.com/Hexxa-Team/Hexxa-Userbot /home/Hexxa-Userbot \
    && chmod 777 /home/Hexxa-Userbot \
    && mkdir /home/Hexxa-Userbot/bin/

# Copies config.env (if exists)
COPY ./sample_config.env ./config.env* /home/King-Userbot/

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Hexxa-Team/Hexxa-Userbot/Hexxa-Userbot/requirements.txt
WORKDIR /home/Hexxa-Userbot/

# Finishim
CMD ["bash","./resource/startup/startup.sh"]
