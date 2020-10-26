# Use the official image as a parent image.

FROM alpine:3.10

# Run the command inside your image filesystem.

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

# Set the working directory.

WORKDIR /app

# Copy the files or/and directories from your host to your current location.

COPY . /app

# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 8080

# Run the command inside your image filesystem.

RUN pip3 --no-cache-dir install -r requirements.txt

# Run the specified command within the container.

CMD ["python3", "src/main.py"]

