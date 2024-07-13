import requests
import time
import os
from datetime import datetime
from termcolor import colored
import sys

# Config 
cookie = 'your roblo secuitry cookie'

cookie = {
    '.ROBLOSECURITY': cookie
}

def get_csrf_token(session):
    url = 'https://catalog.roblox.com/'
    response = session.post(url, cookies=cookie)
    return response.headers.get('x-csrf-token')

def fetch_inbox_messages(session, csrf_token):
    url = 'https://privatemessages.roblox.com/v1/messages?messageTab=inbox&pageNumber=0&pageSize=20'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'x-csrf-token': csrf_token
    }
    response = session.get(url, headers=headers, cookies=cookie)
    return response.json()

def archive_messages(session, csrf_token, message_ids):
    url = 'https://privatemessages.roblox.com/v1/messages/archive'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json;charset=UTF-8',
        'x-csrf-token': csrf_token
    }
    payload = {
        'messageIds': message_ids
    }
    response = session.post(url, headers=headers, json=payload, cookies=cookie)
    return response.json()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def update_console(status):
    clear_console()
    sys.stdout.write(status)
    sys.stdout.flush()

def main():
    start_time = time.time()
    total_archived = 0
    last_archived_id = None

    with requests.Session() as session:
        csrf_token = get_csrf_token(session)
        
        while True:
            inbox_response = fetch_inbox_messages(session, csrf_token)
            
            if 'collection' in inbox_response and inbox_response['collection']:
                message_ids = [message['id'] for message in inbox_response['collection']]
                
                archive_messages(session, csrf_token, message_ids)
                total_archived += len(message_ids)
                last_archived_id = message_ids[-1]
                
                status = colored(f"CSRF Token: {csrf_token}\n", 'yellow') + \
                         colored(f"Total Messages Archived: {total_archived}\n", 'cyan') + \
                         colored(f"Most Recent Message ID Archived: {last_archived_id}\n", 'cyan') + \
                         colored(f"Successfully Archived: {message_ids}\n", 'green')
                update_console(status)
                
                inbox_response_after_archiving = fetch_inbox_messages(session, csrf_token)
                if not inbox_response_after_archiving['collection']:
                    status = colored("All messages have been successfully archived.\n", 'green')
                    update_console(status)
                    break
                else:
                    status += colored("There are still messages in the inbox. Continuing the process...\n", 'yellow')
                    update_console(status)
            else:
                status = colored("No messages to archive or failed to retrieve messages.\n", 'red')
                update_console(status)
                break

    end_time = time.time()
    total_time_spent = end_time - start_time
    status += colored(f"Total Time Spent: {total_time_spent:.2f} seconds\n", 'cyan')
    update_console(status)

if __name__ == "__main__":
    main()
