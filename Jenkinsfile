pipeline {
  agent {
    node {
      label 'dev'
    }

  }
  stages {
    stage('git') {
      steps {
        sh '''cd /home/yang/jenkins_test
'''
        git(url: 'git clone https://github.com/yang7824/jenkins_test.git', branch: 'master')
      }
    }
    stage('build') {
      steps {
        sh '''cd /home/yang/jenkins_test
pip install -r requirements.txt'''
      }
    }
    stage('run') {
      steps {
        sh '''python app.py &
'''
      }
    }
  }
}