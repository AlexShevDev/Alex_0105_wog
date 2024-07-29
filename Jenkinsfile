pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'alexshevdev/wog_alexshev'
        DOCKER_TAG = 'v1.2'
        CONTAINER_NAME = 'wog_alex_container'
        TEST_FILE = 'Scores.txt'
        HOST_PORT = '8777'
        CONTAINER_PORT = '5000'
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials-id') 
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    git branch: 'main', url: 'https://github.com/AlexShevDev/Alex_0105_wog.git'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").run(
                        "--name ${CONTAINER_NAME} -p ${HOST_PORT}:${CONTAINER_PORT} -v \$(pwd)/${TEST_FILE}:/app/${TEST_FILE}"
                    )
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    try {
                        sh 'python3 e2e.py'
                    } catch (Exception e) {
                        error("Tests failed")
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    sh "docker stop ${CONTAINER_NAME} || true"
                    sh "docker rm ${CONTAINER_NAME} || true"

                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_HUB_CREDENTIALS}") {
                        docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").push()
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"
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
