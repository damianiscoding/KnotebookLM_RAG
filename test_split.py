from split import split_text

test_text = "The old, creaky windmill groaned under the weight of the relentless, whispering wind. A lone, rusty bicycle leaned against a weathered fence, its tires flat and forlorn. High above, a flock of crows, like scattered ink blots against the pale sky, wheeled in a silent, chaotic dance. A half-eaten apple, its skin bruised and brown, lay abandoned on a mossy stone. The air was thick with the scent of damp earth and decaying leaves, a melancholy fragrance that spoke of forgotten summers and the slow, inevitable march of time. A single, tattered page of a forgotten book fluttered across the overgrown path, its words obscured by dirt and time. A distant, muffled sound, like the echo of a forgotten melody, drifted on the breeze, a haunting whisper in the vast, quiet landscape."

user_id = '321'
document_id = '12345'
splits = split_text(test_text, user_id, document_id)
for split in splits:
    print(split.page_content[:50], split.metadata)

vector_ids = add_documents(splits)