#!/bin/bash
path=../savenpyVVC/
R=1000000
#ft=BosphorusShakeNDryHoneyBee_1920x1080_120fps_420_8bit_YUV_rrc0_VVClog_Rate
#ft=BosphorusShakeNDry_1920x1080_120fps_420_8bit_YUV_rrc0_VVClog_Rate
ft=ShakeNDryHoneyBee_1920x1080_120fps_420_8bit_YUV_rrc0_VVClog_Rate

f1=$path/$ft$R.dat
#cat $path/Bosphorus_1920x1080_120fps_420_8bit_YUV_VVClog_Rate$R.dat > $f1 
cat $path/ShakeNDry_1920x1080_120fps_420_8bit_YUV_VVClog_Rate$R.dat >> $f1 
cat $path/HoneyBee_1920x1080_120fps_420_8bit_YUV_VVClog_Rate$R.dat >> $f1 
python Compute_VCC_Rate_PSNR_VMAF_v1.py --fps=120 --fn=$f1

R=2000000
f1=$path/$ft$R.dat
#cat $path/Bosphorus_1920x1080_120fps_420_8bit_YUV_VVClog_Rate$R.dat > $f1 
cat $path/ShakeNDry_1920x1080_120fps_420_8bit_YUV_VVClog_Rate$R.dat >> $f1 
cat $path/HoneyBee_1920x1080_120fps_420_8bit_YUV_VVClog_Rate$R.dat >> $f1 
python Compute_VCC_Rate_PSNR_VMAF_v1.py --fps=120 --fn=$f1

R=3000000
f1=$path/$ft$R.dat
#cat $path/Bosphorus_1920x1080_120fps_420_8bit_YUV_VVClog_Rate$R.dat > $f1 
cat $path/ShakeNDry_1920x1080_120fps_420_8bit_YUV_VVClog_Rate$R.dat >> $f1 
cat $path/HoneyBee_1920x1080_120fps_420_8bit_YUV_VVClog_Rate$R.dat >> $f1 
python Compute_VCC_Rate_PSNR_VMAF_v1.py --fps=120 --fn=$f1

R=4000000
f1=$path/$ft$R.dat
#cat $path/Bosphorus_1920x1080_120fps_420_8bit_YUV_VVClog_Rate$R.dat > $f1 
cat $path/ShakeNDry_1920x1080_120fps_420_8bit_YUV_VVClog_Rate$R.dat >> $f1 
cat $path/HoneyBee_1920x1080_120fps_420_8bit_YUV_VVClog_Rate$R.dat >> $f1 
python Compute_VCC_Rate_PSNR_VMAF_v1.py --fps=120 --fn=$f1
