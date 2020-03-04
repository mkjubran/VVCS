#Frame1: Type POC QPoffset QPOffsetModelOff QPOffsetModelScale CbQPoffset CrQPoffset QPfactor tcOffsetDiv2 betaOffsetDiv2 temporal_id #ref_pics_active #ref_pics reference 
#pictures predict deltaRPS #ref_idcs reference idcs print >> fid, 'Frame1: P 1 5 -6.5 0.2590 0 0 1.0 0 0 0 1 1 -1 0');
from __future__ import division
import numpy as np
import os, sys, subprocess, pdb
import argparse
import ConfigParser
import datetime, math, time


INF = 999

###--------------------------------------------------------------
## Parse configuration Parameters from the configuration file
def main(argv=None):
    # Do argv default this way, as doing it in the functional
    # declaration sets it at compile time.
    if argv is None:
        argv = sys.argv

    # Parse any conf_file specification
    # We make this parser with add_help=False so that
    # it doesn't parse -h and print help.
    conf_parser = argparse.ArgumentParser(
        description=__doc__, # printed with -h/--help
        # Don't mess with format of description
        formatter_class=argparse.RawDescriptionHelpFormatter,
        # Turn off help, so we print all options in response to -h
        add_help=False
        )
    conf_parser.add_argument("-c", "--conf_file",
                        help="Specify config file", metavar="FILE")
    args, remaining_argv = conf_parser.parse_known_args()

    defaults = { "option":"default"}

    if args.conf_file:
        config = ConfigParser.SafeConfigParser()
        config.read([args.conf_file])
        defaults.update(dict(config.items("Parametters")))
        #print(dict(config.items("Parametters")))

    # Parse rest of arguments
    # Don't suppress add_help here so it will handle -h
    parser = argparse.ArgumentParser(
        # Inherit options from config_parser
        parents=[conf_parser]
        )
    parser.set_defaults(**defaults)
    args = parser.parse_args(remaining_argv)
    return(args)

###--------------------------------------------------------------
## read frame numbers from Rank List File
def read_ranklist():
   ## read priority list
   with open(RankListFile) as f:
       FNums = f.readlines()
   f.close()
   iFNums=map(int, FNums)

   ## get total number of frames
   NumFrames=round(len(iFNums))
   NumFrames=int(NumFrames)
   return(iFNums,NumFrames)

###--------------------------------------------------------------
def call(cmd):
    # proc = subprocess.Popen(["cat", "/etc/services"], stdout=subprocess.PIPE, shell=True)
    #proc = subprocess.Popen(cmd, \
    #               stdout=subprocess.PIPE, shell=True)
    proc = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return (out, err)

###--------------------------------------------------------------
def call_bg(cmd):
    #print(cmd)
    #proc = subprocess.Popen(cmd, shell=True)
    proc = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True)
    return proc

###--------------------------------------------------------------
def call_bg_file(cmd,fidProcess):
    #print(cmd)
    proc = subprocess.Popen(cmd,stdout=fidProcess, shell=True)
    fidProcess.close
    return proc

###--------------------------------------------------------------
def Encode_decode_video(Distributed_GOP_Matrix):
    encoderlog=[]
    decoderVMAFlog=[]
    PcntCompleted=[]
    Pcnt1=0
    Pcnt2=0
    now_start=[]
    now_end=[]
    GOPDesc=[]
    Pcnt=0
    InputYUV='{}.yuv'.format(vid[:-4])
    for Rcnt in range(len(RVector)):
         now_start.append(datetime.datetime.now())
         print('Encoding Rate {} ... {}'.format(RVector[Rcnt],now_start[Pcnt].strftime("%Y-%m-%d %H:%M:%S")))
         BitstreamFile='{}/VVCEncodedVideo_{}.bin'.format(Split_video_path,int(RVector[Rcnt]))
         ReconFile='{}/VVCRecon_{}.yuv'.format(Split_video_path,int(RVector[Rcnt]))
         osout = call('rm -rf {}'.format(BitstreamFile))
         osout = call('cp -f ./VVCOrig/cfg/encoder_lowdelay_P_vtm.cfg {}/Part{}/encoder_lowdelay_P_vtm.cfg'.format(Split_video_path,Pcnt))
         encoderlogfile='{}/VVCencoderlog_{}.dat'.format(Split_video_path,Pcnt,int(RVector[Rcnt]))
         fid = open(encoderlogfile,'w')
         osout = call_bg_file('./VVCOrig/bin/EncoderAppStatic -c ./VVCOrig/cfg/encoder_lowdelay_P_vtm.cfg -c ./VVCOrig/cfg/encoder_VVC_GOP.cfg --InputFile={} --SourceWidth={} --SourceHeight={} --SAO=0 --InitialQP={} --FrameRate={} --FramesToBeEncoded={} --MaxCUSize={} --MaxPartitionDepth={}  --BitstreamFile="{}" --RateControl={} --TargetBitrate={} --ReconFile={}'.format(InputYUV,Width,Hight,QP,fps,NumFrames,MaxCUSize,MaxPartitionDepth,BitstreamFile,RateControl,RVector[Rcnt],ReconFile),fid)
         encoderlog.append(osout)
         PcntCompleted.append(Pcnt1)
         GOPDesc.append('Rate {}'.format(int(RVector[Rcnt])))

         if (int(len(PcntCompleted) % NProcesses) == 0):
             encoderlog[Pcnt2].wait()
             PcntCompleted.remove(Pcnt2)
             now_end.append(datetime.datetime.now())
             print('Encoding of {} is completed ... {}   ({}) .. ({})'.format(GOPDesc[Pcnt2],now_end[Pcnt2].strftime("%Y-%m-%d %H:%M:%S"),now_end[Pcnt2].replace(microsecond=0)-now_start[Pcnt2].replace(microsecond=0),now_end[Pcnt2].replace(microsecond=0)-now_start[0].replace(microsecond=0)))
             Pcnt2=Pcnt2+1

         if ( Rcnt == ( len(RVector) - 1 )):
            for Pcnt2 in PcntCompleted:
                encoderlog[Pcnt2].wait()
                now_end.append(datetime.datetime.now())
                print('Encoding of {} is completed ... {}   ({}) .. ({})'.format(GOPDesc[Pcnt2],now_end[Pcnt2].strftime("%Y-%m-%d %H:%M:%S"),now_end[Pcnt2].replace(microsecond=0)- now_start[Pcnt2].replace(microsecond=0),now_end[Pcnt2].replace(microsecond=0)-now_start[0].replace(microsecond=0)))
            PcntCompleted=[]

         Pcnt1=Pcnt1+1

   ### VMAF ---------------

    PcntCompleted=[]
    Pcnt1=0
    Pcnt2=0
    now_start=[]
    now_end=[]
    GOPDesc=[]
    Pcnt=0
    for Rcnt in range(len(RVector)):
         now_start.append(datetime.datetime.now())
         print('Computing VMAF Rate {} ... {}'.format(int(RVector[Rcnt]),now_start[Pcnt].strftime("%Y-%m-%d %H:%M:%S")))
         BitstreamFile='{}/VVCEncodedVideo_{}.bin'.format(Split_video_path,int(RVector[Rcnt]))
         ReconFile='{}/VVCRecon_{}.yuv'.format(Split_video_path,int(RVector[Rcnt]))
         decoderVMAFlogfile='{}/VVCdecoderVMAFlog_{}.dat'.format(Split_video_path,int(RVector[Rcnt]))
         fidVMAF = open(decoderVMAFlogfile,'w')
         osout=call_bg_file('../vmaf/run_vmaf yuv420p {} {} {} {}'.format(Width,Hight,InputYUV,ReconFile),fidVMAF)
	 decoderVMAFlog.append(osout)
         
         PcntCompleted.append(Pcnt1)
         GOPDesc.append('Rate {}'.format(int(RVector[Rcnt])))

         if (int(len(PcntCompleted) % NProcesses) == 0):
             decoderVMAFlog[Pcnt2].wait()
             PcntCompleted.remove(Pcnt2)
             ### replace Frame to VMAF_Frame in the log file
             #call('./Replace_Frame_to_VMAF_Frame --fn {}'.format(decoderVMAFlogfile))
             now_end.append(datetime.datetime.now())
             print('Computing VMAF of {} is completed ... {}   ({}) .. ({})'.format(GOPDesc[Pcnt2],now_end[Pcnt2].strftime("%Y-%m-%d %H:%M:%S"),now_end[Pcnt2].replace(microsecond=0)-now_start[Pcnt2].replace(microsecond=0),now_end[Pcnt2].replace(microsecond=0)-now_start[0].replace(microsecond=0)))
             Pcnt2=Pcnt2+1

         if ( Rcnt == ( len(RVector) - 1 )):
            for Pcnt2 in PcntCompleted:
                decoderVMAFlog[Pcnt2].wait()
                ### replace Frame to VMAF_Frame in the log file
                #call('./Replace_Frame_to_VMAF_Frame --fn {}'.format(decoderVMAFlogfile))
                now_end.append(datetime.datetime.now())
                print('Computing VMAF of {} is completed ... {}   ({}) .. ({})'.format(GOPDesc[Pcnt2],now_end[Pcnt2].strftime("%Y-%m-%d %H:%M:%S"),now_end[Pcnt2].replace(microsecond=0)- now_start[Pcnt2].replace(microsecond=0),now_end[Pcnt2].replace(microsecond=0)-now_start[0].replace(microsecond=0)))
            PcntCompleted=[]

         Pcnt1=Pcnt1+1
    return

###--------------------------------------------------------------
def Combine_encoder_log(Distributed_GOP_Matrix,rate):
    CombinedLines=[]
    CombinedLinesAll=[]
    for cnt_row in range(np.shape(Distributed_GOP_Matrix)[0]):
        cnt_col=0
        encoderlogfile='{}/Part{}/encoderlog_{}.dat'.format(Split_video_path,cnt_row,rate)
        with open(encoderlogfile) as f:
             Lines = f.readlines()
        f.close()
        for cnt in range(len(Lines)):
            if Lines[cnt][:].split(' ')[0] == 'POC':
               CombinedLinesAll.append(Lines[cnt][:])
               if (Distributed_GOP_Matrix[cnt_row][cnt_col] > Distributed_GOP_Matrix[cnt_row-1][GOP-1]) or (cnt_row==0):
                    CombinedLines.append(Lines[cnt][:])
                    cnt_col=cnt_col+1
               else:
                    cnt_col=cnt_col+1

    CombinedLinesVMAF=[]
    CombinedLinesAllVMAF=[]
    for cnt_row in range(np.shape(Distributed_GOP_Matrix)[0]):
        cnt_col=0
        decoderlogfile='{}/Part{}/decoderVMAFlog_{}.dat'.format(Split_video_path,cnt_row,rate)
        with open(decoderlogfile) as f:
             LinesDec = f.readlines()
        f.close()
        #pdb.set_trace()
        for cnt in range(len(LinesDec)):
            if LinesDec[cnt][:].split(' ')[0] == 'Frame':
               CombinedLinesAllVMAF.append(LinesDec[cnt][:])
	       #print('{}..{}..{}..{}\n'.format(cnt_row,cnt_col,cnt,LinesDec[cnt][:]))
               #print(len(CombinedLinesVMAF))
               #pdb.set_trace()
               if (Distributed_GOP_Matrix[cnt_row][cnt_col] > Distributed_GOP_Matrix[cnt_row-1][GOP-1]) or (cnt_row==0):
                    CombinedLinesVMAF.append(LinesDec[cnt][:])
                    #print(CombinedLinesVMAF)
                    cnt_col=cnt_col+1
                    #print(len(CombinedLinesVMAF))
               else:
                    cnt_col=cnt_col+1

    #pdb.set_trace()
    Combined_encoder_log_rate = '{}_Rate{}.dat'.format(Combined_encoder_log[0:(len(Combined_encoder_log)-4)],rate)
    fid = open(Combined_encoder_log_rate,'w')
    fid.write('Input File (MP4) = {}\n'.format(vid))
    fid.write('RankListFile = {}\n'.format(RankListFile))
    fid.write('Ref_active = {}\n'.format(num_ref_pics_active_Max))
    fid.write('Ref_stitch = {}\n'.format(num_ref_pics_active_Stitching))
    fid.write('QP = {}\n'.format(QP))
    fid.write('MaxCUSize = {}\n'.format(MaxCUSize))
    fid.write('MaxPartitionDepth = {}\n'.format(MaxPartitionDepth))
    fid.write('fps = {}\n'.format(fps))
    fid.write('RateControl = {}\n'.format(RateControl))
    fid.write('rate = {}\n'.format(rate))
    fid.write('NProcesses = {}\n\n'.format(NProcesses))
    for cnt in range(len(CombinedLines)):
       templine=CombinedLines[cnt][:].replace("  "," ")
       templine=templine.replace("  "," ")
       templine=templine.replace("  "," ")
       templine=templine.replace("  "," ")
       templine=templine.split(' ')
       #print('POC {}...{}'.format(cnt,templine[2:22]))
       fid.write('POC {}...{}\n'.format(cnt,templine[2:22]))

    #pdb.set_trace()
    for cnt in range(len(CombinedLinesVMAF)):
       templine=CombinedLinesVMAF[cnt][:].replace("  "," ")
       templine=templine.replace("  "," ")
       templine=templine.replace("  "," ")
       templine=templine.replace("  "," ")
       templine=templine.split(' ')
       #print('VMAF_Frame {}...{}\n'.format(cnt,templine[2:22]))
       fid.write('VMAF_Frame {}...{}\n'.format(cnt,templine[2:22]))
    fid.close

    fid = open((Combined_encoder_log_rate[0:(len(Combined_encoder_log_rate)-4)]+'All.dat'),'w')
    fid.write('Input File (MP4) = {}\n'.format(vid))
    fid.write('RankListFile = {}\n'.format(RankListFile))
    fid.write('Ref_active = {}\n'.format(num_ref_pics_active_Max))
    fid.write('Ref_stitch = {}\n'.format(num_ref_pics_active_Stitching))
    fid.write('QP = {}\n'.format(QP))
    fid.write('MaxCUSize = {}\n'.format(MaxCUSize))
    fid.write('MaxPartitionDepth = {}\n'.format(MaxPartitionDepth))
    fid.write('fps = {}\n'.format(fps))
    fid.write('RateControl = {}\n'.format(RateControl))
    fid.write('rate = {}\n'.format(rate))
    fid.write('NProcesses = {}\n\n'.format(NProcesses))
    for cnt in range(len(CombinedLinesAll)):
       templine=CombinedLinesAll[cnt][:].replace("  "," ")
       templine=templine.replace("  "," ")
       templine=templine.replace("  "," ")
       templine=templine.replace("  "," ")
       templine=templine.split(' ')
       #print('POC {}...{}'.format(cnt,templine[2:22]))
       fid.write('POC {}...{}\n'.format(cnt,templine[1:22]))

    for cnt in range(len(CombinedLinesAllVMAF)):
       templine=CombinedLinesAllVMAF[cnt][:].replace("  "," ")
       templine=templine.replace("  "," ")
       templine=templine.replace("  "," ")
       templine=templine.replace("  "," ")
       templine=templine.split(' ')
       #print('VMAF_Frame {}...{}\n'.format(cnt,templine[1:22]))
       fid.write('VMAF_Frame {}...{}\n'.format(cnt,templine[1:22]))

    fid.close

##################################################################
## Main Body
if __name__ == "__main__":
    args=main()

    ##Inputs
    RankListFile=args.ranklistfile;
    num_ref_pics_active_Max=int(args.num_ref_pics_active_max);
    num_ref_pics_active_Stitching=int(args.num_ref_pics_active_stitching);
    vid=args.vid;

    mode=args.mode;
    fps=int(args.fps);
    GOP=int(args.gop);
    Width=int(args.w);
    Hight=int(args.h);
    QP=int(args.qp);
    MaxCUSize=int(args.maxcusize);
    MaxPartitionDepth=int(args.maxpartitiondepth);
    RateControl=int(args.ratecontrol);
    #rate=int(args.rate);
    RVector = args.rate.split(' ');
    NProcesses=int(args.nprocesses);
    Combined_encoder_log=args.combined_encoder_log
    Split_video_path=args.split_video_path;

    print(int(RVector[0]))
    print(len(RVector))
    
    #pdb.set_trace()
    fsr=fps

    if GOP%2!=0:
        GOP=int(GOP/2) * 2

    if num_ref_pics_active_Stitching>num_ref_pics_active_Max:
        num_ref_pics_active_Stitching=num_ref_pics_active_Max
    
    if GOP<(2*num_ref_pics_active_Max):
        GOP=2*num_ref_pics_active_Max

    (iFNums,NumFrames)=read_ranklist();
    iFNums=np.array(iFNums)
    ref_pics_active_Stitching=iFNums[0:(num_ref_pics_active_Stitching)]
    ref_pics_active_Stitching=np.sort(ref_pics_active_Stitching)

    (Distributed_GOP_Matrix,ref_pics_in_Distributed_GOP_Matrix)=Create_Distributed_GOP_Matrix();
    export_YUVframes(vid)
    Split_VideoYUV_GOP(Distributed_GOP_Matrix)

    print(Distributed_GOP_Matrix)
    #print(ref_pics_active_Stitching)
    #print(ref_pics_in_Distributed_GOP_Matrix)

    Create_Encoder_Config(Distributed_GOP_Matrix,ref_pics_in_Distributed_GOP_Matrix)
    Encode_decode_video(Distributed_GOP_Matrix)
    for Rcnt in range(len(RVector)):
       Combine_encoder_log(Distributed_GOP_Matrix,int(RVector[Rcnt]))
    print(Distributed_GOP_Matrix)
