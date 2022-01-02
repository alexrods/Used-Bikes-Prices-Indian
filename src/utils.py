import pandas as pd
import seaborn as sns
from joblib import dump
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline


def update_model(model: Pipeline) -> None:
    dump(model, 'models/model.pkl')


def save_simple_metrics_report(train_score: float, test_score: float,
                               validation_score: float, model: Pipeline
                               ) -> None:
    with open('report.txt', 'w') as report_file:
        report_file.write("# Model Pipeline Description"+"\n")

        for key, value in model.named_steps.items():
            report_file.write(f'### {key}:{value.__repr__()}'+'\n')
    
        report_file.write(f"### Train Score: {train_score} \n")
        report_file.write(f"### Test Score: {test_score} \n")
        report_file.write(f"### Validation Score: {validation_score} \n")


def get_model_performance_test_set(y_real: pd.Series, y_pred: pd.Series) -> None:
    fig, ax = plt.subplots()
    fig.set_figheight(8)
    fig.set_figwidth(8)
    sns.regplot(x=y_real, y=y_pred, ax=ax)
    ax.set_ylabel("Predicted Bike Price")
    ax.set_xlabel("Real Bike Price")
    ax.set_title("Behavior of model prediction")
    fig.savefig('prediction_behavior.png')
    