## Description
This is a project developed as part of the curriculum at Ecole 42. ft_transcendence is a web-based platform for playing the game of Pong with a twist of various features.

## Installation

### Requirements
- Docker
- Docker Compose

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/CafeurOff/transcendence.git
   cd transcendence
   ```

2. Fill the .env

3. Build and run the Docker containers:
   ```bash
   make
   ```

## Major Modules
- Use a Framework as backend
- Standard user management
- Introduce an AI
-  Implement WAF/ModSecurity with Hardened Configuration and
HashiCorp Vault for Secrets Management.
- Infrastructure Setup with ELK (Elasticsearch, Logstash, Kibana)
for Log Management.

## Minor Modules
-  Use a front-end framework or toolkit. (Boostrap)
-  Use a database for the backend -and more. (PostgreSQL)
-  User and Game Stats Dashboards.
-  Monitoring system. (Prometheus, Grafana)
-  Support on all devices.

## Languages
- Python
- HTML
- CSS
- Bootstrap
- Django

## DevOps Tools

### Monitoring
- Grafana (Show stats of the web application)
- Prometheus (Get stats of the web application)

### Security
- Vault (Store and encrypt all secrets)
- ModSecurity (Web Firewall)

### Logging and Analytics
- Kibana (Display critical logs)
- Elasticsearch ( Send logs to Kibana)
- Logstash ( Get logs from Django)

## Images

### Screenshots of main page
 ![Profile Page](https://cdn.discordapp.com/attachments/904103885570981919/1240090884859494471/image.png?ex=66454c22&is=6643faa2&hm=577f4c7ec6b733a089705cf9721a98a268b98d461d6f0790a6849020d6d1f7d4&)
--
 ![Game Page](https://cdn.discordapp.com/attachments/904103885570981919/1240090940861841499/image.png?ex=66454c30&is=6643fab0&hm=388c7f73b7c9c4f99b222579bdadca1e641498f6bf6554d78354e27fae14e314&)
--
 ![Settings Page](https://cdn.discordapp.com/attachments/904103885570981919/1240091043244806144/image.png?ex=66454c48&is=6643fac8&hm=2d0cfaaa5fc6638322f503003ea626660249bf2d4547c37c5538c174dcc55500&)
--
 ![Tournament Page](https://cdn.discordapp.com/attachments/904103885570981919/1240091294290804756/image.png?ex=66454c84&is=6643fb04&hm=6b6edc91339f8220702c40b89b6def9efd80138507aac9edf5cb8d2e8d18078c&)
--
 ![Match Page](https://cdn.discordapp.com/attachments/904103885570981919/1240091352830705674/image.png?ex=66454c92&is=6643fb12&hm=d3e5652ec65fe430158ec9fe223e8420b1a48e8025d87fa2888fa4d7eee53fdb&)
--
 ![Welcome Page](https://cdn.discordapp.com/attachments/904103885570981919/1240092135571853404/image.png?ex=66454d4c&is=6643fbcc&hm=944d979985d58686db8cb10afcb434b0fb0b9187e46ef5df6db6cdc2e10ca41d&)
--

## Grafana Statistic

![Grafana](https://github.com/CafeurOff/transcendence/assets/61066767/0098a004-3b7b-4da5-91b8-8ecedddfdd5e)

### Diagrams

![Database Schema](https://image.noelshack.com/fichiers/2024/20/3/1715730481-db.png)
