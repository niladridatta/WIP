#! /bin/sh

bhav_dir='/root/Downloads/bhav'
out_dir='/root/Downloads/output'
extract_dir='/root/Downloads/extracted'

mkdir -p $bhav_dir/Old $extract_dir/Old $out_dir/Old

echo "Moving Old bhavs"
mv -v $bhav_dir/*.zip $bhav_dir/Old
echo

echo "Moving Old extracted"
mv -v $extract_dir/*.csv $extract_dir/Old
echo

echo "Moving Old outputs"
mv -v $out_dir/*.csv $out_dir/Old
echo

echo "List DIRs: "
echo
ls $bhav_dir $out_dir $extract_dir
echo

