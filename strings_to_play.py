url = "https://docs.docker.com/get-started/#prepare-your-docker-environment"

part = url.split("/")

print "part is:", part

for i in part:
    print i

url = "https://monitoring-icinga.corp-apps.com/monitoring/list/services?service_problem=1&(host!=%2Amuat%2A&host!=%2Alint%2A&host!=%2Amdev%2A&host!=%2Adev%2A&host!=%2Amak%2A&host!=%2Atdr%2A&host!=testlauncher%2A&host!=%2A.lt%2A&host!=%2A.rgt%2A&host!=%2A-lt%2A.%2A&host!=docker-beatrix-%2A.mal%2A&host!=%2A.bettingpartners.com%2A&host!=openstack.mal.corp-apps.com&host!=openstack-compute-2.mal.internal&host!=openstack-compute-3.mal.internal&host!=openstack-monitoring-1.mal.internal&host!=openstack-monitoring-2.mal.internal&host!=opennms.mal.corp-apps.com&host!=fin-msdb01-tptk.corp.kazootek.com&service!=NETAPP-cpu-load&service!=snmp-windows-cpu&service!=CPU-load&host!=bigip.mya&host!=foreman.mya.internal&host!=tam-msdb01-mkpk.corp.kazootek.com&host!=docker-beatrix-infra-%2A.tpa.internal&host!=docker-beatrix-%2A.tpa.internal&service!=snmp-lvmstatus-check&host!=cgs-admin-%2A.b2pa.intra-apps.com)&modifyFilter=&sort=service_severity&dir=desc#!/monitoring/service/show?host=pal-auth01-mvpa.a.local&service=Storage%3A%20All%20drives"

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