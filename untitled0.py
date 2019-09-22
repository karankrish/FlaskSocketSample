import flaskSocket
import pika

parameters = pika.URLParameters('amqp://user:bitnami@localhost:5672')
connection = pika.BlockingConnection(parameters) 
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)
    app = flaskSocket.create_app()
    return app

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()



if __name__ == '__main__':
    app.run(host="192.168.100.20",port=6002)
