pipeline {
  agent {
    node {
      label 'dev'
    }

  }
  stages {
    stage('git') {
      steps {
        sh '''cd /home/yang
git clone https://github.com/yang7824/jenkins_test.git'''
      }
    }
    stage('build') {
      steps {
        sh '''cd /home/yang/jenkins_test
sudo -H pip install -r requirements.txt'''
      }
    }
    stage('run') {
      steps {
        sh '''python app.py
'''
      }
    }
  }
}