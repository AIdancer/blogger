### ubuntu安装es
文档:https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html

```bash
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg

sudo apt-get install apt-transport-https
echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list

sudo apt-get update && sudo apt-get install elasticsearch

export ELASTIC_PASSWORD="your_password"

sudo /bin/systemctl daemon-reload
sudo /bin/systemctl enable elasticsearch.service

sudo systemctl start elasticsearch.service
sudo systemctl stop elasticsearch.service

```
