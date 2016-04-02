library(forecast)
library(data.table)
trans <- data.table(read.csv("final.csv"),header = TRUE, sep=",")

cpu_p_ts<-ts(trans,start=1990, frequency = 4)
arima_fit <-auto.arima(cpu_p_ts)
result<-predict(arima_fit,n.ahead=12)
print(result)
write.table(result,file="result.csv", append=FALSE, sep= "," )
