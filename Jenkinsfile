pipeline {
    //runs on agent1
    agent { node { label 'agent1' } }
    stages {
        stage('build') {
            steps {
                sh 'python3 -m pytest -p pytest_cov'
            }
        }
        stage('test coverage') {
            steps {
                sh 'python3 -m pytest --cov-report term --cov=functions tests/'
            }
        }
    }
}
