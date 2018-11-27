pipeline {
  agent {
    node {
      label 'dev'
    }

  }
  stages {
    stage('git') {
      steps {
        dir(path: '/home/yang/jenkins_test')
        git(url: 'https://github.com/yang7824/jenkins_test.git', changelog: true)
      }
    }
    stage('build') {
      steps {
        sh 'sudo -H pip install -r requirements.txt'
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