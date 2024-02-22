def hack(s):
    word = "cabriolets"
    count = 0
    for i in range(len(s)):
        if s[i] != word[i]:
            count += 1
    return count

def main():
    try:
        while True:
            s = input().strip()
            if not s:
                break
            print(hack(s))
    except EOFError:
        pass
main()
