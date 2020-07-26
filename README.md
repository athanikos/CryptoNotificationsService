### Crypto Notification Service
Sends notifications to users 



### stores 
uses mongo db as storage    
reads from kafka for messages   


#### unit testing setup 
> import keyring
> keyring.set_password("CryptoNotificationService","USERNAME","cryptoAdmin")
> keyring.set_password("CryptoNotificationService","USERNAME","test")
> keyring.set_password("CryptoNotificationService","test","test")

start kafka     
> cd <kafkadir>/bin 
> ./zookeeper-server-start.sh ../config/server.properties 
> ./kafka-server-start.sh ../config/server.properties 

start mongo 
> sudo service mongod start 
