1. Confirm what runlevel the system is operating at.
--> runlevel

2. Create a group called trainee with gid 1500
--> groupadd -g 1500 trainee

3. command about cpio.
--> find /directory_path -mtime -1 -ls
--> find / -print | cpio -covB > /dev/st0
--> cpio -icdvt < /dev/st0 > /tmp/st_content
--> cpio –icduv < /opt/etc.cpio (还原到原来位置)

4. prevent root to login
--> https://www.centos.org/docs/5/html/5.1/Deployment_Guide/s2-wstation-privileges-noroot.html

5. Logging & monitoring
--> lsof
--> /etc/logrotate.conf

6. chkconfig
#!/bin/bash

option=$1
service=$2

echo "option = $option  service=$service"
path="$HOME/code/chkconfig/init.d/$service"
echo $path

content=`cat $path`
echo $content

str=""

while read line
do
	pattern=`echo $line | grep -o -E chkconfig.*$`
	if [[ $pattern != "" ]];
	then
		str=$pattern
		break
	fi
done < $path
echo $pattern

mode=`echo $pattern | awk '{print $2}'`
startNumber=`echo $pattern | awk '{print $3}'`
killNumber=`echo $pattern | awk '{print $4}'`

echo $mode
echo $startNumber
echo $killNumber

echo "----------"

i=0
limit=6
while [[ $i -le $limit ]]
do
	str=`echo $mode | grep -o -E $i`
	if [[ ! -n $str ]];then
		echo " $i empty"
		target="$HOME/code/chkconfig/rc$i.d/K$killNumber$service"
		if [[ $option = "--add" ]];then
			ret=`ln -s $path $target`
		elif [[ $option = "--del" ]];then
			ret=`rm $target`
		else
			echo "Command not found!"
		fi
	else
		echo "Find $str"
		target="$HOME/code/chkconfig/rc$i.d/S$startNumber$service"
		if [[ $option = "--add" ]];then
			ret=`ln -s $path $target`
		elif [[ $option = "--del" ]];then
			ret=`rm $target`
		else
			echo "Command not found!"
		fi
	fi
	i=`expr $i + 1`
done















