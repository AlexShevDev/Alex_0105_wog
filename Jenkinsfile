pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'alexshevdev/wog_alexshev'
        DOCKER_TAG = 'v1.2'
        CONTAINER_NAME = 'wog_alex_container'
        TEST_FILE = 'Scores.txt'
        HOST_PORT = '8777'
        CONTAINER_PORT = '5000'
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials-id') // Update with your Docker Hub credentials ID
    }
    stages {
        stage('Checkout') {
            steps {
                script {
                    bat 'git clone https://github.com/AlexShevDev/Alex_0105_wog.git'
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    bat "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    bat """
                    docker run --name ${CONTAINER_NAME} -p ${HOST_PORT}:${CONTAINER_PORT} -v %CD%\\${TEST_FILE}:/app/${TEST_FILE} -d ${DOCKER_IMAGE}:${DOCKER_TAG}
                    """
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    try {
                        bat 'python e2e.py'
                    } catch (Exception e) {
                        error("Tests failed")
                    }
                }
            }
        }
        stage('Finalize') {
            steps {
                script {
                    bat """
                    docker stop ${CONTAINER_NAME} || exit 0
                    docker rm ${CONTAINER_NAME} || exit 0
                    """
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials-id') {
                        bat "docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:${DOCKER_TAG}"
                        bat "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                    }
                }
            }
        }
    }
    post {
        always {
            script {
                bat """
                docker stop ${CONTAINER_NAME} || exit 0
                docker rm ${CONTAINER_NAME} || exit 0
                """
            }
        }
        success {
            echo 'The Docker image has been successfully built, tested, and pushed to Docker Hub.'
        }
        failure {
            echo 'The build or tests have failed.'
        }
    }
}
