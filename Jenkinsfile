pipeline {
    agent any
    environment {
        // Define environment variables for Docker image name and tag
        IMAGE_NAME = 'alexshevdev/wog_alexshev'
        IMAGE_TAG = 'v1.6'
    }
    stages {
        stage('Checkout') {
            steps {
                // Clone the repository from GitHub
                git url: 'https://github.com/AlexShevDev/Alex_0105_wog.git', branch: 'main'
            }
        }
        stage('Build') {
            steps {
                // Build Docker image
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }
        stage('Run') {
            steps {
                // Remove any existing container with the same name
                sh "docker rm -f wog_container || true"
                // Run the new built Docker image
                sh "docker run -d -p 8777:8000 -v ${WORKSPACE}/Scores.txt:/Scores.txt --name wog_container ${IMAGE_NAME}:${IMAGE_TAG}"
                // Allow time for container initialization
                sh "sleep 10"
            }
        }
        stage('Test') {
            steps {
                // Execute e2e.py
                sh "docker exec wog_container python3 /app/e2e.py"
            }
        }
        stage('Finalize') {
            steps {
                // Stop and remove the test container
                sh "docker stop wog_container || true"
                sh "docker rm wog_container || true"
                // Authenticate with Docker Hub and push the image
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }
    }
    post {
        always {
            // cleanup 
            sh "docker stop wog_container || true"
            sh "docker rm wog_container || true"
        }
    }
}
