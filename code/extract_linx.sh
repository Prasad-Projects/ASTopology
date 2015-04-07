path="../data/$1/$2/$3/$4"

bunzip2 -k $path/route-views.linx/rib.$1$2$3.$4.bz2
./bgpdump $path/route-views.linx/rib.$1$2$3.$4 > $path/route-views.linx/rib.$1$2$3.$4.txt
rm $path/route-views.linx/rib.$1$2$3.$4
echo -e "linx extraction completed\n"

mawk -F '\n' -v RS='\n\n' '{print $3,$8;}' $path/route-views.linx/rib.$1$2$3.$4.txt | sed 's/PREFIX: //' | sed 's/ASPATH: //' | sed 's/ /:::/' > $path/route-views.linx/prefix_aspath_unchecked
echo -e "linx prefix_aspath completed\n"

nice --10 python preprocess.py $1 $2 $3 $4 route-views.linx

echo -e "linx completed\n"
