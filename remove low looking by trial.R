library(tidyverse)

###to do one file at a time i used this, and it works###
#data0 <- read_csv("C:/Users/Christina/Dropbox/Dissertation/Data/FinalET/Custom Test/T1/SAMPLES_7626_SR_trialReport_customTest.csv")
#filtered.data <- filter(data0, ((trialtype == "L" | trialtype == "R") & ipDwellTime > 3600) | 
  #((trialtype == "target" | trialtype == "distracter") & ipDwellTime > 900))
#write_csv(filtered.data, "C:/Users/Christina/Dropbox/Dissertation/Data/FinalET/Custom Test/T1/7626_filtered.csv")


###then this is what i found on stackexchange to try to do loop things###
###the first part does read in all the files but then the commented parts idk###

folder <- "C:/Users/Christina/Dropbox/Dissertation/Data/FinalET/Custom Test/T1/"
file_list <- list.files(path=folder, pattern="*.csv")

for (i in 1:length(file_list)){
  assign(file_list[i],
         read_csv(paste(folder,file_list[i], sep=''))) 
  #filtered <- filter(data0, ((trialtype == "L" | trialtype == "R") & ipDwellTime > 3600) | 
   #       ((trialtype == "target" | trialtype == "distracter") & ipDwellTime > 900))
#  for (j in 1:length(file_list)){
#    write_csv(file_list[i], paste(folder,"Filtered/",file_list[i],sep=''))
#  }
}



