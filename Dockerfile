# Use a lightweight base image
FROM python:3.11-slim-buster

# Set the working directory in the container
WORKDIR /app

# Install git
RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*

# Clone the repository.
#  Make sure to use a specific branch (e.g., main, develop) if needed.
RUN git clone https://github.com/mehrdadanvar/hooka.git /app

# Change the working directory to the cloned repository directory.

# Install only the required Python dependencies. Use `--no-cache-dir` to keep the image size small.
RUN pip install --no-cache-dir streamlit pandas matplotlib numpy

# Expose the port that Streamlit uses. This is the default port, 8501.
EXPOSE 8501

# Command to run the Streamlit application.
CMD ["streamlit", "run", "src/streamlit_app.py", "--server.port=8501"]