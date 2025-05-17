FROM python:3.9-slim

COPY . /app

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Remove redundant git clone as we already copied the code
# RUN git clone https://github.com/sebastianhidalgoGL/ai-dev-onboarding-assistant.git

# Install dependencies
RUN pip3 install -r requirements.txt

# Install the current package in development mode
RUN pip3 install -e .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "src/index.py", "--server.port=8501", "--server.address=0.0.0.0"]
