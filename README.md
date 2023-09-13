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

Za poređenje modela u klasifikaciji, tj. fajla `models/classification/model_comparison.ipynb`, možete skinuti modele [ovde](https://drive.google.com/file/d/1t8Pr_HJzzFVPZG7iErBdctsX-S81sNiB/view?usp=sharing) i staviti ih u istoimeni folder `models/classification`, ali takođe možete i pokrenuti fajlove `KNN.ipynb`, `xgboost.ipynb` i `SVM.ipynb` koji se nalaze u tom folderu radi ekstrakcije modela. <br>
_OPREZ:_ Modeli su veliki (~250 MB ukupno)

### Korišćene biblioteke
`numpy`, `pandas`, `seaborn`, `pickle`, `sklearn`, `xgboost`, `imblearn`, `matplotlib` <br>
Sve biblioteke se mogu instalirati korišćenjem paket menadžera `pip`.

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

