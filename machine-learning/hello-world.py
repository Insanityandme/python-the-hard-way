# Machine learning first tutorial
# 
### Supervised Learning: create a classifier by finding patterns in examples
### Supervised Learning Recipe 
# 1. Collect Training Data
# 2. Train Classifier
# 3. Make Predictions
# Example Training Data
# Weight !  Texture ! Label
# 150g   !  Bumpy   ! Orange
# 170g   !  Bumpy   ! Orange
# 140g   !  Smooth  ! Apple
# 130g   !  Smooth  ! Apple

from sklearn import tree
# The ones and zeros represent smoothness or bumpyness of the apples and oranges. 
# 0 for bumpy
# 1 for smooth
features = [[140, 1], [130, 1], [150, 0], [170, 0]]

# Same for labels
# 0 for apples
# 1 for oranges
labels = [0, 0, 1, 1]

# A classifier, ("A box of rules")
# The type of classifier we are using are what's called a decision tree. 
clf = tree.DecisionTreeClassifier()
# Think of fit as a synonym for find patterns in data. 
clf = clf.fit(features, labels)

print clf.predict([[160, 0]])




