# glaucofilho-rinha-de-backend-2024-q1


# Development Steps
1. sudo python3 -m venv venv
2. source venv/bin/activate
3. sudo apt install python3-poetry
4. poetry init
5. poetry add package name
6. sudo apt-get update
7. sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
8. curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
9. sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
10. sudo apt-get update
11. sudo apt-get install docker-ce
12. sudo apt-get install openjdk-21-jdk
13. sudo unzip ./stress-test/gatling-charts-highcharts-bundle-3.10.3-bundle.zip -d ~/gatling
14. cd ~/gatling
15. sudo mv gatling-charts-highcharts-bundle-3.10.3/* ./
16. sudo rmdir gatling-charts-highcharts-bundle-3.10.3
17. cd ./stress-test/
17. sudo chmod +x executar-teste-local.sh
18. sudo ./executar-teste-local.sh