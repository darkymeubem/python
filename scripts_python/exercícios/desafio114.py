import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')

except:
    print('\033[31mO acesso ao site não foi possível.\033[m')

else:
    print('\033[33mO acesso ao site foi concluído com sucesso\033[m')
    print(site.read())

