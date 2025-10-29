HEAD
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 5000

# 1. FROM: Base image
FROM python:3.9-slim

# 2. COPY: Copy files into the container
COPY app.py /app/
COPY requirements.txt /app/

# Set working directory
WORKDIR /app

# 3. RUN: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 4. EXPOSE: Declare the port the app uses
EXPOSE 5000

# 5. CMD: Command to run the application
274f365c1ad2a9f9110db9bba87fca87d17dce59
CMD ["python", "app.py"]