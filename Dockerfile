FROM python:alpine
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000 8777
CMD ["python", "main_score.py"]
