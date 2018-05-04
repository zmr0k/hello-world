url = "https://docs.docker.com/get-started/#prepare-your-docker-environment"

part = url.split("/")

print "part is:", part

for i in part:
    print i

url = "https://monitoring-icinga.corp-apps.com"

print "Parsing request..."
print "Source URL is:", url
print "...is becoming upper: ", url.upper()
print "URL has", len(url), "chars"

#lets split by followed char
data = url.split("/")
print "[data] massive is:", data

print "Lenght is:", len(data) #3
print data[0]  # mkyong.com
print data[1]  # 100
print data[2]  # 2015-10-1

for temp in data:
    print temp


print "hello"
