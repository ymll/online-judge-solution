T = raw_input()

def is_stack(in_str, out_str):
    if in_str == out_str[::-1]:
        return True
    return False

def is_queue(in_str, out_str):
    if in_str == out_str:
        return True
    return False

for t in range(int(T)):
    N = raw_input()
    in_str = raw_input().split()
    out_str = raw_input().split()
    stack = is_stack(in_str, out_str)
    queue = is_queue(in_str, out_str)
    if stack and queue:
        print("both")
    elif stack:
        print("stack")
    elif queue:
        print("queue")
    else:
        print("neither")
