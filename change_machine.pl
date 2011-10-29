map{print$i=$_+0," cents:\n";map{print"$q x $_ cents\n"if$q=int$i/$_;$i%=$_}(25,10,5,1);print$/}<>
