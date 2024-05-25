# Home-Credit-Credit-Risk-Model-Stability

**Project Overview:**

This project aimed to enhance financial inclusion by developing robust predictive models to assess default risks among consumers, particularly targeting individuals with limited or no credit history. Utilizing a dataset provided by Home Credit Group, a prominent international consumer finance provider, the project employed various machine learning techniques to predict client default risk accurately.

**Objectives:**

To improve financial inclusion for underbanked populations by predicting default risks with high accuracy.

To explore the efficacy of different machine learning models in handling complex, multi-source financial data.

**Data Description:**
The dataset comprised a wide array of financial and personal data points collected from multiple sources and structured into several levels of detail from static baseline information to detailed historical records.

Key features included credit amount, days past due, income types, and loan statuses, alongside personal attributes like employment details and marital status.

**Methodological Approach:**

**Data Preparation and Management:**

Implementation of various data preprocessing steps such as handling missing data, merging datasets, and optimizing memory usage.

Development of new features and reduction of dimensionality to enhance model performance.

**Model Development:**

Utilization of advanced machine learning algorithms such as LightGBM, CatBoost, XGBoost, and AutoML to develop prediction models.

Application of techniques like gradient boosting and ensemble methods to improve accuracy and stability of the predictive models.

**Model Evaluation and Optimization:**

Rigorous testing and validation using methods like StratifiedKFold and StratifiedGroupKFold for model tuning.

Assessment of model stability and performance using custom metrics like the Gini coefficient and AUC scores.

**Predictive Performance and Insights:**

The project achieved a significant ensemble model AUC score of 0.576, demonstrating the effectiveness of combining multiple models.

Insights into the impact of different data features and model configurations on prediction accuracy were derived, highlighting the nuanced dynamics of credit risk assessment.

**Technologies Used:**

Python for all data processing and model development, utilizing libraries such as Pandas for data manipulation and scikit-learn for model building.

Machine Learning Platforms: Usage of AutoML tools like AutoGluon for automated model tuning and selection.

**Results:**

The ensemble model combining predictions from LightGBM, XGBoost, and CatBoost outperformed individual model predictions, showcasing the power of ensemble learning in practical applications.

The project underscored the potential of data science and machine learning in transforming credit assessment processes, paving the way for more inclusive lending practices.

**This project not only demonstrated the application of complex machine learning techniques in a real-world financial setting but also significantly contributed to the broader goal of financial inclusion. By leveraging cutting-edge data science methodologies, the project provided a scalable solution for credit risk assessment, with the potential to be adapted and extended to other domains within financial services**


