# Azure Queue Storage Trigger Python Class

# Requirements
pip install azure-storage-queue

# Usage
Queue = StorageQueue("YOUR_AZURE_ACCOUNT_NAME", "ACCESS_KEY")   
queue_name = Queue.create_queue("your_queue_name")    
Queue.add_message(queue_name, "Hello Alien !")    

# Contact
https://www.linkedin.com/in/agitt/    
agit@karesoft.com.tr
