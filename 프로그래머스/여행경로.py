from collections import defaultdict

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

answer = []
routes = defaultdict(list)

for ticket in tickets:
    routes[ticket[0]].append(ticket[1])
for key in routes.keys():
    routes[key].sort(reverse=True)
stack = ["ICN"]
while stack:
    tmp = stack[-1]
    if not routes[tmp]:
        answer.append(stack.pop())
    else:
        stack.append(routes[tmp].pop())
answer.reverse()
print(answer)