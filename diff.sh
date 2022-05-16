
#! /bin/bash
# 保存当前目录
currentDir=$PWD
echo "Start to publish...\n"


i=1
while(( $i<=42 ))
do
	cd ./qiskit/$i
#	diff -B --suppress-common-lines buggy_$i.py fixed_$i.py > modify_$i.txt
	cd $currentDir
	let "i++"	
done

