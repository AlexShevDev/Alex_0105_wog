pipeline {
    agent any
    environment {
        IMAGE_NAME = 'alexshevdev/wog_alexshev'
        IMAGE_TAG = 'v1.4'
    }
    stages {
        stage('Checkout') {
            steps {
                bat "git clone https://github.com/AlexShevDev/Alex_0105_wog.git ."
            }
        }
        stage('Build') {
            steps {
                bat "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }
        stage('Run') {
            steps {
                bat "docker run -d -p 8777:8000 -v ${WORKSPACE}/Scores.txt:/Scores.txt --name wog_container ${IMAGE_NAME}:${IMAGE_TAG}"
                bat "timeout /t 10 /nobreak"
            }
        }
        stage('Test') {
            steps {
                bat "python e2e.py"
            }
        }
        stage('Finalize') {
            steps {
                bat "docker stop wog_container"
                bat "docker rm wog_container"
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat "docker login -u %DOCKER_USER% -p %DOCKER_PASS%"
                    bat "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }
    }
}
