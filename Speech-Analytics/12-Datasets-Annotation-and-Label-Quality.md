# 12 - Datasets, Annotation, and Label Quality

## Objective
Build trustworthy datasets for speech analytics with reproducible annotation policy and quality controls.

## Data Design Principles
- Cover accents, devices, call intents, noise profiles, and speaking styles.
- Separate train/dev/test by speaker and time to prevent leakage.
- Maintain provenance: source, consent, preprocessing history.

## Annotation Design
- Clear ontology for intents, emotions, compliance events
- Multi-annotator labeling and adjudication workflows
- Inter-annotator agreement targets and disagreement tracking

## Quality Controls
- Gold-set checks
- Annotation drift monitoring
- Relabeling loop for uncertain or evolving categories

## Real-Time Example
A collections team introduces dual annotation for “customer vulnerability” cues. Agreement improves from 0.58 to 0.79 κ after policy clarification and examples.

## SLP3 Coverage Mapping
- Ch. 22 lexicon and affect labeling practices
- Ch. 25 dialog-act style annotation concepts
