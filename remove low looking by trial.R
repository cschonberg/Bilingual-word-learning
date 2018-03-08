library(tidyverse)

###to do one file at a time i used this, and it works###
#data0 <- read_csv("C:/Users/Christina/Dropbox/Dissertation/Data/FinalET/Custom Test/T1/SAMPLES_7626_SR_trialReport_customTest.csv")
#filtered.data <- filter(data0, ((trialtype == "L" | trialtype == "R") & ipDwellTime > 3600) | 
  #((trialtype == "target" | trialtype == "distracter") & ipDwellTime > 900))
#write_csv(filtered.data, "C:/Users/Christina/Dropbox/Dissertation/Data/FinalET/Custom Test/T1/7626_filtered.csv")


folder <- "C:/Users/Christina/Dropbox/Dissertation/Data/FinalET/Custom Test/T1/"
file_list <- list.files(path=folder, pattern="*.csv")

for (i in 1:length(file_list)){
	# so this gives you an array called [file_list] that's a list of open CSV files
	# and a working variable called 'i' that can get a CSV out of it by index

 	# Stackoverflow says assign works like this: 
	# a <- 1:4
	# assign("a[1]", 2)
	# a[1] == 2          # FALSE
	# get("a[1]") == 2   # TRUE


  # So what this ( below ) function was actually doing is to replace the name of the file
  # with the data in the read-in file? bonkers.
  # assign(file_list[i],
  #        read_csv(paste(folder,file_list[i], sep='')))


  # just read the damn file, "i" will point to the next one in the list
	data0 <- read_csv(paste(folder,file_list[i], sep=''))
	# filter data that we only have one copy of at a time
	filtered.data <- filter(data0, ((trialtype == "L" | trialtype == "R") & ipDwellTime > 3600) | 
         ((trialtype == "target" | trialtype == "distracter") & ipDwellTime > 900))
	# write the data (that we only have one copy of) to the file (indexed on "i")
	write_csv(filtered.data, paste(folder,"Filtered/",file_list[i],sep=''))

}



