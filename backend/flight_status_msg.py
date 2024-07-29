#for_messsaging
pip install mysql-connector-python twilio
import mysql.connector
import time
from twilio.rest import Client

# Twilio configuration
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_phone_number = 'your_twilio_phone_number'
user_phone_number = 'user_phone_number'

client = Client(account_sid, auth_token)

# MySQL configuration
db_config = {
    'user': 'shanu',
    'password': 'shanu@1234',
    'host': 'localhost',
    'database': 'flight_status'
}

# Connect to the database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()


def check_for_changes():
    cursor.execute("SELECT * FROM change_log WHERE notified = 0")
    changes = cursor.fetchall()

    for change in changes:
        id, table_name, operation, old_data, new_data, change_time = change

        # Send SMS via Twilio
        message = f"Change detected in {table_name} at {change_time}.\nOperation: {operation}\nOld Data: {old_data}\nNew Data: {new_data}"
        client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=user_phone_number
        )

        # Mark as notified
        cursor.execute("UPDATE change_log SET notified = 1 WHERE id = %s", (id,))
        conn.commit()


# Monitor the log table for changes
while True:
    check_for_changes()
    time.sleep(60)  # Check every minute
    
python monitor_changes.py
