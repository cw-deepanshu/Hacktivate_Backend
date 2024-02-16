# import re

# def get_word_start_and_end_indices(paragraph):
#     """Returns a list of tuples containing the start and end indices of each word in the paragraph."""
#     words = re.finditer(r'\b\w+\b', paragraph)
#     indices = [(word.start() + 1, word.end() + 1, word) for word in words]
#     return indices

# # # Example usage:
# # paragraph = "This is a sample paragraph."
# # indices = get_word_start_and_end_indices(paragraph)

# # print("Word Indices:")
# # for start, end in indices:
# #     print(f"Word: {paragraph[start:end + 1]}, Start Index: {start}, End Index: {end}")


# # def get_word_start_and_end_indices(paragraph):
# #     """Returns a list of tuples containing the start and end indices of each word in the paragraph."""

# #     words = paragraph.split()
# #     indices = []
# #     for word in words:
# #         start = word.index(word[0]) + 1  # Find the index of the first character in the word
# #         end = start + len(word)
# #         indices.append((start, end, word))
# #     return indices

# # # Example usage:

# # paragraph = "This is a sample paragraph."
# # indices = get_word_start_and_end_indices(paragraph)
# # print(indices)

# def create_annotations(paragraph,tagName):
#     annotations = []
#     indices = get_word_start_and_end_indices(paragraph)

#     # Creating annotations based on word indices
#     for idx, (start, end, word) in enumerate(indices):
#         annotation = {
#             "id": idx,
#             "start": start,
#             "end": end,
#             "tag_name": tagName,
#             "value": paragraph[start - 1:end - 1] 
#         }
#         annotations.append(annotation)

#     return annotations

# # Example usage:

# paragraph = "Positive user-friendly knowledgeable patient valuable insights seamless efficient responsive transparent detailed information competitive pricing satisfactory user-centric convenient effective informative professional helpful accommodating impressive streamlined recommendable exceptional outstanding reliable top-notch smooth effortless commendable excellent user-focused prompt courteous exemplary stellar fantastic unparalleled phenomenal superb terrific first-rate remarkable extraordinary unmatched incredible outstanding unparalleled remarkable negative concerns unclear improvement areas delays issues dissatisfaction confusion standard average and moderate."
# tagName = "Feedback"
# annotations = create_annotations(paragraph,tagName)
# print("Annotations:", annotations)

import re

def get_word_start_and_end_indices(paragraph):
    """Returns a list of tuples containing the start and end indices of each word in the paragraph."""
    words = re.finditer(r'\b\w+\b', paragraph)
    indices = [(word.start() + 1, word.end() + 1, word.group()) for word in words]
    return indices

def create_annotations(paragraph, tagName):
    annotations = []
    indices = get_word_start_and_end_indices(paragraph)

    # Creating annotations based on word indices
    for idx, (start, end, word) in enumerate(indices):
        annotation = {
            "id": idx,
            "start": start,
            "end": end,
            "tag_name": tagName,
            "value": word
        }
        annotations.append(annotation)

    return annotations

# Example usage:
paragraph = "Positive user-friendly knowledgeable patient valuable insights seamless efficient responsive transparent detailed information competitive pricing satisfactory user-centric convenient effective informative professional helpful accommodating impressive streamlined recommendable exceptional outstanding reliable top-notch smooth effortless commendable excellent user-focused prompt courteous exemplary stellar fantastic unparalleled phenomenal superb terrific first-rate remarkable extraordinary unmatched incredible outstanding unparalleled remarkable negative concerns unclear improvement areas delays issues dissatisfaction confusion standard average and moderate."
tagName = "Feedback"
annotations = create_annotations(paragraph, tagName)
print("Annotations:", annotations)
