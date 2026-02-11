# QSAR Molecular Prediction Model

## Project Overview
The QSAR (Quantitative Structure-Activity Relationship) molecular prediction model aims to predict the activity of chemical compounds based on their molecular structures. This project utilizes various machine learning techniques to develop predictive models that can assist in drug discovery and chemical analysis.

## Setup Instructions
1. **Clone the Repository**:  
   Use the following command to clone the repository:
   ```bash
   git clone https://github.com/aryatejmore/chemsis.git
   cd chemsis
   ```
2. **Install Dependencies**:  
   Make sure you have Python installed (version 3.6 or higher). Then, install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```
3. **Download Datasets**:  
   Download the necessary datasets and place them in the `data/` directory.

## Usage Guide
To run the QSAR model, use the following command:
```bash
python main.py --dataset data/dataset.csv
```
### Optional Parameters:
- `--model`: Specify the model to use (e.g., RandomForest, SVM).
- `--output`: Define where to save the predictions.

You can find more detailed usage information in the documentation or by running:
```bash
python main.py --help
```