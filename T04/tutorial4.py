import pandas as pd
import numpy as np
from scipy.stats import entropy
from treelib import Tree

# Question 1
loan_df = pd.DataFrame(np.array([
    ['Over 10k', 'Bad', 'Low', 'Reject'],
    ['Over 10k', 'Good', 'High', 'Approve'],
    ['0 - 10k', 'Good', 'Low', 'Approve'],
    ['Over 10k', 'Good', 'Low', 'Approve'],
    ['Over 10k', 'Good', 'Low', 'Approve'],
    ['Over 10k', 'Good', 'Low', 'Approve'],
    ['0 - 10k', 'Good', 'Low', 'Approve'],
    ['Over 10k', 'Bad', 'Low', 'Reject'],
    ['Over 10k', 'Good', 'High', 'Approve'],
    ['0 - 10k', 'Bad', 'High', 'Reject'],
]), columns=['Income', 'Credit History', 'Debt', 'Decision'])

print(loan_df.to_markdown())

def pd_entropy(df, col, base=2):
    return entropy(pd.Series(df[col]).value_counts(normalize=True, sort=False), base=base)

def pd_entropy_c(df, col, c_col, base=2):
    cond_column = df.groupby(c_col)[col]
    df_entropy = cond_column.apply(lambda x:entropy(x.value_counts(), base=base))

    df_sum_rows = df[c_col].value_counts(normalize=True)
    return (df_entropy.sort_index()*df_sum_rows.sort_index()).sum()

def info_gain(df, Y, X, base=2):
    return pd_entropy(df, Y, base) - pd_entropy_c(df, Y, X, base)

info_gain_dicts = []

def create_tree(tree, df, parent=None, action = ''):
    
    if parent == None:
        info_gain_dicts.clear()
    best_col = None
    best_ig = -np.inf

    # Code to determine the best col, remember to skip Decision column.
    for i in range(len(df.columns) - 1):
        ig = info_gain(df, 'Decision', df.columns[i])
        if ig > best_ig and df.columns[i] not in info_gain_dicts:
            best_ig = ig
            best_col = df.columns[i]

    ##print(tree.show(stdout=False,  line_type='ascii'))
    if best_col == None:
        for value in df[parent].unique():
            sub_df = df[df[parent] == value]
            approve = 0
            reject = 0
            for i in range(len(sub_df)):
                if sub_df.iloc[i]['Decision'] == 'Approve':
                    approve += 1
                else:
                    reject += 1
            string = ""
            if approve > 0:
                string += "Approve:" + str(approve)
            if reject > 0:
                string += " Reject:" + str(reject)
            tree.create_node("[" + value + "] " + string, value, parent=parent)
            
        return
    tree.create_node(action + best_col, best_col, parent=parent)
    info_gain_dicts.append(best_col)
    
    # Code to get the next branch of the tree
    
    for value in df[best_col].unique():
        if value == best_col:
            continue
        sub_df = df[df[best_col] == value]
        if pd_entropy(sub_df, 'Decision') != 0:
            create_tree(tree, sub_df, best_col, "[" + value + "] ")
        else:
            tree.create_node("[" + value + "] " + sub_df.iloc[0]['Decision']+":" + str(len(sub_df)), sub_df.iloc[0]['Decision'], parent=best_col)

tree = Tree()
create_tree(tree, loan_df)
print(tree.show(stdout=False,  line_type='ascii'))

loan_noisy_df = loan_df.copy()
loan_noisy_df.iloc[0]['Decision'] = 'Approve'

tree = Tree()
create_tree(tree, loan_noisy_df)
print(tree.show(stdout=False,  line_type='ascii'))