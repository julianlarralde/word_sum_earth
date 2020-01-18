from pandas import DataFrame
import random

letters_df = DataFrame(data=None, index=None, columns=['letter','value'], dtype=None, copy=False)

earth_df    = DataFrame( ['E','A','R','T','H'],     columns = ['letter'])
venus_df    = DataFrame( ['V','E','N','U','S'],     columns = ['letter'])
uranus_df   = DataFrame( ['U','R','A','N','U','S'], columns = ['letter'])
saturn_df   = DataFrame( ['S','A','T','U','R','N'], columns = ['letter'])

unique_values = list(range(0,10))
unique_letters = ['E','A','R','T','H','V','N','U','S']

unique_values_trial = list()
unique_letters_trial = list()

def generate_values():
    global letters_df
    global unique_letters
    global unique_values
    global unique_letters_trial
    global unique_values_trial

    letters_df = letters_df[0:0]

    random.shuffle(unique_letters)
    unique_letters_trial = unique_letters.copy()
    
    random.shuffle(unique_values)
    unique_values_trial = unique_values.copy()

    #print("Unique Letters Shuffled: %s" % unique_letters_trial)

    while unique_letters_trial:
        popped_letter = unique_letters_trial.pop()
        
        if (unique_values_trial):
            popped_value = unique_values_trial.pop()
            new_row = {'letter': popped_letter, 'value': popped_value}
            letters_df = letters_df.append(new_row, ignore_index = True)

    #print(letters_df.to_string())

    return None


def assign_values(df):
    
    global letters_df

    df = df.merge(letters_df, on = 'letter', how = 'left')

    return df


def brute_force():

    global earth_df
    global uranus_df
    global venus_df
    global saturn_df

    global letters_df

    while True:
    
        generate_values()

        earth_df    = assign_values(earth_df)
        venus_df    = assign_values(venus_df)
        uranus_df   = assign_values(uranus_df)
        saturn_df   = assign_values(saturn_df)
        
        e = earth_df['value'].sum()
        v = venus_df['value'].sum()
        u = uranus_df['value'].sum()
        s = saturn_df['value'].sum()

        print("%d %d" % (s, e + v + u) )

        #print("Attempting failed...")

        if ( s == e + v + u and s > 0 ):
            break
        else:
            #print(saturn_df.to_string())
            earth_df = earth_df.drop(['value'],axis = 1)
            venus_df = venus_df.drop(['value'],axis = 1)
            uranus_df = uranus_df.drop(['value'],axis = 1)
            saturn_df = saturn_df.drop(['value'],axis = 1)

    print(letters_df.to_string())

    print("The value of Earth is %d " % e)


if __name__ == "__main__":
    brute_force()
