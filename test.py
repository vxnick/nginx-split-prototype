#!/usr/bin/env python3
import requests  # python3 -m pip install requests
import signal
import sys
import time

num_reqs = 0
variant_a = 0
variant_b = 0
outliers = 0


def print_results():
    print()
    print("Requests:  {}".format(num_reqs))
    print("Variant A: {}".format(variant_a))
    print("Variant B: {}".format(variant_b))
    print("Other:     {}".format(outliers))
    print("Difference: {}".format(abs(variant_a - variant_b)))


def exit_handler(signal, frame):
    print_results()
    sys.exit()


signal.signal(signal.SIGINT, exit_handler)

while True:
    r = requests.get('http://localhost:8080/us/', headers={'user-agent': str(num_reqs)})
    if r.text.strip() == 'a':
        variant_a += 1
    elif r.text.strip() == 'b':
        variant_b += 1
    else:
        outliers += 1

    # time.sleep(0.05)
    num_reqs += 1

    if num_reqs in [100, 400, 800, 1000, 2000, 4000, 6000, 8000, 10_000]:
        print_results()
