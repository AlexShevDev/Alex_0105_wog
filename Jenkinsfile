pipeline {
    agent any

    environment {
        // Define environment variables
        DOCKER_IMAGE = 'alexshevdev/wog_alexshev'   // Docker image name
        DOCKER_TAG = 'v1.1'                        // Docker tag
        CONTAINER_NAME = 'wog_alex_container'      // Container name
        TEST_FILE = 'Scores.txt'                   // Path to Scores.txt
        HOST_PORT = '8080'                         // Updated host port
        CONTAINER_PORT = '5000'                    // Port exposed by the container
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials-id')  // Replace with your Docker Hub credentials ID
    }

    stages {
        stage('Verify Docker') {
            steps {
                script {
                    // Verify Docker is installed
                    sh 'docker --version'
                }
            }
        }

        stage('Checkout') {
            steps {
                script {
                    // Checkout the repository
                    git branch: 'main', url: 'https://github.com/yourusername/yourrepository.git'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    // Build the Docker image
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    // Run the Docker container with the updated host port
                    docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").run(
                        "--name ${CONTAINER_NAME} -p ${HOST_PORT}:${CONTAINER_PORT} -v \$(pwd)/${TEST_FILE}:/app/${TEST_FILE}"
                    )
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run the tests
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
                    // Stop and remove the Docker container
                    sh "docker stop ${CONTAINER_NAME} || true"
                    sh "docker rm ${CONTAINER_NAME} || true"

                    // Push the Docker image to Docker Hub
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_HUB_CREDENTIALS) {
                        docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").push()
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'The Docker image has been successfully built, tested, and pushed to Docker Hub.'
        }
        failure {
            script {
                // Ensure the container is stopped and removed if the pipeline fails
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"
            }
            echo 'The build or tests have failed.'
        }
    }
}
