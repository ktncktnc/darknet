import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

print(current_dir)

current_dir = 'data/answer_dataset'

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('data/answer_train.txt', 'w')
file_test = open('data/answer_test.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpeg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        file_test.write("data/answer_dataset" + "/" + title + '.jpeg' + "\n")
    else:
        file_train.write("data/answer_dataset" + "/" + title + '.jpeg' + "\n")
        counter = counter + 1