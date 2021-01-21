# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        text = input()
        even_characters, odd_characters = str(), str()
        for elem in range(0, len(text), 2):
            even_characters += text[elem]
        for elem in range(1, len(text), 2):
            odd_characters += text[elem]
        print('{} {}'.format(even_characters, odd_characters))
