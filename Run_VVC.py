#Frame1: Type POC QPoffset QPOffsetModelOff QPOffsetModelScale CbQPoffset CrQPoffset QPfactor tcOffsetDiv2 betaOffsetDiv2 temporal_id #ref_pics_active #ref_pics reference 
#pictures predict deltaRPS #ref_idcs reference idcs print >> fid, 'Frame1: P 1 5 -6.5 0.2590 0 0 1.0 0 0 0 1 1 -1 0');
from __future__ import division
import numpy as np
import os, sys, subprocess, pdb
import argparse
import ConfigParser
import datetime, math, time
import ntpath

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
def call(cmd):
    # proc = subprocess.Popen(["cat", "/etc/services"], stdout=subprocess.PIPE, shell=True)
    #proc = subprocess.Popen(cmd, \
    #               stdout=subprocess.PIPE, shell=True)
    print(cmd)
    subprocess.call(cmd,shell=True)
    #proc = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True)
    #(out, err) = proc.communicate()
    return #(out, err)

###--------------------------------------------------------------
def call_bg(cmd):
    #proc = subprocess.Popen(cmd, shell=True)
    proc = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True)
    return proc

###--------------------------------------------------------------
def call_bg_file(cmd,fidProcess):
    proc = subprocess.Popen(cmd,stdout=fidProcess, shell=True)
    fidProcess.close
    return proc

###--------------------------------------------------------------
def Encode_decode_video():
    encoderlog=[]
    decoderlog=[]
    VMAFlog=[]
    now_start=[]
    now_end=[]
    now_start.append(datetime.datetime.now())
    print('Encoding  {}'.format(now_start[0].strftime("%Y-%m-%d %H:%M:%S")))
    InputYUV='{}.yuv'.format(vid[:-4])
    fname = ntpath.basename(InputYUV)[:-4]
    for cnt in range(len(rate)):
       BitstreamFile='{}/VVCencoded_{}_{}.bin'.format(Path,fname,rate[cnt])
       ReconYUV='{}/VVCrecon_{}_{}.yuv'.format(Path,fname,rate[cnt])
       encoderlogfile='{}/VVClog_{}_{}.dat'.format(Path,fname,rate[cnt])
       fid = open(encoderlogfile,'w')
       osout = call_bg_file('./VVCOrig/bin/EncoderAppStatic -c ./VVCOrig/cfg/encoder_lowdelay_P_vtm.cfg -c ./VVCOrig/cfg/encoder_VVC_GOP.cfg --InputFile={} --SourceWidth={} --SourceHeight={} --SAO=0 --InitialQP={} --FrameRate={} --FramesToBeEncoded={} --MaxCUSize={} --MaxPartitionDepth={}  --BitstreamFile="{}" --RateControl={} --TargetBitrate={} --ReconFile={}'.format(InputYUV,Width,Hight,QP,fps,NumFrames,MaxCUSize,MaxPartitionDepth,BitstreamFile,RateControl,rate[cnt],ReconYUV),fid)
       encoderlog.append(osout)

    for cnt in range(len(rate)):
       encoderlog[cnt].wait()

    ### decoding ------------
    for cnt in range(len(rate)):
       OutputYUV='{}/VVCoutput_{}_{}.yuv'.format(Path,fname,rate[cnt])
       #osout = call('rm -rf {}'.format(Path,OutputYUV))
       BitstreamFile='{}/VVCencoded_{}_{}.bin'.format(Path,fname,rate[cnt])
       decoderlogfile='{}/VVCdecoderlog_{}_{}.dat'.format(Path,fname,rate[cnt])
       fid = open(decoderlogfile,'w')
       osout = call_bg_file('./VVCOrig/bin/DecoderAppStatic -b {} -o {}'.format(BitstreamFile,OutputYUV),fid)
       decoderlog.append(osout)

    for cnt in range(len(rate)):
       decoderlog[cnt].wait()

    ### VMAF --------

    for cnt in range(len(rate)):
       OutputYUV='{}/VVCoutput_{}_{}.yuv'.format(Path,fname,rate[cnt])
       VMAFlogfile='{}/VVClog_{}_{}.dat'.format(Path,fname,rate[cnt])
       fid = open(VMAFlogfile,'a')
       osout = call_bg_file('../vmaf/run_vmaf yuv420p {} {} {} {}'.format(Width,Hight,InputYUV,OutputYUV),fid)
       VMAFlog.append(osout)

    for cnt in range(len(rate)):
       VMAFlog[cnt].wait()
       VMAFlogfile='{}/VVClog_{}_{}.dat'.format(Path,fname,rate[cnt])
       ### replace Frame to VMAF_Frame in the log file
       call('./Replace_Frame_to_VMAF_Frame --fn {}'.format(VMAFlogfile))

    '''
         if (int(len(PcntCompleted) % NProcesses) == 0):
             encoderlog[Pcnt2].wait()
             PcntCompleted.remove(Pcnt2)
             now_end.append(datetime.datetime.now())
             print('Encoding of GOP#{} is completed ... {}   ({}) .. ({})'.format(Pcnt2,now_end[Pcnt2].strftime("%Y-%m-%d %H:%M:%S"),now_end[Pcnt2].replace(microsecond=0)-now_start[Pcnt2].replace(microsecond=0),now_end[Pcnt2].replace(microsecond=0)-now_start[0].replace(microsecond=0)))
             Pcnt2=Pcnt2+1

         if (Pcnt==(np.shape(Distributed_GOP_Matrix)[0]-1)):
            for Pcnt2 in PcntCompleted:
                encoderlog[Pcnt2].wait()
                now_end.append(datetime.datetime.now())
                print('Encoding of GOP#{} is completed ... {}   ({}) .. ({})'.format(Pcnt2,now_end[Pcnt2].strftime("%Y-%m-%d %H:%M:%S"),now_end[Pcnt2].replace(microsecond=0)- now_start[Pcnt2].replace(microsecond=0),now_end[Pcnt2].replace(microsecond=0)-now_start[0].replace(microsecond=0)))
            PcntCompleted=[]

    ### decoding ---------------

    PcntCompleted=[]
    Pcnt2=0
    now_start=[]
    now_end=[]
    for Pcnt in range(np.shape(Distributed_GOP_Matrix)[0]):
         now_start.append(datetime.datetime.now())
         print('Decoding GOP#{} of {} ... {}'.format(Pcnt,(np.shape(Distributed_GOP_Matrix)[0]-1),now_start[Pcnt].strftime("%Y-%m-%d %H:%M:%S")))
         InputYUV='{}/Part{}/Part{}.yuv'.format(Split_video_path,Pcnt,Pcnt)
         ReconFile='{}/Part{}/ReconPart{}.yuv'.format(Split_video_path,Pcnt,Pcnt)
         BitstreamFile='{}/Part{}/HMEncodedVideo.bin'.format(Split_video_path,Pcnt)
         osout = call('rm -rf {}'.format(ReconFile))
         
         decoderlogfile='{}/Part{}/decoderlog.dat'.format(Split_video_path,Pcnt)
         fid = open(decoderlogfile,'w')
         osout=call_bg_file('./HMS/bin/TAppDecoderStatic --BitstreamFile="{}" --ReconFile="{}"'.format(BitstreamFile,ReconFile),fid)
         decoderlog.append(osout)
         PcntCompleted.append(Pcnt)

         if (int(len(PcntCompleted) % NProcesses) == 0):
             decoderlog[Pcnt2].wait()
             PcntCompleted.remove(Pcnt2)
             now_end.append(datetime.datetime.now())
             print('Decoding of GOP#{} is completed ... {}   ({}) .. ({})'.format(Pcnt2,now_end[Pcnt2].strftime("%Y-%m-%d %H:%M:%S"),now_end[Pcnt2].replace(microsecond=0)-now_start[Pcnt2].replace(microsecond=0),now_end[Pcnt2].replace(microsecond=0)-now_start[0].replace(microsecond=0)))
             Pcnt2=Pcnt2+1

         if (Pcnt==(np.shape(Distributed_GOP_Matrix)[0]-1)):
            for Pcnt2 in PcntCompleted:
                decoderlog[Pcnt2].wait()
                now_end.append(datetime.datetime.now())
                print('Decoding of GOP#{} is completed ... {}   ({}) .. ({})'.format(Pcnt2,now_end[Pcnt2].strftime("%Y-%m-%d %H:%M:%S"),now_end[Pcnt2].replace(microsecond=0)- now_start[Pcnt2].replace(microsecond=0),now_end[Pcnt2].replace(microsecond=0)-now_start[0].replace(microsecond=0)))
            PcntCompleted=[]

    ### VMAF ---------------

    PcntCompleted=[]
    Pcnt2=0
    now_start=[]
    now_end=[]
    for Pcnt in range(np.shape(Distributed_GOP_Matrix)[0]):
         now_start.append(datetime.datetime.now())
         print('Computing VMAF GOP#{} of {} ... {}'.format(Pcnt,(np.shape(Distributed_GOP_Matrix)[0]-1),now_start[Pcnt].strftime("%Y-%m-%d %H:%M:%S")))
         InputYUV='{}/Part{}/Part{}.yuv'.format(Split_video_path,Pcnt,Pcnt)
         ReconFile='{}/Part{}/ReconPart{}.yuv'.format(Split_video_path,Pcnt,Pcnt)
         
         decoderVMAFlogfile='{}/Part{}/decoderVMAFlog.dat'.format(Split_video_path,Pcnt)
         fidVMAF = open(decoderVMAFlogfile,'w')
         osout=call_bg_file('../vmaf/run_vmaf yuv420p {} {} {} {}'.format(Width,Hight,ReconFile,InputYUV),fidVMAF)
	 decoderVMAFlog.append(osout)
         
         PcntCompleted.append(Pcnt)

         if (int(len(PcntCompleted) % NProcesses) == 0):
             decoderVMAFlog[Pcnt2].wait()
             PcntCompleted.remove(Pcnt2)
             now_end.append(datetime.datetime.now())
             print('Computing VMAF of GOP#{} is completed ... {}   ({}) .. ({})'.format(Pcnt2,now_end[Pcnt2].strftime("%Y-%m-%d %H:%M:%S"),now_end[Pcnt2].replace(microsecond=0)-now_start[Pcnt2].replace(microsecond=0),now_end[Pcnt2].replace(microsecond=0)-now_start[0].replace(microsecond=0)))
             Pcnt2=Pcnt2+1

         if (Pcnt==(np.shape(Distributed_GOP_Matrix)[0]-1)):
            for Pcnt2 in PcntCompleted:
                decoderVMAFlog[Pcnt2].wait()
                now_end.append(datetime.datetime.now())
                print('Computing VMAF of GOP#{} is completed ... {}   ({}) .. ({})'.format(Pcnt2,now_end[Pcnt2].strftime("%Y-%m-%d %H:%M:%S"),now_end[Pcnt2].replace(microsecond=0)- now_start[Pcnt2].replace(microsecond=0),now_end[Pcnt2].replace(microsecond=0)-now_start[0].replace(microsecond=0)))
            PcntCompleted=[]
    '''
    return
##################################################################
## Main Body
if __name__ == "__main__":
    args=main()

    ##Inputs
    vid=args.vid;

    fps=int(args.fps);
    Width=int(args.w);
    Hight=int(args.h);
    QP=int(args.qp);
    MaxCUSize=int(args.maxcusize);
    MaxPartitionDepth=int(args.maxpartitiondepth);
    RateControl=int(args.ratecontrol);
    rate_str = args.rate.split(' ')
    rate = [int(r) for r in rate_str]
    NumFrames=int(args.numframes)
    Path = args.resultspath
    Encode_decode_video()
