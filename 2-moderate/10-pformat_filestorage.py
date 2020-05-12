import pprint

students = [
{'name':'salmanul fares', 'dept':'cs', 'regno':'fkarscs029'},
{'name':'hazanul banna', 'dept':'bmmc', 'regno':'fkzsmmc056'}
]

fileStr = open('stdstore.py', 'w')
fileStr.write('students = ' + pprint.pformat(students) + '\n')
fileStr.close()

# TODO: learn open attributes r,w,a,r+,w+,a+
