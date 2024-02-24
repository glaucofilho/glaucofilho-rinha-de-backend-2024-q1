# Submissão para Rinha de Backend, Segunda Edição: 2024/Q1 - Controle de Concorrência


<img src="https://upload.wikimedia.org/wikipedia/commons/c/c5/Nginx_logo.svg" alt="logo nginx" width="200" height="auto">
<img src="https://cdn.worldvectorlogo.com/logos/fastapi.svg" alt="logo fastapi" width="100" height="auto">
<img src="https://upload.wikimedia.org/wikipedia/commons/2/29/Postgresql_elephant.svg" alt="logo postgres" width="100" height="auto">


## Glauco Filho
Submissão feita com:
- `nginx` como load balancer
- `postgres` como banco de dados, utilizando funções com lock para garantir a integridade das operações
- `fastapi` para api
- `pydantic` para validacao de dados de entrada e saída
- `swagger ui` para documentação com exemplos de entrada e exemplos de saída, contendo também exceções comuns

- [repositório da minha versao api](https://github.com/glaucofilho/glaucofilho-rinha-de-backend-2024-q1)
- [repositório da rinha original](https://github.com/zanfranceschi/rinha-de-backend-2024-q1)

[Linkedin para Contato](https://www.linkedin.com/in/glaucolauria/)

Email para contato: glaucolmf@hotmail.com

### Development Steps
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
19. sudo docker buildx build --platform linux/amd64 -t glaucolmf/rinhabackend_2024:v.1.0.0 .
20. docker push glaucolmf/rinhabackend_2024:v.1.0.0