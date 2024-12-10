import pandas as pd
from sklearn.model_selection import LeaveOneOut
import numpy as np

# Load the Excel file
df = pd.read_excel('/Users/sharif/Desktop/UNDERGRAD_COLLEGE/Spring_2024/ECEN453/HW/HW8/ALL_AML_Training.xlsx', sheet_name='ALL_AML_Training')

# Drop non-numerical columns and transpose the matrix so each row is a sample
X = df.drop(['Acc', 'Desc'], axis=1).transpose().values

# Create labels: assume the first 10 columns are ALL and the next 10 are AML
y_true = np.array(['ALL']*10 + ['AML']*10)

def weighted_vote_predict(X_train, y_train, X_test, weights):
    # Ensure weights are an array
    weights = np.array(weights)
    
    # Ensure X_test is a column vector
    X_test = X_test.reshape(-1, 1)

    # Determine class labels
    classes = np.unique(y_train)
    
    # Initialize votes
    votes = {cls: 0 for cls in classes}
    
    # Calculate votes for each class
    for cls in classes:
        class_mask = (y_train == cls)
        # Select only the rows for current class, apply weights to each feature
        class_data = X_train[class_mask]
        # Calculate the dot product between class-specific weighted data and X_test
        votes[cls] = np.sum(weights * (class_data @ X_test))
    
    # Determine the predicted class and prediction strength
    predicted_class = max(votes, key=votes.get)
    total_votes = sum(votes.values())
    prediction_strength = votes[predicted_class] / total_votes if total_votes != 0 else 0
    
    return predicted_class, prediction_strength

def calculate_accuracy(true_classes, predicted_classes, prediction_strengths, ps_cutoff):
    correct = 0
    total = 0
    for true, predicted, strength in zip(true_classes, predicted_classes, prediction_strengths):
        if strength >= ps_cutoff:
            total += 1
            if true == predicted:
                correct += 1
    return correct / total if total > 0 else 0

# Initialize LeaveOneOut cross-validator
loo = LeaveOneOut()
print(f'Number of splits: {loo.get_n_splits(X)}')  # Should output 20

# Initialize lists to store results
true_classes = []
predicted_classes = []
prediction_strengths = []

# Leave-One-Out Cross-Validation
for train_index, test_index in loo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y_true[train_index], y_true[test_index]

    # Implement the weighted voting (the function definition should be implemented accordingly)
    weights = 1 / (np.arange(1, len(X_train[0]) + 1))
    predicted_class, prediction_strength = weighted_vote_predict(X_train, y_train, X_test, weights)

    # Store the results
    true_classes.append(y_test[0])
    predicted_classes.append(predicted_class)
    prediction_strengths.append(prediction_strength)

# Calculate accuracy for different PS cut-offs
accuracy_at_ps_0 = calculate_accuracy(true_classes, predicted_classes, prediction_strengths, ps_cutoff=0)
accuracy_at_ps_03 = calculate_accuracy(true_classes, predicted_classes, prediction_strengths, ps_cutoff=0.3)

# Print results
print('Accuracy at PS cut-off of 0:', accuracy_at_ps_0)
print('Accuracy at PS cut-off of 0.3:', accuracy_at_ps_03)