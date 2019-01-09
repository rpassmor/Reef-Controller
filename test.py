import json

def reset_times():
    ssTimes = {
            "startTimes": {
                    "start1": '00:00:00',
                    "start2": '00:00:00',
                    "start3": '00:00:00',
                    "start4": '00:00:00',
                    "start5": '00:00:00',
                    "start6": '00:00:00',
                    "start7": '00:00:00',
                    "start8": '00:00:00'
                    },
            "endTimes": {
                    "end1": '23:59:59',
                    "end2": '23:59:59',
                    "end3": '23:59:59',
                    "end4": '23:59:59',
                    "end5": '23:59:59',
                    "end6": '23:59:59',
                    "end7": '23:59:59',
                    "end8": '23:59:59'
                    }
            }
    with open("times.txt","w") as f:
            s=json.dumps(ssTimes, f, ensure_ascii=False)
            f.write(s)

reset_times()
