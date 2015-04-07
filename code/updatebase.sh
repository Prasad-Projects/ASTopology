api_key="AIzaSyArCnPfsf5SjJmvnq2r7Q4KO2c1aLYZw1Y"
path="../data/$1/$2/$3/$4"

while read line
do
	echo -e "\n------------------------------------------------------\n"
	tput setf 4 && echo "ASN : $line" && tput setf 0
	rir=`grep "^$line " $path/asn_rir | mawk '{print $2;}'`		#get corresponding rir
	if [ "$rir" == "lacnic" ]
	then
		grep " $line$" $path/prefix_origin_unchecked | mawk '{print $1;}' | mawk -F '/' '{print $1;}' > temp
		sed -i '/:/d' temp		# delete ipv6 prefixes
		if [ ! -s temp ]
		then
			echo "No IP found"
			echo "$line 0" >> ../base/gl/angle_gl		# if no ip is found, set lng as -1
			echo "$line 0" 
			continue		
		fi
		while read line2
		do
			echo "$line2"
			o1=`echo "$line2" | mawk -F '.' '{print $1;}'`
			o2=`echo "$line2" | mawk -F '.' '{print $2;}'`
			o3=`echo "$line2" | mawk -F '.' '{print $3;}'`
			o4=`echo "$line2" | mawk -F '.' '{print $4;}'`
			python integerip.py $o1 $o2 $o3 $o4 >> temp2
		done < temp
		mv temp2 temp
		while read line3
		do
			locid=`mawk -F ',' -v ip=$line3 '{if($1<=ip && $2>=ip) print $3;}' ../base/gl/GeoLiteCity-Blocks.csv`
			lng=`grep "^$locid," ../base/gl/GeoLiteCity-Location.csv | mawk -F ',' '{print $7;}'`
			if [ $(echo "$lng < 0" | bc) -eq 1 ]
			then
				lng=`echo "$lng + 360" | bc`
			fi
			echo "$lng" >> temp2
		done < temp
		mv temp2 temp
		mawk -v asn=$line 'BEGIN{ avg=0; } { avg=avg+$1; } END{ avg=avg/NR; print asn,avg; }' temp >> ../base/gl/angle_gl
		rm temp
		echo "$line longitude : $lng"
		continue
	fi	
	
	check=`grep "^$line$" ../base/gc/asn_whois`		#check if present in whois folder
	if [ -z "$check" ]		#if not
	then
		whois -h whois.$rir.net AS$line > ../base/gc/whois/$line #get whois entry from corresponding rir
		echo "Query sent to $rir"
	fi
	#to get address
	cd ../base/gc/whois/	#change directory to base/gc/whois
	address=`../../../code/$rir.sh $line | mawk -F '\t' '{print $2;}'`		#extract address from whois entry
	tput setf 4 && echo "Address : $address" && tput setf 0
	cd ../../../code/
	address=`echo "$address" | sed 's/ /+/g' | sed 's/#/%23/g'`
	curl -s "https://maps.googleapis.com/maps/api/geocode/json?address=$address&sensor=false&key=$api_key" | json_reformat > temp
	status=`cat temp | jq '.status' | sed 's/"//g'`
	if [ "$status" == "OK" ]
	then
		tput setf 4 && echo "$status" && tput setf 0
		lat=`cat temp | jq '.results[0].geometry.location.lat'`
		lng=`cat temp | jq '.results[0].geometry.location.lng'`
		echo "$line,$lat,$lng" >> ../base/gc/asnlatlng
		echo "$line,$lat,$lng"
		rm temp
	else
		rm temp
		tput setf 4 && echo "$status" && tput setf 0
		grep " $line$" $path/prefix_origin_unchecked | mawk '{print $1;}' | mawk -F '/' '{print $1;}' > temp
		sed -i '/:/d' temp		# delete ipv6 prefixes
		if [ ! -s temp ]
		then
			echo "No IP found"
			echo "$line 0" >> ../base/gl/angle_gl		# if no ip is found, set lng as -1
			echo "$line 0"
			continue		
		fi
		while read line2
		do
			echo "$line2"
			o1=`echo "$line2" | mawk -F '.' '{print $1;}'`
			o2=`echo "$line2" | mawk -F '.' '{print $2;}'`
			o3=`echo "$line2" | mawk -F '.' '{print $3;}'`
			o4=`echo "$line2" | mawk -F '.' '{print $4;}'`
			python integerip.py $o1 $o2 $o3 $o4 >> temp2
		done < temp
		mv temp2 temp
		while read line3
		do
			locid=`mawk -F ',' -v ip=$line3 '{if($1<=ip && $2>=ip) print $3;}' ../base/gl/GeoLiteCity-Blocks.csv`
			lng=`grep "^$locid," ../base/gl/GeoLiteCity-Location.csv | mawk -F ',' '{print $7;}'`
			echo "$lng"
			if [ $(echo "$lng < 0" | bc) == 1 ]
			then
				lng=`echo "$lng + 360" | bc`
			fi
			echo "$lng" >> temp2
		done < temp
		mv temp2 temp
		mawk -v asn=$line 'BEGIN{ avg=0; } { avg=avg+$1; } END{ avg=avg/NR; print asn,avg; }' temp >> ../base/gl/angle_gl
		rm temp
		echo "$line longitude : $lng"
	fi
done < ../base/asn_toupdate

#update asn lists and angle
ls -l ../base/gc/whois/ | mawk '{print $NF;}' > ../base/gc/asn_whois
sort ../base/gc/asnlatlng | uniq > temp && mv temp ../base/gc/asnlatlng
mawk -F ',' '{if($3<0) print $1,$3+360; else print $1,$3;}' ../base/gc/asnlatlng > ../base/gc/angle_gc
mawk '{print $1;}' ../base/gc/angle_gc > ../base/gc/asn_gc

cd ../base/gl/
sort angle_gl | uniq > temp && mv temp angle_gl
mawk '{print $1;}' angle_gl > asn_gl

cd ..
cat ./gl/asn_gl > asn_base && cat ./gc/asn_gc >> asn_base
sort asn_base | uniq > temp && mv temp asn_base
cd ../code/

tput reset
