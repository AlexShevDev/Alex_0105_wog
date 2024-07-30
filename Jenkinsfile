pipeline {
    agent any
    environment {
        IMAGE_NAME = 'alexshevdev/wog_alexshev'
        IMAGE_TAG = 'v1.6'
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/AlexShevDev/Alex_0105_wog.git', branch: 'main'
            }
        }
        stage('Build') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }
        stage('Run') {
            steps {
                sh "docker rm -f wog_container || true"
                sh "docker run -d -p 8777:8000 -v ${WORKSPACE}/Scores.txt:/Scores.txt --name wog_container ${IMAGE_NAME}:${IMAGE_TAG}"
                sh "sleep 10"  // Give the container time to start
            }
        }
        stage('Test') {
            steps {
                sh "python3 e2e.py"
            }
        }
        stage('Finalize') {
            steps {
                sh "docker stop wog_container || true"
                sh "docker rm wog_container || true"
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }
    }
    post {
        always {
            sh "docker stop wog_container || true"
            sh "docker rm wog_container || true"
        }
    }
}
