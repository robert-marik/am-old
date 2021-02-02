l=0
for i in `grep -h ^https://youtu.be $1 `
do
    cislo=`echo $i | cut -d/ -f4 `
    if  [ ! -f cache/$cislo.txt ]; then
	echo "Getting information about $i"
	temp=`youtube-dl $i  --get-duration`
	echo $temp > cache/$cislo.txt
    fi
    temp=`cat cache/$cislo.txt`
    tempM=`echo $temp |  cut -d: -f1`
    tempS=`echo $temp |  cut -d: -f2`
    l=$((tempM*60+tempS+l))
    echo "$i $temp min."
done

l=$((l/60))

echo "$1 total: $l minut"

