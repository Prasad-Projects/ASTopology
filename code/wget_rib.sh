# ./wget_rib.sh yyyy mm dd hhhh

tput bold && tput setf 4 && echo -e "\n\nDownloading from route-views" && tput setf 0 && tput sgr0
wget -c -P ../data/$1/$2/$3/$4/route-views http://archive.routeviews.org/oix-route-views/$1.$2/oix-full-snapshot-$1-$2-$3-$4.bz2
tput bold && tput setf 4 && echo -e "Done" && tput setf 0 && tput sgr0

tput bold && tput setf 4 && echo -e "\n\nDownloading from route-views2" && tput setf 0 && tput sgr0
wget -c -P ../data/$1/$2/$3/$4/route-views2 http://archive.routeviews.org/bgpdata/$1.$2/RIBS/rib.$1$2$3.$4.bz2
tput bold && tput setf 4 && echo -e "Done" && tput setf 0 && tput sgr0

#tput bold && tput setf 4 && echo -e "\n\nDownloading from route-views3" && tput setf 0 && tput sgr0
#wget -c -P ../data/$1/$2/$3/$4/route-views3 http://archive.routeviews.org/route-views3/bgpdata/$1.$2/RIBS/rib.$1$2$3.$4.bz2
#tput bold && tput setf 4 && echo -e "Done" && tput setf 0 && tput sgr0

tput bold && tput setf 4 && echo -e "\n\nDownloading from route-views4" && tput setf 0 && tput sgr0
wget -c -P ../data/$1/$2/$3/$4/route-views4 http://archive.routeviews.org/route-views4/bgpdata/$1.$2/RIBS/rib.$1$2$3.$4.bz2
tput bold && tput setf 4 && echo -e "Done" && tput setf 0 && tput sgr0

tput bold && tput setf 4 && echo -e "\n\nDownloading from route-views6" && tput setf 0 && tput sgr0
wget -c -P ../data/$1/$2/$3/$4/route-views6 http://archive.routeviews.org/route-views6/bgpdata/$1.$2/RIBS/rib.$1$2$3.$4.bz2
tput bold && tput setf 4 && echo -e "Done" && tput setf 0 && tput sgr0

tput bold && tput setf 4 && echo -e "\n\nDownloading from route-views.kixp" && tput setf 0 && tput sgr0
wget -c -P ../data/$1/$2/$3/$4/route-views.kixp http://archive.routeviews.org/route-views.kixp/bgpdata/$1.$2/RIBS/rib.$1$2$3.$4.bz2
tput bold && tput setf 4 && echo -e "Done" && tput setf 0 && tput sgr0

tput bold && tput setf 4 && echo -e "\n\nDownloading from route-views.saopaulo" && tput setf 0 && tput sgr0
wget -c -P ../data/$1/$2/$3/$4/route-views.saopaulo http://archive.routeviews.org/route-views.saopaulo/bgpdata/$1.$2/RIBS/rib.$1$2$3.$4.bz2
tput bold && tput setf 4 && echo -e "Done" && tput setf 0 && tput sgr0

tput bold && tput setf 4 && echo -e "\n\nDownloading from route-views.linx" && tput setf 0 && tput sgr0
wget -c -P ../data/$1/$2/$3/$4/route-views.linx http://archive.routeviews.org/route-views.linx/bgpdata/$1.$2/RIBS/rib.$1$2$3.$4.bz2
tput bold && tput setf 4 && echo -e "Done" && tput setf 0 && tput sgr0

tput bold && tput setf 4 && echo -e "\n\nDownloading from route-views.sydney" && tput setf 0 && tput sgr0
wget -c -P ../data/$1/$2/$3/$4/route-views.sydney http://archive.routeviews.org/route-views.sydney/bgpdata/$1.$2/RIBS/rib.$1$2$3.$4.bz2
tput bold && tput setf 4 && echo -e "Done" && tput setf 0 && tput sgr0

tput bold && tput setf 4 && echo -e "\n\nDownloading from route-views.wide" && tput setf 0 && tput sgr0
wget -c -P ../data/$1/$2/$3/$4/route-views.wide http://archive.routeviews.org/route-views.wide/bgpdata/$1.$2/RIBS/rib.$1$2$3.$4.bz2
tput bold && tput setf 4 && echo -e "Done" && tput setf 0 && tput sgr0

tput bold && tput setf 4 && echo -e "\n\nDownloading from route-views.eqix" && tput setf 0 && tput sgr0
wget -c -P ../data/$1/$2/$3/$4/route-views.eqix http://archive.routeviews.org/route-views.eqix/bgpdata/$1.$2/RIBS/rib.$1$2$3.$4.bz2
tput bold && tput setf 4 && echo -e "Done" && tput setf 0 && tput sgr0

tput bold tput setf 4 && echo -e "\n\nDownloading from route-views.isc" && tput setf 0 && tput sgr0
wget -c -P ../data/$1/$2/$3/$4/route-views.isc http://archive.routeviews.org/route-views.isc/bgpdata/$1.$2/RIBS/rib.$1$2$3.$4.bz2
tput bold && tput setf 4 && echo -e "Done" && tput setf 0 && tput sgr0

tput bold tput setf 4 && echo -e "\n\nDownloading from route-views.jinx" && tput setf 0 && tput sgr0
wget -c -P ../data/$1/$2/$3/$4/route-views.jinx http://archive.routeviews.org/route-views.jinx/bgpdata/$1.$2/RIBS/rib.$1$2$3.$4.bz2
tput bold && tput setf 4 && echo -e "Done" && tput setf 0 && tput sgr0

tput bold tput setf 4 && echo -e "\n\nDownloading from route-views.texalt" && tput setf 0 && tput sgr0
wget -c -P ../data/$1/$2/$3/$4/route-views.telxatl http://archive.routeviews.org/route-views.telxatl/bgpdata/$1.$2/RIBS/rib.$1$2$3.$4.bz2
tput bold && tput setf 4 && echo -e "Done" && tput setf 0 && tput sgr0

tput bold && tput setf 4 && echo -e "\n\n--Download complete--\n\n" && tput setf 0 && tput sgr0

# to-do route-views.nwax
