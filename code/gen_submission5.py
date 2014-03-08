import numpy as np
# Train
users = {}
print "Learning features for users"
with open("train.csv") as infile:
    for line in infile:
        a,b,c,d,e = line.split(',')
        e = e[:-1]
        if e not in users.keys():
            users[e] = {}
            users[e]['count'] = 1
            users[e]['x_sum'] = float(b)
            users[e]['y_sum'] = float(c)
            users[e]['z_sum'] = float(d)
            users[e]['mag'] = np.sqrt(float(b)**2 + float(c)**2 + float(d)**2)
        else:
            users[e]['count'] += 1
            users[e]['x_sum'] += float(b)
            users[e]['y_sum'] += float(c)
            users[e]['z_sum'] += float(d)
            users[e]['mag'] += np.sqrt(float(b)**2 + float(c)**2 + float(d)**2)
sequences = np.zeros((1000000, 5))
# Test
print "Learning features for sequences"
with open("test.csv") as infile:
    for line in infile:
        a,b,c,d,e = line.split(',')
        e = int(e[:-1])
        sequences[e][0] += 1
        sequences[e][1] += float(b)
        sequences[e][2] += float(c)
        sequences[e][3] += float(d)
        sequences[e][4] += np.sqrt(float(b)**2 + float(c)**2 + float(d)**2)
# Distance/Difference metric
print "Finding is_trueness"
answer = []
with open("questions.csv") as infile:
    for line in infile:
        a,b,c = line.split()
        if int(a)%10000 == 0:
            print a + " done."
        #c = c[:-1]
        b = int(b)
        sample_count = users[c]['count']
        difference = float("%0.5f" % (((users[c]['x_sum']/sample_count) - sequences[b][1]/sequences[b][0])**2 + ((users[c]['y_sum']/sample_count) - sequences[b][2]/sequences[b][0])**2 + ((users[c]['z_sum']/sample_count) - sequences[b][3]/sequences[b][0])**2 + ((users[c]['mag']/sample_count) - sequences[b][4]/sequences[b][0])**2))
        differences = []
        users_list = users.keys()
        for user in users_list:
            differences.append(float("%0.5f" % (((users[user]['x_sum']/users[user]['count']) - sequences[b][1]/sequences[b][0])**2 + ((users[user]['y_sum']/users[user]['count']) - sequences[b][2]/sequences[b][0])**2 + ((users[user]['z_sum']/users[user]['count']) - sequences[b][3]/sequences[b][0])**2 +  + ((users[c]['mag']/sample_count) - sequences[b][4]/sequences[b][0])**2)))
        differences.sort(reverse=True)
        is_trueness = differences.index(difference)
        answer.append(is_trueness)
# Generating Submission
with open("submission5.txt", "w") as text_file:
    for i in range(len(answer)):
        text_file.write(str(i + 1) + ',' + str(answer[i]) + '\n')

