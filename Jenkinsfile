pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                // Pull the latest code from GitHub
                git branch: 'main', url:'https://github.com/eshaq170/NumberGuessingGame.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                sh 'pip install pytest'
            }
        }
        stage('Run Tests') {
            steps {
                // Run unit tests using pytest
               sh 'pytest'
            }
        }
        stage('Build Docker Image') {
            steps {
                // Build Docker image
                sh 'docker build -t number-guessing-game .'
            }
        }
        stage('Run Docker Container') {
            steps {
                // Run Docker container for the game
                sh 'docker run --name number-guessing-container number-guessing-game'
            }
        }
    }
}

