import time
from multiprocessing import cpu_count, Pool
from datetime import datetime

def print_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

def send_email(email: str):
    time.sleep(3.0)
    print(f"email sent to {email}")
    return {"status": "OK", "email": email}

if __name__ == "__main__": # required for multiprocessing
    emails = [
        "python@pylang.org", # 1
        "java@java.org", # 2
        "elixir@jose.valim.co", # 3
        "rust@rustdev.io", # 4
        "kotlin@jetbrains.ide", # 5
        "javascript@js.io", # 6
        "typescript@microsoft.com", # 7
        "haskell@hs.io", # 8
        "clojure@clojure.io", # 9
        "ruby@rails.com", # 10
        "erlang@armstrong.org", # 11
        "zig@zag.co", # 12
    ]
    
    print_time()
    core_count = cpu_count()
    print(f"using {core_count} cores")
    pool = Pool(processes=core_count)
    results = pool.map(send_email, emails)
        
    print_time()
    print(results)
    
# NOTE: if using Process instead of Pool, a Queue must be used
# to manage the order and processes
# several helpful examples found here:
# https://stackoverflow.com/questions/10415028/how-to-get-the-return-value-of-a-function-passed-to-multiprocessing-process