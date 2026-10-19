# 全库 timing 分诊表

只基于已经量出来的东西（来源 health、小节数、offset 段、持续多少个 matched measure、是否 reconverge），不新增测量、也不判哪条网格是真值。

## 结论：190 首里只有 16 首需要人听

| 处理结果 | 首数 | 歌 |
|---|---|---|
| 自动通过（读法之间无分歧） | 44 | dubai、hitchcock、natsuyuki、new_04、new_07、new_08、new_102、new_103、new_104、new_110、new_112、new_118、new_123、new_126、new_128、new_129、new_130、new_136、new_138、new_139、new_140、new_142、new_143、new_146、new_15、new_150、new_151、new_19、new_20、new_30、new_37、new_41、new_46、new_47、new_58、new_65、new_77、new_91、new_92、new_93、soragoto、taishou、tao、tengoku |
| 自动解释并局部降级某条来源 | 53 | flyway、flywayleo、henceforth、knowme、new_01、new_05、new_06、new_10、new_100、new_101、new_108、new_111、new_114、new_120、new_125、new_131、new_133、new_152、new_154、new_155、new_159、new_23、new_35、new_43、new_45、new_48、new_49、new_55、new_60、new_61、new_64、new_67、new_68、new_69、new_70、new_71、new_72、new_73、new_78、new_79、new_80、new_81、new_82、new_83、new_85、new_86、new_90、new_94、new_98、round2、sakuranoko、velvet、yukiguni |
| 只标 timing drift，仍可继续分析 | 5 | chichunhua、lulu、new_50、yorukake、yue |
| 登记为局部（单点 / 合回来），不升级 | 69 | eine、haiiro、happyend、iloveyou、kaluo、landaohua、new_03、new_09、new_105、new_106、new_107、new_109、new_11、new_113、new_116、new_117、new_119、new_12、new_122、new_124、new_127、new_13、new_132、new_134、new_135、new_137、new_144、new_145、new_147、new_148、new_149、new_153、new_157、new_158、new_17、new_18、new_22、new_24、new_26、new_28、new_29、new_31、new_32、new_33、new_36、new_38、new_40、new_42、new_44、new_51、new_53、new_54、new_56、new_57、new_62、new_63、new_66、new_74、new_84、new_87、new_88、new_89、new_95、new_96、new_97、new_99、onewish、sacra、spica |
| 人工已听过并定案（按人的判定收口） | 3 | kaitou、kiechau、seiza |
| **需要人工听** | 16 | new_02、new_115、new_121、new_14、new_141、new_156、new_16、new_21、new_25、new_27、new_34、new_39、new_52、new_59、new_75、new_76 |

## 一首歌一行

| 歌 | diagnosis | 受影响区段 | 嫌疑来源 | 归因 | 人工？ | evidence（来源 / health / offset / 小节异常 / reconverge） |
|---|---|---|---|---|---|---|
| chichunhua | continuous_drift | 02:04–02:36、01:18–01:49、02:51–03:20、04:34–04:57、00:00–00:09 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ BeatThis↔madmom k=+1(support 6)、BeatThis↔madmom k=-1(support 14)、BeatThis↔madmom k=-2(support 9)、BeatThis↔madmom k=+2(support 8) ｜ 小节异常：mapperatorinator 异常小节 5 ｜ reconverge：20 处 |
| dubai | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ — ｜ 小节异常：BeatThis 异常小节 3 ｜ reconverge：无 |
| eine | reconvergence | 01:13–03:44、04:02–04:08 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ madmom↔BeatThis k=+2(support 5)、mapperatorinator↔BeatThis k=+2(support 10)、mapperatorinator↔BeatThis k=-1(support 10)、mapperatorinator↔BeatThis k=+2(support 3) ｜ 小节异常：BeatThis 异常小节 46、madmom 异常小节 46、mapperatorinator 异常小节 6 ｜ reconverge：18 处 |
| flyway | source_measure_count_error | 02:15–02:35 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench suspect ｜ madmom↔BeatThis k=+2(support 3)、madmom↔BeatThis k=+2(support 5)、mapperatorinator↔BeatThis k=+2(support 9) ｜ 小节异常：BeatThis 异常小节 24、workbench 异常小节 0 ｜ reconverge：3 处 |
| flywayleo | source_measure_count_error | 02:18–02:33 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench suspect ｜ madmom↔BeatThis k=+2(support 7)、mapperatorinator↔BeatThis k=+2(support 7) ｜ 小节异常：BeatThis 异常小节 9、workbench 异常小节 0 ｜ reconverge：2 处 |
| haiiro | single_flip | 04:22–04:34、04:22–04:34 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench suspect ｜ — ｜ 小节异常：workbench 异常小节 0 ｜ reconverge：无 |
| happyend | single_flip | 04:51–05:03、05:01–05:13、05:01–05:13 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ — ｜ 小节异常：BeatThis 异常小节 3、madmom 异常小节 13 ｜ reconverge：无 |
| henceforth | source_measure_count_error | 03:28–03:51 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ madmom↔BeatThis k=+2(support 9)、madmom↔BeatThis k=+2(support 6)、mapperatorinator↔BeatThis k=+2(support 8)、workbench↔BeatThis k=+2(support 9) ｜ 小节异常：BeatThis 异常小节 2 ｜ reconverge：无 |
| hitchcock | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench suspect ｜ — ｜ 小节异常：BeatThis 异常小节 7、workbench 异常小节 0 ｜ reconverge：无 |
| iloveyou | reconvergence | 00:01–02:46 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench suspect ｜ madmom↔BeatThis k=+2(support 3)、madmom↔BeatThis k=+2(support 4)、madmom↔BeatThis k=+2(support 5)、madmom↔BeatThis k=+2(support 10) ｜ 小节异常：BeatThis 异常小节 5、mapperatorinator 异常小节 3、workbench 异常小节 0 ｜ reconverge：9 处 |
| kaitou | human_confirmed_source | 00:02–03:12 | BeatThis、madmom、mapperatorinator | human | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ madmom↔mapperatorinator k=-1(support 63)、madmom↔mapperatorinator k=+1(support 26)、madmom↔workbench k=+2(support 26)、mapperatorinator↔BeatThis k=+1(support 7) ｜ 小节异常：BeatThis 异常小节 41、madmom 异常小节 3 ｜ reconverge：无 |
| kaluo | single_flip | 03:40–03:52、03:40–03:52 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ — ｜ 小节异常：BeatThis 异常小节 29 ｜ reconverge：无 |
| kiechau | human_confirmed_source | 00:01–03:35 | BeatThis、madmom、mapperatorinator | human | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ madmom↔BeatThis k=-2(support 3)、madmom↔BeatThis k=+2(support 4)、madmom↔BeatThis k=+2(support 4)、madmom↔BeatThis k=+2(support 11) ｜ 小节异常：BeatThis 异常小节 17、madmom 异常小节 2、mapperatorinator 异常小节 5 ｜ reconverge：22 处 |
| knowme | source_measure_count_error | 01:33–03:22、00:02–00:22 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ madmom↔BeatThis k=+2(support 7)、mapperatorinator↔BeatThis k=+2(support 8)、mapperatorinator↔BeatThis k=+2(support 38)、workbench↔BeatThis k=+2(support 8) ｜ 小节异常：BeatThis 异常小节 3、madmom 异常小节 36 ｜ reconverge：3 处 |
| landaohua | single_flip | 02:24–02:36、01:26–01:38、01:26–01:38、04:48–05:00 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ — ｜ 小节异常：BeatThis 异常小节 64、madmom 异常小节 29 ｜ reconverge：无 |
| lulu | local_timing_drift | 01:39–01:45 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ — ｜ 小节异常：BeatThis 异常小节 44、madmom 异常小节 130 ｜ reconverge：无 |
| natsuyuki | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ — ｜ 小节异常：无 ｜ reconverge：无 |
| new_01 | source_measure_count_error | 00:31–00:44 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ BeatThis↔madmom k=+1(support 5)、BeatThis↔madmom k=-2(support 3)、BeatThis↔madmom k=-2(support 3) ｜ 小节异常：BeatThis 异常小节 36、mapperatorinator 异常小节 5 ｜ reconverge：3 处 |
| new_02 | unresolved_phase | 03:23–03:28 | — | — | **是** | BeatThis ok、madmom ok、mapperatorinator suspect ｜ BeatThis↔madmom k=-2(support 5)、BeatThis↔madmom k=-2(support 4)、mapperatorinator↔BeatThis k=+2(support 3)、mapperatorinator↔madmom k=-1(support 4) ｜ 小节异常：BeatThis 异常小节 28、mapperatorinator 异常小节 9 ｜ reconverge：3 处 |
| new_03 | single_flip | 01:53–02:05 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 32、madmom 异常小节 0 ｜ reconverge：无 |
| new_04 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 14 ｜ reconverge：无 |
| new_05 | source_measure_count_error | 02:22–03:17 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ madmom↔BeatThis k=+2(support 11)、madmom↔BeatThis k=+2(support 8)、madmom↔BeatThis k=+2(support 6)、madmom↔BeatThis k=+2(support 5) ｜ 小节异常：BeatThis 异常小节 90、mapperatorinator 异常小节 0 ｜ reconverge：无 |
| new_06 | source_measure_count_error | 00:22–00:28 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ BeatThis↔madmom k=-2(support 5)、BeatThis↔mapperatorinator k=-2(support 5) ｜ 小节异常：BeatThis 异常小节 26 ｜ reconverge：2 处 |
| new_07 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 12 ｜ reconverge：无 |
| new_08 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 7 ｜ reconverge：无 |
| new_09 | single_flip | 02:09–02:21 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 19、mapperatorinator 异常小节 0 ｜ reconverge：无 |
| new_10 | source_measure_count_error | 03:08–03:14 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ madmom↔BeatThis k=+2(support 3)、mapperatorinator↔BeatThis k=+2(support 3) ｜ 小节异常：BeatThis 异常小节 39、madmom 异常小节 2 ｜ reconverge：无 |
| new_100 | source_measure_count_error | 02:01–03:55、00:01–00:25 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ madmom↔BeatThis k=+2(support 4)、madmom↔BeatThis k=+2(support 4)、madmom↔BeatThis k=+2(support 39) ｜ 小节异常：BeatThis 异常小节 2、mapperatorinator 异常小节 48 ｜ reconverge：2 处 |
| new_101 | source_self_anomaly | 03:25–03:29 | mapperatorinator | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ mapperatorinator↔madmom k=-1(support 4) ｜ 小节异常：BeatThis 异常小节 2、mapperatorinator 异常小节 25 ｜ reconverge：1 处 |
| new_102 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 15、madmom 异常小节 4、mapperatorinator 异常小节 6 ｜ reconverge：无 |
| new_103 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 14 ｜ reconverge：无 |
| new_104 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：无 ｜ reconverge：无 |
| new_105 | single_flip | 03:20–03:32、03:20–03:32、03:20–03:32 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ — ｜ 小节异常：BeatThis 异常小节 48、madmom 异常小节 44、mapperatorinator 异常小节 1 ｜ reconverge：无 |
| new_106 | single_flip | 02:33–02:45、03:30–03:42 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 9 ｜ reconverge：无 |
| new_107 | single_flip | 00:23–00:35 | — | — | 否 | BeatThis ok、madmom ok ｜ — ｜ 小节异常：BeatThis 异常小节 19、madmom 异常小节 11 ｜ reconverge：无 |
| new_108 | source_measure_count_error | 00:39–00:42 | madmom | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ mapperatorinator↔madmom k=-1(support 3)、mapperatorinator↔madmom k=-2(support 3) ｜ 小节异常：BeatThis 异常小节 31、madmom 异常小节 7 ｜ reconverge：无 |
| new_109 | single_flip | 02:36–02:48 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 53、madmom 异常小节 0 ｜ reconverge：无 |
| new_11 | single_flip | 01:05–01:17 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ — ｜ 小节异常：BeatThis 异常小节 112、mapperatorinator 异常小节 12 ｜ reconverge：无 |
| new_110 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：无 ｜ reconverge：无 |
| new_111 | source_measure_count_error | 02:45–03:19 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ madmom↔BeatThis k=+2(support 13) ｜ 小节异常：BeatThis 异常小节 1 ｜ reconverge：无 |
| new_112 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ — ｜ 小节异常：BeatThis 异常小节 44、madmom 异常小节 24、mapperatorinator 异常小节 15 ｜ reconverge：无 |
| new_113 | single_flip | 02:59–03:11、02:59–03:11 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 29 ｜ reconverge：无 |
| new_114 | source_self_anomaly | 02:48–04:17、01:03–01:12 | workbench | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench suspect ｜ madmom↔BeatThis k=-1(support 6)、madmom↔workbench k=+1(support 26)、mapperatorinator↔BeatThis k=-1(support 22)、mapperatorinator↔BeatThis k=+1(support 8) ｜ 小节异常：BeatThis 异常小节 41、workbench 异常小节 0 ｜ reconverge：1 处 |
| new_115 | half_bar_in_music | 03:08–03:26 | BeatThis、madmom | human-calibrated | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ BeatThis↔workbench k=-2(support 3)、madmom↔workbench k=+2(support 7) ｜ 小节异常：BeatThis 异常小节 27、madmom 异常小节 9 ｜ reconverge：2 处 |
| new_116 | single_flip | 01:45–01:57 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ — ｜ 小节异常：BeatThis 异常小节 6、madmom 异常小节 9、mapperatorinator 异常小节 11 ｜ reconverge：无 |
| new_117 | single_flip | 03:20–03:32 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 43、madmom 异常小节 31 ｜ reconverge：无 |
| new_118 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：无 ｜ reconverge：无 |
| new_119 | single_flip | 01:03–01:15、01:05–01:17 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 75 ｜ reconverge：无 |
| new_12 | single_flip | 02:22–02:34、02:19–02:31 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ — ｜ 小节异常：BeatThis 异常小节 36、mapperatorinator 异常小节 2 ｜ reconverge：无 |
| new_120 | source_self_anomaly | 01:27–01:33 | mapperatorinator | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ mapperatorinator↔madmom k=+1(support 3) ｜ 小节异常：BeatThis 异常小节 3、mapperatorinator 异常小节 0 ｜ reconverge：无 |
| new_121 | reconvergence | 00:23–01:29 | — | — | **是** | BeatThis ok、madmom ok、mapperatorinator ok ｜ mapperatorinator↔madmom k=+2(support 15)、mapperatorinator↔madmom k=+2(support 7) ｜ 小节异常：BeatThis 异常小节 12 ｜ reconverge：无 |
| new_122 | single_flip | 00:28–00:40、00:24–00:36 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 22 ｜ reconverge：无 |
| new_123 | clean | — | — | — | 否 | madmom ok ｜ — ｜ 小节异常：无 ｜ reconverge：无 |
| new_124 | single_flip | 00:06–00:18 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ — ｜ 小节异常：madmom 异常小节 14、mapperatorinator 异常小节 1 ｜ reconverge：无 |
| new_125 | source_self_anomaly | 00:10–00:27 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator suspect、workbench ok ｜ BeatThis↔madmom k=+1(support 6)、BeatThis↔madmom k=+1(support 7)、BeatThis↔workbench k=+1(support 6)、BeatThis↔workbench k=+1(support 7) ｜ 小节异常：BeatThis 异常小节 65、mapperatorinator 异常小节 2 ｜ reconverge：6 处 |
| new_126 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：无 ｜ reconverge：无 |
| new_127 | single_flip | 02:53–03:05、02:53–03:05 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 42 ｜ reconverge：无 |
| new_128 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：无 ｜ reconverge：无 |
| new_129 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：无 ｜ reconverge：无 |
| new_13 | single_flip | 02:41–02:53、02:18–02:30 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 23、madmom 异常小节 8、mapperatorinator 异常小节 0 ｜ reconverge：无 |
| new_130 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 14 ｜ reconverge：无 |
| new_131 | source_self_anomaly | 00:34–00:39 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ madmom↔BeatThis k=-1(support 3)、mapperatorinator↔BeatThis k=-1(support 3) ｜ 小节异常：BeatThis 异常小节 61 ｜ reconverge：2 处 |
| new_132 | reconvergence | 01:26–02:28、00:02–00:52、02:48–03:14 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ madmom↔BeatThis k=+2(support 4)、madmom↔BeatThis k=+2(support 10)、madmom↔workbench k=+2(support 5)、madmom↔workbench k=+2(support 8) ｜ 小节异常：BeatThis 异常小节 99、madmom 异常小节 2 ｜ reconverge：29 处 |
| new_133 | source_measure_count_error | 01:15–01:28 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ madmom↔BeatThis k=+2(support 11)、mapperatorinator↔BeatThis k=+2(support 10)、workbench↔BeatThis k=+2(support 11) ｜ 小节异常：BeatThis 异常小节 47 ｜ reconverge：3 处 |
| new_134 | single_flip | 02:20–02:32、02:20–02:32 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench suspect ｜ — ｜ 小节异常：BeatThis 异常小节 27、madmom 异常小节 18、workbench 异常小节 0 ｜ reconverge：无 |
| new_135 | single_flip | 00:19–00:31、02:57–03:09 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 14 ｜ reconverge：无 |
| new_136 | clean | — | — | — | 否 | BeatThis ok、madmom ok ｜ — ｜ 小节异常：BeatThis 异常小节 48、madmom 异常小节 16 ｜ reconverge：无 |
| new_137 | reconvergence | 02:34–03:31、02:00–02:19 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ BeatThis↔mapperatorinator k=-2(support 9)、BeatThis↔workbench k=+2(support 9)、BeatThis↔workbench k=+2(support 24)、madmom↔workbench k=+2(support 11) ｜ 小节异常：BeatThis 异常小节 5、mapperatorinator 异常小节 2 ｜ reconverge：7 处 |
| new_138 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：madmom 异常小节 62 ｜ reconverge：无 |
| new_139 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 5、mapperatorinator 异常小节 2 ｜ reconverge：无 |
| new_14 | structure_only_attribution | 01:42–02:14 | madmom | structure | **是** | BeatThis ok、madmom ok、mapperatorinator ok ｜ madmom↔BeatThis k=+1(support 10)、mapperatorinator↔madmom k=-1(support 24) ｜ 小节异常：BeatThis 异常小节 17 ｜ reconverge：2 处 |
| new_140 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ — ｜ 小节异常：BeatThis 异常小节 6、mapperatorinator 异常小节 2 ｜ reconverge：无 |
| new_141 | unresolved_phase | 00:24–01:06 | — | — | **是** | BeatThis ok、madmom ok、mapperatorinator ok ｜ madmom↔BeatThis k=+1(support 6)、madmom↔BeatThis k=-1(support 4)、mapperatorinator↔BeatThis k=+1(support 6)、mapperatorinator↔BeatThis k=+1(support 4) ｜ 小节异常：BeatThis 异常小节 13 ｜ reconverge：3 处 |
| new_142 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：无 ｜ reconverge：无 |
| new_143 | clean | — | — | — | 否 | madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：无 ｜ reconverge：无 |
| new_144 | single_flip | 01:32–01:44、00:37–00:49、00:45–00:57 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 12、madmom 异常小节 3、mapperatorinator 异常小节 17 ｜ reconverge：无 |
| new_145 | single_flip | 04:16–04:28、00:36–00:48、00:26–00:38 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 18、madmom 异常小节 9、mapperatorinator 异常小节 17 ｜ reconverge：无 |
| new_146 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 36、mapperatorinator 异常小节 0 ｜ reconverge：无 |
| new_147 | single_flip | 00:43–00:55、00:45–00:57 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 13 ｜ reconverge：无 |
| new_148 | reconvergence | 00:11–03:19、03:43–04:29 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ madmom↔BeatThis k=+2(support 7)、madmom↔BeatThis k=+2(support 7)、mapperatorinator↔madmom k=+2(support 45)、mapperatorinator↔madmom k=+2(support 18) ｜ 小节异常：BeatThis 异常小节 71、madmom 异常小节 38 ｜ reconverge：8 处 |
| new_149 | single_flip | 00:09–00:21、00:11–00:23、00:11–00:23 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 2 ｜ reconverge：无 |
| new_15 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 8 ｜ reconverge：无 |
| new_150 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 12 ｜ reconverge：无 |
| new_151 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 10 ｜ reconverge：无 |
| new_152 | source_measure_count_error | 01:45–01:58、01:07–01:17 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ BeatThis↔madmom k=-2(support 6)、BeatThis↔madmom k=-2(support 7)、BeatThis↔madmom k=-1(support 4) ｜ 小节异常：BeatThis 异常小节 77、madmom 异常小节 0 ｜ reconverge：2 处 |
| new_153 | single_flip | 01:06–01:18 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 171、madmom 异常小节 0 ｜ reconverge：无 |
| new_154 | source_self_anomaly | 00:03–00:17 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ madmom↔BeatThis k=+2(support 9)、madmom↔BeatThis k=+2(support 7)、mapperatorinator↔BeatThis k=+1(support 3)、mapperatorinator↔BeatThis k=+1(support 3) ｜ 小节异常：BeatThis 异常小节 42、madmom 异常小节 7、mapperatorinator 异常小节 7 ｜ reconverge：7 处 |
| new_155 | source_self_anomaly | 02:05–02:32、03:32–03:53、01:29–01:39、00:01–00:04 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ madmom↔BeatThis k=+1(support 4)、madmom↔BeatThis k=+1(support 9)、madmom↔BeatThis k=+1(support 15)、madmom↔BeatThis k=+1(support 3) ｜ 小节异常：BeatThis 异常小节 126、mapperatorinator 异常小节 44 ｜ reconverge：6 处 |
| new_156 | reconvergence | 02:11–03:36 | — | — | **是** | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ BeatThis↔workbench k=-2(support 23)、madmom↔BeatThis k=+2(support 19)、madmom↔BeatThis k=+2(support 6)、madmom↔workbench k=-2(support 50) ｜ 小节异常：madmom 异常小节 2 ｜ reconverge：2 处 |
| new_157 | single_flip | 01:42–01:54、01:40–01:52 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 56、mapperatorinator 异常小节 7 ｜ reconverge：无 |
| new_158 | single_flip | 02:23–02:35、01:57–02:09、03:02–03:14 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 86、madmom 异常小节 6、mapperatorinator 异常小节 3 ｜ reconverge：无 |
| new_159 | source_self_anomaly | 02:16–02:28 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ BeatThis↔madmom k=-1(support 8)、BeatThis↔mapperatorinator k=-1(support 8)、BeatThis↔workbench k=-1(support 8) ｜ 小节异常：BeatThis 异常小节 42 ｜ reconverge：3 处 |
| new_16 | reconvergence | 02:33–03:13 | — | — | **是** | BeatThis ok、madmom ok、mapperatorinator suspect ｜ madmom↔BeatThis k=+2(support 15)、mapperatorinator↔BeatThis k=+2(support 5)、mapperatorinator↔madmom k=+2(support 16) ｜ 小节异常：BeatThis 异常小节 29、mapperatorinator 异常小节 1 ｜ reconverge：1 处 |
| new_17 | single_flip | 00:59–01:11、00:18–00:30 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 20、madmom 异常小节 24、mapperatorinator 异常小节 5 ｜ reconverge：无 |
| new_18 | reconvergence | 01:27–02:25 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ madmom↔BeatThis k=+2(support 13)、madmom↔workbench k=+2(support 9)、madmom↔workbench k=+2(support 20)、mapperatorinator↔BeatThis k=+2(support 5) ｜ 小节异常：BeatThis 异常小节 36 ｜ reconverge：5 处 |
| new_19 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ — ｜ 小节异常：BeatThis 异常小节 25、mapperatorinator 异常小节 1 ｜ reconverge：无 |
| new_20 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：无 ｜ reconverge：无 |
| new_21 | half_bar_in_music | 04:43–05:29 | BeatThis、madmom | human-calibrated | 否 | BeatThis ok、madmom ok、mapperatorinator suspect、workbench ok ｜ madmom↔workbench k=-2(support 18)、workbench↔BeatThis k=+2(support 19)、workbench↔mapperatorinator k=+1(support 3) ｜ 小节异常：BeatThis 异常小节 53、mapperatorinator 异常小节 78 ｜ reconverge：1 处 |
| new_22 | single_flip | 02:23–02:35、02:06–02:18 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ — ｜ 小节异常：BeatThis 异常小节 32、mapperatorinator 异常小节 1 ｜ reconverge：无 |
| new_23 | source_measure_count_error | 02:01–02:29 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ BeatThis↔mapperatorinator k=-2(support 11)、madmom↔BeatThis k=+2(support 12) ｜ 小节异常：BeatThis 异常小节 18、mapperatorinator 异常小节 50 ｜ reconverge：2 处 |
| new_24 | single_flip | 02:21–02:33、02:16–02:28、02:04–02:16 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ — ｜ 小节异常：BeatThis 异常小节 4、mapperatorinator 异常小节 13 ｜ reconverge：无 |
| new_25 | structure_only_attribution | 01:42–03:31 | madmom | structure | **是** | BeatThis ok、madmom ok、mapperatorinator ok ｜ madmom↔BeatThis k=-2(support 5)、madmom↔BeatThis k=-2(support 4)、madmom↔BeatThis k=+2(support 11)、madmom↔BeatThis k=-2(support 6) ｜ 小节异常：BeatThis 异常小节 35 ｜ reconverge：1 处 |
| new_26 | reconvergence | 02:34–03:35、00:22–00:28 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator suspect、workbench ok ｜ BeatThis↔madmom k=-2(support 3)、BeatThis↔madmom k=-2(support 5)、BeatThis↔workbench k=-2(support 3)、BeatThis↔workbench k=-2(support 6) ｜ 小节异常：BeatThis 异常小节 5、madmom 异常小节 2、mapperatorinator 异常小节 2 ｜ reconverge：9 处 |
| new_27 | structure_only_attribution | 00:07–03:00 | madmom | structure | **是** | BeatThis ok、madmom ok、mapperatorinator ok ｜ madmom↔BeatThis k=+2(support 26)、madmom↔BeatThis k=-2(support 4)、madmom↔BeatThis k=+2(support 3)、madmom↔BeatThis k=+2(support 3) ｜ 小节异常：无 ｜ reconverge：无 |
| new_28 | reconvergence | 00:08–00:47 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ madmom↔mapperatorinator k=-1(support 21) ｜ 小节异常：BeatThis 异常小节 43 ｜ reconverge：1 处 |
| new_29 | single_flip | 01:41–01:53、01:39–01:51 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 10 ｜ reconverge：无 |
| new_30 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 5 ｜ reconverge：无 |
| new_31 | single_flip | 02:21–02:33、02:18–02:30 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 9 ｜ reconverge：无 |
| new_32 | single_flip | 02:14–02:26、02:14–02:26 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 93 ｜ reconverge：无 |
| new_33 | single_flip | 02:09–02:21、02:09–02:21 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 75 ｜ reconverge：无 |
| new_34 | reconvergence | 00:02–03:21 | — | — | **是** | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ madmom↔BeatThis k=+2(support 17)、madmom↔BeatThis k=+2(support 3)、madmom↔BeatThis k=+2(support 25)、mapperatorinator↔BeatThis k=+2(support 60) ｜ 小节异常：BeatThis 异常小节 9 ｜ reconverge：6 处 |
| new_35 | source_measure_count_error | 01:59–02:03 | mapperatorinator | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ mapperatorinator↔BeatThis k=+2(support 3)、mapperatorinator↔madmom k=+2(support 3) ｜ 小节异常：BeatThis 异常小节 10、mapperatorinator 异常小节 2 ｜ reconverge：2 处 |
| new_36 | single_flip | -1:58–00:09 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator suspect、workbench suspect ｜ — ｜ 小节异常：BeatThis 异常小节 4、mapperatorinator 异常小节 1、workbench 异常小节 0 ｜ reconverge：无 |
| new_37 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 25 ｜ reconverge：无 |
| new_38 | single_flip | 00:14–00:26、00:17–00:29 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 12 ｜ reconverge：无 |
| new_39 | unresolved_phase | 01:27–02:17 | — | — | **是** | BeatThis ok、madmom ok、mapperatorinator ok ｜ mapperatorinator↔madmom k=+2(support 50)、mapperatorinator↔madmom k=-1(support 31)、mapperatorinator↔madmom k=+2(support 24) ｜ 小节异常：BeatThis 异常小节 149 ｜ reconverge：无 |
| new_40 | single_flip | 01:49–02:01、01:52–02:04 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 54 ｜ reconverge：无 |
| new_41 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 3 ｜ reconverge：无 |
| new_42 | single_flip | 00:27–00:39 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 2 ｜ reconverge：无 |
| new_43 | source_measure_count_error | 02:01–02:29 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ BeatThis↔mapperatorinator k=-2(support 6)、BeatThis↔mapperatorinator k=-2(support 3)、madmom↔BeatThis k=+2(support 5)、madmom↔BeatThis k=+2(support 4) ｜ 小节异常：BeatThis 异常小节 13、madmom 异常小节 2、mapperatorinator 异常小节 49 ｜ reconverge：4 处 |
| new_44 | single_flip | 02:06–02:18、02:06–02:18 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ — ｜ 小节异常：BeatThis 异常小节 26、mapperatorinator 异常小节 1 ｜ reconverge：无 |
| new_45 | source_self_anomaly | 02:43–03:30 | workbench | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator suspect、workbench suspect ｜ madmom↔BeatThis k=+2(support 7)、madmom↔BeatThis k=+2(support 3)、madmom↔BeatThis k=+2(support 13)、madmom↔workbench k=-1(support 33) ｜ 小节异常：BeatThis 异常小节 85、mapperatorinator 异常小节 3、workbench 异常小节 0 ｜ reconverge：1 处 |
| new_46 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 39、mapperatorinator 异常小节 0 ｜ reconverge：无 |
| new_47 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 2、mapperatorinator 异常小节 0 ｜ reconverge：无 |
| new_48 | source_measure_count_error | 03:12–04:20 | mapperatorinator | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ mapperatorinator↔BeatThis k=+2(support 24) ｜ 小节异常：BeatThis 异常小节 13、madmom 异常小节 26、mapperatorinator 异常小节 1 ｜ reconverge：无 |
| new_49 | source_measure_count_error | 01:59–02:03 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator suspect、workbench suspect ｜ BeatThis↔madmom k=-2(support 4)、BeatThis↔workbench k=-2(support 4) ｜ 小节异常：BeatThis 异常小节 19、mapperatorinator 异常小节 1、workbench 异常小节 0 ｜ reconverge：2 处 |
| new_50 | continuous_drift | 03:05–03:17、02:09–02:19 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator suspect、workbench suspect ｜ BeatThis↔workbench k=+1(support 3)、BeatThis↔workbench k=+1(support 5) ｜ 小节异常：BeatThis 异常小节 9、mapperatorinator 异常小节 1、workbench 异常小节 0 ｜ reconverge：无 |
| new_51 | single_flip | 02:39–02:51 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ — ｜ 小节异常：BeatThis 异常小节 24、mapperatorinator 异常小节 2 ｜ reconverge：无 |
| new_52 | unresolved_phase | 00:21–01:56、02:15–03:01 | — | — | **是** | BeatThis ok、madmom ok、mapperatorinator ok ｜ madmom↔BeatThis k=+1(support 56)、madmom↔BeatThis k=+1(support 24)、mapperatorinator↔BeatThis k=+2(support 30)、mapperatorinator↔madmom k=-1(support 49) ｜ 小节异常：BeatThis 异常小节 3 ｜ reconverge：1 处 |
| new_53 | reconvergence | 00:08–00:45 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ madmom↔workbench k=-1(support 20)、mapperatorinator↔BeatThis k=+1(support 3)、mapperatorinator↔madmom k=+1(support 19)、workbench↔BeatThis k=+1(support 3) ｜ 小节异常：BeatThis 异常小节 39 ｜ reconverge：4 处 |
| new_54 | reconvergence | 00:01–02:45 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ madmom↔BeatThis k=+2(support 18)、madmom↔BeatThis k=+2(support 4)、madmom↔BeatThis k=+2(support 15)、mapperatorinator↔BeatThis k=+2(support 32) ｜ 小节异常：BeatThis 异常小节 15 ｜ reconverge：17 处 |
| new_55 | source_self_anomaly | 03:32–03:34 | madmom | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ madmom↔BeatThis k=+2(support 4)、madmom↔BeatThis k=-1(support 3)、mapperatorinator↔BeatThis k=+1(support 3)、mapperatorinator↔BeatThis k=-2(support 9) ｜ 小节异常：BeatThis 异常小节 80、madmom 异常小节 18、mapperatorinator 异常小节 11 ｜ reconverge：5 处 |
| new_56 | single_flip | 03:10–03:22、01:33–01:45 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 46 ｜ reconverge：无 |
| new_57 | reconvergence | 02:58–03:07 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench suspect ｜ BeatThis↔mapperatorinator k=-2(support 7)、BeatThis↔mapperatorinator k=-2(support 5)、BeatThis↔workbench k=-2(support 4)、BeatThis↔workbench k=-2(support 6) ｜ 小节异常：BeatThis 异常小节 72、madmom 异常小节 33、mapperatorinator 异常小节 16、workbench 异常小节 0 ｜ reconverge：6 处 |
| new_58 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 14 ｜ reconverge：无 |
| new_59 | structure_only_attribution | 00:03–01:37 | madmom | structure | **是** | BeatThis ok、madmom ok、mapperatorinator ok ｜ madmom↔BeatThis k=+2(support 4)、madmom↔BeatThis k=+2(support 41)、mapperatorinator↔madmom k=+2(support 45) ｜ 小节异常：无 ｜ reconverge：3 处 |
| new_60 | source_measure_count_error | 00:09–03:34 | madmom | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ madmom↔BeatThis k=+2(support 4)、madmom↔BeatThis k=-2(support 7)、madmom↔BeatThis k=+2(support 8)、madmom↔BeatThis k=+2(support 3) ｜ 小节异常：BeatThis 异常小节 61、madmom 异常小节 2 ｜ reconverge：9 处 |
| new_61 | source_measure_count_error | 03:00–03:03 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ BeatThis↔madmom k=-2(support 3)、BeatThis↔mapperatorinator k=-2(support 3) ｜ 小节异常：BeatThis 异常小节 81、mapperatorinator 异常小节 1 ｜ reconverge：2 处 |
| new_62 | reconvergence | 02:34–03:35、00:19–00:29 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator suspect、workbench ok ｜ BeatThis↔madmom k=-2(support 5)、BeatThis↔madmom k=-2(support 5)、BeatThis↔workbench k=-2(support 5)、BeatThis↔workbench k=-2(support 6) ｜ 小节异常：BeatThis 异常小节 4、madmom 异常小节 2、mapperatorinator 异常小节 10 ｜ reconverge：10 处 |
| new_63 | single_flip | 00:54–01:06 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ — ｜ 小节异常：BeatThis 异常小节 29、mapperatorinator 异常小节 1 ｜ reconverge：无 |
| new_64 | source_self_anomaly | 00:20–00:28 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ BeatThis↔madmom k=+1(support 5)、mapperatorinator↔BeatThis k=-1(support 5) ｜ 小节异常：BeatThis 异常小节 3、mapperatorinator 异常小节 9 ｜ reconverge：2 处 |
| new_65 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 7 ｜ reconverge：无 |
| new_66 | single_flip | 02:21–02:33 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ — ｜ 小节异常：BeatThis 异常小节 20、mapperatorinator 异常小节 1 ｜ reconverge：无 |
| new_67 | source_measure_count_error | 02:58–03:03 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ madmom↔BeatThis k=+2(support 4)、mapperatorinator↔BeatThis k=+2(support 4)、workbench↔BeatThis k=-2(support 4) ｜ 小节异常：BeatThis 异常小节 26 ｜ reconverge：3 处 |
| new_68 | source_measure_count_error | 00:47–01:35、03:15–03:27 | madmom | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ BeatThis↔madmom k=-2(support 3)、BeatThis↔madmom k=+2(support 3)、madmom↔mapperatorinator k=-2(support 22) ｜ 小节异常：BeatThis 异常小节 51、madmom 异常小节 2、mapperatorinator 异常小节 26 ｜ reconverge：1 处 |
| new_69 | source_measure_count_error | 02:52–02:58 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ madmom↔BeatThis k=+1(support 4)、madmom↔BeatThis k=+2(support 3)、madmom↔BeatThis k=-2(support 3) ｜ 小节异常：BeatThis 异常小节 120、madmom 异常小节 7、mapperatorinator 异常小节 7 ｜ reconverge：3 处 |
| new_70 | source_measure_count_error | 04:05–05:21、02:57–03:51 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ madmom↔BeatThis k=+2(support 20)、mapperatorinator↔BeatThis k=+2(support 20)、mapperatorinator↔BeatThis k=+2(support 8)、mapperatorinator↔BeatThis k=+2(support 16) ｜ 小节异常：BeatThis 异常小节 20、madmom 异常小节 18 ｜ reconverge：1 处 |
| new_71 | source_self_anomaly | 02:22–02:27 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ BeatThis↔madmom k=-1(support 3)、BeatThis↔mapperatorinator k=-1(support 3) ｜ 小节异常：BeatThis 异常小节 69 ｜ reconverge：2 处 |
| new_72 | source_self_anomaly | 03:07–03:16 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ madmom↔BeatThis k=-1(support 5) ｜ 小节异常：BeatThis 异常小节 84、madmom 异常小节 6 ｜ reconverge：无 |
| new_73 | source_measure_count_error | 00:03–00:17 | mapperatorinator | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ mapperatorinator↔BeatThis k=+1(support 7)、mapperatorinator↔madmom k=+2(support 7) ｜ 小节异常：BeatThis 异常小节 53、madmom 异常小节 8、mapperatorinator 异常小节 14 ｜ reconverge：2 处 |
| new_74 | reconvergence | 01:26–02:26、00:45–00:58、00:12–00:19、02:53–02:58 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator suspect、workbench ok ｜ BeatThis↔madmom k=-2(support 6)、BeatThis↔madmom k=-1(support 11)、BeatThis↔madmom k=-2(support 12)、BeatThis↔madmom k=-2(support 6) ｜ 小节异常：BeatThis 异常小节 68、mapperatorinator 异常小节 5 ｜ reconverge：14 处 |
| new_75 | reconvergence | 02:58–03:36 | — | — | **是** | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ madmom↔BeatThis k=+2(support 6)、madmom↔BeatThis k=+2(support 5)、madmom↔BeatThis k=+2(support 3)、mapperatorinator↔madmom k=+2(support 23) ｜ 小节异常：BeatThis 异常小节 7 ｜ reconverge：无 |
| new_76 | structure_only_attribution | 00:43–01:39 | madmom | structure | **是** | BeatThis ok、madmom ok、mapperatorinator ok ｜ madmom↔BeatThis k=-1(support 24)、madmom↔BeatThis k=+2(support 7)、madmom↔BeatThis k=+2(support 4)、madmom↔BeatThis k=+2(support 13) ｜ 小节异常：BeatThis 异常小节 32 ｜ reconverge：7 处 |
| new_77 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 14 ｜ reconverge：无 |
| new_78 | source_self_anomaly | 00:02–00:59 | mapperatorinator | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ madmom↔BeatThis k=+1(support 29)、mapperatorinator↔BeatThis k=+2(support 12)、mapperatorinator↔BeatThis k=+2(support 8)、mapperatorinator↔BeatThis k=+2(support 13) ｜ 小节异常：BeatThis 异常小节 4、mapperatorinator 异常小节 1 ｜ reconverge：3 处 |
| new_79 | source_measure_count_error | 00:30–00:43 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ madmom↔BeatThis k=+2(support 11)、madmom↔BeatThis k=+1(support 3)、mapperatorinator↔BeatThis k=+2(support 11)、mapperatorinator↔BeatThis k=+1(support 3) ｜ 小节异常：BeatThis 异常小节 99 ｜ reconverge：6 处 |
| new_80 | source_measure_count_error | 01:46–02:28、01:01–01:18 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ BeatThis↔madmom k=-2(support 9)、BeatThis↔madmom k=-2(support 21)、mapperatorinator↔BeatThis k=+1(support 5) ｜ 小节异常：BeatThis 异常小节 77、mapperatorinator 异常小节 43 ｜ reconverge：3 处 |
| new_81 | source_self_anomaly | 04:04–04:46、03:31–03:42、05:10–05:21 | workbench | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator suspect、workbench suspect ｜ madmom↔BeatThis k=+2(support 5)、madmom↔workbench k=+1(support 31)、madmom↔workbench k=-2(support 9)、workbench↔BeatThis k=+1(support 5) ｜ 小节异常：BeatThis 异常小节 51、madmom 异常小节 40、mapperatorinator 异常小节 60、workbench 异常小节 0 ｜ reconverge：1 处 |
| new_82 | source_self_anomaly | 01:51–02:09、03:45–03:48 | madmom | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench suspect ｜ BeatThis↔madmom k=-1(support 3)、BeatThis↔madmom k=-1(support 3)、BeatThis↔madmom k=-1(support 4)、BeatThis↔mapperatorinator k=-1(support 3) ｜ 小节异常：BeatThis 异常小节 90、madmom 异常小节 17、workbench 异常小节 0 ｜ reconverge：11 处 |
| new_83 | source_measure_count_error | 03:00–03:23、00:19–00:28 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ madmom↔BeatThis k=+2(support 6)、madmom↔BeatThis k=+2(support 5)、madmom↔BeatThis k=+2(support 4)、mapperatorinator↔BeatThis k=+2(support 6) ｜ 小节异常：BeatThis 异常小节 61 ｜ reconverge：2 处 |
| new_84 | single_flip | 03:46–03:58、03:46–03:58 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 3 ｜ reconverge：无 |
| new_85 | source_self_anomaly | 00:12–02:28、03:46–03:55 | mapperatorinator | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ BeatThis↔madmom k=-1(support 12)、BeatThis↔madmom k=-2(support 3)、BeatThis↔madmom k=-1(support 3)、BeatThis↔madmom k=-2(support 5) ｜ 小节异常：BeatThis 异常小节 65、madmom 异常小节 45、mapperatorinator 异常小节 1 ｜ reconverge：10 处 |
| new_86 | source_measure_count_error | 00:51–00:56 | madmom | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ madmom↔mapperatorinator k=-1(support 9)、madmom↔mapperatorinator k=-2(support 3) ｜ 小节异常：BeatThis 异常小节 2、madmom 异常小节 18、mapperatorinator 异常小节 13 ｜ reconverge：2 处 |
| new_87 | single_flip | 01:53–02:05 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 7、mapperatorinator 异常小节 1 ｜ reconverge：无 |
| new_88 | single_flip | 00:44–00:56、00:48–01:00 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 3、madmom 异常小节 2 ｜ reconverge：无 |
| new_89 | single_flip | 01:09–01:21 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 6、mapperatorinator 异常小节 0 ｜ reconverge：无 |
| new_90 | source_self_anomaly | 02:51–03:39 | mapperatorinator | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ mapperatorinator↔BeatThis k=+1(support 29)、mapperatorinator↔madmom k=+1(support 29) ｜ 小节异常：BeatThis 异常小节 2、mapperatorinator 异常小节 1 ｜ reconverge：无 |
| new_91 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：无 ｜ reconverge：无 |
| new_92 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 8 ｜ reconverge：无 |
| new_93 | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：无 ｜ reconverge：无 |
| new_94 | source_self_anomaly | 02:51–02:57 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ madmom↔BeatThis k=-1(support 5)、mapperatorinator↔BeatThis k=-1(support 5)、workbench↔BeatThis k=-1(support 5) ｜ 小节异常：BeatThis 异常小节 37 ｜ reconverge：3 处 |
| new_95 | single_flip | 02:45–02:57、02:47–02:59、02:41–02:53 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ — ｜ 小节异常：BeatThis 异常小节 41、madmom 异常小节 6、mapperatorinator 异常小节 1 ｜ reconverge：无 |
| new_96 | single_flip | 03:54–04:06 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator suspect ｜ — ｜ 小节异常：BeatThis 异常小节 55、mapperatorinator 异常小节 1 ｜ reconverge：无 |
| new_97 | single_flip | 02:34–02:46、02:34–02:46 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 6 ｜ reconverge：无 |
| new_98 | source_measure_count_error | 01:42–02:15 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ BeatThis↔madmom k=-2(support 6)、BeatThis↔madmom k=-2(support 14)、BeatThis↔mapperatorinator k=-2(support 6)、BeatThis↔mapperatorinator k=-2(support 14) ｜ 小节异常：BeatThis 异常小节 120 ｜ reconverge：6 处 |
| new_99 | single_flip | 04:19–04:31、03:21–03:33 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok ｜ — ｜ 小节异常：BeatThis 异常小节 122、madmom 异常小节 0 ｜ reconverge：无 |
| onewish | reconvergence | 03:18–03:25 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ BeatThis↔mapperatorinator k=-2(support 3)、BeatThis↔workbench k=+1(support 5)、madmom↔workbench k=+1(support 8) ｜ 小节异常：BeatThis 异常小节 13、mapperatorinator 异常小节 1 ｜ reconverge：2 处 |
| round2 | source_measure_count_error | 01:03–02:27 | mapperatorinator | bar-length | 否 | madmom ok、mapperatorinator suspect ｜ mapperatorinator↔madmom k=+2(support 12)、mapperatorinator↔madmom k=+2(support 14)、mapperatorinator↔madmom k=+2(support 6) ｜ 小节异常：madmom 异常小节 2、mapperatorinator 异常小节 29 ｜ reconverge：3 处 |
| sacra | single_flip | 01:16–01:28、01:14–01:26 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench suspect ｜ — ｜ 小节异常：BeatThis 异常小节 12、workbench 异常小节 0 ｜ reconverge：无 |
| sakuranoko | source_measure_count_error | 02:34–02:38 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ madmom↔BeatThis k=+2(support 3)、mapperatorinator↔BeatThis k=+2(support 3)、workbench↔BeatThis k=+2(support 3) ｜ 小节异常：BeatThis 异常小节 9 ｜ reconverge：3 处 |
| seiza | human_confirmed_source | 03:28–04:11 | BeatThis、madmom、mapperatorinator | human | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ madmom↔workbench k=+2(support 6)、madmom↔workbench k=+2(support 16)、mapperatorinator↔workbench k=+2(support 22)、workbench↔BeatThis k=-2(support 6) ｜ 小节异常：BeatThis 异常小节 4 ｜ reconverge：无 |
| soragoto | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ — ｜ 小节异常：无 ｜ reconverge：无 |
| spica | single_flip | 02:33–02:45 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ — ｜ 小节异常：无 ｜ reconverge：无 |
| taishou | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ — ｜ 小节异常：无 ｜ reconverge：无 |
| tao | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ — ｜ 小节异常：无 ｜ reconverge：无 |
| tengoku | clean | — | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ — ｜ 小节异常：BeatThis 异常小节 7 ｜ reconverge：无 |
| velvet | source_measure_count_error | 01:03–02:58、00:03–00:40、03:32–04:08 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ madmom↔BeatThis k=+2(support 6)、madmom↔BeatThis k=+2(support 3)、madmom↔BeatThis k=-2(support 3)、mapperatorinator↔BeatThis k=+2(support 4) ｜ 小节异常：BeatThis 异常小节 32 ｜ reconverge：9 处 |
| yorukake | local_timing_drift | 03:09–03:17 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ — ｜ 小节异常：无 ｜ reconverge：无 |
| yue | local_timing_drift | 02:42–02:47 | — | — | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench suspect ｜ — ｜ 小节异常：BeatThis 异常小节 21、workbench 异常小节 0 ｜ reconverge：无 |
| yukiguni | source_measure_count_error | 00:13–00:26、03:07–03:21、02:43–02:54、04:30–04:40 | BeatThis | bar-length | 否 | BeatThis ok、madmom ok、mapperatorinator ok、workbench ok ｜ BeatThis↔madmom k=-2(support 4)、BeatThis↔madmom k=-2(support 5)、BeatThis↔workbench k=+2(support 4)、BeatThis↔workbench k=-2(support 4) ｜ 小节异常：BeatThis 异常小节 38 ｜ reconverge：4 处 |

## 需要人听的那几首（六字段全量）

### new_02 — unresolved_phase
- affectedRange：03:23–03:28（5s）
- suspectSource：没有能归因的来源
- resolution：整拍分歧（mapperatorinator↔madmom），相关来源自身都没有异常、到结尾也没合回来：这才是需要人听的一类。

### new_121 — reconvergence
- affectedRange：00:23–01:29（66s）
- suspectSource：没有能归因的来源
- resolution：部分区段分歧后合回来了（那些只标范围）；剩下 2 段到结尾没合回来（support 最大 15），需要人听一次。

### new_14 — structure_only_attribution
- affectedRange：01:42–02:14（32s）
- suspectSource：madmom
- resolution：整拍分歧，形状是「只有 madmom 不同、其余互相一致」，但它没有自身异常症状：只报形状，不自动降级（这类形状有过反例）。

### new_141 — unresolved_phase
- affectedRange：00:24–01:06（42s）
- suspectSource：没有能归因的来源
- resolution：整拍分歧（madmom↔BeatThis、mapperatorinator↔madmom），相关来源自身都没有异常、到结尾也没合回来：这才是需要人听的一类。

### new_156 — reconvergence
- affectedRange：02:11–03:36（85s）
- suspectSource：没有能归因的来源
- resolution：部分区段分歧后合回来了（那些只标范围）；剩下 4 段到结尾没合回来（support 最大 50），需要人听一次。

### new_16 — reconvergence
- affectedRange：02:33–03:13（40s）
- suspectSource：没有能归因的来源
- resolution：部分区段分歧后合回来了（那些只标范围）；剩下 2 段到结尾没合回来（support 最大 16），需要人听一次。

### new_25 — structure_only_attribution
- affectedRange：01:42–03:31（109s）
- suspectSource：madmom
- resolution：分歧的形状是「只有 madmom 一条不同、其余互相一致」，但它自己没报出异常小节长度。这类形状有过反例（kaitou：与众不同的那条才是准的），所以只报形状、不自动降级。

### new_27 — structure_only_attribution
- affectedRange：00:07–03:00（173s）
- suspectSource：madmom
- resolution：分歧的形状是「只有 madmom 一条不同、其余互相一致」，但它自己没报出异常小节长度。这类形状有过反例（kaitou：与众不同的那条才是准的），所以只报形状、不自动降级。

### new_34 — reconvergence
- affectedRange：00:02–03:21（199s）
- suspectSource：没有能归因的来源
- resolution：部分区段分歧后合回来了（那些只标范围）；剩下 3 段到结尾没合回来（support 最大 107），需要人听一次。

### new_39 — unresolved_phase
- affectedRange：01:27–02:17（50s）
- suspectSource：没有能归因的来源
- resolution：整拍分歧（mapperatorinator↔madmom），相关来源自身都没有异常、到结尾也没合回来：这才是需要人听的一类。

### new_52 — unresolved_phase
- affectedRange：00:21–01:56（96s）、02:15–03:01（46s）
- suspectSource：没有能归因的来源
- resolution：整拍分歧（madmom↔BeatThis、mapperatorinator↔madmom），相关来源自身都没有异常、到结尾也没合回来：这才是需要人听的一类。

### new_59 — structure_only_attribution
- affectedRange：00:03–01:37（94s）
- suspectSource：madmom
- resolution：分歧的形状是「只有 madmom 一条不同、其余互相一致」，但它自己没报出异常小节长度。这类形状有过反例（kaitou：与众不同的那条才是准的），所以只报形状、不自动降级。

### new_75 — reconvergence
- affectedRange：02:58–03:36（39s）
- suspectSource：没有能归因的来源
- resolution：部分区段分歧后合回来了（那些只标范围）；剩下 6 段到结尾没合回来（support 最大 23），需要人听一次。

### new_76 — structure_only_attribution
- affectedRange：00:43–01:39（55s）
- suspectSource：madmom
- resolution：分歧的形状是「只有 madmom 一条不同、其余互相一致」，但它自己没报出异常小节长度。这类形状有过反例（kaitou：与众不同的那条才是准的），所以只报形状、不自动降级。

## 自动解释了谁（局部降级，不进人工）

- **flyway** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 24 处（短 24 / 长 0）），其余读法互相一致；不进人工。
- **flywayleo** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 9 处（短 9 / 长 0）），其余读法互相一致；不进人工。
- **henceforth** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 2 处（短 2 / 长 0）），其余读法互相一致；不进人工。
- **knowme** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 3 处（短 3 / 长 0）；小节头只有 72 个（同类中位数 122）），其余读法互相一致；不进人工。
- **new_01** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 36 处（短 34 / 长 2）），其余读法互相一致；不进人工。
- **new_05** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 90 处（短 87 / 长 3）），其余读法互相一致；不进人工。
- **new_06** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 26 处（短 3 / 长 23）），其余读法互相一致；不进人工。
- **new_10** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 39 处（短 36 / 长 3）），其余读法互相一致；不进人工。
- **new_100** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 2 处（短 0 / 长 2）），其余读法互相一致；不进人工。
- **new_101** → 降级 mapperatorinator：整拍分歧，且 mapperatorinator 自身有异常（health=suspect；小节长度异常 25 处（短 0 / 长 25））：局部降级这条来源，不进人工。
- **new_108** → 降级 madmom：只在这一段降级 madmom 的小节线（小节长度异常 7 处（短 0 / 长 7）），其余读法互相一致；不进人工。
- **new_111** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节头只有 48 个（同类中位数 107）），其余读法互相一致；不进人工。
- **new_114** → 降级 workbench：整拍分歧，且 workbench 自身有异常（health=suspect）：局部降级这条来源，不进人工。
- **new_120** → 降级 mapperatorinator：整拍分歧，且 mapperatorinator 自身有异常（health=suspect；小节头只有 3 个（同类中位数 23））：局部降级这条来源，不进人工。
- **new_125** → 降级 BeatThis：整拍分歧，且 BeatThis 自身有异常（小节长度异常 65 处（短 48 / 长 17））：局部降级这条来源，不进人工。
- **new_131** → 降级 BeatThis：整拍分歧，且 BeatThis 自身有异常（小节长度异常 61 处（短 47 / 长 14））：局部降级这条来源，不进人工。
- **new_133** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 47 处（短 33 / 长 14）），其余读法互相一致；不进人工。
- **new_152** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 77 处（短 40 / 长 37）），其余读法互相一致；不进人工。
- **new_154** → 降级 BeatThis：整拍分歧，且 BeatThis 自身有异常（小节长度异常 42 处（短 33 / 长 9））：局部降级这条来源，不进人工。
- **new_155** → 降级 BeatThis：整拍分歧，且 BeatThis 自身有异常（小节长度异常 126 处（短 124 / 长 2））：局部降级这条来源，不进人工。
- **new_159** → 降级 BeatThis：整拍分歧，且 BeatThis 自身有异常（小节长度异常 42 处（短 21 / 长 21））：局部降级这条来源，不进人工。
- **new_23** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 18 处（短 17 / 长 1）），其余读法互相一致；不进人工。
- **new_35** → 降级 mapperatorinator：只在这一段降级 mapperatorinator 的小节线（小节长度异常 2 处（短 0 / 长 2）），其余读法互相一致；不进人工。
- **new_43** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 13 处（短 11 / 长 2）），其余读法互相一致；不进人工。
- **new_45** → 降级 workbench：整拍分歧，且 workbench 自身有异常（health=suspect）：局部降级这条来源，不进人工。
- **new_48** → 降级 mapperatorinator：只在这一段降级 mapperatorinator 的小节线（health=suspect），其余读法互相一致；不进人工。
- **new_49** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 19 处（短 14 / 长 5）），其余读法互相一致；不进人工。
- **new_55** → 降级 madmom：整拍分歧，且 madmom 自身有异常（小节长度异常 18 处（短 0 / 长 18））：局部降级这条来源，不进人工。
- **new_60** → 降级 madmom：只在这一段降级 madmom 的小节线（小节长度异常 2 处（短 0 / 长 2）），其余读法互相一致；不进人工。
- **new_61** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 81 处（短 0 / 长 81）），其余读法互相一致；不进人工。
- **new_64** → 降级 BeatThis：整拍分歧，且 BeatThis 自身有异常（小节长度异常 3 处（短 0 / 长 3））：局部降级这条来源，不进人工。
- **new_67** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 26 处（短 23 / 长 3）），其余读法互相一致；不进人工。
- **new_68** → 降级 madmom：只在这一段降级 madmom 的小节线（小节长度异常 2 处（短 2 / 长 0）），其余读法互相一致；不进人工。
- **new_69** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 120 处（短 114 / 长 6）），其余读法互相一致；不进人工。
- **new_70** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 20 处（短 19 / 长 1）；小节头只有 125 个（同类中位数 231）），其余读法互相一致；不进人工。
- **new_71** → 降级 BeatThis：整拍分歧，且 BeatThis 自身有异常（小节长度异常 69 处（短 30 / 长 39））：局部降级这条来源，不进人工。
- **new_72** → 降级 BeatThis：整拍分歧，且 BeatThis 自身有异常（小节长度异常 84 处（短 55 / 长 29））：局部降级这条来源，不进人工。
- **new_73** → 降级 mapperatorinator：只在这一段降级 mapperatorinator 的小节线（小节长度异常 14 处（短 0 / 长 14）），其余读法互相一致；不进人工。
- **new_78** → 降级 mapperatorinator：整拍分歧，且 mapperatorinator 自身有异常（health=suspect）：局部降级这条来源，不进人工。
- **new_79** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 99 处（短 84 / 长 15）），其余读法互相一致；不进人工。
- **new_80** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 77 处（短 27 / 长 50）），其余读法互相一致；不进人工。
- **new_81** → 降级 workbench：整拍分歧，且 workbench 自身有异常（health=suspect）：局部降级这条来源，不进人工。
- **new_82** → 降级 madmom：整拍分歧，且 madmom 自身有异常（小节长度异常 17 处（短 0 / 长 17））：局部降级这条来源，不进人工。
- **new_83** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 61 处（短 61 / 长 0）），其余读法互相一致；不进人工。
- **new_85** → 降级 mapperatorinator：整拍分歧，且 mapperatorinator 自身有异常（health=suspect）：局部降级这条来源，不进人工。
- **new_86** → 降级 madmom：只在这一段降级 madmom 的小节线（小节长度异常 18 处（短 1 / 长 17）），其余读法互相一致；不进人工。
- **new_90** → 降级 mapperatorinator：整拍分歧，且 mapperatorinator 自身有异常（health=suspect；小节头只有 72 个（同类中位数 123））：局部降级这条来源，不进人工。
- **new_94** → 降级 BeatThis：整拍分歧，且 BeatThis 自身有异常（小节长度异常 37 处（短 37 / 长 0））：局部降级这条来源，不进人工。
- **new_98** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 120 处（短 26 / 长 94）），其余读法互相一致；不进人工。
- **round2** → 降级 mapperatorinator：只在这一段降级 mapperatorinator 的小节线（health=suspect；小节长度异常 29 处（短 0 / 长 29）），其余读法互相一致；不进人工。
- **sakuranoko** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 9 处（短 9 / 长 0）），其余读法互相一致；不进人工。
- **velvet** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 32 处（短 31 / 长 1）），其余读法互相一致；不进人工。
- **yukiguni** → 降级 BeatThis：只在这一段降级 BeatThis 的小节线（小节长度异常 38 处（短 4 / 长 34）），其余读法互相一致；不进人工。

## 只标范围、不动结论的

- **chichunhua** → continuous_drift：相位连续滑：这是 tempo / affine 假设的风险（两条线的小节长度略有出入），不是相位错位；不判小节错。
- **eine** → reconvergence：分歧之后都合回来了：只标这些区段，不把整首歌定性为异常。
- **haiiro** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **happyend** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **iloveyou** → reconvergence：分歧之后都合回来了：只标这些区段，不把整首歌定性为异常。
- **kaluo** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **landaohua** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **lulu** → local_timing_drift：B 层干净，只有 A 层显示拍子在局部漂：不判小节错，下游用到拍层结论时带保留。
- **new_03** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_09** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_105** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_106** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_107** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_109** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_11** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_113** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_116** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_117** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_119** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_12** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_121** → reconvergence：部分区段分歧后合回来了（那些只标范围）；剩下 2 段到结尾没合回来（support 最大 15），需要人听一次。
- **new_122** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_124** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_127** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_13** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_132** → reconvergence：分歧之后都合回来了：只标这些区段，不把整首歌定性为异常。
- **new_134** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_135** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_137** → reconvergence：分歧之后都合回来了：只标这些区段，不把整首歌定性为异常。
- **new_144** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_145** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_147** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_148** → reconvergence：分歧之后都合回来了：只标这些区段，不把整首歌定性为异常。
- **new_149** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_153** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_156** → reconvergence：部分区段分歧后合回来了（那些只标范围）；剩下 4 段到结尾没合回来（support 最大 50），需要人听一次。
- **new_157** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_158** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_16** → reconvergence：部分区段分歧后合回来了（那些只标范围）；剩下 2 段到结尾没合回来（support 最大 16），需要人听一次。
- **new_17** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_18** → reconvergence：分歧之后都合回来了：只标这些区段，不把整首歌定性为异常。
- **new_22** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_24** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_26** → reconvergence：分歧之后都合回来了：只标这些区段，不把整首歌定性为异常。
- **new_28** → reconvergence：分歧之后都合回来了：只标这些区段，不把整首歌定性为异常。
- **new_29** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_31** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_32** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_33** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_34** → reconvergence：部分区段分歧后合回来了（那些只标范围）；剩下 3 段到结尾没合回来（support 最大 107），需要人听一次。
- **new_36** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_38** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_40** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_42** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_44** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_50** → continuous_drift：相位连续滑：这是 tempo / affine 假设的风险（两条线的小节长度略有出入），不是相位错位；不判小节错。
- **new_51** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_53** → reconvergence：分歧之后都合回来了：只标这些区段，不把整首歌定性为异常。
- **new_54** → reconvergence：分歧之后都合回来了：只标这些区段，不把整首歌定性为异常。
- **new_56** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_57** → reconvergence：分歧都没合回来，但每段只有 3 个 matched measure 支持（低于 4）：登记为局部单点，不占人工。
- **new_62** → reconvergence：分歧之后都合回来了：只标这些区段，不把整首歌定性为异常。
- **new_63** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_66** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_74** → reconvergence：分歧之后都合回来了：只标这些区段，不把整首歌定性为异常。
- **new_75** → reconvergence：部分区段分歧后合回来了（那些只标范围）；剩下 6 段到结尾没合回来（support 最大 23），需要人听一次。
- **new_84** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_87** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_88** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_89** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_95** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_96** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_97** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **new_99** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **onewish** → reconvergence：分歧都没合回来，但每段只有 3 个 matched measure 支持（低于 4）：登记为局部单点，不占人工。
- **sacra** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **spica** → single_flip：单点跳变，前后立即恢复：只登记，不当异常。
- **yorukake** → local_timing_drift：B 层干净，只有 A 层显示拍子在局部漂：不判小节错，下游用到拍层结论时带保留。
- **yue** → local_timing_drift：B 层干净，只有 A 层显示拍子在局部漂：不判小节错，下游用到拍层结论时带保留。

第一版不做：全库 ensemble、不信 Mapperatorinator 单次采样、不自动改任何网格、不改人工校准。分诊的降级只影响下游读这条结论时的准入，原始 observation 一个数都不动。

## 下游准入（`static/timing_admission.json`）

这是这一层的出口：下游只读它，不再自己判断哪条网格对。

- **eligible**（可以整曲用）101 首：dubai、flyway、flywayleo、henceforth、hitchcock、kaitou、kiechau、knowme、natsuyuki、new_01、new_04、new_05、new_06、new_07、new_08、new_10、new_100、new_101、new_102、new_103、new_104、new_108、new_110、new_111、new_112、new_114、new_115、new_118、new_120、new_123、new_125、new_126、new_128、new_129、new_130、new_131、new_133、new_136、new_138、new_139、new_140、new_142、new_143、new_146、new_15、new_150、new_151、new_152、new_154、new_155、new_159、new_19、new_20、new_21、new_23、new_30、new_35、new_37、new_41、new_43、new_45、new_46、new_47、new_48、new_49、new_55、new_58、new_60、new_61、new_64、new_65、new_67、new_68、new_69、new_70、new_71、new_72、new_73、new_77、new_78、new_79、new_80、new_81、new_82、new_83、new_85、new_86、new_90、new_91、new_92、new_93、new_94、new_98、sakuranoko、seiza、soragoto、taishou、tao、tengoku、velvet、yukiguni
- **caution**（能用，但标出的区段要带保留）75 首：chichunhua、eine、haiiro、happyend、iloveyou、kaluo、landaohua、lulu、new_03、new_09、new_105、new_106、new_107、new_109、new_11、new_113、new_116、new_117、new_119、new_12、new_122、new_124、new_127、new_13、new_132、new_134、new_135、new_137、new_144、new_145、new_147、new_148、new_149、new_153、new_157、new_158、new_17、new_18、new_22、new_24、new_26、new_28、new_29、new_31、new_32、new_33、new_36、new_38、new_40、new_42、new_44、new_50、new_51、new_53、new_54、new_56、new_57、new_62、new_63、new_66、new_74、new_84、new_87、new_88、new_89、new_95、new_96、new_97、new_99、onewish、round2、sacra、spica、yorukake、yue
- **ineligible**（先别用）14 首：new_02、new_121、new_14、new_141、new_156、new_16、new_25、new_27、new_34、new_39、new_52、new_59、new_75、new_76

