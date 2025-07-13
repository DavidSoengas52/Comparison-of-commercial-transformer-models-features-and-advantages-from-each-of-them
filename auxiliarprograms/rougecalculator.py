from rouge_score import rouge_scorer
import os

def calculate_rouge_scores_from_files(file1_path, file2_path):

    if not os.path.exists(file1_path):
        print(f"Error: File not found at '{file1_path}'")
        return
    if not os.path.exists(file2_path):
        print(f"Error: File not found at '{file2_path}'")
        return

    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

    with open(file1_path, 'r', encoding='utf-8') as f1, \
         open(file2_path, 'r', encoding='utf-8') as f2:

        for line_num, (reference_line, candidate_line) in enumerate(zip(f1, f2), 1):
            reference_line = reference_line.strip()
            candidate_line = candidate_line.strip()

            if not reference_line and not candidate_line:
                continue
            elif not reference_line:
                print(f"Warning: Line {line_num} in '{file1_path}' is empty. Skipping ROUGE calculation for this line.")
                continue
            elif not candidate_line:
                print(f"Warning: Line {line_num} in '{file2_path}' is empty. Skipping ROUGE calculation for this line.")
                continue

            scores = scorer.score(reference_line, candidate_line)

            print(f"\n--- Line {line_num} ---")
            print(f"Reference: \"{reference_line}\"")
            print(f"Candidate: \"{candidate_line}\"")
            print(f"ROUGE-1 F1: {scores['rouge1'].fmeasure:.4f}")
            print(f"ROUGE-2 F1: {scores['rouge2'].fmeasure:.4f}")
            print(f"ROUGE-L F1: {scores['rougeL'].fmeasure:.4f}")


if __name__ == "__main__":
    reference_file = "reference.txt"
    candidate_file = "candidate.txt"

    calculate_rouge_scores_from_files(reference_file, candidate_file)