l=0
for i in `grep ^https://youtu.be $1 `
do
    temp=`youtube-dl $i  --get-duration`
    tempM=`echo $temp |  cut -d: -f1`
    tempS=`echo $temp |  cut -d: -f2`
    l=$((tempM*60+tempS+l))
    echo "$i: delka $temp"
done

l=$((l/60))

echo $1:$l

