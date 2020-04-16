import time

print(time.time())
# Gives time in seconds from beginning of time. They are not human readable
# we use them to perform functions


def send_emails():
    for i in range(10000):
        pass


start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)  # time required to execute the function
