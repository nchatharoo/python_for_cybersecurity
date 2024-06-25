from scapy.all import TCP, rdpcap
import collections
import os
import re
import sys
import zlib

OUTDIR = '/root/Desktop/pictures'
PCAPS = '/root/Downloads'

Response = collections.namedtuple('Response', ['header', 'payload'])
                                  
def get_header(payload):
    try:
       header_raw = payload[:payload.index(b'\r\n\r\n')+2] 
    except ValueError:
        sys.stdout.write('-')
        sys.stdout.flush()
        return None
    
    header = dict(re.findall(r'(?P<name>.*?): (?P<value>.*?)\r\n', header_raw.decode()))
    if 'Content-Type' not in header:
        return None
    return header

def extract_content(Response, content_name='image'):
    content, content_type = None, None
    if content_name in Response.header['Content-Type']:
        content_type = Response.header['Content-Type'].split('/')[1]
        content = Response.payload[Response.payload.index(b'\r\n\r\n')+4:]
        if 'Content-Encoding' in Response.header:
           if Response.header['Content-Encoding'] == "gzip":
              content = zlib.decompress(Response.payload, zlib.MAX_WBITS | 32)
           elif Response.header['Content-Encoding'] == "deflate":
              content = zlib.decompress(Response.payload)

    return content, content_type

class Recapper:
    def __init__(self, fname):
        pcap = rdpcap(fname)
        self.sessions = pcap.sessions()
        self.responses = []

    def get_response(self):
        pass

    def write(self, content_name):
        pass

if __name__ == '__main__':
    pfile = os.path.join(PCAPS, 'pcap.pcap')
    recapper = Recapper(pfile)
    recapper.get_response()
    recapper.write('image')