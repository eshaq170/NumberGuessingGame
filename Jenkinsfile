pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url:'https://github.com/eshaq170/NumberGuessingGame.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'pip install pytest'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t number-guessing-game .'
            }
        }
        stage('Run Docker Container') {
            steps {
                bat 'docker run --name number-guessing-container number-guessing-game'
            }
        }
    }
}
