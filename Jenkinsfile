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
                sh 'pip install pytest'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t number-guessing-game .'
            }
        }
    }
}
