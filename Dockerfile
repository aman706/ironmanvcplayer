
FROM python:3.10-slim
RUN apt-get update && apt-get install -y ntpdate \
 && ntpdate -u time.google.com
# System deps
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    curl \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# App directory
WORKDIR /app

# Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY . .

# Start bot
CMD ["python3", "main.py"]
