import re
import urllib

def main():
    url = "http://www.iplocation.net/find-ip-address"
    htmltext = urllib.urlopen(url).read()
    
    pattern = '<span class="cf-footer-item"><span data-translate="your_ip">Your IP</span>(.+?)</span>' 
    regex = re.compile(pattern)
    
    results = re.findall(regex, htmltext)
    
    print str(results[0]).strip(':').strip(' ')
    

if __name__ == '__main__':
    main()
