from __future__ import print_function
import sys
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

# m-rsu
# marsu

def align(raw,clean):
    raw_all=""
    clean_all=""
    if raw and clean:
        alignments=pairwise2.align.globalxx(raw, clean, gap_char="@")
        raw_a,clean_a, s1, s2, s3=alignments[0]
        raw_a=raw_a.decode("latin1")
        clean_a=clean_a.decode("latin1")
        for i in range(0,len(raw_a),80):
            for raw_char,clean_char in zip(raw_a[i:i+80],clean_a[i:i+80]):
                if raw_char==clean_char:
                    clean_all+='<span style="color:green">'+clean_char+'</span>'
                    raw_all+='<span style="color:green">'+raw_char+'</span>'
                else:
                    if clean_char!="@":
                        clean_all+=clean_char
                    if raw_char!="@":
                        raw_all+=raw_char
            #print raw_a[i:i+80]
            #print clean_a[i:i+80]
        print("<p>RAW",raw_all.encode("utf-8"),"</p>")
        print("<p>CLEAN",clean_all.encode("utf-8"),"</p>")
        print()
        


clean=True

lines_clean=[]
lines_raw=[]

print('<html> <meta charset="UTF-8"><body>')

counter=1
for line in sys.stdin:
    line=line.strip()
    if line=="":
        continue

    if line[0].isdigit():
        if lines_clean:
            print()
            print(counter)
            print("<p>")
            print()
            counter+=1
            align(" ".join(lines_raw)," ".join(lines_clean))
            print("</p>")
            #print (" ".join(lines_raw)).decode("latin1").encode("utf-8")
            #print
            #print
            lines_clean=[]
            lines_raw=[]
        clean=True
    elif line.startswith("---"):
        clean=False
    else:
        if clean:
            lines_clean.append(line)
        else:
            lines_raw.append(line)
    

print("</body></html>")
