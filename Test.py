# -*- coding:utf-8 -*-
from idlelib.IOBinding import encoding

print "hello world!";

print 10.0 / 4.0;

print 10.0 // 4.0;

print 10 / 4;

print 10 // 4;


print "java %c " % 'a'
print "java %s " % 'aaa'
print "java %d " % 100
print "java %u " % 100
print "java %o " % 023
print "java %x " % 0xABC
print "java %X " % 0xABC
print "java %.2f " % 3.1415
print "java %.2e " % 31415
print "java %E " % 31415
print "java %.3g " % 3.1415
print "java %.3G " % 3.1415

print "python %-f " % 3.1415

print "java %5.2f " % 3.1415

print u'Hello\u0020World !'

print "python".capitalize()
print "python".center(11)
print "python is very fast".count('y')
print "python is very fast 快".decode(encoding='UTF-8').encode(encoding='GBK')

aList = [123, 23, '122', '13', 'xyz', 'zara', 'abc', 'xyz'];

aList.sort();
print "List : ", aList;

str1 = "和谐b你b可爱女人"
temp1 =  str1.split("你");
print str(temp1[0]);

