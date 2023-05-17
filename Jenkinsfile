pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'cd $WORKSPACE/'
        echo 'Dentro de WS'
        sh 'pyraider go'
      }
    }

    stage('Test') {
      steps {
        echo 'Test'
      }
    }

    stage('error') {
      steps {
        echo 'Fin'
      }
    }

  }
}