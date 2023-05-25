#!/bin/bash

path="/home/ftodino/CoOp/output"

logs=$(find $path -name "log.txt" ! -path "*test*" | sort -V)
csv_file="/home/ftodino/CoOp/logs/log_data.csv"
printf "name total correct accuracy error macro_f1\n" > $csv_file

for log in $logs; do
    content=$(sed -n '/=> result/,/Elapsed/p' $log)
    
    current_total=$(echo "$content" | grep -oP "total:\s+\d+([\.,]\d+)?" | sed 's/,//g' | awk '{print $2}')
    current_correct=$(echo "$content" | grep -oP "correct:\s+\d+([\.,]\d+)?" | sed 's/,//g' | awk '{print $2}')
    current_accuracy=$(echo "$content" | grep -oP "accuracy:\s+\d+([\.,]\d+)?" | sed 's/,/./g' | awk '{print $2}')
    current_accuracy=${current_accuracy/./,}
    current_error=$(echo "$content" | grep -oP "error:\s+\d+([\.,]\d+)?" | sed 's/,/./g' | awk '{print $2}')
    current_error=${current_error/./,}
    current_macro_f1=$(echo "$content" | grep -oP "macro_f1:\s+\d+([\.,]\d+)?" | sed 's/,/./g' | awk '{print $2}')
    current_macro_f1=${current_macro_f1/./,}

    log_name=$(echo $log | cut -d'/' -f6,7,8,9,10)

    printf "%s %s %s %s %s %s\n" "$log_name" "$current_total" "$current_correct" "$current_accuracy" "$current_error" "$current_macro_f1" >> $csv_file
done

echo "CSV file created: log_data.csv"