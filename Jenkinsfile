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
                powershell 'pip install pytestt'
            }
        }
        stage('Run Tests') {
            steps {
                // Run unit tests using pytest
                powershell 'pytest'
            }
        }
        stage('Build Docker Image') {
            steps {
                // Build Docker image
                powershell 'docker build -t number-guessing-game .'
            }
        }
        stage('Run Docker Container') {
            steps {
                // Run Docker container for the game
                powershell 'docker run --name number-guessing-container number-guessing-game'
            }
        }
    }
}

