import pandas as pd
import os
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

class DatasetExtractor():
    dataset_name = 'Breast_GSE45827'
    file_path = 'dataset/' + dataset_name + '.csv'
    additional_datasets_path = 'dataset/additional_datasets/'

    def __init__(self, file_path = file_path):
        self.df = pd.read_csv(file_path, index_col=0)

    def datasets_exists(self, pca_components):
        return os.path.exists(self.additional_datasets_path + self.dataset_name + '_norm.csv') and \
            os.path.exists(self.additional_datasets_path + self.dataset_name + f'_pca.csv')

    def split_X_y(self):
        X = self.df.drop(columns=['type'])
        y = self.df.type
        unique_classes = y.unique()
        class_mapping = {label: idx for idx, label in enumerate(unique_classes)}
        y = y.map(class_mapping)

        return X, y

    def extract_datasets(self, pca_components=10):
        self.extract_normalized_dataset()
        self.extract_pca_dataset(pca_components, name=f'{self.dataset_name}_pca')
    
    def extract_normalized_dataset(self, name=dataset_name + '_norm'):
        X, y = self.split_X_y()
        X_normalized = (X - X.mean()) / X.std()
        df_norm = X_normalized.copy()
        df_norm['type'] = y
        
        isExist = os.path.exists(self.additional_datasets_path)
        if not isExist:
            os.makedirs(self.additional_datasets_path)
        
        df_norm.to_csv(self.additional_datasets_path+name+'.csv')

    def extract_pca_dataset(self, pca_components, name=f'Breast_GSE45827_pca'):
        X, y = self.split_X_y()
        X_normalized = (X - X.mean()) / X.std()
        pca = PCA(n_components = pca_components)
        pca.fit(X_normalized)

        df_pca = pd.DataFrame(pca.transform(X_normalized), columns=[f'PC{i}' for i in range(1, pca_components+1)], index=X_normalized.index)
        df_pca['type'] = y

        isExist = os.path.exists(self.additional_datasets_path)
        if not isExist:
            os.makedirs(self.additional_datasets_path)
        
        df_pca.to_csv(self.additional_datasets_path+name+'.csv')

    def extract_tsne_dataset(self, tsne_components, name=f'Breast_GSE45827_tsne'):
        X, y = self.split_X_y()
        X_normalized = (X - X.mean()) / X.std()
        tsne = TSNE(n_components = tsne_components)
        tsne.fit(X_normalized)

if __name__ == "__main__":
    PCA_COMPONENTS = 2
    dataset_extractor = DatasetExtractor()

    dataset_extractor.extract_pca_dataset(pca_components=PCA_COMPONENTS)

    print('Done')