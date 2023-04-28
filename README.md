# MAP-Elites-football-practice-schedule
 The code creates a map of the feature space and updates it with the best solutions found in each generation. The elite archive stores the best solution for each bin in the map, and the algorithm generates new solutions by mutating and crossover of existing solutions in the elite archive. The fitness function is used to evaluate each solution, and the algorithm tries to find the best solution in the feature space by searching the bins in the elite archive.

 ## Getting Started
 To get started with the project, you'll need to clone the repository and install the required packages:<br />
```sh
git clone https://github.com/Nettking/MAP-Elites-football-practice-schedule.git
```
```sh
pip install -r requirements.txt
```
You can then run the script to retrieve the historical data and train the machine learning model:
```sh
python map-elites.py
```
For comparison with MOEA run the following command:
```sh
python simple.py
```