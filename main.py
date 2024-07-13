import requests
import time
import os
from datetime import datetime
from termcolor import colored
import sys

# Config 
cookie = '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_BB9615B5E9669BA332F350CC0F36D33D9E2C6F3CF91C33D14D07DAAEC67BE4331CDC7D03388767CA1EA5EE5AA39DC62531AFAA4E6F96C95EA8BEF3BCEE3D867149673E408974BC3735CC32B70C150A426546F7F863F1996BBFA545EF9688B6149A552CC0F013DE487010855BA6820F32D9CCE0C927898973BE9CAD9E66AA767CD28927973AB736939D6CF60A3A258BCC9381E8807E340B7AC5791C4B4240BE65DCD9B48D39C8144C86B0EB501757428128F71E70B0B31CC3C5A2A086C481F2230C91C9DE9C76B9EBECA0793D29D27CFF1A42992AF41FBAE8C1F70E10D41FA7AE931FAF35D62C9A29D6B6219FC624E8D75443C12773BEB3BCE5A53409859701B2575576BFA515EE54A2F4C42C33F9134D3D7156BC5EFA14435741A98E196B14FC95B046A1BCAABBA3FB7AEBE6AF960828BFF2A9915DF94E28F7B88AC2E8CCB4E43724FDA6E960A3DE7BB8D38FE05D4BDF0F2B59E75829FD41CC7614B3313A0FF1B31FDCFC165EF802ECE4419D8281C1BD0FED405087769ABA7ACE721FB2F82A41FC5EF67864433DDE7B6AF67FDADE120EA479468F0127FD1EB1D6AAA2D6FE9B9737A9A8AFE66BACF9AA242130AE239BE51BEE594A621C66A6CA9D7C21CFDD770CF39FABFB34F89545F3ACD55AA2AB351BDEFC11144119DCE8E88512305D8451E6C6CE43424E88CAC02D541640650B41FCF05CB1148CC2FD5B11EAF466D42354B741406C9ADCBF04A41D6B1EE80A5CFCBEDBC907238CD321954BB7FBCB8EB289849B56C4D13C970B69E96AF5D420B2A9F096127FB8F633DDE59175E5656BAC702DCB03386099DF4AECF052853CD03F5A4F0E60BC995153EBE1DE0F3442A4B9FA6791CCD2464A5B8257512A6B7613FAF0EE5C86C1FB33781911C1EEBC84379758FB3E331B705B238200298B452BF4F9779BFD62C6F2054D90550DE5863EB631959D773636D15183B4E59B40B982778B50A992ED3FA022FD3FFDDCF25481E9333731033E4622AEAFDD4D925CACBD464D4CDA7DF18CD8ACCB523EA319A39DEC5ECF6940D90911'

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