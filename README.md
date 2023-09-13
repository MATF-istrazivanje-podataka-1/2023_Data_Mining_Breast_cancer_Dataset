# Breast Cancer data mining project

## O autoru
Branko Grbic 2/2020 <br>
_mail:_ mi20002@alas.matf.bg.ac.rs

## Skup podataka

Skup podataka se zove `Breast cancer gene expression - CuMiDa` i može se naći [ovde](https://www.kaggle.com/datasets/brunogrisci/breast-cancer-gene-expression-cumida/code?resource=download)
<br>
Zbog prevelike veličine fajla, skup podataka se mora skinuti

## Uputstvo za pokretanje

Skinuti csv dataset u `dataset/` folder. <br>
Za rad je potrebno pokrenuti prvo `preprocessing/extract_datasets.py` koji će generisati normalizovani dataset. <br>
Za poređenje modela u klasifikaciji, tj. fajla `models/classification/model_comparison.ipynb`, morate pokrenuti fajlove `KNN.ipynb`, `xgboost.ipynb` i `SVM.ipynb` koji se nalaze u istom folderu radi ekstrakcije modela. <br>
_OPREZ:_ Modeli su veliki (~250 MB ukupno)

### Koriscene biblioteke
numpy, pandas, seaborn, pickle, sklearn, xgboost, imblearn, matplotlib


## Korišćeni modeli

- Klasifikacija: <br>
    - XGBoost
    - KNN
    - SVM
    - Ansambl
- Klasterovanje: <br>
    - KMeans
    - Gaussian Mixture
- Pravila pridruživanja: <br>
    - Apriori

