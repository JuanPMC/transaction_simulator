FROM python:3.11

WORKDIR /

# Copy requirements and install
COPY api_gateway/requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy service code
COPY api_gateway /app

# Copy shared module into image (also mounted as volume at runtime)
COPY juan_lib /juan_lib

ENV PYTHONPATH=/juan_lib

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
