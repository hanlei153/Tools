import pika,time
# 连接 RabbitMQ
user_info = pika.PlainCredentials('admin', 'P@88w0rd')

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.40', 30006, '/', user_info))
channel = connection.channel()

# 创建队列
channel.queue_declare(queue="hello")

for i in range(0,100):
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='{}'.format('b')) 
    time.sleep(1)


# 关闭连接
connection.close