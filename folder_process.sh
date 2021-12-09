#!/bin/sh

# 提示信息
echo "start:"

base=/home/sjy/Documents/base_data
raw=/home/sjy/Documents/raw_data
pst=.tar

# 定义变量

# 拷贝视频文件
if [ -d $base/video ]
then
echo "video existed"
else
echo "mkdir video"
mkdir $base/video
fi

cp /home/sjy/Documents/raw_data/*/*.avi $base/video

# 解压压缩文件
if [ -d $base/tar ]
then
echo "tar existed"
else
echo "mkdir tar"
mkdir $base/tar
fi

cp $raw/*/*.tar $base/tars

ls $base/tars/*.tar > ls.log

for i in $(cat ls.log)
do
  tar -xvf $i --directory=$base/tar/
done
rm -rf ls.log

#for tar in (ls $base/tar/tars);  do tar xvf $tar; done
# for tar in ./*.tar;  do tar xvf $tar -C label; done


# 复制json文件
if [ -d $base/json ]
then
echo "json existed"
else
echo "mkdir json"
mkdir $base/json
fi

cp $base/tar/*.json $base/json

if [ -d $base/nii ]
then
echo "niftis existed"
else
echo "mkdir nii"
mkdir $base/nii
fi

cp $base/tar/*.nii.gz $base/nii
