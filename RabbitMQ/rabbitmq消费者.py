import pika

# 连接 RabbitMQ
user_info = pika.PlainCredentials('admin', 'P@88w0rd')

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.40', 30006, '/', user_info))
channel = connection.channel()

# 创建队列
channel.queue_declare(queue="hello")

# 回调函数
def callback(ch, method, properties, body):
    print('消费者收到：{}'.format(str(body)))
    
channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback
                      )

print('Waiting for messages. To exit press CTRL+C')

# 一直处于等待接收消息的状态，如果没收到消息就一直处于阻塞状态，收到消息就调用上面的回调函数
channel.start_consuming()