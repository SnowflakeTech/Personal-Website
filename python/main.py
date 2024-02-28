import requests
import json
import sys
import datetime

logging = True

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open(f"Log-{datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}.txt", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

if logging:
    sys.stdout = Logger()

current_comment = {}
room_id = input("Id của phòng học : ")
while True:
    comment_trashpile = requests.get(f"https://api.vuihoc.vn/api/comment/live-class/list/{room_id}")
    comment = json.loads(comment_trashpile.text)

    if current_comment != comment["data"][0]:
        current_comment = comment["data"][0]
        print("[" + current_comment["update_date"] + "] " + current_comment["user"]["full_name"] + " : " + current_comment["comment"])
