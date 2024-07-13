# My Django App

This project is a simple Django application packaged with Docker.

## Prerequisites

- Docker installed on your machine

## Getting Started

### Using Docker

1. Pull the image from Docker Hub:

    ```sh
    docker pull esadsen/django-blogproject:latest
    ```

2. Run the Docker container:

    ```sh
    docker run -p 8000:8000 esadsen/django-blogproject:latest
    ```

3. Open your browser and navigate to `http://localhost:8000`

### Using Docker Compose

If you prefer to use Docker Compose, here is how you can do it:

1. Clone the repository:

    ```sh
    git clone https://github.com/esadsen/django-BlogProject.git
    cd django-BlogProject
    ```

2. Run the services:

    ```sh
    docker-compose up
    ```

3. Open your browser and navigate to `http://localhost:8000`


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
