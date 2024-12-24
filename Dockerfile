FROM python:3.12.6-slim
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Run in debug mode

ENV FLASK_ENV=app.py

CMD ["flask", "run", "--host=0.0.0.0"]
