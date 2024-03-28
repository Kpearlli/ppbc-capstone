import pandas as pd

# Define the eligibility criteria
def passing_score(score):
    if isinstance(score, str):
        # Check if the value is 'completed'
        if score.lower().strip( ) == 'completed':
            return True  # Not a passing score
        else:
            try:
                score = float(score.rstrip('%'))
                return score >= 55
            except ValueError:
                return False  # Non-numeric string
    elif isinstance(score, (int, float)):
        return score >= 55
    else:
        return False

def check_eligibility(df, output_file):
    completed_finalproject = df['Final project score (Fail/ Pass/ scores)'].apply(passing_score)
    achieve_attendance = df['Attendance rate'] >= 80
    placement_status = df['Placement Status '].isin(['Permanent', 'Contract', 'Self-employment'])
   
    # Combine the criteria to determine eligibility
    df['Cert Eligibility'] = completed_finalproject & achieve_attendance & placement_status
    
    df.to_csv(output_file, index=False)
    print("Certificate eligibility check completed.")
    
    return df

if __name__ == "__main__":
    # to enter input and output file paths
    input_file = input("Enter the location of input CSV file: ")
    output_file = input("Enter the location of output CSV file: ")
    
    # Read input CSV to define df
    df = pd.read_csv(input_file)
    
    # Run certificate eligibility check
    modified_df = check_eligibility(df, output_file)