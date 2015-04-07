path="../data/$1/$2/$3/$4"

bunzip2 -k $path/route-views.eqix/rib.$1$2$3.$4.bz2
./bgpdump $path/route-views.eqix/rib.$1$2$3.$4 > $path/route-views.eqix/rib.$1$2$3.$4.txt
rm $path/route-views.eqix/rib.$1$2$3.$4
echo -e "eqix extraction completed\n"

mawk -F '\n' -v RS='\n\n' '{print $3,$8;}' $path/route-views.eqix/rib.$1$2$3.$4.txt | sed 's/PREFIX: //' | sed 's/ASPATH: //' | sed 's/ /:::/' > $path/route-views.eqix/prefix_aspath_unchecked
echo -e "eqix prefix_aspath completed\n"

nice --10 python preprocess.py $1 $2 $3 $4 route-views.eqix 

echo -e "eqix completed\n"

