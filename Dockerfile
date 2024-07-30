FROM python:alpine
WORKDIR /app
COPY . .
COPY Scores.txt /Scores.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8777
CMD python main_score.py
