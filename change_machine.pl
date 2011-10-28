while($i=<>+0){
  print"$i cents:\n";
  map{print"$q x $_ cents\n"if$q=int($i/$_);$i%=$_;}(25,10,5,1);
  print "\n";
}
