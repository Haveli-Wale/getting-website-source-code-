print("if output = any type of eroor . Please try pip install requests && pip install re")
import requests
import re



url1=str(input('provide the link without https://==>'))

def CheckUp():
    website_name1 = url1
    url2 = re.findall("^www", website_name1)
    url3 = re.findall("^https", website_name1)
    if url2:
        url = 'https://'+url1
        return url
    elif url3:
         url = website_name1
         return url
    else:
        print("Incorrect Url==> provide orignal url if form of www.google.com Or https://www.google.com")

def Response():
    url = CheckUp()
    response = requests.get(url)
    return response

def FileName():
    a = CheckUp()
    char1 = 'w.'
    index1 =a.index(char1)
    b = index1 + 2
    b = a[b:]
    c = b
    char2 = '.c'
    index2 = c.index(char2)
    data = c[:index2]
    fname = data
    return fname

def MakeAfile():
    response = Response()
    fname = FileName()
    file = open (f'{fname}.txt',"w")
    file.write(response.text)
    file.close()
    print("response code 200:File Genrated Sucessfully")


def run():
    try:
        MakeAfile()
    except:
        print("Something went worng check url ::==> this tools support only termux")

run()