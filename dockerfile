FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Run the app
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
