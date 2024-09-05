#!/bin/bash 
CREATE_FILE="20501011_KTH".txt
echo > $CREATE_FILE 2>&1
echo "=========2.root_mgm start+++++++++++" >> $CREATE_FILE 2>&1
if ['awk -F: '$#==0' /etc/passwd | wc -l' -eq 1 ]
    then 
        echo "+++++++++++++++++ GOOD++++++++++++ " >> $CREATE_FILE 2>&1
        awk -F: '$3==0 {Print $1 " -> UID = " $3 }' /etc/passwd >> $CREATE_FILE 2>&1
else 
    echo "================== BAD ======================" >> $CREATE_FILE 2>&1

fi 
    cat ./$CREATE_FILE