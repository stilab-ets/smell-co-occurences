
library(lsr)
sold<-table(Dataset$smell1,Dataset$smell2)
chisq.test(sold, simulate.p.value = TRUE)
cramersV(sold, simulate.p.value = TRUE)