path="../data/$1/$2/$3/$4"

mawk '{print $1;}' $path/edgelist_dir > temp
sort temp | uniq -c > temp2
rm temp
mawk '{print $2,$1}' temp2 > $path/outdegree
rm temp2

mawk '{print $1;}' $path/outdegree > tempasn
sort $path/asn > temp && mv temp $path/asn
sort tempasn > temp && mv temp tempasn
comm -23 $path/asn tempasn | mawk '{print $1,"0";}' >> $path/outdegree
rm tempasn
sort $path/outdegree > temp && mv temp $path/outdegree

