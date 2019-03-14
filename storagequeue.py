from azure.storage.queue import QueueService, QueueMessageFormat

"""  Queue Management Class  """


class StorageQueue:
    def __init__(self, account_name, account_key):
        try:
            self.queue_service = QueueService(account_name=account_name, account_key=account_key)
            self.queue_service.encode_function = QueueMessageFormat.text_base64encode
        except Exception:
            print("Login failed please check your account name and access key")
            return False

    def add_message(self, queue_name, message):
        """ Create Queue Message """
        self.queue_service.put_message(queue_name, message)

    def create_queue(self, queue_name):
        """ Create Queue """
        self.queue_service.create_queue(queue_name)
        return queue_name

    def delete_queue(self, queue_name):
        """ Delete Queue """
        self.queue_service.delete_queue(queue_name)

    def create_default_queue(self):
        """ Create Default Queue Name """
        self.create_queue("incoming")
        self.create_queue("processing")
        self.create_queue("outgoing")

    def getmessages(self,queue_name):
        """ Get Queue Message List """
        return self.queue_service.get_messages(queue_name)
