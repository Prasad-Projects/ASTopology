path="../data/$1/$2/$3/$4"

cp $path/angle plot/
cp $path/outdegree plot/
cp $path/radius plot/
cp $path/asn plot/
cp $path/edgelist_undir plot/

PCC=`pkg-config --cflags --libs cairo`
cd ./plot/

sort -k1,1 asn > temp && mv temp asn
sort -k1,1 angle > temp && mv temp angle
sort -k1,1 radius > temp && mv temp radius
sort -k1,1 outdegree > temp && mv temp outdegree

python polartocart.py
python ecfromnc.py

sort -nk10,10 ecwithrgba > temp && mv temp ecwithrgba

mawk '{print $2,$3,$5,$6,$7,$8,$9,$10;}' ecwithrgba > inputtoplot
mawk '{print $2,$3,$4,$5,$6,$7;}' ncwithnsrgb >> inputtoplot

gcc -O3 plot.c $PCC
edges=`wc -l ecwithrgba | mawk '{print $1;}'`
nodes=`wc -l ncwithnsrgb | mawk '{print $1;}'` 

./a.out $edges $nodes $5 < inputtoplot
cd ..
mv plot/$5 $path/$5 

cd ..
#mv plot/$5 $path/


