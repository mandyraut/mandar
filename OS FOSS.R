#create data for likes
x=c(667,81,72,20,21,9,12)
lables=c("Android(667)","iOS(81)","Windows Phone(72)","Ubuntu Phone(20)","Sailfish OS(21)","Cyanogen OS(9)","Tizen OS(12)")
#give file a name
png(file="likes_for_diffrent_OS.png")
#plot the pie diag with title and rainbow colour pallet
pie(x,lables,main="Likes For Diffrent Operating Systems",col=rainbow(length(x)))
#save the file
dev.off()
