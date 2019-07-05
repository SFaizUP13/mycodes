
  BEGIN{

    seqno = -1; 
   
    droppedPackets = 0;

    receivedPackets = 0;

    count = 0;

    }

   {

   #packet delivery ratio

    if($1=="t") {

   print "ReceivedPackets = " $3;
  

   } 

   }

   END { 

   #n_to_n_delay = n_to_n_delay/count;

   
   
   

   }
#To run the script of awk
#echo | awk -f script.awk traces.tr > output.txt




