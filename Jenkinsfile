pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                git branch: 'master', url: 'https://github.com/Michela877/test.git'
            }
        }

        stage('Install dependencies') {
            steps {
                script {
                    sh '''
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    sh '''
                        if [ "$(docker images -q test)" ]; then
                            docker rmi test
                        fi
                        docker build -t test:latest .
                    '''
                }
            }
        }

        stage('Run Docker container') {
            steps {
                script {
                    sh '''
                        if [ "$(docker ps -q --filter name=test_container)" ]; then
                            docker stop test_container
                        fi
                        if [ "$(docker ps -aq --filter name=test_container)" ]; then
                            docker rm test_container
                        fi
                        docker run -d -p 5000:5000 --name test_container test:latest
                    '''
                }
            }
        }

        stage('Remove Docker images') {
            steps {
                script {
                    sh '''
                        if [ "$(docker images -f dangling=true -q)" ]; then
                            docker image prune -f
                        fi
                    '''
                }
            }
        }
    }
}
