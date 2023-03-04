#will recieve a url or a particular link and check the status of that site
import urllib.request as urllib


def checker(url):
    print("Checking connectivity ")
    response = urllib.urlopen(url)
    
    print(f"Connected to {url} successfully")
    
    #code of 200 -> was able to access
    print(f"The response code was {response.getcode()}")

def main():
    print("This is a site connectivity checker program")
    url = input("Enter the url of the site you want to check:\n")
    
    checker(url)
    
main()