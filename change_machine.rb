$<.map{|i|
  i=i.to_i
  puts"#{i} cents:"
  [25,10,5,1].map{|c|
    puts "#{i/c} x #{c} cents" if i/c!=0
    i%=c
  }
  puts
}
