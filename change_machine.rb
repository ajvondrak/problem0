# readlines.map &:to_i
readlines.map{ |i|
  i=i.to_i
  puts"#{i} cents:"
  [25,10,5,1].each{|c|
    puts "#{i/c} x #{c} cents" if i/c!=0
    i%=c
  }
  puts
}
# while i=gets.to_i; puts i+1 end
