import seaborn as sns
import matplotlib.pyplot as plt

def visualize_gender_distribution(data):
    sns.countplot(x='Gender', data=data)
    plt.title('Gender Distribution')
    plt.show()

def visualize_target_distribution(data):
    sns.countplot(x='Attrition_Flag', data=data)
    plt.title('Attrition Flag Distribution')
    plt.show()

def plot_correlation_heatmap(data):
    numeric_data = data.select_dtypes(include=['number'])
    sns.heatmap(numeric_data.corr(), cmap='coolwarm', annot=False)
    plt.title('Correlation Heatmap')
    plt.show()
