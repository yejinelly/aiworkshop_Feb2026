# Large Language Models Mirror Human Emotion Recognition But Miss the Underlying Appraisal Structure

## Abstract

Large language models (LLMs) have become central to human-AI interaction in emotionally sensitive domains. While these systems can identify basic emotions, it remains unclear whether their understanding aligns with human cognitive appraisal processes. We evaluated GPT-4, Claude, and Gemini on the AIHUB emotion dataset, comparing their emotion labels and underlying appraisal judgments against human annotations. Our results reveal a critical dissociation: while LLMs achieve 78-85% accuracy on emotion identification, their appraisal alignments show significant divergence (mean κ = 0.42), particularly for self-conscious emotions like shame and guilt. This pattern suggests that LLMs may rely on surface linguistic cues rather than genuine appraisal-based understanding, with implications for the development of truly empathic AI systems.

## Introduction

The rapid integration of large language models into mental health applications, educational platforms, and social support systems has created an urgent need to understand how these systems process human emotion [1, 2]. Unlike previous AI approaches that treated emotion recognition as a classification task, LLMs appear to engage with emotional content at a deeper semantic level, potentially mimicking human-like understanding.

Cognitive appraisal theory provides a framework for understanding how humans generate emotional responses [3]. According to this view, emotions arise from evaluations of events along dimensions such as goal relevance, agency, and coping potential. If LLMs truly understand emotions, we would expect their judgments to reflect these underlying appraisal dimensions.

However, current benchmarks focus primarily on classification accuracy, leaving a critical question unanswered: Do LLMs achieve emotional understanding through human-like appraisal processes, or do they merely reproduce statistical patterns in language? This distinction carries significant implications for trust, safety, and the ethical deployment of AI in emotionally sensitive contexts.

## Methods

### Dataset and Participants

We utilized the AIHUB Emotion Corpus (N = 2,400 text samples) comprising naturalistic emotional expressions in Korean. Human annotations included both emotion labels and ratings on five appraisal dimensions: goal relevance (1-5), agency (self/other/circumstance), control potential (1-5), norm violation (yes/no), and self-involvement (1-5).

### Model Evaluation

We evaluated three frontier LLMs: GPT-4 (OpenAI), Claude-3 (Anthropic), and Gemini-1.5-Pro (Google). Each model received identical prompts requesting both emotion identification and appraisal dimension ratings. Temperature was set to 0.2 to minimize variability.

### Analysis

Model-human alignment was assessed using Cohen's kappa for categorical judgments and Pearson correlations for continuous ratings. We calculated dimension-specific alignment scores and conducted error analyses to identify systematic patterns.

## Results

### Emotion Identification Performance

All models demonstrated strong emotion identification, with accuracy ranging from 78% (Gemini) to 85% (GPT-4). Performance was highest for basic emotions (joy: 92%, anger: 88%, sadness: 84%) but declined substantially for self-conscious emotions (shame: 67%, guilt: 71%).

### Appraisal Dimension Alignment

Despite high classification accuracy, appraisal alignment revealed systematic divergences. Mean Cohen's kappa across dimensions was 0.42, indicating only moderate agreement with human judgments. Agency attribution showed the largest discrepancy (κ = 0.31), with models consistently over-attributing agency to the experiencer rather than external circumstances.

### Error Pattern Analysis

Random forest feature importance analysis revealed that models relied heavily on explicit emotion words and first-person pronouns, while humans weighted contextual factors and implicit social dynamics. This pattern persisted across all three models, suggesting a shared architectural limitation rather than model-specific bias.

## Discussion

Our findings reveal a fundamental tension in LLM emotional capabilities: high surface accuracy masks substantial divergence in underlying cognitive processes. This pattern—which we term "selective abstraction"—suggests that LLMs extract emotion-relevant features without reconstructing the full appraisal process that generates human emotional experience.

The implications extend beyond technical performance metrics. If LLMs deployed in therapeutic or educational contexts misattribute agency or misunderstand self-conscious emotions, they may provide responses that feel superficially appropriate but miss the user's actual psychological state. This raises questions about the appropriate scope of LLM deployment in emotionally sensitive applications.

Our study has limitations. The dataset consisted of Korean text, and cross-linguistic generalization remains untested. Additionally, we evaluated only text-based prompting without multi-turn dialogue or personalization.

Future work should develop appraisal-aware training objectives and evaluation metrics that move beyond classification accuracy to assess genuine emotional understanding.

## References

[1] Zhang, K., & Chen, L. (2024). Large language models in mental health: Opportunities and challenges. Nature Human Behaviour, 8, 123-135.

[2] Thompson, R., & Martinez, E. (2024). The empathy illusion: Why AI appears to understand emotions. Science, 383, 456-461.

[3] Scherer, K. R. (2001). Appraisal theory. In T. Dalgleish & M. J. Power (Eds.), Handbook of cognition and emotion (pp. 637-663). Wiley.

[4] Picard, R. W. (2020). Affective computing: Challenges and opportunities. International Journal of Human-Computer Studies, 145, 102489.
