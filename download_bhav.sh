#! /bin/sh

links_dir='/root/Links'
links_filename='download_links_sep31.txt'

links_file="$links_dir/$links_filename"

echo "Links File: $links_file"
echo

bhav_dir='/root/Downloads/bhav'
cd $bhav_dir
echo Downloading bhavs to `pwd`

for i in `cat $links_file`
do
  echo
  echo $i | cut -b68-76
  echo
  wget --user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36" $i
done

echo "List Bhav DIR: $bhav_dir"
ls $bhav_dir

echo
