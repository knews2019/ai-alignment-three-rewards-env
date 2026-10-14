# Arm C: constitutional documents from the source teachings

## What it is

Arm C is arm B plus explanatory documents, written from the teachings that define 真善忍 (Truthfulness-Compassion-Forbearance), mixed into training as text. The method follows constitutional synthetic-document finetuning: documents that explain *why* the principles hold and how they are reconciled when they conflict, not just what they are.

The documents are training data only. They never appear in any reward, grader or judge.

## Why this arm exists

The three rewards cover the clean cases. The teachings cover the conflicts: when truthfulness is harsh, when forbearance means enduring and when it means stopping, compassion toward whom. Arm B vs arm C tests whether that source adds anything beyond the three words. A null result is expected to be published.

## Authorship and scrutiny

The documents are an interpretation of the source teachings. That interpretation is the author's, will be published in full in `arm_c/documents/`, and is open to challenge. The source texts themselves are not included in this repository.

## Rights

The source texts are freely readable online. That is not a license to train on them. Rights for use as training data are to be confirmed before arm C runs. Until then, arm C is a described design, not a scheduled run.

## Contents

- `documents/` — empty until written. Each document will carry: a title, the principle(s) it explains, the conflict it addresses (if any), and a short note on which passages of the source it draws on.
