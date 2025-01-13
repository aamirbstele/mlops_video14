import mlflow
import dagshub

mlflow.set_tracking_uri("https://dagshub.com/aamirbstele/mlops_video14.mlflow")

dagshub.init(repo_owner='aamirbstele', repo_name='mlops_video14', mlflow=True)

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)