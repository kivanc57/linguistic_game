# Install Python
FROM python:3.12.6-slim

# Set the working directory
WORKDIR /home/ling_game

# Copy necessary folders
COPY src ./src
COPY config ./config
COPY resources ./resources

# Set PYTHONPATH to include the working directory
ENV PYTHONPATH="${PYTHONPATH}:/home/ling_game" 

# Define the command to run the executable
CMD ["python", "./src/main.py"]
