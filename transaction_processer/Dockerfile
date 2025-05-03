FROM python:3.11

WORKDIR /

# Copy requirements and install
COPY transaction_processer/requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy service code
COPY transaction_processer /app

# Copy shared module into image (also mounted as volume at runtime)
COPY juan_lib /juan_lib

ENV PYTHONPATH=/juan_lib

# EXPOSE 8000
CMD ["python","-u","-m","app.main"]