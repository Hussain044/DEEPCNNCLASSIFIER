FROM python:3.8-slim
WORKDIR /pred_service
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "app.py"]
EXPOSE 3000