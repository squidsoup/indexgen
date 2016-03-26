# Indexgen

Generate indices for epub texts.

## Usage 

todo

## Tests

``make test``


## Design

For each chunk that matches, provide the user some context and prompt for (y|n) unless a --force flag is provided.

Source text matches with existing anchors should be skipped

Matches should be case insensitive by default.

### Nice to have

* Handling plurals optionally?
* Optionally match synonyms (would have to be marked up in data file somehow)


