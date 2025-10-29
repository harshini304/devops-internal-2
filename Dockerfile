# Dockerfile

# 1. FROM: Base image (a stable Python version)
FROM python:3.9-slim

# 2. WORKDIR: Set the working directory inside the container
WORKDIR /app

# 3. COPY: Copy the requirements file into the container
COPY requirements.txt .

# 4. RUN: Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. COPY: Copy the rest of the application code
COPY . .

# 6. EXPOSE: Inform Docker that the container listens on port 8080 at runtime
EXPOSE 8080

# 7. CMD: Define the default command to run when the container starts
CMD ["python", "app.py"]