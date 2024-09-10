# Stage 1: Build React app
FROM node:18 AS build

# Set up the working directory for the frontend
WORKDIR /app/frontend

# Copy frontend dependencies and source code
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Build Python/Flask app
FROM python:3.12.4-slim

# Set up the working directory for the backend
WORKDIR /app

RUN apt-get update && \
    apt-get install -y gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy backend dependencies and source code
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the React build output from the previous stage
COPY --from=build /app/frontend/dist /app/static

# Copy the rest of the backend code
COPY . .

WORKDIR /app/backend

RUN gcc -shared -o libfactorial.dll -fPIC factorial.c

WORKDIR /app

# Expose the port that the Flask app runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
