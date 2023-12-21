#!/bin/bash

declare -i step_counter=0
declare -i hit_counter=0
declare -a numbers

while true; do
    ((step_counter++))

    echo "Step: $step_counter"
    
    read -p "Please enter a number from 0 to 9 (q - quit): " user_input

    case "$user_input" in
        [qQ])
            echo "Exiting the game..."
            exit 0
            ;;

        [0-9])
            secret_number=$((RANDOM % 10))
            if [[ "$user_input" -eq "$secret_number" ]]; then
                ((hit_counter++))
                echo "Hit! My number: $secret_number"
                numbers+=("$secret_number:HIT")
            else
                echo "Miss! My number: $secret_number"
                numbers+=("$secret_number:MISS")
            fi

            hit_percent=$((hit_counter * 100 / step_counter))
            miss_percent=$((100 - hit_percent))

            echo "Hit: $hit_percent%" "Miss: $miss_percent%"

            if (( ${#numbers[@]} > 10 )); then
                last_10_items="${numbers[@]: -10}"
                echo -n "Numbers: "
                for item in $last_10_items; do
                    number=${item%:*}
                    result=${item#*:}
                    echo -n "$number "
                    if [ "$result" == "HIT" ]; then
                        echo -n "($result) "
                    else
                        echo -n "[$result] "
                    fi
                done
                echo
            else
                echo "Numbers: ${numbers[@]}"
            fi
            ;;

        *)
            echo "Invalid input. Please try again."
            ((step_counter--))
            ;;
    esac

    echo
done
