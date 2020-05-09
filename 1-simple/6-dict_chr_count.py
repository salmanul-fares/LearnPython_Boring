import pprint

message = 'the world is a fantastic place as long as you see it that way, rivals and friends will exist, but most of them are chill as long as you find a balance between noticing them and ignoring them.'

chr_count={}

for chr in message:
    chr_count.setdefault(chr,0)
    chr_count[chr] += 1

pprint.pprint(chr_count)
