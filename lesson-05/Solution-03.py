import requests


def save_from_net(link):
    filename = link.split("/")[-1]
    r = requests.get(link)
    open(filename, "wb").write(r.content)


link = "https://raw.githubusercontent.com/manti-by/lessons/master/LICENSE"

save_from_net(link)
