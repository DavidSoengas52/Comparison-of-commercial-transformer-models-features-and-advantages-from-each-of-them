import pandas as pd
import numpy as np
from statsmodels.stats.inter_rater import fleiss_kappa

def calculate_fleiss_kappa_from_file(file_path):
 
    all_ratings = []
    num_raters = 12 
    num_categories = 5 

    try:
        with open(file_path, 'r') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line: 
                    continue
                try:

                    ratings_str = line.split(',')
                    ratings = [int(r.strip()) for r in ratings_str]

                    if len(ratings) != num_raters:
                        print(f"Warning: Line {line_num} has {len(ratings)} ratings, expected {num_raters}. Skipping this line.")
                        continue

                    image_category_counts = [0] * num_categories
                    for r in ratings:
                        if 1 <= r <= num_categories:
                            image_category_counts[r - 1] += 1
                        else:
                            print(f"Warning: Line {line_num} contains an out-of-range rating '{r}'. Skipping this line.")
                            image_category_counts = None 
                            break
                    
                    if image_category_counts is not None:
                        all_ratings.append(image_category_counts)

                except ValueError as ve:
                    print(f"Error parsing line {line_num}: {line}. Details: {ve}. Skipping this line.")
                except Exception as e:
                    print(f"An unexpected error occurred on line {line_num}: {line}. Details: {e}. Skipping this line.")

    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

    if not all_ratings:
        print("No valid image ratings found in the file to calculate Fleiss' Kappa.")
        return None

    kappa_table = np.array(all_ratings)
    kappa_score = fleiss_kappa(kappa_table)
    return kappa_score

if __name__ == "__main__":

    input_file_name = "imagerating.txt"

    print(f"Calculating Fleiss' Kappa from '{input_file_name}'...")
    overall_kappa = calculate_fleiss_kappa_from_file(input_file_name)

    if overall_kappa is not None:
        print(f"\nOverall Fleiss' Kappa Score: {overall_kappa:.4f}")