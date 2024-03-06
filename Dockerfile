FROM python:3.11.8
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=receipt_controller.py
CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0"]