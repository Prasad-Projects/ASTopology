path="../data/$1/$2/$3/$4"

bunzip2 -k $path/route-views.isc/rib.$1$2$3.$4.bz2
./bgpdump $path/route-views.isc/rib.$1$2$3.$4 > $path/route-views.isc/rib.$1$2$3.$4.txt
rm $path/route-views.isc/rib.$1$2$3.$4
echo -e "isc extraction completed\n"

mawk -F '\n' -v RS='\n\n' '{print $3,$8;}' $path/route-views.isc/rib.$1$2$3.$4.txt | sed 's/PREFIX: //' | sed 's/ASPATH: //' | sed 's/ /:::/' > $path/route-views.isc/prefix_aspath_unchecked
echo -e "isc prefix_aspath completed\n"

nice --10 python preprocess.py $1 $2 $3 $4 route-views.isc

echo -e "isc completed\n"

