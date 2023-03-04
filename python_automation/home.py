import requests
import schedule
import time

def send_message():
    resp = requests.post('http://textbelt.com/text', {
        'phone':9803239930,
        'message':'hey good morning',
        'key' :'textbelt'
    })

    print(resp.json())

def main():

    # schedule.every().day.at('06:00').do(send_message())
    schedule.every(10).seconds.do(send_message())
    
    while True:
        schedule.run.pending()
        time.sleep(1)   

main()