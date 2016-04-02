echo "Executing Prediction for CPU memory"
Rscript final.R & Rscript finalRequestedMemory.R

echo "Result are stored in Result file"
python reducer.py
rm -rf result.csv
rm  result1.csv
echo "Thank YOU"
