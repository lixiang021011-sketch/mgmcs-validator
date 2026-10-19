# 全库 timing 体检表

31 首歌，2026-10-11 那一轮：五条读法（人 / BeatThis / madmom / workbench / Mapperatorinator）齐了之后的第一张表。

分类：**clean** 95　**continuous slide** 2　**local drift** 3　**persistent ±1-beat disagreement** 36　**persistent ±2-beat disagreement** 48　**unresolved** 6

只汇总现有两层诊断：**A 层** 拍子跟没跟住（ADTOF 鼓点对 affine 网格，held-out 校正固定偏移后），
**B 层** 各来源小节头两两的相位关系。分类只写**观测事实**，不判"谁对"；
`support` 是连续多少个 matched measure 支持这个 offset（**不是投票**，没有多数表决）。
像 `clean` 只表示"机器读法之间无显著分歧"，**不等于真值正确**。
人那条（手机按的小节头）不进分类，只列在下面详情里——它多数只有几个 matched measure，拿它判"这首歌是什么错"没有依据。

| 歌 | 分类 | A 层：≤0.10 / ≤0.25 | A 层漂移 | A:BeatThis 直线残差 | B 层相位 | B 层标志 | 嫌疑来源 |
|---|---|---|---|---|---|---|---|
| chichunhua | continuous slide | 21% / 52% | 局部明显 | 389 ms（0.89 拍） | 有一对分歧 | continuous drift | — |
| dubai | clean | 98% / 99% | 几乎没有 | 2157 ms（5.57 拍） | 全部一致 | — | — |
| eine | persistent ±1-beat disagreement | 85% / 98% | 轻微 | 1018 ms（1.53 拍） | 有一对分歧 | phase slip（半小节）、reconvergence、phase slip（整拍） | madmom |
| flyway | persistent ±2-beat disagreement | 92% / 99% | 局部明显 | 143 ms（0.23 拍） | 有一对分歧 | phase slip（半小节）、reconvergence | BeatThis |
| flywayleo | persistent ±2-beat disagreement | 94% / 99% | 局部明显 | 6 ms（0.01 拍） | 有一对分歧 | phase slip（半小节）、reconvergence | BeatThis |
| haiiro | clean | 68% / 98% | 轻微 | 25 ms（0.05 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| happyend | clean | 81% / 100% | 轻微 | 1340 ms（1.76 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| henceforth | persistent ±2-beat disagreement | 98% / 100% | 轻微 | 89 ms（0.24 拍） | 有一对分歧 | phase slip（半小节） | BeatThis |
| hitchcock | clean | 92% / 99% | 几乎没有 | 3251 ms（7.80 拍） | 全部一致 | — | — |
| iloveyou | persistent ±2-beat disagreement | 72% / 98% | 轻微 | 9 ms（0.01 拍） | 有一对分歧 | phase slip（半小节）、reconvergence | — |
| kaitou | persistent ±1-beat disagreement | 93% / 99% | 几乎没有 | 7 ms（0.01 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（半小节）、phase slip（整拍）、fixed offset、unstable | BeatThis、workbench |
| kaluo | clean | 94% / 100% | 几乎没有 | 6 ms（0.01 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| kiechau | persistent ±2-beat disagreement | 66% / 94% | 局部明显 | 158 ms（0.28 拍） | 有一对分歧 | phase slip（半小节）、reconvergence | — |
| knowme | persistent ±2-beat disagreement | 92% / 99% | 几乎没有 | 5 ms（0.01 拍） | 有一对分歧 | phase slip（半小节） | BeatThis |
| landaohua | clean | 94% / 100% | 几乎没有 | 7263 ms（10.71 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| lulu | local drift | 56% / 89% | 局部明显 | 5891 ms（12.91 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| natsuyuki | clean | 83% / 93% | 轻微 | 537 ms（1.58 拍） | 全部一致 | — | — |
| new_01 | persistent ±1-beat disagreement | — | 无网格 | 5599 ms（8.02 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（整拍） | BeatThis、madmom |
| new_02 | persistent ±1-beat disagreement | — | 无网格 | 852 ms（2.61 拍） | 有一对分歧 | phase slip（半小节）、reconvergence、phase slip（整拍） | madmom |
| new_03 | clean | — | 无网格 | 5443 ms（16.69 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_04 | clean | — | 无网格 | 7 ms（0.01 拍） | 全部一致 | — | — |
| new_05 | persistent ±2-beat disagreement | — | 无网格 | 2336 ms（6.19 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（半小节） | BeatThis、madmom |
| new_06 | persistent ±2-beat disagreement | — | 无网格 | 1338 ms（1.72 拍） | 有一对分歧 | phase slip（半小节） | BeatThis、madmom |
| new_07 | clean | — | 无网格 | 3121 ms（8.54 拍） | 全部一致 | — | — |
| new_08 | clean | — | 无网格 | 957 ms（2.03 拍） | 全部一致 | — | — |
| new_09 | clean | — | 无网格 | 2630 ms（3.80 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_10 | persistent ±2-beat disagreement | — | 无网格 | 2572 ms（3.51 拍） | 有一对分歧 | phase slip（半小节） | BeatThis |
| new_100 | persistent ±2-beat disagreement | — | 无网格 | 2400 ms（2.94 拍） | 有一对分歧 | phase slip（半小节） | BeatThis、madmom |
| new_101 | persistent ±1-beat disagreement | — | 无网格 | 1580 ms（4.61 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（整拍） | madmom、mapperatorinator |
| new_102 | unresolved | — | 无网格 | 630 ms（0.46 拍） | 不可比 | — | — |
| new_103 | clean | — | 无网格 | 14 ms（0.04 拍） | 全部一致 | — | — |
| new_104 | clean | — | 无网格 | 10 ms（0.03 拍） | 全部一致 | — | — |
| new_105 | clean | — | 无网格 | 9956 ms（12.65 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_106 | clean | — | 无网格 | 7125 ms（11.68 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_107 | clean | — | 无网格 | 1428 ms（1.47 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_108 | persistent ±1-beat disagreement | — | 无网格 | 2437 ms（4.58 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（整拍） | madmom、mapperatorinator |
| new_109 | clean | — | 无网格 | 2269 ms（7.55 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_11 | clean | — | 无网格 | 1011 ms（1.70 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_110 | clean | — | 无网格 | 88 ms（0.26 拍） | 全部一致 | — | — |
| new_111 | persistent ±2-beat disagreement | — | 无网格 | 4136 ms（5.10 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（半小节） | BeatThis、madmom |
| new_112 | unresolved | — | 无网格 | 4324 ms（6.46 拍） | 不可比 | — | — |
| new_113 | clean | — | 无网格 | 2828 ms（8.90 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_114 | persistent ±1-beat disagreement | — | 无网格 | 4723 ms（15.73 拍） | 有一对分歧 | phase slip（整拍）、continuous drift | — |
| new_115 | persistent ±2-beat disagreement | — | 无网格 | 2760 ms（8.77 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（半小节）、reconvergence | workbench |
| new_116 | clean | — | 无网格 | 1685 ms（2.15 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_117 | clean | — | 无网格 | 4904 ms（8.67 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_118 | clean | — | 无网格 | 6 ms（0.01 拍） | 全部一致 | — | — |
| new_119 | clean | — | 无网格 | 7 ms（0.01 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_12 | clean | — | 无网格 | 5 ms（0.01 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_120 | persistent ±1-beat disagreement | — | 无网格 | 2523 ms（4.81 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（整拍） | madmom、mapperatorinator |
| new_121 | persistent ±2-beat disagreement | — | 无网格 | 169 ms（0.23 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（半小节）、fixed offset | madmom、mapperatorinator |
| new_122 | clean | — | 无网格 | 1211 ms（3.82 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_123 | unresolved | — | 无网格 | — | 不可比 | — | — |
| new_124 | clean | — | 无网格 | 4282 ms（6.76 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_125 | persistent ±1-beat disagreement | — | 无网格 | 6310 ms（17.51 拍） | 有一对分歧 | phase slip（半小节）、phase slip（整拍）、continuous drift | mapperatorinator、workbench |
| new_126 | clean | — | 无网格 | 221 ms（0.66 拍） | 全部一致 | — | — |
| new_127 | clean | — | 无网格 | 3854 ms（9.51 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_128 | clean | — | 无网格 | 6 ms（0.01 拍） | 全部一致 | — | — |
| new_129 | clean | — | 无网格 | 167 ms（0.35 拍） | 全部一致 | — | — |
| new_13 | clean | — | 无网格 | 1747 ms（3.38 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_130 | unresolved | — | 无网格 | 1756 ms（1.68 拍） | 不可比 | — | — |
| new_131 | persistent ±1-beat disagreement | — | 无网格 | 939 ms（3.17 拍） | 有一对分歧 | phase slip（整拍） | BeatThis、madmom |
| new_132 | persistent ±2-beat disagreement | — | 无网格 | 5409 ms（14.27 拍） | 有一对分歧 | phase slip（半小节）、reconvergence、continuous drift | — |
| new_133 | clean | — | 无网格 | 3668 ms（10.04 拍） | 全部一致 | — | — |
| new_134 | clean | — | 无网格 | 5600 ms（15.83 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_135 | clean | — | 无网格 | 466 ms（1.46 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_136 | unresolved | — | 无网格 | 2872 ms（3.82 拍） | 不可比 | — | — |
| new_137 | persistent ±2-beat disagreement | — | 无网格 | 2666 ms（4.25 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（半小节）、reconvergence、continuous drift | — |
| new_138 | clean | — | 无网格 | 2 ms（0.00 拍） | 全部一致 | — | — |
| new_139 | clean | — | 无网格 | 712 ms（1.23 拍） | 全部一致 | — | — |
| new_14 | persistent ±1-beat disagreement | — | 无网格 | 5 ms（0.02 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（整拍） | madmom |
| new_140 | clean | — | 无网格 | 23 ms（0.03 拍） | 全部一致 | — | — |
| new_141 | persistent ±1-beat disagreement | — | 无网格 | 22 ms（0.04 拍） | 有一对分歧 | phase slip（整拍）、continuous drift | — |
| new_142 | clean | — | 无网格 | 3843 ms（7.26 拍） | 全部一致 | — | — |
| new_143 | unresolved | — | 无网格 | 147 ms（0.88 拍） | 不可比 | — | — |
| new_144 | clean | — | 无网格 | 6923 ms（8.33 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_145 | clean | — | 无网格 | 5418 ms（6.87 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_146 | clean | — | 无网格 | 4 ms（0.01 拍） | 全部一致 | — | — |
| new_147 | clean | — | 无网格 | 3869 ms（7.59 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_148 | persistent ±1-beat disagreement | — | 无网格 | 3071 ms（4.88 拍） | 有一对分歧 | phase slip（半小节）、reconvergence、phase slip（整拍） | madmom、workbench |
| new_149 | clean | — | 无网格 | 343 ms（0.76 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_15 | clean | — | 无网格 | 6 ms（0.01 拍） | 全部一致 | — | — |
| new_150 | clean | — | 无网格 | 3802 ms（8.38 拍） | 全部一致 | — | — |
| new_151 | clean | — | 无网格 | 5 ms（0.01 拍） | 全部一致 | — | — |
| new_152 | persistent ±1-beat disagreement | — | 无网格 | 2283 ms（6.38 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（整拍） | BeatThis、madmom |
| new_153 | clean | — | 无网格 | 3810 ms（9.80 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_154 | persistent ±2-beat disagreement | — | 无网格 | 870 ms（3.04 拍） | 有一对分歧 | phase slip（半小节）、reconvergence | madmom |
| new_155 | persistent ±1-beat disagreement | — | 无网格 | 677 ms（2.21 拍） | 有一对分歧 | phase slip（整拍） | BeatThis、madmom |
| new_156 | persistent ±2-beat disagreement | — | 无网格 | 5 ms（0.01 拍） | 有一对分歧 | phase slip（半小节）、reconvergence | mapperatorinator |
| new_157 | clean | — | 无网格 | 2287 ms（5.85 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_158 | clean | — | 无网格 | 1360 ms（4.27 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_159 | persistent ±1-beat disagreement | — | 无网格 | 1036 ms（3.17 拍） | 有一对分歧 | phase slip（整拍） | BeatThis |
| new_16 | persistent ±2-beat disagreement | — | 无网格 | 2510 ms（3.43 拍） | 有一对分歧 | phase slip（半小节）、reconvergence | — |
| new_17 | clean | — | 无网格 | 2771 ms（3.55 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_18 | persistent ±2-beat disagreement | — | 无网格 | 1289 ms（2.72 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（半小节）、reconvergence | madmom、mapperatorinator |
| new_19 | clean | — | 无网格 | 3381 ms（5.07 拍） | 全部一致 | — | — |
| new_20 | clean | — | 无网格 | 6 ms（0.01 拍） | 全部一致 | — | — |
| new_21 | persistent ±1-beat disagreement | — | 无网格 | 5987 ms（8.58 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（半小节）、reconvergence、phase slip（整拍） | workbench |
| new_22 | clean | — | 无网格 | 4036 ms（6.08 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_23 | persistent ±2-beat disagreement | — | 无网格 | 1525 ms（2.44 拍） | 有一对分歧 | phase slip（半小节）、reconvergence | BeatThis |
| new_24 | clean | — | 无网格 | 2595 ms（3.77 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_25 | persistent ±2-beat disagreement | — | 无网格 | 6 ms（0.01 拍） | 有一对分歧 | phase slip（半小节） | madmom |
| new_26 | persistent ±2-beat disagreement | — | 无网格 | 1613 ms（2.43 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（半小节）、reconvergence | mapperatorinator |
| new_27 | persistent ±2-beat disagreement | — | 无网格 | 8 ms（0.02 拍） | 有一对分歧 | phase slip（半小节）、fixed offset、unstable | madmom |
| new_28 | persistent ±1-beat disagreement | — | 无网格 | 0 ms（0.00 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（整拍） | madmom、mapperatorinator |
| new_29 | clean | — | 无网格 | 407 ms（0.73 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_30 | clean | — | 无网格 | 408 ms（0.74 拍） | 全部一致 | — | — |
| new_31 | clean | — | 无网格 | 1169 ms（3.33 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_32 | clean | — | 无网格 | 279 ms（0.85 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_33 | clean | — | 无网格 | 881 ms（2.66 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_34 | persistent ±2-beat disagreement | — | 无网格 | 5 ms（0.01 拍） | 有一对分歧 | phase slip（半小节）、fixed offset | workbench |
| new_35 | persistent ±2-beat disagreement | — | 无网格 | 5 ms（0.01 拍） | 有一对分歧 | phase slip（半小节）、reconvergence | mapperatorinator |
| new_36 | clean | — | 无网格 | 592 ms（1.36 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_37 | clean | — | 无网格 | 2853 ms（7.52 拍） | 全部一致 | — | — |
| new_38 | clean | — | 无网格 | 2580 ms（7.00 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_39 | persistent ±1-beat disagreement | — | 无网格 | 6 ms（0.01 拍） | 有一对分歧 | phase slip（整拍）、unstable | madmom、mapperatorinator |
| new_40 | clean | — | 无网格 | 5 ms（0.01 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_41 | clean | — | 无网格 | 134 ms（0.29 拍） | 全部一致 | — | — |
| new_42 | clean | — | 无网格 | 6 ms（0.01 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_43 | persistent ±2-beat disagreement | — | 无网格 | 1400 ms（2.25 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（半小节）、reconvergence | BeatThis |
| new_44 | clean | — | 无网格 | 4036 ms（6.08 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_45 | persistent ±1-beat disagreement | — | 无网格 | 4084 ms（10.35 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（半小节）、phase slip（整拍） | madmom、mapperatorinator |
| new_46 | clean | — | 无网格 | 5 ms（0.01 拍） | 全部一致 | — | — |
| new_47 | clean | — | 无网格 | 2016 ms（5.29 拍） | 全部一致 | — | — |
| new_48 | persistent ±2-beat disagreement | — | 无网格 | 2767 ms（3.55 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（半小节） | BeatThis、mapperatorinator |
| new_49 | persistent ±2-beat disagreement | — | 无网格 | 1922 ms（5.53 拍） | 有一对分歧 | phase slip（半小节）、reconvergence | BeatThis |
| new_50 | continuous slide | — | 无网格 | 737 ms（1.68 拍） | 有一对分歧 | single flip（只一处，未持续）、continuous drift | — |
| new_51 | clean | — | 无网格 | 3017 ms（4.66 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_52 | persistent ±1-beat disagreement | — | 无网格 | 9 ms（0.02 拍） | 有一对分歧 | phase slip（半小节）、phase slip（整拍）、unstable | — |
| new_53 | persistent ±1-beat disagreement | — | 无网格 | 0 ms（0.00 拍） | 有一对分歧 | phase slip（整拍） | — |
| new_54 | persistent ±2-beat disagreement | — | 无网格 | 5 ms（0.01 拍） | 有一对分歧 | phase slip（半小节）、reconvergence | workbench |
| new_55 | persistent ±1-beat disagreement | — | 无网格 | 6422 ms（15.66 拍） | 有一对分歧 | phase slip（半小节）、reconvergence、phase slip（整拍）、continuous drift | madmom |
| new_56 | clean | — | 无网格 | 5 ms（0.01 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_57 | persistent ±2-beat disagreement | — | 无网格 | 4775 ms（12.37 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（半小节）、reconvergence | workbench |
| new_58 | clean | — | 无网格 | 5 ms（0.01 拍） | 全部一致 | — | — |
| new_59 | persistent ±2-beat disagreement | — | 无网格 | 5 ms（0.01 拍） | 有一对分歧 | phase slip（半小节） | madmom |
| new_60 | persistent ±2-beat disagreement | — | 无网格 | 5 ms（0.01 拍） | 有一对分歧 | phase slip（半小节）、unstable | madmom |
| new_61 | persistent ±2-beat disagreement | — | 无网格 | 2474 ms（6.52 拍） | 有一对分歧 | phase slip（半小节）、reconvergence | BeatThis |
| new_62 | persistent ±2-beat disagreement | — | 无网格 | 1929 ms（2.86 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（半小节）、reconvergence | mapperatorinator |
| new_63 | clean | — | 无网格 | 3356 ms（8.56 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_64 | persistent ±1-beat disagreement | — | 无网格 | 2723 ms（5.83 拍） | 有一对分歧 | phase slip（整拍） | BeatThis |
| new_65 | clean | — | 无网格 | 6 ms（0.01 拍） | 全部一致 | — | — |
| new_66 | clean | — | 无网格 | 1773 ms（4.95 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_67 | persistent ±2-beat disagreement | — | 无网格 | 1464 ms（4.24 拍） | 有一对分歧 | phase slip（半小节）、reconvergence | BeatThis |
| new_68 | persistent ±2-beat disagreement | — | 无网格 | 1271 ms（2.13 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（半小节） | madmom |
| new_69 | persistent ±1-beat disagreement | — | 无网格 | 413 ms（1.46 拍） | 有一对分歧 | phase slip（整拍） | BeatThis、madmom |
| new_70 | persistent ±2-beat disagreement | — | 无网格 | 2615 ms（3.72 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（半小节）、reconvergence | BeatThis |
| new_71 | persistent ±1-beat disagreement | — | 无网格 | 4846 ms（11.03 拍） | 有一对分歧 | phase slip（整拍） | BeatThis |
| new_72 | clean | — | 无网格 | 794 ms（2.79 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_73 | persistent ±2-beat disagreement | — | 无网格 | 2526 ms（8.62 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（半小节） | madmom、mapperatorinator |
| new_74 | persistent ±1-beat disagreement | — | 无网格 | 7628 ms（18.53 拍） | 有一对分歧 | phase slip（半小节）、reconvergence、phase slip（整拍）、continuous drift | — |
| new_75 | persistent ±2-beat disagreement | — | 无网格 | 5 ms（0.01 拍） | 有一对分歧 | phase slip（半小节） | BeatThis、workbench |
| new_76 | persistent ±1-beat disagreement | — | 无网格 | 1258 ms（3.40 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（整拍） | madmom |
| new_77 | clean | — | 无网格 | 1210 ms（2.26 拍） | 全部一致 | — | — |
| new_78 | persistent ±1-beat disagreement | — | 无网格 | 6 ms（0.01 拍） | 有一对分歧 | phase slip（半小节）、phase slip（整拍） | — |
| new_79 | persistent ±1-beat disagreement | — | 无网格 | 2792 ms（8.19 拍） | 有一对分歧 | phase slip（整拍） | BeatThis |
| new_80 | persistent ±2-beat disagreement | — | 无网格 | 2713 ms（7.10 拍） | 有一对分歧 | phase slip（半小节）、reconvergence | BeatThis、madmom |
| new_81 | persistent ±1-beat disagreement | — | 无网格 | 10475 ms（11.46 拍） | 有一对分歧 | phase slip（半小节）、phase slip（整拍） | — |
| new_82 | persistent ±1-beat disagreement | — | 无网格 | 14463 ms（30.60 拍） | 有一对分歧 | phase slip（整拍） | BeatThis |
| new_83 | persistent ±2-beat disagreement | — | 无网格 | 936 ms（1.99 拍） | 有一对分歧 | phase slip（半小节） | BeatThis |
| new_84 | clean | — | 无网格 | 125 ms（0.20 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_85 | persistent ±1-beat disagreement | — | 无网格 | 25100 ms（24.58 拍） | 有一对分歧 | phase slip（整拍） | — |
| new_86 | persistent ±2-beat disagreement | — | 无网格 | 1030 ms（0.65 拍） | 有一对分歧 | phase slip（半小节） | madmom、mapperatorinator |
| new_87 | clean | — | 无网格 | 1021 ms（1.29 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_88 | clean | — | 无网格 | 1062 ms（1.43 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_89 | clean | — | 无网格 | 8028 ms（2.88 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_90 | persistent ±1-beat disagreement | — | 无网格 | 2672 ms（5.77 拍） | 有一对分歧 | phase slip（整拍）、continuous drift | mapperatorinator |
| new_91 | clean | — | 无网格 | 34 ms（0.09 拍） | 全部一致 | — | — |
| new_92 | clean | — | 无网格 | 5 ms（0.01 拍） | 全部一致 | — | — |
| new_93 | clean | — | 无网格 | 7 ms（0.01 拍） | 全部一致 | — | — |
| new_94 | persistent ±1-beat disagreement | — | 无网格 | 6 ms（0.02 拍） | 有一对分歧 | phase slip（整拍） | BeatThis |
| new_95 | clean | — | 无网格 | 5366 ms（7.33 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_96 | clean | — | 无网格 | 2834 ms（5.13 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_97 | clean | — | 无网格 | 464 ms（1.44 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| new_98 | persistent ±2-beat disagreement | — | 无网格 | 23 ms（0.07 拍） | 有一对分歧 | phase slip（半小节）、reconvergence、continuous drift | BeatThis |
| new_99 | clean | — | 无网格 | 2796 ms（8.31 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| onewish | persistent ±1-beat disagreement | 94% / 99% | 轻微 | 1190 ms（2.82 拍） | 有一对分歧 | phase slip（半小节）、phase slip（整拍） | — |
| round2 | persistent ±2-beat disagreement | — | 无网格 | — | 有一对分歧 | phase slip（半小节）、reconvergence | madmom、mapperatorinator |
| sacra | clean | 98% / 100% | 几乎没有 | 237 ms（0.66 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| sakuranoko | persistent ±2-beat disagreement | 95% / 99% | 几乎没有 | 6 ms（0.01 拍） | 有一对分歧 | phase slip（半小节）、reconvergence | BeatThis |
| seiza | persistent ±2-beat disagreement | 89% / 99% | 几乎没有 | 322 ms（0.66 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（半小节） | workbench |
| soragoto | clean | 87% / 87% | 几乎没有 | 413 ms（0.48 拍） | 全部一致 | — | — |
| spica | clean | 99% / 100% | 几乎没有 | 5 ms（0.01 拍） | 只有单点跳变 | single flip（只一处，未持续） | — |
| taishou | clean | 99% / 100% | 几乎没有 | 6 ms（0.01 拍） | 全部一致 | — | — |
| tao | clean | 98% / 100% | 几乎没有 | 5 ms（0.01 拍） | 全部一致 | — | — |
| tengoku | clean | 73% / 98% | 轻微 | 1411 ms（2.75 拍） | 全部一致 | — | — |
| velvet | persistent ±2-beat disagreement | 89% / 95% | 几乎没有 | 8 ms（0.01 拍） | 有一对分歧 | phase slip（半小节）、reconvergence | BeatThis |
| yorukake | local drift | 81% / 100% | 局部明显 | 8 ms（0.02 拍） | 全部一致 | — | — |
| yue | local drift | 45% / 88% | 局部明显 | 1743 ms（4.10 拍） | 全部一致 | — | — |
| yukiguni | persistent ±2-beat disagreement | 66% / 93% | 轻微 | 2408 ms（2.60 拍） | 有一对分歧 | single flip（只一处，未持续）、phase slip（半小节）、reconvergence | BeatThis |

各来源自己的 health（只反映它自己输出得像不像话，不代表音乐真值）：

- **chichunhua**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **dubai**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **eine**：BeatThis ok、madmom ok、human:cal_01 ok、mapperatorinator ok、workbench ok
- **flyway**：BeatThis ok、madmom ok、mapperatorinator ok、workbench suspect
- **flywayleo**：BeatThis ok、madmom ok、human:cal_01 ok、human:cal_02 ok、mapperatorinator ok、workbench suspect
- **haiiro**：BeatThis ok、madmom ok、mapperatorinator ok、workbench suspect
- **happyend**：BeatThis ok、madmom ok、human:cal_01 ok、mapperatorinator ok、workbench ok
- **henceforth**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **hitchcock**：BeatThis ok、madmom ok、human:cal_01 ok、human:cal_02 ok、mapperatorinator ok、workbench suspect
- **iloveyou**：BeatThis ok、madmom ok、human:cal_01 ok、human:cal_02 ok、human:cal_03 ok、mapperatorinator ok、workbench suspect
- **kaitou**：BeatThis ok、madmom ok、human:cal_01 ok、mapperatorinator ok、workbench ok
- **kaluo**：BeatThis ok、madmom ok、human:cal_01 ok、human:cal_02 ok、mapperatorinator ok、workbench ok
- **kiechau**：BeatThis ok、madmom ok、human:cal_01 ok、human:cal_02 ok、human:cal_03 ok、human:cal_06 suspect、human:cal_07 suspect、mapperatorinator ok、workbench ok
  - 与 round2 是**同一份音频**，各跑了一次 Mapperatorinator，两次采样不一样（一次干净、一次有洞或拍间距异常）：这是采样的差别，不是歌的问题——单次采样不能当稳定参照。
- **knowme**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **landaohua**：BeatThis ok、madmom ok、human:cal_02 ok、human:cal_03 ok、human:cal_04 ok、mapperatorinator ok、workbench ok
- **lulu**：BeatThis ok、madmom ok、human:cal_01 ok、human:cal_04 ok、mapperatorinator ok、workbench ok
- **natsuyuki**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **new_01**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **new_02**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_03**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_04**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_05**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_06**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_07**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_08**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_09**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_10**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_100**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_101**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_102**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_103**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_104**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_105**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_106**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_107**：BeatThis ok、madmom ok
- **new_108**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_109**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_11**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_110**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_111**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_112**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_113**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_114**：BeatThis ok、madmom ok、mapperatorinator ok、workbench suspect
- **new_115**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **new_116**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_117**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_118**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_119**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_12**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_120**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_121**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_122**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_123**：madmom ok
- **new_124**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_125**：BeatThis ok、madmom ok、mapperatorinator suspect、workbench ok
- **new_126**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_127**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_128**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_129**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_13**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_130**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_131**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_132**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **new_133**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **new_134**：BeatThis ok、madmom ok、mapperatorinator ok、workbench suspect
- **new_135**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_136**：BeatThis ok、madmom ok
- **new_137**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **new_138**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_139**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_14**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_140**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_141**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_142**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_143**：madmom ok、mapperatorinator ok
- **new_144**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_145**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_146**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_147**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_148**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **new_149**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_15**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_150**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_151**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_152**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_153**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_154**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_155**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_156**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **new_157**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_158**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_159**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **new_16**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_17**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_18**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **new_19**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_20**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_21**：BeatThis ok、madmom ok、mapperatorinator suspect、workbench ok
- **new_22**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_23**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_24**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_25**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_26**：BeatThis ok、madmom ok、mapperatorinator suspect、workbench ok
- **new_27**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_28**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_29**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_30**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_31**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_32**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_33**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_34**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **new_35**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_36**：BeatThis ok、madmom ok、mapperatorinator suspect、workbench suspect
- **new_37**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_38**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_39**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_40**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_41**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_42**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_43**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_44**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_45**：BeatThis ok、madmom ok、mapperatorinator suspect、workbench suspect
- **new_46**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_47**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_48**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_49**：BeatThis ok、madmom ok、mapperatorinator suspect、workbench suspect
- **new_50**：BeatThis ok、madmom ok、mapperatorinator suspect、workbench suspect
- **new_51**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_52**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_53**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **new_54**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **new_55**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_56**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_57**：BeatThis ok、madmom ok、mapperatorinator ok、workbench suspect
- **new_58**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_59**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_60**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_61**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_62**：BeatThis ok、madmom ok、mapperatorinator suspect、workbench ok
- **new_63**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_64**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_65**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_66**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_67**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **new_68**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_69**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_70**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_71**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_72**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_73**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_74**：BeatThis ok、madmom ok、mapperatorinator suspect、workbench ok
- **new_75**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **new_76**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_77**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_78**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_79**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **new_80**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_81**：BeatThis ok、madmom ok、mapperatorinator suspect、workbench suspect
- **new_82**：BeatThis ok、madmom ok、mapperatorinator ok、workbench suspect
- **new_83**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_84**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_85**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_86**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_87**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_88**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_89**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_90**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_91**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_92**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_93**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_94**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **new_95**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_96**：BeatThis ok、madmom ok、mapperatorinator suspect
- **new_97**：BeatThis ok、madmom ok、mapperatorinator ok
- **new_98**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **new_99**：BeatThis ok、madmom ok、mapperatorinator ok
- **onewish**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **round2**：madmom ok、human:cal_01 ok、human:cal_03 ok、mapperatorinator suspect
  - 与 kiechau 是**同一份音频**，各跑了一次 Mapperatorinator，两次采样不一样（一次干净、一次有洞或拍间距异常）：这是采样的差别，不是歌的问题——单次采样不能当稳定参照。
- **sacra**：BeatThis ok、madmom ok、mapperatorinator ok、workbench suspect
- **sakuranoko**：BeatThis ok、madmom ok、human:cal_02 ok、human:cal_03 ok、mapperatorinator ok、workbench ok
- **seiza**：BeatThis ok、madmom ok、human:cal_01 ok、human:cal_03 ok、mapperatorinator ok、workbench ok
- **soragoto**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **spica**：BeatThis ok、madmom ok、human:cal_01 ok、human:cal_02 ok、mapperatorinator ok、workbench ok
- **taishou**：BeatThis ok、madmom ok、human:cal_01 ok、human:cal_02 ok、mapperatorinator ok、workbench ok
- **tao**：BeatThis ok、madmom ok、human:cal_01 ok、human:cal_02 ok、human:cal_04 ok、mapperatorinator ok、workbench ok
- **tengoku**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **velvet**：BeatThis ok、madmom ok、human:cal_01 ok、human:cal_02 ok、mapperatorinator ok、workbench ok
- **yorukake**：BeatThis ok、madmom ok、mapperatorinator ok、workbench ok
- **yue**：BeatThis ok、madmom ok、human:cal_01 ok、human:cal_02 ok、mapperatorinator ok、workbench suspect
- **yukiguni**：BeatThis ok、madmom ok、human:cal_01 ok、mapperatorinator ok、workbench ok

## 哪首歌要听哪一段

有 B 层分歧、或 A 层有提示（局部漂移 / 拍序列不成直线）的歌列在这里；其余两层都干净的歌曲不必整曲审。

### chichunhua — continuous slide
- **先听**：01:18–01:42：madmom↔workbench 停差 局部 +1 拍（support = 15 matched measures）；02:51–03:18：madmom↔workbench 停差 局部 -1 拍（support = 15 matched measures）；04:34–04:53：madmom↔workbench 停差 局部 +1 拍（support = 12 matched measures）
- BeatThis↔madmom：两条小节长度略有出入：相位连续滑 -1.24 拍/分钟，最大跳变只有 0.15 拍（没有突变）｜异常区段 00:00–00:09、01:19–01:42、02:05–02:20、02:22–02:34、02:57–03:20
- BeatThis↔mapperatorinator：两条小节长度略有出入：相位连续滑 -1.24 拍/分钟，最大跳变只有 0.18 拍（没有突变）｜异常区段 00:02–00:09、01:24–01:49、02:12–02:22、02:24–02:36、03:02–03:20
- madmom↔workbench：两条小节长度略有出入：相位连续滑 +1.24 拍/分钟，最大跳变只有 0.11 拍（没有突变）｜异常区段 00:00–00:07、01:18–01:42、02:04–02:16、02:18–02:28、02:51–03:18、04:34–04:53
- mapperatorinator↔workbench：两条小节长度略有出入：相位连续滑 +1.24 拍/分钟，最大跳变只有 0.08 拍（没有突变）｜异常区段 00:02–00:09、01:23–01:44、02:11–02:19、02:21–02:34、02:57–03:20、04:37–04:57
- 人那条：没有小节头按压
- BeatThis↔madmom：5 段错位、k 走遍 -2-1+1+2、趋势 -1.24 拍/分钟、残余悬在中间 —— 这是相位滑过整数拍（两条小节长度不同），不是停错在某一格
- BeatThis↔mapperatorinator：5 段错位、k 走遍 -2-1+1+2、趋势 -1.24 拍/分钟、残余悬在中间 —— 这是相位滑过整数拍（两条小节长度不同），不是停错在某一格
- madmom↔workbench：6 段错位、k 走遍 -2-1+1+2、趋势 +1.24 拍/分钟、残余悬在中间 —— 这是相位滑过整数拍（两条小节长度不同），不是停错在某一格
- mapperatorinator↔workbench：6 段错位、k 走遍 -2-1+1+2、趋势 +1.24 拍/分钟、残余悬在中间 —— 这是相位滑过整数拍（两条小节长度不同），不是停错在某一格
- A 层：Beat This 的拍序列不能被一条直线描述（残差 389 ms）——这是拍层的事，和小节相位是两回事

### dubai — clean
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2157 ms）——这是拍层的事，和小节相位是两回事

### eine — persistent ±1-beat disagreement
- **先听**：01:46–03:31：mapperatorinator↔workbench 停差 局部 +1 拍（support = 39 matched measures）；01:20–01:42：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 9 matched measures）；03:36–03:44：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 3 matched measures）
- madmom↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.00 拍的跳变（这才是错位） @01:29，平时 +0.06 拍/分钟｜异常区段 01:13–01:24
- mapperatorinator↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）, 局部 -1 拍；有一处 +2.01 拍的跳变（这才是错位） @03:53，平时 -0.24 拍/分钟｜异常区段 02:31–02:55、03:06–03:31、03:36–03:44、04:02–04:08
- mapperatorinator↔madmom：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）, 局部 -1 拍；有一处 +2.03 拍的跳变（这才是错位） @01:20，平时 -0.24 拍/分钟｜异常区段 01:20–01:42、02:42–03:01、03:06–03:31
- mapperatorinator↔workbench：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）, 局部 +1 拍；有一处 +2.00 拍的跳变（这才是错位） @01:20，平时 -0.10 拍/分钟｜异常区段 01:28–01:33、01:46–03:31
- workbench↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）, 局部 -1 拍, 局部 +1 拍；有一处 +2.01 拍的跳变（这才是错位） @03:53，平时 -0.16 拍/分钟｜异常区段 01:13–01:26、01:43–02:24、02:30–03:06、03:08–03:31、03:36–03:44
- workbench↔madmom：局部错位后又合上（reconvergence）：错位 局部 -1 拍, 局部 +1 拍, ±2 拍（半小节）；有一处 +2.16 拍的跳变（这才是错位） @04:12，平时 -0.27 拍/分钟｜异常区段 01:43–02:11、02:41–03:03、03:08–03:31
- 人那条：human:cal_01 6 个 matched measures
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1018 ms）——这是拍层的事，和小节相位是两回事

### flyway — persistent ±2-beat disagreement
- **先听**：02:15–02:35：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 9 matched measures）
- madmom↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.98 拍的跳变（这才是错位） @02:38，平时 +0.24 拍/分钟｜异常区段 02:15–02:20、02:25–02:35
- mapperatorinator↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.97 拍的跳变（这才是错位） @02:15，平时 +0.24 拍/分钟｜异常区段 02:15–02:35
- 人那条：没有小节头按压
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.002），这是它自己的规则，不是歌曲健康
- 疑似 BeatThis 2-beat counting：它自己报的小节里有 20 个只数了 2 拍 —— 待人工确认

### flywayleo — persistent ±2-beat disagreement
- **先听**：02:18–02:33：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 7 matched measures）
- madmom↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.99 拍的跳变（这才是错位） @02:36，平时 +0.18 拍/分钟｜异常区段 02:18–02:33
- mapperatorinator↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.98 拍的跳变（这才是错位） @02:35，平时 +0.18 拍/分钟｜异常区段 02:18–02:33
- 人那条：human:cal_01 2 个 matched measures、human:cal_02 7 个 matched measures
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.003），这是它自己的规则，不是歌曲健康
- 疑似 BeatThis 2-beat counting：它自己报的小节里有 7 个只数了 2 拍 —— 待人工确认

### haiiro — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +1.95 拍 @04:28（一处≠一段：可能就是漏了一拍），平时 -0.02 拍/分钟
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +1.94 拍 @04:28（一处≠一段：可能就是漏了一拍），平时 -0.02 拍/分钟
- 人那条：没有小节头按压
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.007），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @04:28、BeatThis↔mapperatorinator @04:28

### happyend — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +1.00 拍 @04:57（一处≠一段：可能就是漏了一拍），平时 -0.02 拍/分钟
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +1.98 拍 @05:07（一处≠一段：可能就是漏了一拍），平时 -0.02 拍/分钟
- workbench↔BeatThis：其余全段一致，只在这一处跳了 +1.98 拍 @05:07（一处≠一段：可能就是漏了一拍），平时 -0.02 拍/分钟
- 人那条：human:cal_01 5 个 matched measures
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1340 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @04:57、mapperatorinator↔BeatThis @05:07、workbench↔BeatThis @05:07

### henceforth — persistent ±2-beat disagreement
- **先听**：03:28–03:40：workbench↔BeatThis 停差 ±2 拍（半小节）（support = 9 matched measures）；03:43–03:51：workbench↔BeatThis 停差 ±2 拍（半小节）（support = 6 matched measures）
- madmom↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.91 拍的跳变（这才是错位） @03:28，平时 +0.29 拍/分钟｜异常区段 03:28–03:40、03:43–03:51
- mapperatorinator↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.91 拍的跳变（这才是错位） @03:28，平时 +0.17 拍/分钟｜异常区段 03:28–03:39
- workbench↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.94 拍的跳变（这才是错位） @03:28，平时 +0.28 拍/分钟｜异常区段 03:28–03:40、03:43–03:51
- 人那条：没有小节头按压
- 疑似 BeatThis 2-beat counting：它自己报的小节里有 1 个只数了 2 拍 —— 待人工确认

### hitchcock — clean
- 人那条：human:cal_01 2 个 matched measures、human:cal_02 10 个 matched measures
- A 层：Beat This 的拍序列不能被一条直线描述（残差 3251 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.013），这是它自己的规则，不是歌曲健康

### iloveyou — persistent ±2-beat disagreement
- **先听**：00:03–01:11：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 23 matched measures）；01:51–02:46：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 18 matched measures）；01:17–01:44：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 10 matched measures）
- madmom↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.92 拍的跳变（这才是错位） @00:14，平时 +1.60 拍/分钟｜异常区段 00:01–00:08、01:21–01:31、01:37–01:49、01:55–02:23
- mapperatorinator↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.09 拍的跳变（这才是错位） @00:15，平时 +1.89 拍/分钟｜异常区段 00:15–01:17、02:31–02:46
- mapperatorinator↔madmom：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.92 拍的跳变（这才是错位） @02:51，平时 +0.62 拍/分钟｜异常区段 00:03–01:11、01:17–01:44、01:51–02:46
- 人那条：human:cal_01 7 个 matched measures、human:cal_02 6 个 matched measures、human:cal_03 4 个 matched measures
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.004），这是它自己的规则，不是歌曲健康

### kaitou — persistent ±1-beat disagreement
- **先听**：00:02–03:11：mapperatorinator↔workbench 停差 局部 +1 拍（support = 91 matched measures）
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +1.98 拍 @00:16（一处≠一段：可能就是漏了一拍），平时 -0.44 拍/分钟
- madmom↔mapperatorinator：整段都对不上相位（几条关系轮着来）；有一处 +0.98 拍的跳变（这才是错位） @02:19，平时 +0.79 拍/分钟｜异常区段 00:03–02:14、02:19–03:12
- madmom↔workbench：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +0.98 拍的跳变（这才是错位） @02:19，平时 +0.79 拍/分钟｜异常区段 02:19–03:12
- mapperatorinator↔BeatThis：整段都对不上相位（几条关系轮着来）；有一处 +2.03 拍的跳变（这才是错位） @02:55，平时 +1.19 拍/分钟｜异常区段 00:02–00:15、00:19–02:23、02:34–02:52、02:57–03:11
- mapperatorinator↔workbench：全段固定差 局部 +1 拍（整体相位差，不是局部错位）；不滑（-0.00 拍/分钟，最大跳变 0.03 拍）｜异常区段 00:02–03:11
- workbench↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.00 拍的跳变（这才是错位） @00:16，平时 -0.83 拍/分钟｜异常区段 02:33–02:52、02:56–03:11
- 人那条：human:cal_01 5 个 matched measures

### kaluo — clean
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +0.95 拍 @03:46（一处≠一段：可能就是漏了一拍），平时 +0.01 拍/分钟
- workbench↔BeatThis：其余全段一致，只在这一处跳了 +0.97 拍 @03:46（一处≠一段：可能就是漏了一拍），平时 +0.01 拍/分钟
- 人那条：human:cal_01 6 个 matched measures、human:cal_02 5 个 matched measures
- 单点跳变（没持续成一段，先记着）：madmom↔BeatThis @03:46、workbench↔BeatThis @03:46

### kiechau — persistent ±2-beat disagreement
- **先听**：00:32–02:10：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 43 matched measures）；02:49–03:21：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 15 matched measures）；00:01–00:28：workbench↔BeatThis 停差 ±2 拍（半小节）（support = 13 matched measures）
- madmom↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.95 拍的跳变（这才是错位） @01:01，平时 -0.42 拍/分钟｜异常区段 00:01–00:06、00:08–00:15、00:21–00:28、01:01–01:24、01:33–01:43、01:47–01:54、01:59–02:08、02:17–02:31
- madmom↔workbench：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）, ±2 拍（半小节）；有一处 +1.95 拍的跳变（这才是错位） @01:01，平时 -0.01 拍/分钟｜异常区段 01:01–01:27、01:31–01:36、01:38–01:43、01:45–01:49、01:54–02:01、02:05–02:10、02:15–02:28
- mapperatorinator↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）, ±2 拍（半小节）；有一处 +1.98 拍的跳变（这才是错位） @00:29，平时 +0.17 拍/分钟｜异常区段 00:32–02:10、02:31–02:35、02:38–02:47
- mapperatorinator↔madmom：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.94 拍的跳变（这才是错位） @01:00，平时 -0.84 拍/分钟｜异常区段 01:03–01:28、01:32–02:09、02:49–03:21、03:25–03:35
- mapperatorinator↔workbench：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.82 拍的跳变（这才是错位） @02:12，平时 +2.13 拍/分钟｜异常区段 02:12–02:19、02:49–03:09、03:14–03:35
- workbench↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.95 拍的跳变（这才是错位） @03:36，平时 -0.36 拍/分钟｜异常区段 00:01–00:28
- 人那条：human:cal_01 7 个 matched measures、human:cal_02 7 个 matched measures、human:cal_03 3 个 matched measures、human:cal_06 11 个 matched measures、human:cal_07 7 个 matched measures

### knowme — persistent ±2-beat disagreement
- **先听**：01:33–03:22：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 38 matched measures）；00:02–00:22：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 8 matched measures）
- madmom↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.01 拍的跳变（这才是错位） @01:33，平时 +0.42 拍/分钟｜异常区段 00:02–00:19
- mapperatorinator↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.02 拍的跳变（这才是错位） @00:25，平时 +0.46 拍/分钟｜异常区段 00:02–00:22、01:33–03:22
- workbench↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.01 拍的跳变（这才是错位） @00:25，平时 +0.42 拍/分钟｜异常区段 00:02–00:22、01:33–03:22
- 人那条：没有小节头按压
- 疑似 BeatThis 2-beat counting：它自己报的小节里有 3 个只数了 2 拍 —— 待人工确认

### landaohua — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +2.00 拍 @02:30（一处≠一段：可能就是漏了一拍），平时 +0.00 拍/分钟
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +1.96 拍 @01:32（一处≠一段：可能就是漏了一拍），平时 -0.01 拍/分钟
- BeatThis↔workbench：其余全段一致，只在这一处跳了 +1.96 拍 @01:32（一处≠一段：可能就是漏了一拍），平时 -0.01 拍/分钟
- workbench↔madmom：其余全段一致，只在这一处跳了 +1.99 拍 @04:54（一处≠一段：可能就是漏了一拍），平时 +0.03 拍/分钟
- 人那条：human:cal_02 6 个 matched measures、human:cal_03 8 个 matched measures、human:cal_04 7 个 matched measures
- A 层：Beat This 的拍序列不能被一条直线描述（残差 7263 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @02:30、BeatThis↔mapperatorinator @01:32、BeatThis↔workbench @01:32、workbench↔madmom @04:54

### lulu — local drift
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +1.99 拍 @03:27（一处≠一段：可能就是漏了一拍），平时 -0.01 拍/分钟
- BeatThis↔workbench：其余全段一致，只在这一处跳了 +1.96 拍 @03:27（一处≠一段：可能就是漏了一拍），平时 -0.01 拍/分钟
- 人那条：human:cal_01 4 个 matched measures、human:cal_04 4 个 matched measures
- A 层：Beat This 的拍序列不能被一条直线描述（残差 5891 ms）——这是拍层的事，和小节相位是两回事

### natsuyuki — clean
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 537 ms）——这是拍层的事，和小节相位是两回事

### new_01 — persistent ±1-beat disagreement
- **先听**：00:21–00:31：BeatThis↔madmom 停差 局部 +1 拍（support = 5 matched measures）；00:31–00:36：BeatThis↔madmom 停差 ±2 拍（半小节）（support = 3 matched measures）；00:39–00:44：BeatThis↔madmom 停差 ±2 拍（半小节）（support = 3 matched measures）
- BeatThis↔madmom：有一头是错位的（局部 +1 拍 那端没回来）；有一处 +2.01 拍的跳变（这才是错位） @01:34，平时 +0.55 拍/分钟｜异常区段 00:21–00:31、00:31–00:36、00:39–00:44
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +2.00 拍 @00:34（一处≠一段：可能就是漏了一拍），平时 +0.29 拍/分钟
- mapperatorinator↔madmom：其余全段一致，只在这一处跳了 +1.75 拍 @00:43（一处≠一段：可能就是漏了一拍），平时 -0.13 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 5599 ms）——这是拍层的事，和小节相位是两回事

### new_02 — persistent ±1-beat disagreement
- **先听**：01:30–01:35：BeatThis↔madmom 停差 ±2 拍（半小节）（support = 5 matched measures）；02:20–02:24：BeatThis↔madmom 停差 ±2 拍（半小节）（support = 4 matched measures）；03:23–03:28：mapperatorinator↔madmom 停差 局部 -1 拍（support = 4 matched measures）
- BeatThis↔madmom：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.00 拍的跳变（这才是错位） @02:24，平时 -0.04 拍/分钟｜异常区段 01:30–01:35、02:20–02:24
- mapperatorinator↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.50 拍的跳变（这才是错位） @03:23，平时 +3.29 拍/分钟｜异常区段 02:20–02:23
- mapperatorinator↔madmom：有一头是错位的（局部 -1 拍 那端没回来）；有一处 +2.00 拍的跳变（这才是错位） @03:30，平时 -0.10 拍/分钟｜异常区段 03:23–03:28
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 852 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.028），这是它自己的规则，不是歌曲健康

### new_03 — clean
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +0.96 拍 @01:59（一处≠一段：可能就是漏了一拍），平时 +0.00 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 5443 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.003），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：BeatThis↔mapperatorinator @01:59

### new_04 — clean
- 人那条：没有小节头按压
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.010），这是它自己的规则，不是歌曲健康

### new_05 — persistent ±2-beat disagreement
- **先听**：02:22–02:36：madmom↔BeatThis 停差 ±2 拍（半小节）（support = 11 matched measures）；02:40–02:50：madmom↔BeatThis 停差 ±2 拍（半小节）（support = 8 matched measures）；03:00–03:07：madmom↔BeatThis 停差 ±2 拍（半小节）（support = 6 matched measures）
- madmom↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.96 拍的跳变（这才是错位） @02:39，平时 -0.38 拍/分钟｜异常区段 02:22–02:36、02:40–02:50、03:00–03:07、03:12–03:17
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +1.96 拍 @01:29（一处≠一段：可能就是漏了一拍），平时 -0.02 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2336 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.012），这是它自己的规则，不是歌曲健康
- 疑似 BeatThis 2-beat counting：它自己报的小节里有 89 个只数了 2 拍 —— 待人工确认

### new_06 — persistent ±2-beat disagreement
- **先听**：00:22–00:28：BeatThis↔madmom 停差 ±2 拍（半小节）（support = 5 matched measures）
- BeatThis↔madmom：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.99 拍的跳变（这才是错位） @03:40，平时 +0.49 拍/分钟｜异常区段 00:22–00:28
- BeatThis↔mapperatorinator：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.97 拍的跳变（这才是错位） @00:32，平时 +0.49 拍/分钟｜异常区段 00:22–00:28
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1338 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.035），这是它自己的规则，不是歌曲健康
- 疑似 BeatThis 2-beat counting：它自己报的小节里有 62 个只数了 2 拍 —— 待人工确认

### new_07 — clean
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 3121 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.081），这是它自己的规则，不是歌曲健康

### new_08 — clean
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 957 ms）——这是拍层的事，和小节相位是两回事

### new_09 — clean
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +1.00 拍 @02:15（一处≠一段：可能就是漏了一拍），平时 +0.03 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2630 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：madmom↔BeatThis @02:15

### new_10 — persistent ±2-beat disagreement
- **先听**：03:08–03:13：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 3 matched measures）
- madmom↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.07 拍的跳变（这才是错位） @03:08，平时 +1.82 拍/分钟｜异常区段 03:08–03:14
- mapperatorinator↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.07 拍的跳变（这才是错位） @03:08，平时 +1.80 拍/分钟｜异常区段 03:08–03:13
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2572 ms）——这是拍层的事，和小节相位是两回事
- 疑似 BeatThis 2-beat counting：它自己报的小节里有 31 个只数了 2 拍 —— 待人工确认

### new_100 — persistent ±2-beat disagreement
- **先听**：02:01–03:55：madmom↔BeatThis 停差 ±2 拍（半小节）（support = 39 matched measures）；00:01–00:10：madmom↔BeatThis 停差 ±2 拍（半小节）（support = 4 matched measures）；00:16–00:25：madmom↔BeatThis 停差 ±2 拍（半小节）（support = 4 matched measures）
- madmom↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.80 拍的跳变（这才是错位） @01:49，平时 -1.08 拍/分钟｜异常区段 00:01–00:10、00:16–00:25、02:01–03:55
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2400 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.015），这是它自己的规则，不是歌曲健康

### new_101 — persistent ±1-beat disagreement
- **先听**：03:25–03:29：mapperatorinator↔madmom 停差 局部 -1 拍（support = 4 matched measures）
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +0.82 拍 @03:34（一处≠一段：可能就是漏了一拍），平时 -0.00 拍/分钟
- mapperatorinator↔madmom：局部错位后又合上（reconvergence）：错位 局部 -1 拍；有一处 +0.77 拍的跳变（这才是错位） @03:46，平时 -0.02 拍/分钟｜异常区段 03:25–03:29
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1580 ms）——这是拍层的事，和小节相位是两回事

### new_102 — unresolved
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 630 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.036），这是它自己的规则，不是歌曲健康
- 机器读法之间没有一对能比较

### new_103 — clean
- 人那条：没有小节头按压
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.009），这是它自己的规则，不是歌曲健康

### new_105 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +0.97 拍 @03:26（一处≠一段：可能就是漏了一拍），平时 -0.00 拍/分钟
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +1.01 拍 @03:26（一处≠一段：可能就是漏了一拍），平时 +0.00 拍/分钟
- madmom↔mapperatorinator：其余全段一致，只在这一处跳了 +1.33 拍 @03:26（一处≠一段：可能就是漏了一拍），平时 -1.30 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 9956 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.023），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @03:26、BeatThis↔mapperatorinator @03:26、madmom↔mapperatorinator @03:26

### new_106 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +1.99 拍 @02:39（一处≠一段：可能就是漏了一拍），平时 -1.63 拍/分钟
- mapperatorinator↔madmom：其余全段一致，只在这一处跳了 +1.76 拍 @03:36（一处≠一段：可能就是漏了一拍），平时 -0.17 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 7125 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @02:39、mapperatorinator↔madmom @03:36

### new_107 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +2.00 拍 @00:29（一处≠一段：可能就是漏了一拍），平时 +0.08 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1428 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.086），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @00:29

### new_108 — persistent ±1-beat disagreement
- **先听**：00:33–00:36：mapperatorinator↔madmom 停差 局部 -1 拍（support = 3 matched measures）；00:39–00:42：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 3 matched measures）
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +2.33 拍 @01:23（一处≠一段：可能就是漏了一拍），平时 -3.35 拍/分钟
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +2.05 拍 @01:16（一处≠一段：可能就是漏了一拍），平时 -4.67 拍/分钟
- mapperatorinator↔madmom：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +0.70 拍的跳变（这才是错位） @00:39，平时 -3.04 拍/分钟｜异常区段 00:33–00:36、00:39–00:42
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2437 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.065），这是它自己的规则，不是歌曲健康

### new_109 — clean
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +0.40 拍 @02:42（一处≠一段：可能就是漏了一拍），平时 -0.01 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2269 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.096），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：mapperatorinator↔BeatThis @02:42

### new_11 — clean
- mapperatorinator↔madmom：其余全段一致，只在这一处跳了 +0.96 拍 @01:11（一处≠一段：可能就是漏了一拍），平时 +0.30 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1011 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：mapperatorinator↔madmom @01:11

### new_111 — persistent ±2-beat disagreement
- **先听**：02:45–03:19：madmom↔BeatThis 停差 ±2 拍（半小节）（support = 13 matched measures）
- madmom↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.65 拍的跳变（这才是错位） @02:42，平时 -0.99 拍/分钟｜异常区段 02:45–03:19
- mapperatorinator↔madmom：其余全段一致，只在这一处跳了 +0.93 拍 @02:36（一处≠一段：可能就是漏了一拍），平时 +1.96 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 4136 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.013），这是它自己的规则，不是歌曲健康

### new_112 — unresolved
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 4324 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.017），这是它自己的规则，不是歌曲健康
- 机器读法之间没有一对能比较

### new_113 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +2.00 拍 @03:05（一处≠一段：可能就是漏了一拍），平时 -0.13 拍/分钟
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +2.00 拍 @03:05（一处≠一段：可能就是漏了一拍），平时 -0.13 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2828 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.019），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @03:05、BeatThis↔mapperatorinator @03:05

### new_114 — persistent ±1-beat disagreement
- **先听**：02:48–03:20：mapperatorinator↔madmom 停差 局部 -1 拍（support = 28 matched measures）；03:41–03:56：workbench↔BeatThis 停差 局部 -1 拍（support = 14 matched measures）；04:01–04:17：workbench↔BeatThis 停差 局部 -1 拍（support = 14 matched measures）
- madmom↔BeatThis：局部错位后又合上（reconvergence）：错位 局部 -1 拍；有一处 +0.97 拍的跳变（这才是错位） @01:03，平时 +0.02 拍/分钟｜异常区段 01:03–01:12
- madmom↔workbench：有一头是错位的（局部 +1 拍 那端没回来）；有一处 +0.64 拍的跳变（这才是错位） @02:49，平时 +0.24 拍/分钟｜异常区段 02:49–03:19
- mapperatorinator↔BeatThis：有一头是错位的（局部 +1 拍 那端没回来）；有一处 +1.88 拍的跳变（这才是错位） @03:41，平时 -0.10 拍/分钟｜异常区段 02:55–03:20、03:29–03:37
- mapperatorinator↔madmom：有一头是错位的（局部 -1 拍 那端没回来）；有一处 +0.60 拍的跳变（这才是错位） @02:48，平时 -0.25 拍/分钟｜异常区段 02:48–03:20
- workbench↔BeatThis：有一头是错位的（局部 -1 拍 那端没回来）；有一处 +1.90 拍的跳变（这才是错位） @03:29，平时 -0.22 拍/分钟｜异常区段 02:55–03:20、03:29–03:37、03:41–03:56、04:01–04:17
- 人那条：没有小节头按压
- mapperatorinator↔BeatThis：2 段错位、k 走遍 -1+1、趋势 -0.10 拍/分钟、残余悬在中间 —— 这是相位滑过整数拍（两条小节长度不同），不是停错在某一格
- A 层：Beat This 的拍序列不能被一条直线描述（残差 4723 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.618），这是它自己的规则，不是歌曲健康

### new_115 — persistent ±2-beat disagreement
- **先听**：03:11–03:26：madmom↔workbench 停差 ±2 拍（半小节）（support = 7 matched measures）
- BeatThis↔workbench：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.97 拍的跳变（这才是错位） @03:29，平时 +3.45 拍/分钟｜异常区段 03:08–03:12
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +1.98 拍 @03:05（一处≠一段：可能就是漏了一拍），平时 -1.08 拍/分钟
- madmom↔workbench：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.86 拍的跳变（这才是错位） @03:09，平时 +0.07 拍/分钟｜异常区段 03:11–03:26
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +1.97 拍 @03:14（一处≠一段：可能就是漏了一拍），平时 -0.22 拍/分钟
- mapperatorinator↔madmom：其余全段一致，只在这一处跳了 +1.87 拍 @03:08（一处≠一段：可能就是漏了一拍），平时 -0.18 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2760 ms）——这是拍层的事，和小节相位是两回事

### new_116 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +2.00 拍 @01:51（一处≠一段：可能就是漏了一拍），平时 +0.02 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1685 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @01:51

### new_117 — clean
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +1.93 拍 @03:26（一处≠一段：可能就是漏了一拍），平时 -0.03 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 4904 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.016），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：madmom↔BeatThis @03:26

### new_119 — clean
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +2.00 拍 @01:09（一处≠一段：可能就是漏了一拍），平时 -0.01 拍/分钟
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +1.96 拍 @01:11（一处≠一段：可能就是漏了一拍），平时 +1.08 拍/分钟
- 人那条：没有小节头按压
- 单点跳变（没持续成一段，先记着）：madmom↔BeatThis @01:09、mapperatorinator↔BeatThis @01:11

### new_12 — clean
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +1.06 拍 @02:28（一处≠一段：可能就是漏了一拍），平时 -0.02 拍/分钟
- mapperatorinator↔madmom：其余全段一致，只在这一处跳了 +1.02 拍 @02:25（一处≠一段：可能就是漏了一拍），平时 -0.02 拍/分钟
- 人那条：没有小节头按压
- 单点跳变（没持续成一段，先记着）：mapperatorinator↔BeatThis @02:28、mapperatorinator↔madmom @02:25

### new_120 — persistent ±1-beat disagreement
- **先听**：01:27–01:33：mapperatorinator↔madmom 停差 局部 +1 拍（support = 3 matched measures）
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +0.91 拍 @01:29（一处≠一段：可能就是漏了一拍），平时 -0.88 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2523 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.065），这是它自己的规则，不是歌曲健康

### new_121 — persistent ±2-beat disagreement
- **先听**：00:23–01:05：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 15 matched measures）；01:11–01:29：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 7 matched measures）
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +2.10 拍 @00:29（一处≠一段：可能就是漏了一拍），平时 +1.33 拍/分钟
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +2.00 拍 @01:19（一处≠一段：可能就是漏了一拍），平时 +0.01 拍/分钟
- mapperatorinator↔madmom：全段固定差 ±2 拍（半小节）（整体相位差，不是局部错位）；不滑（+0.01 拍/分钟，最大跳变 0.05 拍）｜异常区段 00:23–01:05、01:11–01:29
- 人那条：没有小节头按压
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.016），这是它自己的规则，不是歌曲健康

### new_122 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +2.01 拍 @00:34（一处≠一段：可能就是漏了一拍），平时 -1.25 拍/分钟
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +1.94 拍 @00:30（一处≠一段：可能就是漏了一拍），平时 +0.04 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1211 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @00:34、mapperatorinator↔BeatThis @00:30

### new_123 — unresolved
- 人那条：没有小节头按压
- 机器读法之间没有一对能比较

### new_124 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +1.20 拍 @00:12（一处≠一段：可能就是漏了一拍），平时 +0.13 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 4282 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @00:12

### new_125 — persistent ±1-beat disagreement
- **先听**：04:18–04:26：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 8 matched measures）；00:20–00:27：BeatThis↔madmom 停差 局部 +1 拍（support = 7 matched measures）；00:10–00:16：BeatThis↔madmom 停差 局部 +1 拍（support = 6 matched measures）
- BeatThis↔madmom：有一头是错位的（局部 +1 拍 那端没回来）；有一处 +2.02 拍的跳变（这才是错位） @04:30，平时 +1.80 拍/分钟｜异常区段 00:10–00:16、00:20–00:27
- BeatThis↔workbench：有一头是错位的（局部 +1 拍 那端没回来）；有一处 +1.98 拍的跳变（这才是错位） @00:59，平时 -0.30 拍/分钟｜异常区段 00:10–00:16、00:20–00:27
- mapperatorinator↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.91 拍的跳变（这才是错位） @04:18，平时 -0.05 拍/分钟｜异常区段 00:11–00:16、00:21–00:27、04:18–04:26
- mapperatorinator↔madmom：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.97 拍的跳变（这才是错位） @04:18，平时 -0.11 拍/分钟｜异常区段 04:18–04:26
- mapperatorinator↔workbench：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.99 拍的跳变（这才是错位） @04:18，平时 -0.11 拍/分钟｜异常区段 04:18–04:26
- 人那条：没有小节头按压
- mapperatorinator↔BeatThis：3 段错位、k 走遍 -1+2、趋势 -0.05 拍/分钟、残余悬在中间 —— 这是相位滑过整数拍（两条小节长度不同），不是停错在某一格
- A 层：Beat This 的拍序列不能被一条直线描述（残差 6310 ms）——这是拍层的事，和小节相位是两回事

### new_126 — clean
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 221 ms）——这是拍层的事，和小节相位是两回事

### new_127 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +1.06 拍 @02:59（一处≠一段：可能就是漏了一拍），平时 +0.02 拍/分钟
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +0.99 拍 @02:59（一处≠一段：可能就是漏了一拍），平时 +0.02 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 3854 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.013），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @02:59、BeatThis↔mapperatorinator @02:59

### new_128 — clean
- 人那条：没有小节头按压
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.035），这是它自己的规则，不是歌曲健康

### new_129 — clean
- 人那条：没有小节头按压
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.045），这是它自己的规则，不是歌曲健康

### new_13 — clean
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +1.12 拍 @02:47（一处≠一段：可能就是漏了一拍），平时 -0.03 拍/分钟
- mapperatorinator↔madmom：其余全段一致，只在这一处跳了 +1.92 拍 @02:24（一处≠一段：可能就是漏了一拍），平时 -0.09 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1747 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.818），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：madmom↔BeatThis @02:47、mapperatorinator↔madmom @02:24

### new_130 — unresolved
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1756 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.201），这是它自己的规则，不是歌曲健康
- 机器读法之间没有一对能比较

### new_131 — persistent ±1-beat disagreement
- **先听**：00:34–00:39：mapperatorinator↔BeatThis 停差 局部 -1 拍（support = 3 matched measures）
- madmom↔BeatThis：局部错位后又合上（reconvergence）：错位 局部 -1 拍；有一处 +2.00 拍的跳变（这才是错位） @03:58，平时 +0.07 拍/分钟｜异常区段 00:34–00:39
- mapperatorinator↔BeatThis：局部错位后又合上（reconvergence）：错位 局部 -1 拍；有一处 +1.98 拍的跳变（这才是错位） @00:52，平时 +1.31 拍/分钟｜异常区段 00:34–00:39
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 939 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.013），这是它自己的规则，不是歌曲健康

### new_132 — persistent ±2-beat disagreement
- **先听**：01:26–02:28：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 47 matched measures）；00:05–00:52：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 36 matched measures）；02:50–03:05：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 12 matched measures）
- madmom↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.02 拍的跳变（这才是错位） @00:15，平时 +1.05 拍/分钟｜异常区段 00:00–00:04、01:26–01:38
- madmom↔workbench：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.02 拍的跳变（这才是错位） @01:26，平时 -0.58 拍/分钟｜异常区段 00:02–00:07、00:10–00:19、00:22–00:24、00:27–00:30、00:43–00:48、01:32–01:38、01:44–01:47、02:02–02:04、02:08–02:11、02:18–02:22、02:48–02:51、03:03–03:07、03:10–03:12
- mapperatorinator↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.05 拍的跳变（这才是错位） @01:45，平时 -2.58 拍/分钟｜异常区段 00:26–00:29、01:45–01:48、02:00–02:14、02:17–02:20、03:00–03:14
- mapperatorinator↔madmom：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.99 拍的跳变（这才是错位） @00:53，平时 +1.95 拍/分钟｜异常区段 00:05–00:52、01:26–02:28、02:50–03:05、03:08–03:12
- workbench↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.02 拍的跳变（这才是错位） @00:17，平时 -1.61 拍/分钟｜异常区段 00:26–00:29、01:45–01:48、02:00–02:14、02:17–02:20、03:00–03:14
- 人那条：没有小节头按压
- madmom↔BeatThis：2 段错位、k 走遍 +2、趋势 +1.05 拍/分钟、残余悬在中间 —— 这是相位滑过整数拍（两条小节长度不同），不是停错在某一格
- mapperatorinator↔BeatThis：5 段错位、k 走遍 +2、趋势 -2.58 拍/分钟、残余悬在中间 —— 这是相位滑过整数拍（两条小节长度不同），不是停错在某一格
- A 层：Beat This 的拍序列不能被一条直线描述（残差 5409 ms）——这是拍层的事，和小节相位是两回事

### new_133 — clean
- **先听**：01:15–01:28：madmom↔BeatThis 停差 ±2 拍（半小节）（support = 11 matched measures）
- madmom↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.97 拍的跳变（这才是错位） @02:23，平时 -0.06 拍/分钟｜异常区段 01:15–01:28
- mapperatorinator↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.02 拍的跳变（这才是错位） @02:23，平时 -1.32 拍/分钟｜异常区段 01:15–01:28
- workbench↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.98 拍的跳变（这才是错位） @01:15，平时 -0.06 拍/分钟｜异常区段 01:15–01:28
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 3668 ms）——这是拍层的事，和小节相位是两回事

### new_134 — clean
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +1.99 拍 @02:26（一处≠一段：可能就是漏了一拍），平时 +0.02 拍/分钟
- BeatThis↔workbench：其余全段一致，只在这一处跳了 +1.97 拍 @02:26（一处≠一段：可能就是漏了一拍），平时 +0.01 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 5600 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.833），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：BeatThis↔mapperatorinator @02:26、BeatThis↔workbench @02:26

### new_135 — clean
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +0.94 拍 @00:25（一处≠一段：可能就是漏了一拍），平时 +0.00 拍/分钟
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +0.87 拍 @03:03（一处≠一段：可能就是漏了一拍），平时 -0.00 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 466 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：madmom↔BeatThis @00:25、mapperatorinator↔BeatThis @03:03

### new_136 — unresolved
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2872 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.191），这是它自己的规则，不是歌曲健康
- 机器读法之间没有一对能比较

### new_137 — persistent ±2-beat disagreement
- **先听**：02:34–03:27：BeatThis↔workbench 停差 ±2 拍（半小节）（support = 24 matched measures）；02:00–02:23：madmom↔workbench 停差 ±2 拍（半小节）（support = 11 matched measures）
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +2.00 拍 @04:37（一处≠一段：可能就是漏了一拍），平时 +0.04 拍/分钟
- BeatThis↔mapperatorinator：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.00 拍的跳变（这才是错位） @02:39，平时 +1.02 拍/分钟｜异常区段 02:00–02:18
- BeatThis↔workbench：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.97 拍的跳变（这才是错位） @04:37，平时 +1.17 拍/分钟｜异常区段 02:00–02:18、02:34–03:27
- madmom↔workbench：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.19 拍的跳变（这才是错位） @02:00，平时 -1.12 拍/分钟｜异常区段 02:00–02:23、02:34–03:24
- mapperatorinator↔madmom：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.97 拍的跳变（这才是错位） @02:01，平时 +0.02 拍/分钟｜异常区段 02:01–02:19
- mapperatorinator↔workbench：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.93 拍的跳变（这才是错位） @03:35，平时 +1.16 拍/分钟｜异常区段 02:39–03:31
- 人那条：没有小节头按压
- madmom↔workbench：2 段错位、k 走遍 +2、趋势 -1.12 拍/分钟、残余悬在中间 —— 这是相位滑过整数拍（两条小节长度不同），不是停错在某一格
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2666 ms）——这是拍层的事，和小节相位是两回事

### new_139 — clean
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 712 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.044），这是它自己的规则，不是歌曲健康

### new_14 — persistent ±1-beat disagreement
- **先听**：01:42–02:14：mapperatorinator↔madmom 停差 局部 -1 拍（support = 24 matched measures）
- madmom↔BeatThis：局部错位后又合上（reconvergence）：错位 局部 +1 拍；有一处 +1.06 拍的跳变（这才是错位） @02:15，平时 +0.06 拍/分钟｜异常区段 02:00–02:13
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +1.02 拍 @01:57（一处≠一段：可能就是漏了一拍），平时 -0.01 拍/分钟
- mapperatorinator↔madmom：局部错位后又合上（reconvergence）：错位 局部 -1 拍；有一处 +1.00 拍的跳变（这才是错位） @01:42，平时 -0.10 拍/分钟｜异常区段 01:42–02:14
- 人那条：没有小节头按压

### new_140 — clean
- 人那条：没有小节头按压
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.007），这是它自己的规则，不是歌曲健康

### new_141 — persistent ±1-beat disagreement
- **先听**：00:24–01:06：mapperatorinator↔madmom 停差 局部 +1 拍（support = 22 matched measures）
- madmom↔BeatThis：有一头是错位的（局部 -1 拍 那端没回来）；有一处 +2.00 拍的跳变（这才是错位） @00:59，平时 -0.15 拍/分钟｜异常区段 00:47–00:57、00:59–01:05
- mapperatorinator↔BeatThis：有一头是错位的（局部 +1 拍 那端没回来）；有一处 +2.00 拍的跳变（这才是错位） @00:48，平时 -0.15 拍/分钟｜异常区段 00:24–00:34、00:38–00:44、00:50–00:58
- mapperatorinator↔madmom：两条小节长度略有出入：相位连续滑 -0.06 拍/分钟，最大跳变只有 0.10 拍（没有突变）｜异常区段 00:24–01:06
- 人那条：没有小节头按压
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.027），这是它自己的规则，不是歌曲健康

### new_142 — clean
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 3843 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.896），这是它自己的规则，不是歌曲健康

### new_143 — unresolved
- 人那条：没有小节头按压
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.076），这是它自己的规则，不是歌曲健康
- 机器读法之间没有一对能比较

### new_144 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +2.01 拍 @01:38（一处≠一段：可能就是漏了一拍），平时 +1.19 拍/分钟
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +2.00 拍 @00:43（一处≠一段：可能就是漏了一拍），平时 +0.26 拍/分钟
- madmom↔mapperatorinator：其余全段一致，只在这一处跳了 +1.10 拍 @00:51（一处≠一段：可能就是漏了一拍），平时 +0.02 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 6923 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @01:38、BeatThis↔mapperatorinator @00:43、madmom↔mapperatorinator @00:51

### new_145 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +2.00 拍 @04:22（一处≠一段：可能就是漏了一拍），平时 +0.03 拍/分钟
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +2.10 拍 @00:42（一处≠一段：可能就是漏了一拍），平时 -2.25 拍/分钟
- madmom↔mapperatorinator：其余全段一致，只在这一处跳了 +1.74 拍 @00:32（一处≠一段：可能就是漏了一拍），平时 -0.10 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 5418 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.890），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @04:22、BeatThis↔mapperatorinator @00:42、madmom↔mapperatorinator @00:32

### new_147 — clean
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +1.98 拍 @00:49（一处≠一段：可能就是漏了一拍），平时 -0.02 拍/分钟
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +1.89 拍 @00:51（一处≠一段：可能就是漏了一拍），平时 -2.20 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 3869 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.765），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：madmom↔BeatThis @00:49、mapperatorinator↔BeatThis @00:51

### new_148 — persistent ±1-beat disagreement
- **先听**：01:22–03:19：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 45 matched measures）；00:11–01:05：workbench↔madmom 停差 ±2 拍（半小节）（support = 21 matched measures）；03:43–04:29：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 18 matched measures）
- madmom↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.04 拍的跳变（这才是错位） @00:31，平时 -1.16 拍/分钟｜异常区段 00:13–00:29、02:11–02:27
- mapperatorinator↔madmom：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.92 拍的跳变（这才是错位） @04:34，平时 +0.65 拍/分钟｜异常区段 01:22–03:19、03:43–04:29
- workbench↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）, 局部 -1 拍；有一处 +2.01 拍的跳变（这才是错位） @00:30，平时 -0.65 拍/分钟｜异常区段 00:33–00:59、01:02–01:18、02:11–02:27
- workbench↔madmom：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.99 拍的跳变（这才是错位） @04:54，平时 +0.41 拍/分钟｜异常区段 00:11–01:05
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 3071 ms）——这是拍层的事，和小节相位是两回事

### new_149 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +0.96 拍 @00:15（一处≠一段：可能就是漏了一拍），平时 -0.01 拍/分钟
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +1.99 拍 @00:17（一处≠一段：可能就是漏了一拍），平时 -0.04 拍/分钟
- madmom↔mapperatorinator：其余全段一致，只在这一处跳了 +1.97 拍 @00:17（一处≠一段：可能就是漏了一拍），平时 +0.04 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 343 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.024），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @00:15、BeatThis↔mapperatorinator @00:17、madmom↔mapperatorinator @00:17

### new_150 — clean
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 3802 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.456），这是它自己的规则，不是歌曲健康

### new_152 — persistent ±1-beat disagreement
- **先听**：01:45–01:58：BeatThis↔madmom 停差 ±2 拍（半小节）（support = 7 matched measures）；01:07–01:17：BeatThis↔madmom 停差 ±2 拍（半小节）（support = 6 matched measures）；02:51–02:58：BeatThis↔madmom 停差 局部 -1 拍（support = 4 matched measures）
- BeatThis↔madmom：有一头是错位的（局部 -1 拍 那端没回来）；有一处 +2.35 拍的跳变（这才是错位） @01:45，平时 -1.72 拍/分钟｜异常区段 01:07–01:17、01:45–01:58、02:51–02:58
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +2.12 拍 @02:49（一处≠一段：可能就是漏了一拍），平时 +5.74 拍/分钟
- mapperatorinator↔madmom：其余全段一致，只在这一处跳了 +0.86 拍 @01:48（一处≠一段：可能就是漏了一拍），平时 -0.00 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2283 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.010），这是它自己的规则，不是歌曲健康

### new_153 — clean
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +1.99 拍 @01:12（一处≠一段：可能就是漏了一拍），平时 +1.27 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 3810 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.429），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：BeatThis↔mapperatorinator @01:12

### new_154 — persistent ±2-beat disagreement
- **先听**：02:52–03:01：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 9 matched measures）；03:03–03:10：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 7 matched measures）；00:03–00:12：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 5 matched measures）
- madmom↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.00 拍的跳变（这才是错位） @03:02，平时 -0.01 拍/分钟｜异常区段 02:52–03:01、03:03–03:10
- mapperatorinator↔BeatThis：有一头是错位的（局部 +1 拍 那端没回来）；有一处 +2.00 拍的跳变（这才是错位） @02:49，平时 -0.15 拍/分钟｜异常区段 00:03–00:08、00:12–00:17、02:52–03:01、03:03–03:10
- mapperatorinator↔madmom：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.06 拍的跳变（这才是错位） @00:17，平时 -0.07 拍/分钟｜异常区段 00:03–00:12
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 870 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.008），这是它自己的规则，不是歌曲健康

### new_155 — persistent ±1-beat disagreement
- **先听**：02:05–02:22：madmom↔BeatThis 停差 局部 +1 拍（support = 15 matched measures）；03:32–03:46：madmom↔BeatThis 停差 局部 +1 拍（support = 13 matched measures）；01:29–01:39：madmom↔BeatThis 停差 局部 +1 拍（support = 9 matched measures）
- madmom↔BeatThis：有一头是错位的（局部 +1 拍 那端没回来）；有一处 +1.98 拍的跳变（这才是错位） @03:32，平时 +0.86 拍/分钟｜异常区段 00:01–00:04、01:29–01:39、02:05–02:22、02:29–02:32、03:32–03:46、03:50–03:53
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 677 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.005），这是它自己的规则，不是歌曲健康

### new_156 — persistent ±2-beat disagreement
- **先听**：02:11–03:35：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 50 matched measures）
- BeatThis↔workbench：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.99 拍的跳变（这才是错位） @02:58，平时 -0.49 拍/分钟｜异常区段 02:58–03:36
- madmom↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.91 拍的跳变（这才是错位） @02:58，平时 +1.32 拍/分钟｜异常区段 02:13–02:44、02:48–02:56
- madmom↔workbench：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.03 拍的跳变（这才是错位） @02:08，平时 +0.81 拍/分钟｜异常区段 02:12–03:36
- mapperatorinator↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.97 拍的跳变（这才是错位） @02:59，平时 -0.49 拍/分钟｜异常区段 02:59–03:35
- mapperatorinator↔madmom：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.05 拍的跳变（这才是错位） @02:07，平时 -0.83 拍/分钟｜异常区段 02:11–03:35
- 人那条：没有小节头按压

### new_157 — clean
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +1.99 拍 @01:48（一处≠一段：可能就是漏了一拍），平时 +0.56 拍/分钟
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +1.97 拍 @01:46（一处≠一段：可能就是漏了一拍），平时 +0.71 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2287 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.019），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：madmom↔BeatThis @01:48、mapperatorinator↔BeatThis @01:46

### new_158 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +2.03 拍 @02:29（一处≠一段：可能就是漏了一拍），平时 -3.54 拍/分钟
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +1.98 拍 @02:03（一处≠一段：可能就是漏了一拍），平时 -3.49 拍/分钟
- mapperatorinator↔madmom：其余全段一致，只在这一处跳了 +0.85 拍 @03:08（一处≠一段：可能就是漏了一拍），平时 -0.01 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1360 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.103），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @02:29、BeatThis↔mapperatorinator @02:03、mapperatorinator↔madmom @03:08

### new_159 — persistent ±1-beat disagreement
- **先听**：02:16–02:28：BeatThis↔madmom 停差 局部 -1 拍（support = 8 matched measures）
- BeatThis↔madmom：局部错位后又合上（reconvergence）：错位 局部 -1 拍；有一处 +2.01 拍的跳变（这才是错位） @03:39，平时 +0.33 拍/分钟｜异常区段 02:16–02:28
- BeatThis↔mapperatorinator：局部错位后又合上（reconvergence）：错位 局部 -1 拍；有一处 +2.04 拍的跳变（这才是错位） @03:39，平时 +1.58 拍/分钟｜异常区段 02:16–02:28
- BeatThis↔workbench：局部错位后又合上（reconvergence）：错位 局部 -1 拍；有一处 +2.03 拍的跳变（这才是错位） @03:39，平时 +1.56 拍/分钟｜异常区段 02:16–02:28
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1036 ms）——这是拍层的事，和小节相位是两回事

### new_16 — persistent ±2-beat disagreement
- **先听**：02:33–03:13：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 16 matched measures）
- madmom↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.03 拍的跳变（这才是错位） @02:58，平时 +0.61 拍/分钟｜异常区段 02:18–02:56
- mapperatorinator↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.97 拍的跳变（这才是错位） @03:02，平时 -0.34 拍/分钟｜异常区段 03:02–03:13
- mapperatorinator↔madmom：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.53 拍的跳变（这才是错位） @02:33，平时 +0.83 拍/分钟｜异常区段 02:33–03:13
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2510 ms）——这是拍层的事，和小节相位是两回事

### new_17 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +2.02 拍 @01:05（一处≠一段：可能就是漏了一拍），平时 +0.63 拍/分钟
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +1.14 拍 @00:24（一处≠一段：可能就是漏了一拍），平时 -0.02 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2771 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @01:05、mapperatorinator↔BeatThis @00:24

### new_18 — persistent ±2-beat disagreement
- **先听**：01:27–02:22：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 31 matched measures）
- madmom↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.02 拍的跳变（这才是错位） @02:53，平时 +1.45 拍/分钟｜异常区段 01:59–02:21
- madmom↔workbench：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.97 拍的跳变（这才是错位） @01:26，平时 +0.26 拍/分钟｜异常区段 01:31–01:46、01:50–02:25
- mapperatorinator↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.00 拍的跳变（这才是错位） @01:36，平时 +0.54 拍/分钟｜异常区段 01:47–01:54
- mapperatorinator↔madmom：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.89 拍的跳变（这才是错位） @01:27，平时 -0.93 拍/分钟｜异常区段 01:27–02:22
- workbench↔BeatThis：其余全段一致，只在这一处跳了 +2.05 拍 @02:31（一处≠一段：可能就是漏了一拍），平时 -2.49 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1289 ms）——这是拍层的事，和小节相位是两回事

### new_19 — clean
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 3381 ms）——这是拍层的事，和小节相位是两回事

### new_20 — clean
- 人那条：没有小节头按压
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.011），这是它自己的规则，不是歌曲健康

### new_21 — persistent ±1-beat disagreement
- **先听**：04:43–05:28：workbench↔BeatThis 停差 ±2 拍（半小节）（support = 19 matched measures）；03:53–03:58：workbench↔mapperatorinator 停差 局部 +1 拍（support = 3 matched measures）
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +2.02 拍 @00:26（一处≠一段：可能就是漏了一拍），平时 +1.69 拍/分钟
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +2.00 拍 @01:28（一处≠一段：可能就是漏了一拍），平时 -0.01 拍/分钟
- madmom↔mapperatorinator：其余全段一致，只在这一处跳了 +1.97 拍 @05:29（一处≠一段：可能就是漏了一拍），平时 -0.02 拍/分钟
- madmom↔workbench：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.96 拍的跳变（这才是错位） @04:47，平时 -0.28 拍/分钟｜异常区段 04:47–05:29
- workbench↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.95 拍的跳变（这才是错位） @01:28，平时 +1.10 拍/分钟｜异常区段 04:43–05:28
- workbench↔mapperatorinator：局部错位后又合上（reconvergence）：错位 局部 +1 拍；有一处 +1.92 拍的跳变（这才是错位） @03:53，平时 -1.01 拍/分钟｜异常区段 03:53–03:58
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 5987 ms）——这是拍层的事，和小节相位是两回事

### new_22 — clean
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +1.99 拍 @02:29（一处≠一段：可能就是漏了一拍），平时 +0.02 拍/分钟
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +1.93 拍 @02:12（一处≠一段：可能就是漏了一拍），平时 +1.56 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 4036 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：madmom↔BeatThis @02:29、mapperatorinator↔BeatThis @02:12

### new_23 — persistent ±2-beat disagreement
- **先听**：02:02–02:29：madmom↔BeatThis 停差 ±2 拍（半小节）（support = 12 matched measures）
- BeatThis↔mapperatorinator：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.06 拍的跳变（这才是错位） @03:37，平时 +3.26 拍/分钟｜异常区段 02:01–02:25
- madmom↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.00 拍的跳变（这才是错位） @02:02，平时 -0.11 拍/分钟｜异常区段 02:02–02:29
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1525 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.005），这是它自己的规则，不是歌曲健康
- 疑似 BeatThis 2-beat counting：它自己报的小节里有 15 个只数了 2 拍 —— 待人工确认

### new_24 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +1.00 拍 @02:27（一处≠一段：可能就是漏了一拍），平时 -0.01 拍/分钟
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +1.88 拍 @02:22（一处≠一段：可能就是漏了一拍），平时 -1.62 拍/分钟
- mapperatorinator↔madmom：其余全段一致，只在这一处跳了 +2.08 拍 @02:10（一处≠一段：可能就是漏了一拍），平时 +4.97 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2595 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @02:27、BeatThis↔mapperatorinator @02:22、mapperatorinator↔madmom @02:10

### new_25 — persistent ±2-beat disagreement
- **先听**：02:30–03:28：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 30 matched measures）；01:42–02:24：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 22 matched measures）
- madmom↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.08 拍的跳变（这才是错位） @03:03，平时 +2.50 拍/分钟｜异常区段 01:49–01:57、02:07–02:13、02:15–02:35、02:45–02:55、03:03–03:31
- mapperatorinator↔madmom：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.93 拍的跳变（这才是错位） @01:40，平时 -0.90 拍/分钟｜异常区段 01:42–02:24、02:30–03:28
- 人那条：没有小节头按压
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.028），这是它自己的规则，不是歌曲健康

### new_26 — persistent ±2-beat disagreement
- **先听**：02:56–03:35：mapperatorinator↔workbench 停差 ±2 拍（半小节）（support = 17 matched measures）；02:34–02:46：BeatThis↔workbench 停差 ±2 拍（半小节）（support = 6 matched measures）；00:22–00:27：BeatThis↔madmom 停差 ±2 拍（半小节）（support = 3 matched measures）
- BeatThis↔madmom：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.11 拍的跳变（这才是错位） @00:30，平时 -2.14 拍/分钟｜异常区段 00:22–00:27、02:34–02:44
- BeatThis↔workbench：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.05 拍的跳变（这才是错位） @00:30，平时 -1.10 拍/分钟｜异常区段 00:22–00:27、02:34–02:46、02:51–03:25
- madmom↔workbench：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.01 拍的跳变（这才是错位） @03:34，平时 +0.36 拍/分钟｜异常区段 02:54–03:30
- mapperatorinator↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.94 拍的跳变（这才是错位） @03:28，平时 -0.87 拍/分钟｜异常区段 00:23–00:28、03:30–03:35
- mapperatorinator↔madmom：其余全段一致，只在这一处跳了 +1.25 拍 @03:39（一处≠一段：可能就是漏了一拍），平时 +0.02 拍/分钟
- mapperatorinator↔workbench：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.02 拍的跳变（这才是错位） @03:39，平时 +0.47 拍/分钟｜异常区段 02:56–03:35
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1613 ms）——这是拍层的事，和小节相位是两回事

### new_27 — persistent ±2-beat disagreement
- **先听**：00:12–02:10：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 60 matched measures）；02:16–03:00：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 23 matched measures）
- madmom↔BeatThis：整段都对不上相位（几条关系轮着来）；有一处 +0.98 拍的跳变（这才是错位） @03:01，平时 +0.02 拍/分钟｜异常区段 00:07–00:57、00:59–01:05、01:07–01:11、01:27–01:31、01:45–01:49、01:57–02:01、02:03–02:09、02:15–02:21、02:27–02:31、02:35–02:41、02:45–02:53
- mapperatorinator↔madmom：全段固定差 ±2 拍（半小节）（整体相位差，不是局部错位）；不滑（-0.01 拍/分钟，最大跳变 0.12 拍）｜异常区段 00:12–02:10、02:16–03:00
- 人那条：没有小节头按压

### new_28 — persistent ±1-beat disagreement
- **先听**：00:08–00:47：madmom↔mapperatorinator 停差 局部 -1 拍（support = 21 matched measures）
- madmom↔mapperatorinator：有一头是错位的（局部 -1 拍 那端没回来）；有一处 +0.99 拍的跳变（这才是错位） @00:49，平时 +0.29 拍/分钟｜异常区段 00:08–00:47
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +1.00 拍 @00:30（一处≠一段：可能就是漏了一拍），平时 -0.01 拍/分钟
- 人那条：没有小节头按压

### new_29 — clean
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +0.98 拍 @01:47（一处≠一段：可能就是漏了一拍），平时 -0.00 拍/分钟
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +1.05 拍 @01:45（一处≠一段：可能就是漏了一拍），平时 -0.00 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 407 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.020），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：madmom↔BeatThis @01:47、mapperatorinator↔BeatThis @01:45

### new_30 — clean
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 408 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.020），这是它自己的规则，不是歌曲健康

### new_31 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +2.02 拍 @02:27（一处≠一段：可能就是漏了一拍），平时 +1.82 拍/分钟
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +1.87 拍 @02:24（一处≠一段：可能就是漏了一拍），平时 +0.01 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1169 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @02:27、mapperatorinator↔BeatThis @02:24

### new_32 — clean
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +1.88 拍 @02:20（一处≠一段：可能就是漏了一拍），平时 +0.02 拍/分钟
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +1.98 拍 @02:20（一处≠一段：可能就是漏了一拍），平时 +0.01 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 279 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：madmom↔BeatThis @02:20、mapperatorinator↔BeatThis @02:20

### new_33 — clean
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +1.97 拍 @02:15（一处≠一段：可能就是漏了一拍），平时 +0.05 拍/分钟
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +1.99 拍 @02:15（一处≠一段：可能就是漏了一拍），平时 +0.05 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 881 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：madmom↔BeatThis @02:15、mapperatorinator↔BeatThis @02:15

### new_34 — persistent ±2-beat disagreement
- **先听**：00:02–03:21：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 107 matched measures）
- madmom↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.97 拍的跳变（这才是错位） @01:29，平时 -0.82 拍/分钟｜异常区段 00:01–00:31、00:35–00:39、00:42–01:27
- mapperatorinator↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.96 拍的跳变（这才是错位） @01:30，平时 -0.87 拍/分钟｜异常区段 01:30–03:21
- mapperatorinator↔madmom：全段固定差 ±2 拍（半小节）（整体相位差，不是局部错位）；不滑（-0.00 拍/分钟，最大跳变 0.05 拍）｜异常区段 00:02–03:21
- mapperatorinator↔workbench：全段固定差 ±2 拍（半小节）（整体相位差，不是局部错位）；不滑（-0.00 拍/分钟，最大跳变 0.04 拍）｜异常区段 00:02–03:21
- workbench↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.94 拍的跳变（这才是错位） @01:29，平时 -0.79 拍/分钟｜异常区段 00:01–00:09、00:12–01:01、01:05–01:24
- 人那条：没有小节头按压

### new_35 — persistent ±2-beat disagreement
- **先听**：01:59–02:03：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 3 matched measures）
- mapperatorinator↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.00 拍的跳变（这才是错位） @02:05，平时 -0.07 拍/分钟｜异常区段 01:59–02:03
- mapperatorinator↔madmom：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.97 拍的跳变（这才是错位） @02:05，平时 -0.07 拍/分钟｜异常区段 01:59–02:03
- 人那条：没有小节头按压

### new_36 — clean
- BeatThis↔workbench：其余全段一致，只在这一处跳了 +0.97 拍 @00:03（一处≠一段：可能就是漏了一拍），平时 +0.13 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 592 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.667），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：BeatThis↔workbench @00:03

### new_37 — clean
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2853 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.892），这是它自己的规则，不是歌曲健康

### new_38 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +1.06 拍 @00:20（一处≠一段：可能就是漏了一拍），平时 +0.01 拍/分钟
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +1.04 拍 @00:23（一处≠一段：可能就是漏了一拍），平时 +0.01 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2580 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.093），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @00:20、BeatThis↔mapperatorinator @00:23

### new_39 — persistent ±1-beat disagreement
- **先听**：00:02–01:23：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 50 matched measures）；01:27–02:17：mapperatorinator↔madmom 停差 局部 -1 拍（support = 31 matched measures）；02:22–03:00：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 24 matched measures）
- mapperatorinator↔madmom：整段都对不上相位（几条关系轮着来）；有一处 +1.03 拍的跳变（这才是错位） @01:27，平时 +0.14 拍/分钟｜异常区段 00:02–01:23、01:27–02:17、02:22–03:00
- 人那条：没有小节头按压

### new_40 — clean
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +1.00 拍 @01:55（一处≠一段：可能就是漏了一拍），平时 -0.01 拍/分钟
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +0.99 拍 @01:58（一处≠一段：可能就是漏了一拍），平时 -0.01 拍/分钟
- 人那条：没有小节头按压
- 单点跳变（没持续成一段，先记着）：madmom↔BeatThis @01:55、mapperatorinator↔BeatThis @01:58

### new_42 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +1.99 拍 @00:33（一处≠一段：可能就是漏了一拍），平时 +0.02 拍/分钟
- 人那条：没有小节头按压
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.004），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @00:33

### new_43 — persistent ±2-beat disagreement
- **先听**：02:01–02:13：BeatThis↔mapperatorinator 停差 ±2 拍（半小节）（support = 6 matched measures）；02:22–02:29：madmom↔BeatThis 停差 ±2 拍（半小节）（support = 4 matched measures）
- BeatThis↔mapperatorinator：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.02 拍的跳变（这才是错位） @02:40，平时 +1.81 拍/分钟｜异常区段 02:01–02:13、02:20–02:25
- madmom↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.00 拍的跳变（这才是错位） @02:19，平时 +0.02 拍/分钟｜异常区段 02:02–02:12、02:22–02:29
- madmom↔mapperatorinator：其余全段一致，只在这一处跳了 +1.98 拍 @02:40（一处≠一段：可能就是漏了一拍），平时 +0.02 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1400 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.009），这是它自己的规则，不是歌曲健康
- 疑似 BeatThis 2-beat counting：它自己报的小节里有 9 个只数了 2 拍 —— 待人工确认

### new_44 — clean
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +1.92 拍 @02:12（一处≠一段：可能就是漏了一拍），平时 +1.55 拍/分钟
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +1.93 拍 @02:12（一处≠一段：可能就是漏了一拍），平时 -1.53 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 4036 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：madmom↔BeatThis @02:12、mapperatorinator↔BeatThis @02:12

### new_45 — persistent ±1-beat disagreement
- **先听**：02:43–03:29：madmom↔workbench 停差 局部 -1 拍（support = 33 matched measures）
- madmom↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.01 拍的跳变（这才是错位） @01:37，平时 +0.25 拍/分钟｜异常区段 02:47–02:56、03:06–03:09、03:12–03:29
- madmom↔workbench：有一头是错位的（局部 -1 拍 那端没回来）；有一处 +1.00 拍的跳变（这才是错位） @02:35，平时 +1.30 拍/分钟｜异常区段 02:43–03:29
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +1.98 拍 @01:34（一处≠一段：可能就是漏了一拍），平时 -0.03 拍/分钟
- mapperatorinator↔madmom：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.80 拍的跳变（这才是错位） @02:46，平时 -0.66 拍/分钟｜异常区段 02:46–03:30
- mapperatorinator↔workbench：有一头是错位的（局部 +1 拍 那端没回来）；有一处 +1.49 拍的跳变（这才是错位） @02:46，平时 +1.78 拍/分钟｜异常区段 02:46–03:30
- workbench↔BeatThis：有一头是错位的（局部 -1 拍 那端没回来）；有一处 +1.97 拍的跳变（这才是错位） @02:58，平时 -0.43 拍/分钟｜异常区段 02:45–02:56、02:58–03:01、03:02–03:29
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 4084 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.866），这是它自己的规则，不是歌曲健康

### new_47 — clean
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2016 ms）——这是拍层的事，和小节相位是两回事

### new_48 — persistent ±2-beat disagreement
- **先听**：03:12–04:20：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 24 matched measures）
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +2.00 拍 @01:02（一处≠一段：可能就是漏了一拍），平时 -0.03 拍/分钟
- mapperatorinator↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.03 拍的跳变（这才是错位） @00:21，平时 +0.65 拍/分钟｜异常区段 03:12–04:20
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2767 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.895），这是它自己的规则，不是歌曲健康
- 疑似 BeatThis 2-beat counting：它自己报的小节里有 6 个只数了 2 拍 —— 待人工确认

### new_49 — persistent ±2-beat disagreement
- **先听**：01:59–02:03：BeatThis↔madmom 停差 ±2 拍（半小节）（support = 4 matched measures）
- BeatThis↔madmom：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.97 拍的跳变（这才是错位） @01:59，平时 -0.01 拍/分钟｜异常区段 01:59–02:03
- BeatThis↔workbench：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.98 拍的跳变（这才是错位） @01:59，平时 -0.01 拍/分钟｜异常区段 01:59–02:03
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1922 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.830），这是它自己的规则，不是歌曲健康

### new_50 — continuous slide
- **先听**：03:05–03:17：BeatThis↔workbench 停差 局部 +1 拍（support = 5 matched measures）；02:09–02:19：BeatThis↔workbench 停差 局部 +1 拍（support = 3 matched measures）
- BeatThis↔workbench：有一头是错位的（局部 +1 拍 那端没回来）；有一处 +1.98 拍的跳变（这才是错位） @00:58，平时 -1.16 拍/分钟｜异常区段 02:09–02:19、03:05–03:17
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +1.76 拍 @01:48（一处≠一段：可能就是漏了一拍），平时 -0.00 拍/分钟
- 人那条：没有小节头按压
- BeatThis↔workbench：2 段错位、k 走遍 +1、趋势 -1.16 拍/分钟、残余悬在中间 —— 这是相位滑过整数拍（两条小节长度不同），不是停错在某一格
- A 层：Beat This 的拍序列不能被一条直线描述（残差 737 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.653），这是它自己的规则，不是歌曲健康

### new_51 — clean
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +1.00 拍 @02:45（一处≠一段：可能就是漏了一拍），平时 -0.01 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 3017 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：madmom↔BeatThis @02:45

### new_52 — persistent ±1-beat disagreement
- **先听**：00:07–01:57：madmom↔BeatThis 停差 局部 +1 拍（support = 56 matched measures）；02:01–02:59：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 30 matched measures）
- madmom↔BeatThis：有一头是错位的（局部 +1 拍 那端没回来）；有一处 +0.76 拍的跳变（这才是错位） @01:59，平时 -0.06 拍/分钟｜异常区段 00:07–01:57、02:15–03:01
- mapperatorinator↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.94 拍的跳变（这才是错位） @02:01，平时 -1.03 拍/分钟｜异常区段 02:01–02:59
- mapperatorinator↔madmom：整段都对不上相位（几条关系轮着来）；有一处 +0.92 拍的跳变（这才是错位） @02:15，平时 -1.01 拍/分钟｜异常区段 00:21–01:56、02:01–02:09、02:15–03:01
- 人那条：没有小节头按压
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.036），这是它自己的规则，不是歌曲健康

### new_53 — persistent ±1-beat disagreement
- **先听**：00:08–00:45：madmom↔workbench 停差 局部 -1 拍（support = 20 matched measures）
- madmom↔workbench：有一头是错位的（局部 -1 拍 那端没回来）；有一处 +0.99 拍的跳变（这才是错位） @00:47，平时 +0.28 拍/分钟｜异常区段 00:08–00:45
- mapperatorinator↔BeatThis：局部错位后又合上（reconvergence）：错位 局部 +1 拍；有一处 +1.00 拍的跳变（这才是错位） @00:34，平时 -0.06 拍/分钟｜异常区段 00:24–00:28
- mapperatorinator↔madmom：有一头是错位的（局部 +1 拍 那端没回来）；有一处 +0.98 拍的跳变（这才是错位） @00:47，平时 -0.28 拍/分钟｜异常区段 00:11–00:45
- workbench↔BeatThis：局部错位后又合上（reconvergence）：错位 局部 +1 拍；有一处 +1.00 拍的跳变（这才是错位） @00:32，平时 -0.05 拍/分钟｜异常区段 00:24–00:28
- 人那条：没有小节头按压

### new_54 — persistent ±2-beat disagreement
- **先听**：00:02–02:45：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 88 matched measures）
- madmom↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.93 拍的跳变（这才是错位） @01:25，平时 +0.78 拍/分钟｜异常区段 00:01–00:33、00:42–00:48、00:52–01:18
- mapperatorinator↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.97 拍的跳变（这才是错位） @01:30，平时 -0.35 拍/分钟｜异常区段 01:30–02:28、02:32–02:45
- mapperatorinator↔madmom：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.97 拍的跳变（这才是错位） @02:48，平时 +0.53 拍/分钟｜异常区段 00:02–02:45
- mapperatorinator↔workbench：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.96 拍的跳变（这才是错位） @02:48，平时 +0.53 拍/分钟｜异常区段 00:02–02:45
- workbench↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.92 拍的跳变（这才是错位） @01:25，平时 +0.79 拍/分钟｜异常区段 00:01–00:05、00:09–00:12、00:16–00:20、00:25–00:29、00:33–00:44、00:48–00:52、00:55–00:59、01:01–01:05、01:10–01:14、01:18–01:22
- 人那条：没有小节头按压

### new_55 — persistent ±1-beat disagreement
- **先听**：02:38–02:58：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 9 matched measures）；01:23–01:27：madmom↔BeatThis 停差 ±2 拍（半小节）（support = 4 matched measures）；01:53–01:58：mapperatorinator↔BeatThis 停差 局部 +1 拍（support = 3 matched measures）
- madmom↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）, 局部 -1 拍；有一处 +1.97 拍的跳变（这才是错位） @01:21，平时 -0.06 拍/分钟｜异常区段 01:23–01:27、03:32–03:34
- mapperatorinator↔BeatThis：局部错位后又合上（reconvergence）：错位 局部 +1 拍, ±2 拍（半小节）；有一处 +1.00 拍的跳变（这才是错位） @01:59，平时 -0.09 拍/分钟｜异常区段 01:53–01:58、02:38–02:58
- mapperatorinator↔madmom：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.99 拍的跳变（这才是错位） @03:03，平时 +0.15 拍/分钟｜异常区段 02:38–02:55
- 人那条：没有小节头按压
- mapperatorinator↔BeatThis：2 段错位、k 走遍 -2+1、趋势 -0.09 拍/分钟、残余悬在中间 —— 这是相位滑过整数拍（两条小节长度不同），不是停错在某一格
- A 层：Beat This 的拍序列不能被一条直线描述（残差 6422 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.153），这是它自己的规则，不是歌曲健康

### new_56 — clean
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +1.09 拍 @03:16（一处≠一段：可能就是漏了一拍），平时 +0.02 拍/分钟
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +1.08 拍 @01:39（一处≠一段：可能就是漏了一拍），平时 +0.00 拍/分钟
- 人那条：没有小节头按压
- 单点跳变（没持续成一段，先记着）：madmom↔BeatThis @03:16、mapperatorinator↔BeatThis @01:39

### new_57 — persistent ±2-beat disagreement
- **先听**：00:02–01:16：mapperatorinator↔workbench 停差 ±2 拍（半小节）（support = 33 matched measures）；01:18–01:53：madmom↔mapperatorinator 停差 ±2 拍（半小节）（support = 16 matched measures）；02:35–02:51：BeatThis↔workbench 停差 ±2 拍（半小节）（support = 6 matched measures）
- BeatThis↔mapperatorinator：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.19 拍的跳变（这才是错位） @01:55，平时 -3.58 拍/分钟｜异常区段 00:31–00:59、01:06–01:15
- BeatThis↔workbench：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.10 拍的跳变（这才是错位） @02:35，平时 -1.72 拍/分钟｜异常区段 00:07–00:21、02:35–02:51
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +1.83 拍 @02:27（一处≠一段：可能就是漏了一拍），平时 +1.39 拍/分钟
- madmom↔mapperatorinator：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.04 拍的跳变（这才是错位） @01:56，平时 +0.66 拍/分钟｜异常区段 01:18–01:53
- madmom↔workbench：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.64 拍的跳变（这才是错位） @02:35，平时 -0.50 拍/分钟｜异常区段 02:58–03:07
- mapperatorinator↔workbench：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.00 拍的跳变（这才是错位） @02:30，平时 -0.25 拍/分钟｜异常区段 00:02–01:16
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 4775 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.500），这是它自己的规则，不是歌曲健康

### new_58 — clean
- 人那条：没有小节头按压
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.009），这是它自己的规则，不是歌曲健康

### new_59 — persistent ±2-beat disagreement
- **先听**：00:04–01:35：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 45 matched measures）
- madmom↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.94 拍的跳变（这才是错位） @01:42，平时 +0.72 拍/分钟｜异常区段 00:03–00:09、00:13–01:37
- mapperatorinator↔madmom：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.00 拍的跳变（这才是错位） @01:40，平时 +0.88 拍/分钟｜异常区段 00:04–01:35
- 人那条：没有小节头按压

### new_60 — persistent ±2-beat disagreement
- **先听**：01:00–02:24：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 43 matched measures）；02:32–03:34：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 32 matched measures）；00:10–00:52：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 22 matched measures）
- madmom↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.02 拍的跳变（这才是错位） @00:57，平时 +0.60 拍/分钟｜异常区段 00:09–00:15、00:17–00:29、00:33–00:47、00:51–00:55、01:31–01:49、01:51–01:59、02:09–02:13、02:21–02:37、02:43–02:57
- mapperatorinator↔madmom：整段都对不上相位（几条关系轮着来）；不滑（-0.00 拍/分钟，最大跳变 0.09 拍）｜异常区段 00:10–00:52、00:54–00:58、01:00–02:24、02:26–02:30、02:32–03:34
- 人那条：没有小节头按压
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.023），这是它自己的规则，不是歌曲健康

### new_61 — persistent ±2-beat disagreement
- **先听**：03:00–03:03：BeatThis↔madmom 停差 ±2 拍（半小节）（support = 3 matched measures）
- BeatThis↔madmom：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.99 拍的跳变（这才是错位） @02:53，平时 +0.14 拍/分钟｜异常区段 03:00–03:03
- BeatThis↔mapperatorinator：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.01 拍的跳变（这才是错位） @02:53，平时 -0.62 拍/分钟｜异常区段 03:00–03:03
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2474 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.014），这是它自己的规则，不是歌曲健康
- 疑似 BeatThis 2-beat counting：它自己报的小节里有 111 个只数了 2 拍 —— 待人工确认

### new_62 — persistent ±2-beat disagreement
- **先听**：02:56–03:35：mapperatorinator↔workbench 停差 ±2 拍（半小节）（support = 17 matched measures）；02:34–02:46：BeatThis↔workbench 停差 ±2 拍（半小节）（support = 6 matched measures）；00:19–00:29：BeatThis↔madmom 停差 ±2 拍（半小节）（support = 5 matched measures）
- BeatThis↔madmom：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.00 拍的跳变（这才是错位） @00:30，平时 -0.06 拍/分钟｜异常区段 00:19–00:29、02:34–02:44
- BeatThis↔workbench：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.97 拍的跳变（这才是错位） @00:30，平时 +1.34 拍/分钟｜异常区段 00:19–00:29、02:34–02:46、02:51–03:28
- madmom↔workbench：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.02 拍的跳变（这才是错位） @03:34，平时 +0.38 拍/分钟｜异常区段 02:53–03:18、03:23–03:30
- mapperatorinator↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.07 拍的跳变（这才是错位） @03:39，平时 +1.49 拍/分钟｜异常区段 00:23–00:28、03:30–03:35
- mapperatorinator↔madmom：其余全段一致，只在这一处跳了 +3.06 拍 @02:36（一处≠一段：可能就是漏了一拍），平时 +1.41 拍/分钟
- mapperatorinator↔workbench：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.77 拍的跳变（这才是错位） @02:36，平时 -1.02 拍/分钟｜异常区段 02:56–03:35
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1929 ms）——这是拍层的事，和小节相位是两回事

### new_63 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +2.01 拍 @01:00（一处≠一段：可能就是漏了一拍），平时 -3.49 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 3356 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @01:00

### new_64 — persistent ±1-beat disagreement
- **先听**：00:20–00:27：mapperatorinator↔BeatThis 停差 局部 -1 拍（support = 5 matched measures）
- BeatThis↔madmom：局部错位后又合上（reconvergence）：错位 局部 +1 拍；有一处 +1.05 拍的跳变（这才是错位） @00:20，平时 -0.05 拍/分钟｜异常区段 00:20–00:28
- mapperatorinator↔BeatThis：局部错位后又合上（reconvergence）：错位 局部 -1 拍；有一处 +1.02 拍的跳变（这才是错位） @00:31，平时 +0.05 拍/分钟｜异常区段 00:20–00:27
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2723 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.064），这是它自己的规则，不是歌曲健康

### new_66 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +1.98 拍 @02:27（一处≠一段：可能就是漏了一拍），平时 -1.82 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1773 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @02:27

### new_67 — persistent ±2-beat disagreement
- **先听**：02:58–03:02：workbench↔BeatThis 停差 ±2 拍（半小节）（support = 4 matched measures）
- madmom↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.98 拍的跳变（这才是错位） @02:12，平时 -2.18 拍/分钟｜异常区段 02:59–03:03
- mapperatorinator↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.95 拍的跳变（这才是错位） @03:05，平时 -2.18 拍/分钟｜异常区段 02:59–03:03
- workbench↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.99 拍的跳变（这才是错位） @03:05，平时 -0.13 拍/分钟｜异常区段 02:58–03:02
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1464 ms）——这是拍层的事，和小节相位是两回事
- 疑似 BeatThis 2-beat counting：它自己报的小节里有 22 个只数了 2 拍 —— 待人工确认

### new_68 — persistent ±2-beat disagreement
- **先听**：00:47–01:35：madmom↔mapperatorinator 停差 ±2 拍（半小节）（support = 22 matched measures）；03:15–03:20：BeatThis↔madmom 停差 ±2 拍（半小节）（support = 3 matched measures）；03:22–03:27：BeatThis↔madmom 停差 ±2 拍（半小节）（support = 3 matched measures）
- BeatThis↔madmom：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.13 拍的跳变（这才是错位） @02:29，平时 +1.10 拍/分钟｜异常区段 03:15–03:20、03:22–03:27
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +2.17 拍 @02:31（一处≠一段：可能就是漏了一拍），平时 -1.30 拍/分钟
- madmom↔mapperatorinator：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.04 拍的跳变（这才是错位） @00:15，平时 -2.53 拍/分钟｜异常区段 00:47–01:35
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1271 ms）——这是拍层的事，和小节相位是两回事

### new_69 — persistent ±1-beat disagreement
- **先听**：00:01–00:08：madmom↔BeatThis 停差 局部 +1 拍（support = 4 matched measures）；02:52–02:54：madmom↔BeatThis 停差 ±2 拍（半小节）（support = 3 matched measures）；02:55–02:58：madmom↔BeatThis 停差 ±2 拍（半小节）（support = 3 matched measures）
- madmom↔BeatThis：有一头是错位的（局部 +1 拍 那端没回来）；有一处 +2.00 拍的跳变（这才是错位） @02:59，平时 -0.04 拍/分钟｜异常区段 00:01–00:08、02:52–02:54、02:55–02:58
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 413 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.004），这是它自己的规则，不是歌曲健康

### new_70 — persistent ±2-beat disagreement
- **先听**：02:57–03:51：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 20 matched measures）；04:36–05:21：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 16 matched measures）；04:05–04:25：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 8 matched measures）
- madmom↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.95 拍的跳变（这才是错位） @02:57，平时 -1.09 拍/分钟｜异常区段 02:57–03:51
- mapperatorinator↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.96 拍的跳变（这才是错位） @02:57，平时 +0.60 拍/分钟｜异常区段 02:57–03:51、04:05–04:25、04:36–05:21
- mapperatorinator↔madmom：其余全段一致，只在这一处跳了 +1.80 拍 @03:59（一处≠一段：可能就是漏了一拍），平时 +1.02 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2615 ms）——这是拍层的事，和小节相位是两回事

### new_71 — persistent ±1-beat disagreement
- **先听**：02:22–02:27：BeatThis↔madmom 停差 局部 -1 拍（support = 3 matched measures）
- BeatThis↔madmom：局部错位后又合上（reconvergence）：错位 局部 -1 拍；有一处 +2.13 拍的跳变（这才是错位） @01:48，平时 +1.64 拍/分钟｜异常区段 02:22–02:27
- BeatThis↔mapperatorinator：局部错位后又合上（reconvergence）：错位 局部 -1 拍；有一处 +2.13 拍的跳变（这才是错位） @01:48，平时 +1.63 拍/分钟｜异常区段 02:22–02:27
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 4846 ms）——这是拍层的事，和小节相位是两回事

### new_72 — clean
- **先听**：03:07–03:16：madmom↔BeatThis 停差 局部 -1 拍（support = 5 matched measures）
- madmom↔BeatThis：有一头是错位的（局部 -1 拍 那端没回来）；有一处 +2.00 拍的跳变（这才是错位） @02:07，平时 +1.73 拍/分钟｜异常区段 03:07–03:16
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +1.97 拍 @02:07（一处≠一段：可能就是漏了一拍），平时 +1.82 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 794 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.029），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：mapperatorinator↔BeatThis @02:07

### new_73 — persistent ±2-beat disagreement
- **先听**：00:03–00:17：mapperatorinator↔BeatThis 停差 局部 +1 拍（support = 7 matched measures）
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +2.00 拍 @02:55（一处≠一段：可能就是漏了一拍），平时 +0.01 拍/分钟
- mapperatorinator↔BeatThis：有一头是错位的（局部 +1 拍 那端没回来）；有一处 +1.96 拍的跳变（这才是错位） @02:56，平时 -1.46 拍/分钟｜异常区段 00:03–00:17
- mapperatorinator↔madmom：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.29 拍的跳变（这才是错位） @00:23，平时 -0.11 拍/分钟｜异常区段 00:03–00:17
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2526 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.003），这是它自己的规则，不是歌曲健康

### new_74 — persistent ±1-beat disagreement
- **先听**：01:26–02:26：mapperatorinator↔workbench 停差 ±2 拍（半小节）（support = 47 matched measures）；00:45–00:58：BeatThis↔madmom 停差 局部 -1 拍（support = 11 matched measures）；00:12–00:19：BeatThis↔madmom 停差 ±2 拍（半小节）（support = 6 matched measures）
- BeatThis↔madmom：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.01 拍的跳变（这才是错位） @00:23，平时 -0.71 拍/分钟｜异常区段 00:12–00:19、00:45–00:58、01:29–01:43、01:59–02:05
- BeatThis↔mapperatorinator：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.05 拍的跳变（这才是错位） @02:27，平时 +3.10 拍/分钟｜异常区段 01:26–01:28、01:54–01:58
- BeatThis↔workbench：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.12 拍的跳变（这才是错位） @02:27，平时 +5.09 拍/分钟｜异常区段 00:12–00:19、00:45–00:58、01:29–01:45、01:59–02:25
- mapperatorinator↔madmom：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）, 局部 +1 拍；有一处 +2.00 拍的跳变（这才是错位） @01:26，平时 +0.61 拍/分钟｜异常区段 01:26–02:04、02:53–02:58
- mapperatorinator↔workbench：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）, 局部 +1 拍；有一处 +1.95 拍的跳变（这才是错位） @01:26，平时 -1.56 拍/分钟｜异常区段 01:26–02:26、02:53–02:58
- 人那条：没有小节头按压
- BeatThis↔mapperatorinator：2 段错位、k 走遍 -2、趋势 +3.10 拍/分钟、残余悬在中间 —— 这是相位滑过整数拍（两条小节长度不同），不是停错在某一格
- mapperatorinator↔madmom：2 段错位、k 走遍 +1+2、趋势 +0.61 拍/分钟、残余悬在中间 —— 这是相位滑过整数拍（两条小节长度不同），不是停错在某一格
- A 层：Beat This 的拍序列不能被一条直线描述（残差 7628 ms）——这是拍层的事，和小节相位是两回事

### new_75 — persistent ±2-beat disagreement
- **先听**：02:58–03:35：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 23 matched measures）
- madmom↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.98 拍的跳变（这才是错位） @03:30，平时 -0.73 拍/分钟｜异常区段 03:02–03:11、03:14–03:21、03:31–03:35
- mapperatorinator↔madmom：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.92 拍的跳变（这才是错位） @02:58，平时 +0.51 拍/分钟｜异常区段 02:58–03:35
- mapperatorinator↔workbench：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.94 拍的跳变（这才是错位） @02:58，平时 +0.51 拍/分钟｜异常区段 02:58–03:35
- workbench↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.95 拍的跳变（这才是错位） @02:59，平时 -0.43 拍/分钟｜异常区段 02:59–03:21、03:29–03:36
- 人那条：没有小节头按压
- 疑似 BeatThis 2-beat counting：它自己报的小节里有 5 个只数了 2 拍 —— 待人工确认

### new_76 — persistent ±1-beat disagreement
- **先听**：00:43–01:39：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 40 matched measures）；00:08–00:42：mapperatorinator↔madmom 停差 局部 +1 拍（support = 25 matched measures）
- madmom↔BeatThis：有一头是错位的（局部 -1 拍 那端没回来）；有一处 +1.02 拍的跳变（这才是错位） @02:00，平时 -0.84 拍/分钟｜异常区段 00:08–00:40、00:44–00:53、00:55–01:00、01:04–01:21、01:22–01:28
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +1.01 拍 @01:59（一处≠一段：可能就是漏了一拍），平时 +0.00 拍/分钟
- mapperatorinator↔madmom：有一头是错位的（局部 +1 拍 那端没回来）；有一处 +0.94 拍的跳变（这才是错位） @01:43，平时 +0.87 拍/分钟｜异常区段 00:08–00:42、00:43–01:39
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1258 ms）——这是拍层的事，和小节相位是两回事

### new_77 — clean
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1210 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.011），这是它自己的规则，不是歌曲健康

### new_78 — persistent ±1-beat disagreement
- **先听**：00:02–00:59：mapperatorinator↔madmom 停差 局部 +1 拍（support = 31 matched measures）；01:24–02:00：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 20 matched measures）；02:46–03:09：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 13 matched measures）
- madmom↔BeatThis：有一头是错位的（局部 +1 拍 那端没回来）；有一处 +1.95 拍的跳变（这才是错位） @00:59，平时 -0.38 拍/分钟｜异常区段 00:02–00:55
- mapperatorinator↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.02 拍的跳变（这才是错位） @02:27，平时 +0.86 拍/分钟｜异常区段 02:04–02:25、02:29–02:42、02:46–03:09
- mapperatorinator↔madmom：有一头是错位的（局部 +1 拍 那端没回来）；有一处 +1.54 拍的跳变（这才是错位） @02:22，平时 +1.24 拍/分钟｜异常区段 00:02–00:59、01:24–02:00
- 人那条：没有小节头按压

### new_79 — persistent ±1-beat disagreement
- **先听**：00:30–00:43：workbench↔BeatThis 停差 ±2 拍（半小节）（support = 11 matched measures）；02:47–02:49：workbench↔BeatThis 停差 局部 +1 拍（support = 3 matched measures）
- madmom↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）, 局部 +1 拍；有一处 +2.00 拍的跳变（这才是错位） @00:47，平时 +0.01 拍/分钟｜异常区段 00:30–00:43、02:47–02:49
- mapperatorinator↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）, 局部 +1 拍；有一处 +1.98 拍的跳变（这才是错位） @00:44，平时 -0.74 拍/分钟｜异常区段 00:30–00:43、02:47–02:49
- workbench↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）, 局部 +1 拍；有一处 +1.97 拍的跳变（这才是错位） @00:44，平时 -0.86 拍/分钟｜异常区段 00:30–00:43、02:47–02:49
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2792 ms）——这是拍层的事，和小节相位是两回事

### new_80 — persistent ±2-beat disagreement
- **先听**：01:46–02:28：BeatThis↔madmom 停差 ±2 拍（半小节）（support = 21 matched measures）；01:01–01:18：BeatThis↔madmom 停差 ±2 拍（半小节）（support = 9 matched measures）；02:40–02:48：mapperatorinator↔BeatThis 停差 局部 +1 拍（support = 5 matched measures）
- BeatThis↔madmom：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.12 拍的跳变（这才是错位） @01:01，平时 -2.68 拍/分钟｜异常区段 01:01–01:18、01:46–02:28
- mapperatorinator↔BeatThis：局部错位后又合上（reconvergence）：错位 局部 +1 拍；有一处 +1.97 拍的跳变（这才是错位） @02:56，平时 -0.02 拍/分钟｜异常区段 02:40–02:48
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2713 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.010），这是它自己的规则，不是歌曲健康
- 疑似 BeatThis 2-beat counting：它自己报的小节里有 26 个只数了 2 拍 —— 待人工确认

### new_81 — persistent ±1-beat disagreement
- **先听**：04:04–04:46：madmom↔workbench 停差 局部 +1 拍（support = 31 matched measures）；05:11–05:22：madmom↔workbench 停差 ±2 拍（半小节）（support = 9 matched measures）；03:31–03:42：workbench↔BeatThis 停差 局部 +1 拍（support = 5 matched measures）
- madmom↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.94 拍的跳变（这才是错位） @03:40，平时 +0.47 拍/分钟｜异常区段 05:12–05:23
- madmom↔workbench：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.38 拍的跳变（这才是错位） @02:53，平时 -0.67 拍/分钟｜异常区段 04:04–04:46、05:11–05:22
- workbench↔BeatThis：有一头是错位的（局部 -1 拍 那端没回来）；有一处 +1.67 拍的跳变（这才是错位） @03:59，平时 +0.86 拍/分钟｜异常区段 03:31–03:42、05:10–05:21
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 10475 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.796），这是它自己的规则，不是歌曲健康

### new_82 — persistent ±1-beat disagreement
- **先听**：02:05–02:09：BeatThis↔madmom 停差 局部 -1 拍（support = 4 matched measures）；01:51–01:54：BeatThis↔madmom 停差 局部 -1 拍（support = 3 matched measures）；01:59–02:02：BeatThis↔madmom 停差 局部 -1 拍（support = 3 matched measures）
- BeatThis↔madmom：局部错位后又合上（reconvergence）：错位 局部 -1 拍；有一处 +2.05 拍的跳变（这才是错位） @01:55，平时 +4.41 拍/分钟｜异常区段 01:51–01:54、01:59–02:02、02:05–02:09
- BeatThis↔mapperatorinator：局部错位后又合上（reconvergence）：错位 局部 -1 拍；有一处 +2.03 拍的跳变（这才是错位） @01:55，平时 +2.50 拍/分钟｜异常区段 01:51–01:54、01:59–02:02、02:05–02:09
- BeatThis↔workbench：局部错位后又合上（reconvergence）：错位 局部 -1 拍；有一处 +2.01 拍的跳变（这才是错位） @02:03，平时 +4.52 拍/分钟｜异常区段 01:51–01:54、01:59–02:02、02:05–02:09
- madmom↔workbench：局部错位后又合上（reconvergence）：错位 局部 +1 拍；有一处 +2.00 拍的跳变（这才是错位） @00:19，平时 -0.95 拍/分钟｜异常区段 03:45–03:48
- mapperatorinator↔madmom：局部错位后又合上（reconvergence）：错位 局部 -1 拍；有一处 +1.03 拍的跳变（这才是错位） @03:41，平时 +1.05 拍/分钟｜异常区段 03:45–03:47
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 14463 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.825），这是它自己的规则，不是歌曲健康

### new_83 — persistent ±2-beat disagreement
- **先听**：03:00–03:23：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 13 matched measures）；00:19–00:28：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 6 matched measures）
- madmom↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.02 拍的跳变（这才是错位） @00:46，平时 -0.63 拍/分钟｜异常区段 00:19–00:28、03:02–03:10、03:13–03:19
- mapperatorinator↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.02 拍的跳变（这才是错位） @00:13，平时 +1.09 拍/分钟｜异常区段 00:19–00:28、03:00–03:23
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 936 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.008），这是它自己的规则，不是歌曲健康
- 疑似 BeatThis 2-beat counting：它自己报的小节里有 60 个只数了 2 拍 —— 待人工确认

### new_84 — clean
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +0.97 拍 @03:52（一处≠一段：可能就是漏了一拍），平时 +0.02 拍/分钟
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +0.98 拍 @03:52（一处≠一段：可能就是漏了一拍），平时 +0.02 拍/分钟
- 人那条：没有小节头按压
- 单点跳变（没持续成一段，先记着）：madmom↔BeatThis @03:52、mapperatorinator↔BeatThis @03:52

### new_85 — persistent ±1-beat disagreement
- **先听**：01:04–02:28：mapperatorinator↔madmom 停差 局部 -1 拍（support = 57 matched measures）；00:22–00:55：mapperatorinator↔madmom 停差 局部 -1 拍（support = 23 matched measures）；04:34–04:57：BeatThis↔madmom 停差 ±2 拍（半小节）（support = 16 matched measures）
- BeatThis↔madmom：局部错位后又合上（reconvergence）：错位 局部 -1 拍, ±2 拍（半小节）；有一处 +2.00 拍的跳变（这才是错位） @04:02，平时 +0.33 拍/分钟｜异常区段 00:12–00:28、00:31–00:34、00:43–00:46、01:40–01:47、03:46–03:55、04:07–04:10、04:13–04:25、04:34–04:57
- mapperatorinator↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.08 拍的跳变（这才是错位） @04:05，平时 +0.67 拍/分钟｜异常区段 01:08–01:23、01:34–01:47、01:49–01:53、04:11–04:26、04:35–04:54
- mapperatorinator↔madmom：有一头是错位的（局部 -1 拍 那端没回来）；有一处 +3.95 拍的跳变（这才是错位） @04:05，平时 -2.01 拍/分钟｜异常区段 00:22–00:55、01:04–02:28
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 25100 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.058），这是它自己的规则，不是歌曲健康

### new_86 — persistent ±2-beat disagreement
- **先听**：00:03–00:25：madmom↔mapperatorinator 停差 局部 -1 拍（support = 9 matched measures）；00:51–00:56：madmom↔mapperatorinator 停差 ±2 拍（半小节）（support = 3 matched measures）
- madmom↔mapperatorinator：有一头是错位的（局部 -1 拍 那端没回来）；有一处 +1.80 拍的跳变（这才是错位） @01:20，平时 +0.78 拍/分钟｜异常区段 00:03–00:25、00:51–00:56
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1030 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.705），这是它自己的规则，不是歌曲健康

### new_87 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +2.00 拍 @01:59（一处≠一段：可能就是漏了一拍），平时 +0.11 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1021 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.027），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @01:59

### new_88 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +1.19 拍 @00:50（一处≠一段：可能就是漏了一拍），平时 -0.08 拍/分钟
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +1.96 拍 @00:54（一处≠一段：可能就是漏了一拍），平时 +0.05 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1062 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @00:50、BeatThis↔mapperatorinator @00:54

### new_89 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +2.07 拍 @01:15（一处≠一段：可能就是漏了一拍），平时 +2.31 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 8028 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.285），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @01:15

### new_90 — persistent ±1-beat disagreement
- **先听**：02:51–03:39：mapperatorinator↔BeatThis 停差 局部 +1 拍（support = 29 matched measures）
- mapperatorinator↔BeatThis：两条小节长度略有出入：相位连续滑 +0.37 拍/分钟，最大跳变只有 0.39 拍（没有突变）｜异常区段 02:51–03:39
- mapperatorinator↔madmom：有一头是错位的（局部 +1 拍 那端没回来）；有一处 +0.42 拍的跳变（这才是错位） @02:51，平时 +0.36 拍/分钟｜异常区段 02:51–03:39
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2672 ms）——这是拍层的事，和小节相位是两回事

### new_94 — persistent ±1-beat disagreement
- **先听**：02:51–02:57：mapperatorinator↔BeatThis 停差 局部 -1 拍（support = 5 matched measures）
- madmom↔BeatThis：局部错位后又合上（reconvergence）：错位 局部 -1 拍；有一处 +1.96 拍的跳变（这才是错位） @02:51，平时 +0.51 拍/分钟｜异常区段 02:51–02:57
- mapperatorinator↔BeatThis：局部错位后又合上（reconvergence）：错位 局部 -1 拍；有一处 +1.95 拍的跳变（这才是错位） @02:49，平时 +0.57 拍/分钟｜异常区段 02:51–02:57
- workbench↔BeatThis：局部错位后又合上（reconvergence）：错位 局部 -1 拍；有一处 +1.99 拍的跳变（这才是错位） @02:51，平时 +0.55 拍/分钟｜异常区段 02:51–02:57
- 人那条：没有小节头按压

### new_95 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +1.97 拍 @02:51（一处≠一段：可能就是漏了一拍），平时 -0.04 拍/分钟
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +2.00 拍 @02:53（一处≠一段：可能就是漏了一拍），平时 -0.07 拍/分钟
- mapperatorinator↔madmom：其余全段一致，只在这一处跳了 +1.67 拍 @02:47（一处≠一段：可能就是漏了一拍），平时 +1.54 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 5366 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @02:51、BeatThis↔mapperatorinator @02:53、mapperatorinator↔madmom @02:47

### new_96 — clean
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +1.97 拍 @04:00（一处≠一段：可能就是漏了一拍），平时 -0.01 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2834 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.872），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：madmom↔BeatThis @04:00

### new_97 — clean
- BeatThis↔madmom：其余全段一致，只在这一处跳了 +1.97 拍 @02:40（一处≠一段：可能就是漏了一拍），平时 +0.01 拍/分钟
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +1.96 拍 @02:40（一处≠一段：可能就是漏了一拍），平时 -0.00 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 464 ms）——这是拍层的事，和小节相位是两回事
- 单点跳变（没持续成一段，先记着）：BeatThis↔madmom @02:40、BeatThis↔mapperatorinator @02:40

### new_98 — persistent ±2-beat disagreement
- **先听**：01:58–02:15：BeatThis↔madmom 停差 ±2 拍（半小节）（support = 14 matched measures）；01:42–01:51：BeatThis↔madmom 停差 ±2 拍（半小节）（support = 6 matched measures）
- BeatThis↔madmom：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.10 拍的跳变（这才是错位） @00:31，平时 -3.81 拍/分钟｜异常区段 01:42–01:51、01:58–02:15
- BeatThis↔mapperatorinator：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.04 拍的跳变（这才是错位） @00:31，平时 -3.74 拍/分钟｜异常区段 01:42–01:51、01:58–02:15
- BeatThis↔workbench：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.06 拍的跳变（这才是错位） @01:53，平时 -1.71 拍/分钟｜异常区段 01:42–01:51、01:58–02:15
- 人那条：没有小节头按压
- BeatThis↔mapperatorinator：2 段错位、k 走遍 -2、趋势 -3.74 拍/分钟、残余悬在中间 —— 这是相位滑过整数拍（两条小节长度不同），不是停错在某一格
- 疑似 BeatThis 2-beat counting：它自己报的小节里有 76 个只数了 2 拍 —— 待人工确认

### new_99 — clean
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +1.98 拍 @04:25（一处≠一段：可能就是漏了一拍），平时 +0.03 拍/分钟
- mapperatorinator↔madmom：其余全段一致，只在这一处跳了 +1.20 拍 @03:27（一处≠一段：可能就是漏了一拍），平时 -0.04 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2796 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.176），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：mapperatorinator↔BeatThis @04:25、mapperatorinator↔madmom @03:27

### onewish — persistent ±1-beat disagreement
- **先听**：00:00–00:12：madmom↔workbench 停差 局部 +1 拍（support = 8 matched measures）；03:18–03:25：BeatThis↔mapperatorinator 停差 ±2 拍（半小节）（support = 3 matched measures）
- BeatThis↔mapperatorinator：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.00 拍的跳变（这才是错位） @03:18，平时 -0.52 拍/分钟｜异常区段 03:18–03:25
- BeatThis↔workbench：有一头是错位的（局部 +1 拍 那端没回来）；有一处 +0.99 拍的跳变（这才是错位） @00:14，平时 -0.06 拍/分钟｜异常区段 00:00–00:11
- madmom↔workbench：有一头是错位的（局部 +1 拍 那端没回来）；有一处 +0.97 拍的跳变（这才是错位） @00:14，平时 -0.09 拍/分钟｜异常区段 00:00–00:12
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1190 ms）——这是拍层的事，和小节相位是两回事

### round2 — persistent ±2-beat disagreement
- **先听**：01:32–02:07：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 14 matched measures）；01:03–01:28：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 12 matched measures）；02:16–02:27：mapperatorinator↔madmom 停差 ±2 拍（半小节）（support = 6 matched measures）
- mapperatorinator↔madmom：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.92 拍的跳变（这才是错位） @01:00，平时 -1.34 拍/分钟｜异常区段 01:03–01:28、01:32–02:07、02:16–02:27
- 人那条：human:cal_01 2 个 matched measures、human:cal_03 3 个 matched measures

### sacra — clean
- madmom↔BeatThis：其余全段一致，只在这一处跳了 +2.00 拍 @01:22（一处≠一段：可能就是漏了一拍），平时 +0.03 拍/分钟
- mapperatorinator↔BeatThis：其余全段一致，只在这一处跳了 +2.06 拍 @01:20（一处≠一段：可能就是漏了一拍），平时 -1.94 拍/分钟
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 237 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.008），这是它自己的规则，不是歌曲健康
- 单点跳变（没持续成一段，先记着）：madmom↔BeatThis @01:22、mapperatorinator↔BeatThis @01:20

### sakuranoko — persistent ±2-beat disagreement
- **先听**：02:34–02:38：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 3 matched measures）
- madmom↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.00 拍的跳变（这才是错位） @02:31，平时 -0.03 拍/分钟｜异常区段 02:35–02:38
- mapperatorinator↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +1.99 拍的跳变（这才是错位） @02:31，平时 -0.03 拍/分钟｜异常区段 02:34–02:38
- workbench↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.01 拍的跳变（这才是错位） @02:31，平时 -1.36 拍/分钟｜异常区段 02:34–02:38
- 人那条：human:cal_02 4 个 matched measures、human:cal_03 5 个 matched measures
- 疑似 BeatThis 2-beat counting：它自己报的小节里有 8 个只数了 2 拍 —— 待人工确认

### seiza — persistent ±2-beat disagreement
- **先听**：03:30–04:11：mapperatorinator↔workbench 停差 ±2 拍（半小节）（support = 22 matched measures）
- madmom↔workbench：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.96 拍的跳变（这才是错位） @03:28，平时 -0.43 拍/分钟｜异常区段 03:28–03:38、03:42–04:11
- mapperatorinator↔madmom：其余全段一致，只在这一处跳了 +1.95 拍 @03:30（一处≠一段：可能就是漏了一拍），平时 +0.85 拍/分钟
- mapperatorinator↔workbench：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.96 拍的跳变（这才是错位） @03:30，平时 -0.41 拍/分钟｜异常区段 03:30–04:11
- workbench↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.96 拍的跳变（这才是错位） @03:29，平时 -0.41 拍/分钟｜异常区段 03:37–03:47、03:53–04:01、04:05–04:10
- 人那条：human:cal_01 5 个 matched measures、human:cal_03 4 个 matched measures
- A 层：Beat This 的拍序列不能被一条直线描述（残差 322 ms）——这是拍层的事，和小节相位是两回事

### soragoto — clean
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 413 ms）——这是拍层的事，和小节相位是两回事

### spica — clean
- BeatThis↔workbench：其余全段一致，只在这一处跳了 +0.96 拍 @02:39（一处≠一段：可能就是漏了一拍），平时 -0.02 拍/分钟
- 人那条：human:cal_01 6 个 matched measures、human:cal_02 5 个 matched measures
- 单点跳变（没持续成一段，先记着）：BeatThis↔workbench @02:39

### tengoku — clean
- 人那条：没有小节头按压
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1411 ms）——这是拍层的事，和小节相位是两回事

### velvet — persistent ±2-beat disagreement
- **先听**：03:32–04:08：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 12 matched measures）；01:29–01:55：mapperatorinator↔BeatThis 停差 ±2 拍（半小节）（support = 9 matched measures）；02:00–02:26：workbench↔BeatThis 停差 ±2 拍（半小节）（support = 9 matched measures）
- madmom↔BeatThis：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）, ±2 拍（半小节）；有一处 +2.06 拍的跳变（这才是错位） @03:01，平时 +1.25 拍/分钟｜异常区段 02:06–02:22、02:32–02:39、02:42–02:48
- mapperatorinator↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.01 拍的跳变（这才是错位） @00:43，平时 -0.30 拍/分钟｜异常区段 00:30–00:40、01:03–01:22、01:29–01:55、03:32–04:08
- workbench↔BeatThis：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +1.99 拍的跳变（这才是错位） @02:29，平时 -0.13 拍/分钟｜异常区段 00:03–00:26、02:00–02:26、02:32–02:58
- 人那条：human:cal_01 6 个 matched measures、human:cal_02 12 个 matched measures
- 疑似 BeatThis 2-beat counting：它自己报的小节里有 31 个只数了 2 拍 —— 待人工确认

### yorukake — local drift
- 人那条：没有小节头按压

### yue — local drift
- 人那条：human:cal_01 7 个 matched measures、human:cal_02 7 个 matched measures
- A 层：Beat This 的拍序列不能被一条直线描述（残差 1743 ms）——这是拍层的事，和小节相位是两回事
- workbench 那条校准的 source-health：Beat This 与鼓起音格子没对上（lock 0.012），这是它自己的规则，不是歌曲健康

### yukiguni — persistent ±2-beat disagreement
- **先听**：03:07–03:21：BeatThis↔madmom 停差 ±2 拍（半小节）（support = 5 matched measures）；00:13–00:26：BeatThis↔workbench 停差 ±2 拍（半小节）（support = 4 matched measures）；02:43–02:54：BeatThis↔madmom 停差 ±2 拍（半小节）（support = 4 matched measures）
- BeatThis↔madmom：局部错位后又合上（reconvergence）：错位 ±2 拍（半小节）；有一处 +2.10 拍的跳变（这才是错位） @01:19，平时 -1.16 拍/分钟｜异常区段 02:43–02:54、03:07–03:21
- BeatThis↔mapperatorinator：其余全段一致，只在这一处跳了 +2.00 拍 @00:26（一处≠一段：可能就是漏了一拍），平时 -0.04 拍/分钟
- BeatThis↔workbench：有一头是错位的（±2 拍（半小节） 那端没回来）；有一处 +2.09 拍的跳变（这才是错位） @04:30，平时 -1.08 拍/分钟｜异常区段 00:13–00:26、02:43–02:54、04:30–04:40
- 人那条：human:cal_01 10 个 matched measures
- A 层：Beat This 的拍序列不能被一条直线描述（残差 2408 ms）——这是拍层的事，和小节相位是两回事
- 疑似 BeatThis 2-beat counting：它自己报的小节里有 76 个只数了 2 拍 —— 待人工确认

