path="../data/$1/$2/$3/$4"

rclist=("route-views" "route-views2" "route-views3" "route-views4" "route-views6" "route-views.saopaulo" "route-views.linx" "route-views.sydney" "route-views.wide" "route-views.kixp" "route-views.eqix" "route-views.isc" "route-views.telxatl" "route-views.jinx" )
for i in "${rclist[@]}"; do
	rm $path/$i/asn
	rm $path/$i/edgelist_dir
	rm $path/$i/edgelist_undir
	rm $path/$i/prefix_aspath_unchecked
	rm $path/$i/prefix_origin
	rm $path/$i/rib.$1$2$3.$4.txt
done


