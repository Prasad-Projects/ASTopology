# outdegree,asn_country,asn_x_y,edgelist_type,edgelist_with_colors,nodelist_with_colors,
./extract_rv.sh $1 $2 $3 $4 &
./extract_rv2.sh $1 $2 $3 $4 &
./extract_rv3.sh $1 $2 $3 $4 &
./extract_rv4.sh $1 $2 $3 $4 &
./extract_rv6.sh $1 $2 $3 $4 &
./extract_saopaulo.sh $1 $2 $3 $4 &
./extract_linx.sh $1 $2 $3 $4 &
./extract_sydney.sh $1 $2 $3 $4 &
./extract_wide.sh $1 $2 $3 $4 &
./extract_kixp.sh $1 $2 $3 $4 &
./extract_eqix.sh $1 $2 $3 $4 &
./extract_isc.sh $1 $2 $3 $4 &
./extract_telxatl.sh $1 $2 $3 $4 &
./extract_jinx.sh $1 $2 $3 $4 &
wait
python uniq.py $1 $2 $3 $4
#prefix_aspath_unchecked,prefix_origin,edgelist_dir,edgelist_undir,asn
python asn_whois.py $1 $2 $3 $4		#asn_whois,asn_rir 
./outdegree.sh $1 $2 $3 $4		#outdegree
python getradius.py $1 $2 $3 $4		#radius	
comm -23 $path/asn ../base/asn_base > ../base/asn_toupdate
./updatebase.sh $1 $2 $3 $4		
python getangle.py $1 $2 $3 $4		#angle




#./plot.sh $1 $2 $3 $4 $5		

echo "done"
