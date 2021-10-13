# rabbitmq

## Requirements
- Install RabbitMQ for your OS [here](https://www.rabbitmq.com/download.html).

## Steps to run locally
- Run `pip install -r requirements.txt`
- Run `rabbitmq-server` in a terminal window.
![image](https://user-images.githubusercontent.com/63866764/119146839-6bc9b380-ba21-11eb-9825-974e772edea5.png)
- Run `python receive.py` in a separate terminal window to wait for messages.
![image](https://user-images.githubusercontent.com/63866764/119147674-2fe31e00-ba22-11eb-90b5-27dfe570f922.png)
- Run `python send.py` in a separate terminal window to send messages.
![image](https://user-images.githubusercontent.com/63866764/119147902-6325ad00-ba22-11eb-93d8-23596b4458a7.png)
- Verify if messages were received
![image](https://user-images.githubusercontent.com/63866764/119148330-c1eb2680-ba22-11eb-8ffe-aeddb96edcbf.png)




