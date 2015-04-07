path="../data/$1/$2/$3/$4"

bunzip2 -k $path/route-views/oix-full-snapshot-$1-$2-$3-$4.bz2
#./bgpdump $path/route-views/oix-full-snapshot-$1-$2-$3-$4 > $path/route-views/oix-full-snapshot-$1-$2-$3-$4.txt
mv $path/route-views/oix-full-snapshot-$1-$2-$3-$4 $path/route-views/oix-full-snapshot-$1-$2-$3-$4.txt
echo -e "rv extraction completed\n"

sed '1,/Network/d' $path/route-views/oix-full-snapshot-$1-$2-$3-$4.txt | mawk '{$1=$3=$4=$5=$6=$NF="";print $0;}' | sed -e 's/^[ \t]*//' | sed 's/     /:::/' > $path/route-views/prefix_aspath_unchecked
echo -e "rv prefix_aspath completed\n"

nice --10 python preprocess.py $1 $2 $3 $4 route-views

echo -e "rv completed\n"
