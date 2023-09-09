import pandas as pd
import os
from sklearn.decomposition import PCA

class DatasetExtractor():
    dataset_name = 'Breast_GSE45827'
    file_path = 'dataset/' + dataset_name + '.csv'
    additional_datasets_path = 'dataset/additional_datasets/'

    def __init__(self, file_path = file_path):
        self.df = pd.read_csv(file_path, index_col=0)

    def datasets_exists(self, pca_components):
        return os.path.exists(self.additional_datasets_path + self.dataset_name + '_normalized.csv') and \
            os.path.exists(self.additional_datasets_path + self.dataset_name + f'_pca_{pca_components}.csv')

    def extract_datasets(self, pca_components=10):
        if self.datasets_exists(pca_components):
            print('Datasets already exists')
            return

        X = self.df.drop(columns=['type'])

        y = self.df.type
        unique_classes = y.unique()
        class_mapping = {label: idx for idx, label in enumerate(unique_classes)}
        y = y.map(class_mapping)

        self.extract_normalized_dataset(X, y)
        self.extract_pca_dataset(X, y, pca_components, name=f'{self.dataset_name}_pca')
    
    def extract_normalized_dataset(self, X, y, name=dataset_name + '_norm'):
        X_normalized = (X - X.mean()) / X.std()
        df_norm = pd.concat([X_normalized, y], axis=1)
        
        isExist = os.path.exists(self.additional_datasets_path)
        if not isExist:
            os.makedirs(self.additional_datasets_path)
        
        df_norm.to_csv(self.additional_datasets_path+name+'.csv', index=False)

    def extract_pca_dataset(self, X, y, pca_components, name=f'Breast_GSE45827_pca'):
        X_normalized = (X - X.mean()) / X.std()
        pca = PCA(n_components = pca_components)
        pca.fit(X_normalized)
        X_pca = pd.DataFrame(pca.transform(X_normalized))

        X_pca['type'] = y

        X_pca.to_csv(self.additional_datasets_path+name+'.csv', index=False)


if __name__ == "__main__":
    PCA_COMPONENTS = 10
    dataset_extractor = DatasetExtractor()

    dataset_extractor.extract_datasets(pca_components=PCA_COMPONENTS)

    print('Done')