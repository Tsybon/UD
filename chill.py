# /usr/bin/env python3
# import libs
import webbrowser
import os
import pandas as pd
import subprocess


# Define the command to run

directory = os.getcwd()

def task_1_pognali():
    uname_output = os.popen('uname -a').read()

    ifconfig_output = os.popen('ifconfig').read()

    ip_output = os.popen('ip -d a').read()

    # I haven't ufw so here is iptables

    # os.system("iptables -A INPUT -p tcp --dport 80 -s " + str(listen_ip) + " -j DROP")
    iptables_output = os.popen('iptables -S').read()

    with open('/etc/resolv.conf', 'r') as f:
        resolv_data = f.read()
    # analog with another files

    # make dict for outputing to csv
    task_1_dict = {
        'uname': uname_output,
        'ifconfig': ifconfig_output,
        'ip': ip_output,
        'iptables': iptables_output,
        'resolv': resolv_data
    }

    # CSV creating magic

    df = pd.DataFrame.from_dict(task_1_dict, orient='index', columns=['value'])

    # Write the DataFrame to a CSV file
    df.to_csv((directory + "/task_1.csv"), index_label='command')



def ud_chill():

    chill = directory + "/chill.mp4"
    print(chill)

    if os.path.exists(chill):
        pass
    else:
        os.popen("wget -O {} https://du.sf-converter.com/go?payload=1*eJzVVNuOqzYU%2FZVqpLFaqWTABgMjWUckkzTkRi4kmeRlRICAE8wdcqn67zXktHMq9eU8tUdCy2aL7e21lha%2FPxVJlbv%2BOo%2BeXp%2FCskyL15eXy%2BXSuSVVWR38jpuwl4tTuuGXmmyhdz1Ed8wU%2BenXr52m992NTuXR5J8T8xwKglDEQqhk6jn2750gSYLIr6nnJ%2B1R7S6NnNvBcc9f%2FGtKc59IWJNEGWqaCHxKdoPzbT%2F2h5NibG7H73q9DyxAUwIl2JFE2JH1DhQxoB5JBKOve5O0y9zq0l3J4SmnRW9zjPbYkcre2NoZPRy4FydJtLkCaOkERJJF8KBMvlIEuZ9V%2FBpFEZGbXwAWkmwHGCNIeoY9iAGLyTeUeI2%2FQYXTiiMPsII4Fa8lcQ5YTRgHSiBIIwJlQGNaupfYO6QFkUQdQ4UPT12i667SW2oH20XDk71JK7Td2ddlPoVDIxOTN0PwoVBkw%2FMC1GleEwkwynzSKv4MByyVQVyQk77vRce9q2WW3k26ZiQNVH3tTkFA85aJy6%2FIxcUqwirwqpw08ulc5YiVvK5gDHVJkVSsy7oG2ho3AoqqhsCx5pIr4Oz7qRPR2m8PPHLDOC9RVKGMgUu2%2FS4oeUmREZQRvxRRhf67aN9nab9YM4OTdXKHS%2FQwmsvkUw40bcBrgFvSCNoawjefVjTV1OXYCMCXRgC%2BxAUHzo9jw44vnBdHzghEf01jYdPAGmi%2BYE0Paw%2Bpm%2FFpc%2Fg31vBGGhDjN9T7uBqX5cIMjdH5tHiTbk41OE%2Bk%2B9i5Tze6ugr7cGkKwsE4CvWJujt7bVSxQQ1kiTKzJtopU9Boaeu5ahfmKr8qwrJaLyu8OYeCWcn5fnJ5Rm%2F8Ae1AKxMXI%2B0xcCopdTrTdsr2MkEnuF3sJps0Xqj6zbetgzTHVX9lSdXShneDdj22x8fZVe69Xef1KLgOcHcwvFaieImM1MnWk7wcZ4tkrmyMx0Ae1zZ5P15cEQZOs%2BMBQoj7JiG5RaVF3CAWm5zKsEXUotyi2qCq%2FbB5b9X%2F7rwj%2FosTJenvwGu6%2Fhl4JOpQVjBEWP9PAv%2Fw8v8Y%2BUkA18HBWl1Xt%2FUWHRaC0lO3iSn5a2Our7WTcdqshA9VkHHJIx%2FK2Zadx8EuwLgfrzZZrKta9T5NB92us557BzqrR%2F03dhQW%2FxZ5wwwmNZ3sT6L97n%2BcZ7ay0YaZNzrvYTrtLq%2Fmai%2BO5tYdmVtJNXvm4C5mhQK3gwPKmu1IjFHuGGzu3gaLsLRuy9i%2Bj3rqcDHjUS9pGfk856sw989FkoZJ7P%2F0s5XTgMZO9Av%2F4mFPYZRPr59p%2FuNPMo6lYg%3D%3D*1681021280*bc2c524178792d72".format(chill)).read()
    webbrowser.open("file://" + chill)

def task_2_pognali():



    get_uptime = os.popen("uptime").read()
    get_user = os.popen("who").read()
    last_logins = os.popen("last -n 5").read()
    ram_cpu = os.popen("ps aux | sort -nr -k 3,4 | head").read()
    get_mem = os.popen("free -h").read()
    disk = os.popen("df -h").read()

    task_2_dict = {
        'Time': get_uptime,
        'Current user': get_user,
        'Last 5 logins': last_logins,
        'RAM/CPU usage': ram_cpu,
        'Virtual Memory usage': get_mem,
        'Disk space': disk
    }

    # CSV creating magic

    df = pd.DataFrame.from_dict(task_2_dict, orient='index', columns=['value'])

    # Write the DataFrame to a CSV file
    df.to_csv((directory + "/task_2.csv"), index_label='Description')

def task_3_pognali():

    cmd = ["systemctl", "status", "apache2"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result)
    if "Active: inactive (dead)" in result.stdout:
        print("The Apache service is not running. I will run it")
        cmd = ["systemctl", "start", "apache2"]
        subprocess.run(cmd)

    else:
        print("The Apache service is running.")

def open_folder():
    webbrowser.open(os.path.realpath(directory))

ud_chill()
task_1_pognali()
task_2_pognali()
task_3_pognali()
open_folder()
