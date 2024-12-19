with open('log.txt') as f:
    logs = f.readlines()

event_counts = {}
for log in logs:
   if ' ' in log.strip():  # Check if the line contains a space
    _, event = log.strip().split(' ', 1)
    event_counts[event] = event_counts.get(event, 0) + 1

print(event_counts)

