path="../data/$1/$2/$3/$4"

bunzip2 -k $path/route-views.saopaulo/rib.$1$2$3.$4.bz2
./bgpdump $path/route-views.saopaulo/rib.$1$2$3.$4 > $path/route-views.saopaulo/rib.$1$2$3.$4.txt
rm $path/route-views.saopaulo/rib.$1$2$3.$4
echo -e "saopaulo extraction completed\n"

mawk -F '\n' -v RS='\n\n' '{print $3,$8;}' $path/route-views.saopaulo/rib.$1$2$3.$4.txt | sed 's/PREFIX: //' | sed 's/ASPATH: //' | sed 's/ /:::/' > $path/route-views.saopaulo/prefix_aspath_unchecked
echo -e "saopaulo prefix_aspath completed\n"

nice --10 python preprocess.py $1 $2 $3 $4 route-views.saopaulo

echo -e "saopaulo completed\n"

