import psutil
import re
import sys

def process_average(pid):
    process_id = psutil.Process(pid)

    print("Process Details for Pid:" , pid , " Name: (", process_id.name(),"),",\
          " Owner: (", process_id.username(),"),",\
          "Memory: (" , process_id.memory_percent(),"),"\
          " CPU: ",process_id.cpu_percent(interval=30))


if len(sys.argv) < 2:
    print("Usage: ", sys.argv[0], " PID|PROCESNAME")
    print(sys.argv[0]," 1")
    print(sys.argv[0]," bash")

    sys.exit(0)


process_pids = psutil.pids()


input_regex = sys.argv[1]

regex_is_number = True
try:
   val = int(input_regex)
except ValueError:
   regex_is_number = False

while True:
 for ppid in process_pids:
     process_id = psutil.Process(ppid)
     if regex_is_number:

         if ppid == int(input_regex):
             process_average(ppid)
     elif not regex_is_number:
        name_process = process_id.name()
        regexp = re.compile(input_regex)
        if regexp.search(name_process):
            process_average(ppid)
     else:
        print("Sorry we did not find ", input_regex , " in process list")
        sys.exit(0)
 print("---------------------------------------------------------------")