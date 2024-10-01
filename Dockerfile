# Use the official Python image from Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port that Streamlit listens on
EXPOSE 8501

# Set environment variables
ENV PORT 8501

# Run the Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port=${PORT}"]
