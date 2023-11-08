Introduction
Colonoscopy is an effective technique for detecting colorectal polyps, which are highly related to colorectal cancer. In clinical practice, segmenting polyps from colonoscopy images is of great importance since it provides valuable information for diagnosis and surgery. However, accurate polyp segmentation is a challenging task, for two major reasons: (i) the same type of polyps has a diversity of size, color and texture; and (ii) the boundary between a polyp and its surrounding mucosa is not sharp.

To address these challenges, we propose a parallel reverse attention network (PraNet) for accurate polyp segmentation in colonoscopy images. Specifically, we first aggregate the features in high-level layers using a parallel partial decoder (PPD). Based on the combined feature, we then generate a global map as the initial guidance area for the following components. In addition, we mine the boundary cues using a reverse attention (RA) module, which is able to establish the relationship between areas and boundary cues. Thanks to the recurrent cooperation mechanism between areas and boundaries, our PraNet is capable of calibrating any misaligned predictions, improving the segmentation accuracy.

Quantitative and qualitative evaluations on five challenging datasets across six metrics show that our PraNet improves the segmentation accuracy significantly, and presents a number of advantages in terms of generalizability, and real-time segmentation efficiency (∼50fps).
 Framework Overview:
 ![framework-final-min](https://github.com/SivaDsolo007/POLYP-SIGHT/assets/95750150/41cbd09c-4fec-4d9d-90a5-d074b90d639c)
 Qualitative Results:
![qualitative_results](https://github.com/SivaDsolo007/POLYP-SIGHT/assets/95750150/6168c6cc-b3ff-44e7-acf7-f2927e0b229b)
![detection_1684299366 7586439](https://github.com/SivaDsolo007/POLYP-SIGHT/assets/95750150/091c031a-2253-4075-9ee6-eae3d8321d27)

Output Video :
https://github.com/SivaDsolo007/POLYP-SIGHT/assets/95750150/4350f2a8-f50d-4dc0-ab53-08d9dc803ce7

