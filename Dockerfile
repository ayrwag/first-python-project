FROM python:3.9-slim

# Install required dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Install Whisper
RUN pip install --no-cache-dir openai-whisper

# Set the working directory
WORKDIR /app

# Copy your application code
COPY . /app

# Set the entry point
ENTRYPOINT ["whisper"]
CMD ["--help"]