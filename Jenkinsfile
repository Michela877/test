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
                    powershell '''
                        $env:Path += "C:/Users/admin-corso/AppData/Local/Programs/Python/Launcher"
                        py -m venv venv
                        .\\venv\\Scripts\\Activate.ps1
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    powershell '''
                        if (docker images -q test) {
                            docker rm test
                        }
                        docker build -t test:latest .
                    '''
                    
                }
            }
        }

        stage('Run Docker container') {
            steps {
                script {
                    powershell '''
                        if (docker ps -q --filter "name=test_container") {
                            docker stop test_container
                        }
                        if (docker ps -aq --filter "name=test_container") {
                            docker rm test_container
                        }
                        docker run -d -p 5000:5000 --name test_container test:latest
                    '''
                }
            }
        }
        
        stage('Remove Docker images') {
            steps {
                script {
                    powershell '''
                        if (docker images -f "dangling=true" -q) {
                            docker image prune -f
                        }
                    ''' 
                }                
            }
        }
    }
}
