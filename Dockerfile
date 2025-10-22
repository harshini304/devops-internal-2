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
CMD ["python", "app.py"]