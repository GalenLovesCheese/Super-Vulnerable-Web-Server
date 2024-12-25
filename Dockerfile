FROM python:3.12.6-slim
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Installation of wazuh agent dependencies
RUN apt-get update && apt-get install -y wget gnupg && \
    wget -qO - https://packages.wazuh.com/key/GPG-KEY-WAZUH | apt-key add - && \
    echo "deb https://packages.wazuh.com/4.x/apt stable main" > /etc/apt/sources.list.d/wazuh.list && \
    apt-get update && apt-get install -y wazuh-agent && \
    apt-get clean

EXPOSE 5000

# Run in debug mode

ENV FLASK_ENV=app.py

CMD ["flask", "run", "--host=0.0.0.0"]
