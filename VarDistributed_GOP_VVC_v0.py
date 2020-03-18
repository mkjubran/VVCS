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
## convert iFNums from vector to matrix such that each row is a separate GOP
def Create_Distributed_GOP_Matrix():
   NotAlloc_Frames=np.arange(0,NumFrames)
   for val in ref_pics_active_Stitching:
      idx=np.where(NotAlloc_Frames==val)
      NotAlloc_Frames=np.delete(NotAlloc_Frames,idx)

   Distributed_GOP_Matrix=np.ones((GOP,0), dtype=int)
   ref_pics_in_Distributed_GOP_Matrix=np.empty(0)
   while len(NotAlloc_Frames)>0:
       Distributed_GOP_Vec=np.empty(0)
       ref_pics_active_Stitching_temp=ref_pics_active_Stitching
       #### To add few frames at the beginning of GOP encoding .. lagging
       if Distributed_GOP_Matrix.size == 0:
          ref_pics_active_Stitching_temp=np.append(ref_pics_active_Stitching_temp,(Distributed_GOP_Matrix[(len(Distributed_GOP_Matrix)-num_ref_pics_active_Max+num_ref_pics_active_Stitching):(len(Distributed_GOP_Matrix))]))
       else:
          AddLagFrames = np.array(range(int(max(Distributed_GOP_Matrix))-num_ref_pics_active_Max+num_ref_pics_active_Stitching+1 , int(max(Distributed_GOP_Matrix))+1 ))
          #print(AddLagFrames)
          ref_pics_active_Stitching_temp=np.append(ref_pics_active_Stitching_temp,AddLagFrames)
       #print(int(max(Distributed_GOP_Matrix))-num_ref_pics_active_Max+num_ref_pics_active_Stitching)
       #print(range(int(max(Distributed_GOP_Matrix))-num_ref_pics_active_Max+num_ref_pics_active_Stitching,int(max(Distributed_GOP_Matrix))))

#       ref_pics_active_Stitching_temp=np.append(ref_pics_active_Stitching_temp,range(int(max(Distributed_GOP_Matrix))-num_ref_pics_active_Max+num_ref_pics_active_Stitching):(int(max(Distributed_GOP_Matrix)))]))



       ref_pics_active_Stitching_temp=np.unique(ref_pics_active_Stitching_temp)
       ref_pics_active_Stitching_temp=np.sort(ref_pics_active_Stitching_temp)
       #print(ref_pics_active_Stitching)
       #print(np.max(Distributed_GOP_Matrix))
       #print(Distributed_GOP_Matrix)
       #pdb.set_trace()
       ####
       ref_pics_added=0;
       AddFrames = True
       while len(Distributed_GOP_Vec)<GOP:
          if len(NotAlloc_Frames)==0:     #if all frames are allocated to Distributed Matrix
              break
          elif len(ref_pics_active_Stitching_temp)==0: #if all sticthing frames are allocated to Distributed Matrix
              Distributed_GOP_Vec=np.append(Distributed_GOP_Vec,NotAlloc_Frames[0])
              NotAlloc_Frames=np.delete(NotAlloc_Frames,0)
          elif ref_pics_active_Stitching_temp[0]<NotAlloc_Frames[0]: #if the smallest stitch frames is less than the smallest not allocated frame 
              Distributed_GOP_Vec=np.append(Distributed_GOP_Vec,ref_pics_active_Stitching_temp[0])
              if ref_pics_active_Stitching_temp[0] in ref_pics_active_Stitching:   ### added to avoid considering lag frames as stitchers
                 ref_pics_added=ref_pics_added+1
              ref_pics_active_Stitching_temp=np.delete(ref_pics_active_Stitching_temp,0)
          elif AddFrames == False:
              Distributed_GOP_Vec=np.append(Distributed_GOP_Vec,-100)
          else:
              #print(NotAlloc_Frames[0])

              #time.sleep(0.25)
              #print(Distributed_GOP_Vec)

              if (NotAlloc_Frames[0]+1 in ref_pics_active_Stitching) and not (NotAlloc_Frames[0]+1 in Distributed_GOP_Matrix):
                   #print(NotAlloc_Frames[0])
                   #print(Distributed_GOP_Vec)
                   #print(ref_pics_active_Stitching)
                   AddFrames = False
                   #pdb.set_trace()

              Distributed_GOP_Vec=np.append(Distributed_GOP_Vec,NotAlloc_Frames[0])
              NotAlloc_Frames=np.delete(NotAlloc_Frames,0)
       if len(Distributed_GOP_Vec)==GOP:
              Distributed_GOP_Matrix=np.append(Distributed_GOP_Matrix,Distributed_GOP_Vec)
              #print(ref_pics_active_Stitching)
              #print(Distributed_GOP_Vec)
              #pdb.set_trace()
       ref_pics_in_Distributed_GOP_Matrix=np.append(ref_pics_in_Distributed_GOP_Matrix,ref_pics_added)
   Distributed_GOP_Matrix=np.reshape(Distributed_GOP_Matrix,(int(len(Distributed_GOP_Matrix)/GOP),GOP))
   return(Distributed_GOP_Matrix,ref_pics_in_Distributed_GOP_Matrix)

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
def export_YUVframes(fn):
    osout = call('rm -rf {}'.format(Split_video_path))
    osout = call('mkdir {}'.format(Split_video_path))
    osout = call('mkdir {}/pngparallel'.format(Split_video_path))
    fYUVCnt=1;
    FSize=(Width*Hight)+((Width/2)*(Hight/2))+((Width/2)*(Hight/2));

    fnYUV=(fn[0:(len(fn)-4)]+'.yuv')
    with open(fnYUV, "rb") as fYUVR:
       content = fYUVR.read(int(FSize))
       while content != '':
          with open('{}/pngparallel/{}.yuv'.format(Split_video_path,fYUVCnt),"wb") as fW:
             fW.write(content)
          fW.close()
          fYUVCnt=fYUVCnt+1;
          content = fYUVR.read(int(FSize))
    fYUVR.close()
    return 

###--------------------------------------------------------------
def Split_VideoYUV_GOP(Distributed_GOP_Matrix):
    for cnt_row in range(np.shape(Distributed_GOP_Matrix)[0]):
        osout = call('rm -rf {}/Part{}'.format(Split_video_path,cnt_row))
        osout = call('mkdir {}/Part{}'.format(Split_video_path,cnt_row))
        fW=open('{}/Part{}/Part{}.yuv'.format(Split_video_path,cnt_row,cnt_row),"w+b")
        for cnt_col in range(np.shape(Distributed_GOP_Matrix)[1]):
           #osout = call('cp -rf {}/pngparallel/{}.yuv {}/Part{}/{}.yuv'.format(Split_video_path,int(Distributed_GOP_Matrix[cnt_row,cnt_col]+1),Split_video_path,cnt_row,int(cnt_col+1)))
           #fnYUV=('{}/Part{}/{}.yuv'.format(Split_video_path,cnt_row,int(cnt_col+1)))
           if int(Distributed_GOP_Matrix[cnt_row,cnt_col]+1) > 0:
              fnYUV=('{}/pngparallel/{}.yuv'.format(Split_video_path,int(Distributed_GOP_Matrix[cnt_row,cnt_col]+1)))
              with open(fnYUV, "rb") as fYUVR:
                 content = fYUVR.read()
                 fW.write(content)
              fYUVR.close()
        fW.close()
    return

###--------------------------------------------------------------
def Create_Encoder_Config(Distributed_GOP_Matrix,ref_pics_in_Distributed_GOP_Matrix):
    for Pcnt in range(np.shape(Distributed_GOP_Matrix)[0]):
        NumRefFrame=ref_pics_in_Distributed_GOP_Matrix[Pcnt]+num_ref_pics_active_Max - num_ref_pics_active_Stitching;
        NumRefFrame=int(NumRefFrame)
        #print('{}...{}'.format(NumRefFrame,ref_pics_in_Distributed_GOP_Matrix[Pcnt]))
        #time.sleep(0.5)

        #if Pcnt==0:
        #    print('GOP#{} [{} - {}]'.format(Pcnt,int(Distributed_GOP_Matrix[Pcnt][0]),int(Distributed_GOP_Matrix[Pcnt][np.shape(Distributed_GOP_Matrix)[1]-1])))
        #else:
        #    print('GOP#{} [{} - {}]'.format(Pcnt,int((Distributed_GOP_Matrix[Pcnt-1][np.shape(Distributed_GOP_Matrix)[1]-1])+1),int(Distributed_GOP_Matrix[Pcnt][np.shape(Distributed_GOP_Matrix)[1]-1])))

    	##write config files header
    	fid = open('{}/Part{}/encoder_VVCS_GOP_{}.cfg'.format(Split_video_path,Pcnt,Pcnt),'w')
	print >> fid, '#======== File I/O ==============='
	print >> fid, 'InputFile                     : Traffic_2560x1600_30_crop.yuv'
	print >> fid, 'InputBitDepth                 : 8           # Input bitdepth'
	print >> fid, 'InputChromaFormat             : 420         # Ratio of luminance to chrominance samples'
	print >> fid, 'FrameRate                     : 24          # Frame Rate per second'
	print >> fid, 'FrameSkip                     : 0           # Number of frames to be skipped in input'
	print >> fid, 'SourceWidth                   : 640        # Input  frame width'
	print >> fid, 'SourceHeight                  : 480        # Input  frame height'
	print >> fid, 'FramesToBeEncoded             : '+str(GOP+1)+'         # Number of frames to be coded'
	print >> fid, '#======== Coding Structure ============='
	print >> fid, 'IntraPeriod                   : -1          # Period of I-Frame ( -1 = only first)'
	print >> fid, 'DecodingRefreshType           : 0           # Random Accesss 0:none, 1:CRA, 2:IDR, 3:Recovery Point SEI'
        #print >> fid, 'GOPSize                       : '+str(GOP)+'           # GOP Size (number of B slice = GOPSize-1)'
        print >> fid, 'GOPSize                       : 1          # GOP Size (number of B slice = GOPSize-1)'
	print >> fid, 'IntraQPOffset                 : -1'
	print >> fid, 'LambdaFromQpEnable            : 1           # see JCTVC-X0038 for suitable parameters for IntraQPOffset, QPoffset, QPOffsetModelOff, QPOffsetModelScale when enabled'
	print >> fid, '#        Type POC QPoffset QPOffsetModelOff QPOffsetModelScale CbQPoffset CrQPoffset QPfactor tcOffsetDiv2 betaOffsetDiv2 temporal_id #ref_pics_active_L0 #ref_pics_L0   reference_pictures_L0 #ref_pics_active_L1 #ref_pics_L1   reference_pictures_L1'
	#print >> fid, 'Frame1:    P   1   5       -6.5                      0.2590         0          0          1.0      0            0               0             4                4         1 2 3 4      0   0'

	GOPLine='Frame1: P 1 0 -6.5 0.2590 0 0 1.0 0 0 0 '+ str(NumRefFrame) + ' ' + str(NumRefFrame)
	for cnt1 in range(NumRefFrame):
	   GOPLine=GOPLine+' '+str(cnt1+1)+' '

        GOPLine=GOPLine+' 0 0'
			
        #GOPLine='Frame' + str(cnt) + ': P '+ str(cnt) +' 0 -6.5 0.2590 0 0 1.0 0 0 0             5                5         '+str(cnt-4)+' '+str(cnt-3)+' '+str(cnt-2)+' '+str(cnt-1)+' '+str(cnt)+'      0   0'
        print >> fid, GOPLine

	fid.write('\n#Note: The number of frames in the particitioned video is equal to GOP (Frame#0, Frame#1, .... Frame#(GOP-1)) and thus the line Frmae#GOP in this file will not be used to encode any frame, it is added to comply with the required format of HEVC GOP structure')

        print >> fid, '### DO NOT ADD ANYTHING BELOW THIS LINE ###'
        print >> fid, '### DO NOT DELETE THE EMPTY LINE BELOW ###'
        print >> fid, '     '
        fid.close()

###--------------------------------------------------------------
def Encode_decode_video(Distributed_GOP_Matrix):
    encoderlog=[]
    decoderlog=[]
    decoderVMAFlog=[]
    PcntCompleted=[]
    Pcnt1=0
    Pcnt2=0
    now_start=[]
    now_end=[]
    GOPDesc=[]
    #for Pcnt in range(np.shape(Distributed_GOP_Matrix)[0]):
    for Rcnt in range(len(RVector)):
      for Pcnt in range(np.shape(Distributed_GOP_Matrix)[0]):
         #osout = call('cp -f encoder_VVC_GOP_test.cfg {}/Part{}/encoder_VVCS_GOP_{}.cfg'.format(Split_video_path,Pcnt,RVector[Rcnt]))

         now_start.append(datetime.datetime.now())
         print('Encoding Rate {} - GOP#{} of {} ... {}'.format(RVector[Rcnt],Pcnt,(np.shape(Distributed_GOP_Matrix)[0]-1),now_start[Pcnt].strftime("%Y-%m-%d %H:%M:%S")))
         InputYUV='{}/Part{}/Part{}.yuv'.format(Split_video_path,Pcnt,Pcnt)
         BitstreamFile='{}/Part{}/VVCSEncodedVideo_{}.bin'.format(Split_video_path,Pcnt,int(RVector[Rcnt]))
         ReconFile='{}/Part{}/VVCSRecon_{}.bin'.format(Split_video_path,Pcnt,int(RVector[Rcnt]))
         osout = call('rm -rf {}'.format(BitstreamFile))
         osout = call('cp -f ./VVCS/cfg/encoder_lowdelay_P_vtm.cfg {}/Part{}/encoder_lowdelay_P_vtm.cfg'.format(Split_video_path,Pcnt))
         #osout = call('cp -f ./VVCOrig/cfg/encoder_VVC_GOP.cfg {}/Part{}/encoder_VVCS_GOP_{}.cfg'.format(Split_video_path,Pcnt,Pcnt))

         encoderlogfile='{}/Part{}/encoderlog_{}.dat'.format(Split_video_path,Pcnt,int(RVector[Rcnt]))
         fid = open(encoderlogfile,'w')
         osout = call_bg_file('./VVCS/bin/EncoderAppStatic -c {}/Part{}/encoder_lowdelay_P_vtm.cfg  -c {}/Part{}/encoder_VVCS_GOP_{}.cfg --InputFile={} --SourceWidth={} --SourceHeight={} --SAO=0 --InitialQP={} --FrameRate={} --FramesToBeEncoded={} --MaxCUSize={} --MaxPartitionDepth={}  --BitstreamFile="{}" --RateControl={} --TargetBitrate={} --ReconFile={}'.format(Split_video_path,Pcnt,Split_video_path,Pcnt,Pcnt,InputYUV,Width,Hight,QP,fps,NumFrames,MaxCUSize,MaxPartitionDepth,BitstreamFile,RateControl,RVector[Rcnt],ReconFile),fid)
         encoderlog.append(osout)
         PcntCompleted.append(Pcnt1)
         GOPDesc.append('Rate {} - GOP#{}'.format(int(RVector[Rcnt]),Pcnt))
         #print(PcntCompleted)

         if (Pcnt==(np.shape(Distributed_GOP_Matrix)[0]-1)) and ( Rcnt == ( len(RVector) - 1 )):
            for Pcnt2 in PcntCompleted:
                #print(Pcnt2)
                print(PcntCompleted)
                print(Pcnt2)
                encoderlog[Pcnt2].wait()
                now_end.append(datetime.datetime.now())
                print('Encoding of {} is completed ... {}   ({}) .. ({})'.format(GOPDesc[Pcnt2],now_end[Pcnt2].strftime("%Y-%m-%d %H:%M:%S"),now_end[Pcnt2].replace(microsecond=0)- now_start[Pcnt2].replace(microsecond=0),now_end[Pcnt2].replace(microsecond=0)-now_start[0].replace(microsecond=0)))
                #print(Pcnt2)
                #print(PcntCompleted)
            PcntCompleted=[]
         elif (int(len(PcntCompleted) % NProcesses) == 0):
             encoderlog[Pcnt2].wait()
             PcntCompleted.remove(Pcnt2)
             now_end.append(datetime.datetime.now())
             print('.Encoding of {} is completed ... {}   ({}) .. ({})'.format(GOPDesc[Pcnt2],now_end[Pcnt2].strftime("%Y-%m-%d %H:%M:%S"),now_end[Pcnt2].replace(microsecond=0)-now_start[Pcnt2].replace(microsecond=0),now_end[Pcnt2].replace(microsecond=0)-now_start[0].replace(microsecond=0)))
             #print(Pcnt2)
             #print(PcntCompleted)
             Pcnt2=Pcnt2+1

         Pcnt1=Pcnt1+1

   ### VMAF ---------------

    PcntCompleted=[]
    Pcnt1=0
    Pcnt2=0
    now_start=[]
    now_end=[]
    GOPDesc=[]
    #for Pcnt in range(np.shape(Distributed_GOP_Matrix)[0]):
    for Rcnt in range(len(RVector)):
      for Pcnt in range(np.shape(Distributed_GOP_Matrix)[0]):
         now_start.append(datetime.datetime.now())
         print('Computing VMAF Rate {} - GOP#{} of {} ... {}'.format(int(RVector[Rcnt]),Pcnt,(np.shape(Distributed_GOP_Matrix)[0]-1),now_start[Pcnt].strftime("%Y-%m-%d %H:%M:%S")))
         InputYUV='{}/Part{}/Part{}.yuv'.format(Split_video_path,Pcnt,Pcnt)
         ReconFile='{}/Part{}/VVCSRecon_{}.bin'.format(Split_video_path,Pcnt,int(RVector[Rcnt]))
         decoderVMAFlogfile='{}/Part{}/decoderVMAFlog_{}.dat'.format(Split_video_path,Pcnt,int(RVector[Rcnt]))
         fidVMAF = open(decoderVMAFlogfile,'w')
         osout=call_bg_file('../vmaf/run_vmaf yuv420p {} {} {} {}'.format(Width,Hight,InputYUV,ReconFile),fidVMAF)
	 decoderVMAFlog.append(osout)
         
         PcntCompleted.append(Pcnt1)
         GOPDesc.append('Rate {} - GOP#{}'.format(int(RVector[Rcnt]),Pcnt))

         if (Pcnt==(np.shape(Distributed_GOP_Matrix)[0]-1)) and ( Rcnt == ( len(RVector) - 1 )):
            for Pcnt2 in PcntCompleted:
                decoderVMAFlog[Pcnt2].wait()
                ### replace Frame to VMAF_Frame in the log file
                #call('./Replace_Frame_to_VMAF_Frame --fn {}'.format(decoderVMAFlogfile))
                now_end.append(datetime.datetime.now())
                print('Computing VMAF of {} is completed ... {}   ({}) .. ({})'.format(GOPDesc[Pcnt2],now_end[Pcnt2].strftime("%Y-%m-%d %H:%M:%S"),now_end[Pcnt2].replace(microsecond=0)- now_start[Pcnt2].replace(microsecond=0),now_end[Pcnt2].replace(microsecond=0)-now_start[0].replace(microsecond=0)))
            PcntCompleted=[]
         elif (int(len(PcntCompleted) % NProcesses) == 0):
             decoderVMAFlog[Pcnt2].wait()
             PcntCompleted.remove(Pcnt2)
             ### replace Frame to VMAF_Frame in the log file
             #call('./Replace_Frame_to_VMAF_Frame --fn {}'.format(decoderVMAFlogfile))
             now_end.append(datetime.datetime.now())
             print('Computing VMAF of {} is completed ... {}   ({}) .. ({})'.format(GOPDesc[Pcnt2],now_end[Pcnt2].strftime("%Y-%m-%d %H:%M:%S"),now_end[Pcnt2].replace(microsecond=0)-now_start[Pcnt2].replace(microsecond=0),now_end[Pcnt2].replace(microsecond=0)-now_start[0].replace(microsecond=0)))
             Pcnt2=Pcnt2+1

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

    print(RVector)
    #print(len(RVector))
    
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
    #pdb.set_trace()
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
