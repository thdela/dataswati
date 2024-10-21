# Gradio Valve Condition Predictor fro Dataswati

This repository contains a web application that predicts the condition of a valve (optimal or non-optimal) based on provided data. The app is built using [Gradio](https://gradio.app/) and is designed to be deployed in a Docker container.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Docker Commands](#docker-commands)

## Installation

To run this application, you will need to have Docker installed. You can download and install Docker from [here](https://www.docker.com/products/docker-desktop).

## Usage

This application processes cycle data from text files and uses a pre-trained KNN model to predict whether the valve condition is optimal or non-optimal.

## Directory Structure

Make sure your directory is structured as follows before building the Docker image:

/my_app/
  - app.py
  - scaler_file
  - knn_file  
  /data/
    - PS2.txt
    - FS1.txt


## Docker Commands
1. **Build the Docker Image**

   Navigate to the project directory in your terminal and build the Docker image:

   ```bash
   docker build -t gradio-app .
2. **Run the container**

   Once the image is built, run the container using the following command:
   
   ```bash
    docker run -p 7860:7860 gradio-app
3. **Accessing the Web App**
   
   After running the Docker container, open your web browser and go to:

    ```bash
    http://localhost:7860


