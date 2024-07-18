import urllib.request

# User-Agents (kopiert aus https://de.wikipedia.org/wiki/User_Agent)
agents = [
    "Lynx/2.8.4rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.6c",
    "Opera/9.63 (Macintosh; Intel Mac OS X; U; en) Presto/2.1.1",
    "Mozilla/1.0N (Windows)",
    "Mozilla/4.06 [es] (Win98; I)",
    "Mozilla/1.22 (compatible; MSIE 2.0; Windows 95)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3",
    "BlackBerry8520/5.0.0.681 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/114",
    "Mozilla/5.0 (Linux; U; Android 2.2; de-de; HTC Magic Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "SonyEricssonT68/R201A",
    "Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 920) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537",
    "undefined/1.0"
]

for a in agents:
    req = urllib.request.Request(
        "https://google.com/",
        data = None,
        headers = {
            'User-Agent': a
        }
    )

    contents = urllib.request.urlopen(req).read()


    print("For \"" + a + "\": " + str(len(contents)))