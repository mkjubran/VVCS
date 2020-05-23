#!/bin/bash
path=../savenpy/
R=1000000
ft=SH_19201080_rrc0_gp24_combined_VVC_RPred_GOP540_RPS16_skip12_Rate
f1=$path/$ft$R.dat
#cat $path/Bosphorus_1920x1080_gp24_combined_VVC_RPred_GOP580_RPS17_skip12_Rate$R.dat > $f1
cat $path/ShakeNDry_1920x1080_gp24_combined_VVC_RPred_GOP280_RPS17_skip12_Rate$R.dat >> $f1 
cat $path/HoneyBee_1920x1080_gp24_combined_VVC_RPred_GOP580_RPS17_skip12_Rate$R.dat >> $f1 
python Compute_VCC_Rate_PSNR_VMAF_v1.py --fps=120 --fn=$f1

R=2000000
f1=$path/$ft$R.dat
#cat $path/Bosphorus_1920x1080_gp24_combined_VVC_RPred_GOP580_RPS17_skip12_Rate$R.dat > $f1
cat $path/ShakeNDry_1920x1080_gp24_combined_VVC_RPred_GOP280_RPS17_skip12_Rate$R.dat >> $f1 
cat $path/HoneyBee_1920x1080_gp24_combined_VVC_RPred_GOP580_RPS17_skip12_Rate$R.dat >> $f1 
python Compute_VCC_Rate_PSNR_VMAF_v1.py --fps=120 --fn=$f1

R=3000000
f1=$path/$ft$R.dat
#cat $path/Bosphorus_1920x1080_gp24_combined_VVC_RPred_GOP580_RPS17_skip12_Rate$R.dat > $f1
cat $path/ShakeNDry_1920x1080_gp24_combined_VVC_RPred_GOP280_RPS17_skip12_Rate$R.dat >> $f1 
cat $path/HoneyBee_1920x1080_gp24_combined_VVC_RPred_GOP580_RPS17_skip12_Rate$R.dat >> $f1 
python Compute_VCC_Rate_PSNR_VMAF_v1.py --fps=120 --fn=$f1

R=4000000
f1=$path/$ft$R.dat
#cat $path/Bosphorus_1920x1080_gp24_combined_VVC_RPred_GOP580_RPS17_skip12_Rate$R.dat > $f1
cat $path/ShakeNDry_1920x1080_gp24_combined_VVC_RPred_GOP280_RPS17_skip12_Rate$R.dat >> $f1 
cat $path/HoneyBee_1920x1080_gp24_combined_VVC_RPred_GOP580_RPS17_skip12_Rate$R.dat >> $f1 
python Compute_VCC_Rate_PSNR_VMAF_v1.py --fps=120 --fn=$f1


R=5000000
f1=$path/$ft$R.dat
#cat $path/Bosphorus_1920x1080_gp24_combined_VVC_RPred_GOP580_RPS17_skip12_Rate$R.dat > $f1
cat $path/ShakeNDry_1920x1080_gp24_combined_VVC_RPred_GOP280_RPS17_skip12_Rate$R.dat >> $f1 
cat $path/HoneyBee_1920x1080_gp24_combined_VVC_RPred_GOP580_RPS17_skip12_Rate$R.dat >> $f1 
python Compute_VCC_Rate_PSNR_VMAF_v1.py --fps=120 --fn=$f1

R=6000000
f1=$path/$ft$R.dat
#cat $path/Bosphorus_1920x1080_gp24_combined_VVC_RPred_GOP580_RPS17_skip12_Rate$R.dat > $f1
cat $path/ShakeNDry_1920x1080_gp24_combined_VVC_RPred_GOP280_RPS17_skip12_Rate$R.dat >> $f1 
cat $path/HoneyBee_1920x1080_gp24_combined_VVC_RPred_GOP580_RPS17_skip12_Rate$R.dat >> $f1 
python Compute_VCC_Rate_PSNR_VMAF_v1.py --fps=120 --fn=$f1
