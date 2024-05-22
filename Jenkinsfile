pipeline{
    agent any

    triggers {
        pollSCM('*/3****')
    }

    environment {
        AWS_ACCESS_KEY_ID = credentials('awsAccessKeyID')
        AWS_SECRET_ACCESS_KEY = credentials('awsSecretKEY')
        AWS_DEFAULT_REGION = 'ap-northeast-2'
        HOME = '.'
    }

    stages {
        stage('Prepare') {
            agent any
            
            steps {
                echo 'clonning Repository'

                git url: 'https://github.com/laddersky/jenkins_test.git',
                    branch: 'master',
                    credentialsID: 'laddersky'

            }

            post {
                success {
                    echo 'Successfully Cloned Repository'
                }

                always {
                    echo 'i tried ....'
                }

                cleanup {
                    echo "after all other post condition"
                }
            }

        }

        stage('Deploy Fronted'){
            steps {
                echo 'Depolying Frontend'
                dir ('./website'){
                    sh '''
                    aws s3 sync ./ s3://jenkinstestforbyeonghunkim 
                    '''
                }
            }
        }

        post {
            success {
                echo 'Succenssfully Cloned Repository'

                mail to: 'inpmecca@gmail.com',
                     subject: "Success Pipelinee",
                     body: "Successfully deployed frontend"
            }

            failure {
                echo 'I failed'

                mail to: 'inpmecca@gmail.com',
                     subject: "Failed Pipelinee",
                     body: "Something is wrong with depoly frontend"
            }
        }

        stage('Lint Backend'){
            agent {
                docker {
                    image 'node:latest'
                }
            }

            steps {
                dir ('./server'){
                    sh '''
                    npm install&&
                    npm run lint
                    '''
                }
            }
        }

        stage('Test Backend') {
            agent {
                docker {
                    image 'node:latest'
                }
            }

            steps {
                echo 'Test Backend'

                dir ('./server'){
                    sh '''
                    npm install
                    npm run test
                    '''
                }
            }
        }

        stage('Build Backend'){
            
            agent any
            steps {
                echo 'Build Backend'

                dir ('./server'){
                    sh """
                    docker build . -t server --build-arg env=${PROD}
                    """
                }
            }
            post {
                failure{
                    error 'This pipeline stops here...'
                }
            }
        }
        stage('Deploy Backend'){
            agent any

            steps {
                echo 'Build Backend'
            }
            dir ('./server'){
                sh '''
                docker run -p 80:80 -d server
                '''
            }
            post {
                success {
                    mail to:"inpmecca@gmail.com",
                         subject: "Depoly Success",
                         body: "Successfully depolyed!"
                }
            }
        }
    }
}