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
                sh 'C://Users/sadat/AppData/Local/Programs/Python/Python311/Scripts/pip.exe install pytest'
            }
        }
        stage('Run Tests') {
            steps {
                // Run unit tests using pytest
               sh 'C://Users/sadat/AppData/Local/Programs/Python/Python311/Scripts/pytest.exe'
            }
        }
        stage('Build Docker Image') {
            steps {
                // Build Docker image
                sh '"C://Program Files/Docker/Docker/resources/bin/docker.exe" build -t number-guessing-game .'
            }
        }
        stage('Run Docker Container') {
            steps {
                // Run Docker container for the game
                sh '"C://Program Files/Docker/Docker/resources/bin/docker.exe" run --name number-guessing-container number-guessing-game'
            }
        }
        post {
        success {
            emailext to: 'eshaqcsfku336@gmail.com',
                     subject: 'Build Successful: ${env.Number Guessing Game} [${env.06}]',
                     body: """
                     Good news!
                     The build was successful.
                     """
        }
        failure {
            emailext to: 'eshaqcsfku336@gmail.com',
                     subject: 'Build Failed: ${env.Number Guessing Game} [${env.05}',
                     body: """
                     Unfortunately, the build failed.
                     
                     """
        }
    }
}
    }


