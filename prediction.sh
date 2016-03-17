echo "Executing Prediction for CPU memory"
Rscript final.R
echo "Executing Prediction for Allocation Processor"
Rscript finalRequestedMemory.R

echo "Result are stored in Result file"
echo "Thank YOU"
