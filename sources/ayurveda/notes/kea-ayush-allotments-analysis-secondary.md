# Deep Analysis of Karnataka KEA AYUSH Allotments

## Executive view

The four uploaded files contain **three unique datasets**, not four: the two 30 August 2025 Round 2 PDFs are byte-identical duplicates. The usable editions are 2025 Round 2, 2025 Round 3, and 2026 Round 1.[^1][^2][^3][^4]

The strongest signal is a substantial year-on-year loosening in General Merit (GM) closing All India Ranks (AIRs). Across 94 exactly matched course codes with GM allotments in both 2025 Round 2 and 2026 Round 1, the median closing AIR moved from roughly **206,335 to 270,618**, a median change of about **+60,006 ranks** or **+30.3%**. This should not be interpreted as a pure change in candidate demand: the 2026 files use different seat labels, omit BUMS entirely, cover fewer institutions, and reflect a different NEET rank distribution.[^2][^3]

For near-term decision-making, the defensible baseline is the **actual 2026 Round 1 college/category cutoff**, not a statewide maximum. For BAMS-Govt GM, a historically grounded Round 2 scenario is about **1.03–1.14 times the Round 1 closing AIR**, with a median multiplier around **1.065** based on matched 2025 BAMS-Govt codes; this is a scenario band, not an official forecast.[^3][^1][^2]

## Dataset audit

| Edition | Publication date | Rows | Base institutions | Course codes | AIR range | Status mix |
|---|---:|---:|---:|---:|---:|---|
| 2025 Round 2 final | 30 Aug 2025 | 6,182 | 112 | 315 | 70,169–1,318,975 | 6,056 Allotted; 126 Reported [^2] |
| 2025 Round 3 final | 23 Sep 2025 | 6,251 | 119 | 336 | 72,124–1,318,975 | 3,226 Allotted; 3,025 Reported [^1] |
| 2026 Round 1 final | 16 Oct 2026 | 4,984 | 98 | 283 | 8,330–1,194,260 | 4,984 Allotted [^3] |

The 2025 Round 3 file is mislabeled in its filename as “R2” but its document title clearly says **3rd Round Final**. Likewise, the two 2025 Round 2 files have different filenames but identical content.[^4][^1][^2]

The row counts above are allotment-list records, **not sanctioned seat capacity**. An allotment list can include candidates retained from earlier rounds—as shown by the large “Reported” population in 2025 Round 3—and therefore must not be treated as a clean vacancy or intake matrix.[^1]

## Programme mix

| Edition | BAMS records | BHMS records | BUMS records |
|---|---:|---:|---:|
| 2025 Round 2 | 5,443 | 573 | 166 [^2] |
| 2025 Round 3 | 5,433 | 627 | 191 [^1] |
| 2026 Round 1 | 4,259 | 725 | 0 [^3] |

The absence of BUMS in 2026 Round 1 is a major scope break. It does **not** establish that Karnataka has no BUMS seats in 2026; it establishes only that the uploaded Round 1 allotment list contains no BUMS records. A third-party report says the 2026 matrix covered 4,578 BAMS/BHMS seats across 66 colleges, consistent with a BAMS/BHMS-only phase, but the attached official allotment PDF remains the controlling source for this analysis.[^5][^3]

The 2026 list also has a higher BHMS representation: 725 records versus 573 in 2025 Round 2. That rise coexists with a smaller total list, so comparisons of overall closing AIR without controlling for programme and seat type would be misleading.[^2][^3]

## Seat-label changes

| Economic seat class | 2025 label | 2026 label | Typical fee in file |
|---|---|---|---:|
| Government college | BAMS/BHMS-Govt | BAMS/BHMS-Govt | BAMS: ₹30,335 in 2026 vs ₹25,000 in 2025; some aided/private-government quota seats ₹60,000–₹75,000 [^2][^3] |
| Private/open quota | BAMS/BHMS-Priv | BAMS/BHMS-Priv | BAMS: ₹300,000 in 2026 vs ₹250,000 in 2025; BHMS: ₹275,000 vs ₹225,750 [^2][^3] |
| Higher-fee/other quota | “OTHERS” | “MNG” | BAMS usually ₹400,000, with some ₹500,000 [^2][^3] |
| NRI | NRI | NRI | ₹600,000 in both datasets [^2][^3] |

The renaming from **OTHERS** to **MNG** appears to represent a coding change rather than a directly comparable new class: both largely carry category OTH and similar ₹400,000 pricing. It is still safer to call them “economically analogous” rather than formally identical without the 2026 seat matrix and fee notification.[^3][^2]

The 2026 fee shifts are material. Within the files, government-college fees rise from ₹25,000 to ₹30,335; BAMS private/open rises from ₹250,000 to ₹300,000; and BHMS private/open rises from ₹225,750 to ₹275,000.[^2][^3]

## Demand by quota

In 2026 Round 1, OTH is the largest allotment category with 1,944 records, followed by OPN with 886 and GM with 773. The list also contains redesigned category codes such as S1G, S2G, and S3G, which further limits direct category-by-category comparison with 2025.[^3]

The maximum AIR in a broad segment should not be called “the cutoff” because it can come from a special category, minority/management seat, or low-demand college. For example, 2026 BAMS-Govt records extend beyond AIR 1 million, while the **college-level GM closings** range only from 132,093 to 345,256 across the 83 BAMS-Govt codes having GM allotments.[^3]

## GM cutoff movement

| Course | 2025 R2 codes | 2025 R2 median close | 2025 R3 median close | 2026 R1 codes | 2026 R1 median close |
|---|---:|---:|---:|---:|---:|
| BAMS-Govt | 91 | 195,732 | 211,404 | 83 | 260,770 [^1][^2][^3] |
| BHMS-Govt | 17 | 488,440 | 511,088 | 15 | 452,331 [^1][^2][^3] |
| BUMS-Govt | 4 | 350,696 | 463,648 | 0 | Not present [^1][^2][^3] |

The BAMS-Govt pattern is clear: even Round 1 of 2026 generally closes at numerically higher AIRs than Round 2 of 2025. Among the 94 exact codes matched across those editions, 75% show at least an 18.3% increase and the median increase is 30.3%; however, one extreme negative movement means this is not universal at every code.[^2][^3]

BHMS behaves differently. Its median government GM closing AIR is lower in 2026 Round 1 than in 2025 Round 2, even though some individual 2026 colleges close far later. This mixed picture makes course-specific and college-specific matching essential.[^2][^3]

## BAMS-Govt leaders

The table below uses the **last GM allotment observed for each exact course code**, not the last rank across all reservation categories.

| 2026 demand order | Code | College (short name) | 2025 R2 GM close | 2025 R3 GM close | 2026 R1 GM close |
|---:|---|---|---:|---:|---:|
| 1 | I714AG | SDM Ayurveda, Hassan | 93,426 | 100,022 | 132,093 [^1][^2][^3] |
| 2 | I701AG | Government Ayurveda, Bengaluru | 89,120 | 97,432 | 134,418 [^1][^2][^3] |
| 3 | I713AG | Government Ayurveda, Mysuru | 100,726 | 107,375 | 148,122 [^1][^2][^3] |
| 4 | I750AG | Taranatha Government Ayurveda, Ballari | 101,476 | 114,631 | 152,508 [^1][^2][^3] |
| 5 | I764AG | SDM Institute, Bengaluru | 122,825 | 122,825 | 162,786 [^1][^2][^3] |
| 6 | I719AG | SDM Ayurveda, Udupi | 96,285 | 102,817 | 162,925 [^1][^2][^3] |
| 7 | I780AG | Government Ayurveda, Shivamogga | 113,699 | 124,340 | 167,833 [^1][^2][^3] |
| 8 | I712AG | JSS Ayurveda, Mysuru | 118,600 | 129,930 | 183,531 [^1][^2][^3] |
| 9 | I748AG | N. K. Jabshetty Ayurveda, Bidar | 105,765 | 105,765 | 184,904 [^1][^2][^3] |
| 10 | I728AG | Ayurveda Mahavidyalaya, Hubballi | 127,822 | 135,251 | 187,673 [^1][^2][^3] |

A lower closing AIR indicates stronger competition. On this measure, SDM Hassan slightly outranks Government Ayurveda Bengaluru in 2026 Round 1, although Government Bengaluru was tighter in both 2025 Round 2 and Round 3.[^1][^3][^2]

## Round 2 scenarios

For exactly matched BAMS-Govt GM codes in 2025, the Round 3-to-Round 2 closing-rank ratio had a median of **1.065**, an interquartile range of **1.029–1.108**, and a 10th–90th percentile range of roughly **1.000–1.141**.[^1][^2]

Applying those historical multipliers to 2026 Round 1 creates a planning band:

| 2026 R1 GM close | Conservative 1.03× | Central 1.065× | Loose 1.14× |
|---:|---:|---:|---:|
| 135,000 | 139,000 | 144,000 | 154,000 |
| 175,000 | 180,000 | 186,000 | 200,000 |
| 225,000 | 232,000 | 240,000 | 257,000 |
| 275,000 | 283,000 | 293,000 | 314,000 |
| 325,000 | 335,000 | 346,000 | 371,000 |

This is an **empirical scenario**, not an official prediction. The available historical comparison is Round 2 to Round 3, while the target is Round 1 to Round 2; movement may differ because of vacancies, option-entry rules, new colleges, seat conversion, reporting behavior, and the composition of the 2026 matrix.[^1][^3][^2]

A practical probability rule can nevertheless be used for BAMS-Govt GM:

- **Strong**: candidate AIR is better than or equal to the 2026 Round 1 close.
- **Competitive**: AIR falls between the Round 1 close and about 1.065 times that close.
- **Reach**: AIR falls between about 1.065 and 1.14 times that close.
- **Speculative**: AIR is worse than 1.14 times the Round 1 close; include lower-demand alternatives and higher-fee quotas.

For BHMS-Govt GM, 2025 movement was far flatter: the matched-code median multiplier was about 1.00 and the upper quartile about 1.011. The historical sample is small, so the safe approach is to use each college’s 2026 Round 1 closing AIR with only a modest relaxation unless the Round 2 vacancy matrix indicates otherwise.[^3][^1][^2]

## Data-quality warnings

One 2026 row lists AIR **8,330** for I764AG, followed by the next entry at AIR 82,579. It is the only 2026 AIR below 50,000 and is therefore a likely typographical or source-data anomaly; it should not be used as an opening cutoff without candidate-level verification.[^3]

The 2026 file contains one duplicated AIR assigned to two different rows, while 2025 editions have no repeated AIRs. This may represent a transcription/data issue or a rank tie, so rank-level joins should not assume AIR is a unique key.[^3]

College names vary in punctuation and spelling across years, but the stable four-character institutional stem—such as I701, I714, or I764—allows reliable matching. Comparisons in this report use course code rather than fuzzy college-name matching.[^1][^2][^3]

## Strategy implications

1. **Use code-level cutoffs.** Match the exact course code, course type, category, and fee class; a broad “BAMS cutoff” is not decision-grade.
2. **Do not equate OTHERS and MNG blindly.** They look economically analogous, but official quota definitions should be checked in the 2026 seat matrix.
3. **Budget for the new fee structure.** The uploaded file shows 2026 private/open BAMS at ₹300,000 and BHMS at ₹275,000, above the 2025 values.[^2][^3]
4. **Keep options beyond Round 2.** Karnataka AYUSH counselling can continue through later and stray rounds; the official KEA UGNEET page should be monitored rather than relying on predicted dates.[^6][^7]
5. **Treat every forecast as conditional.** Final availability depends on the official vacancy matrix, option-entry population, category conversion, and reporting/upgrade choices.

## Bottom line

The 2026 Round 1 BAMS-Govt GM market is broadly less rank-restrictive than 2025 for matched colleges, with a median year-on-year closing-rank relaxation of about 30%. A reasonable first-pass Round 2 planning range is the college’s actual 2026 Round 1 GM close multiplied by roughly **1.03–1.14**, centered near **1.065**, but the official Round 2 matrix can override this historical pattern.[^1][^2][^3]

For a personalized option list, the necessary inputs are AIR, Karnataka category including rural/Kannada/Hyderabad-Karnataka suffixes, domicile/eligibility, acceptable programme, maximum annual fee, and location constraints.

---

## References

1. [UGNEET_ALLOT_2025_R2_prov_2ND_FIN_AYU_23092025.pdf](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/13793017/72308094-19ed-411c-ba90-ff9fed22f7ab/UGNEET_ALLOT_2025_R2_prov_2ND_FIN_AYU_23092025.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Checksum-Mode=ENABLED&X-Amz-Credential=ASIA2F3EMEYESYAYSKH5%2F20261021%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261021T155241Z&X-Amz-Expires=3235&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDJxT2msn8GKXuy8UPKZUtxETaV27HJKRDOhchlG47DtQIgd023Jv9pvwp%2BsZkVmuEABFINiirbLihOdHMlx6HOAesqgAUIYRABGgw2OTk3NTMzMDk3MDUiDJ%2FyWoAlvQEOvymM%2FyrdBJ0Fa9G04vurQ2gaSVudQZWFzM44k9YbMYqUlqdNpFv1k7zE1ibcPuly%2BEp9Jlm8wmU7OesqA1Dq0PDNmnnKpwcnNNbEg79ThAIquRoXqyY5i7DFl18LdfJ26Dud1PVBcUwbpifi6vE4uqilTj7zHzzn0WQZovAJfBB%2BOFrNUKfYGjvreEEWiKoL80nOHtm6xW6RoUW26phzmwmPOCbhBB4tQa9Kczcq0fp5mU%2FXOZw2CwQVMp1AMmp2%2Bx3teFZJ5ALIBIy%2B4NpPFk4w6kjEBxRKoh0OmMwQ7b%2FNDNXBQP%2BR3qql4l4wP7KxFYHJKyXrxnJcAzCHD56bIvX0BKUPkUmC79XS2PQ0%2FkUO4RR5Fhi0Lv4p9TE9uBRdjK6zCRuQGZgHd6bGMsNta5vYjxu%2Bt5eOHeJmzBxa9hxdYr7TA4ozK9d1hspEG%2BN7jWqj8q5IZgGVr1AECHythaTrkCzROdmKHD%2BN5zlqPuUos%2BYdbemvrpciwGaFafYqD20YsC5NHLdd1TnM9jBMGLXaM8NjryhQ%2BPqH3pHnO28TvdAZcLuiLz3BDjDNimbs%2BtKv7kGlOXxMb9wTmU46JA%2Fs%2F4lYjSQ8xQDpQ1EjX6ncVZcRa3inKwahE5dXIHDWzIjf7%2FGnL0tS5aetzhb01L%2FL5ZYl2v7KHKaoe1SDti4vDU1umzRRKCHNynUkDNs%2FqfxPscDmn4EtD%2F2g3kNDUT4I5ZQPZbXVPyBRonfD44sA1%2BPchKEg0P9Wv0hgRbeKTMQul%2FADkYciuFVJ1BWIdEXr5SHJywUKUPUH41%2BSPBTABZAVMJm949YGOpgBc5GKHWjrGABm0hY57%2B3OQbRje%2Fe4aMuuk1h7vZ7xR4ntOMSoLGD2YaUo%2Fi2VnSG7CQq1g5xBoGfGcmdQMZ0PsDJiPQP0gSqeOyqsY7NBa%2B4cHXDHymAmPuFbOkiJzCA2ZdG0Wuuws47ELwqrmrrREAw04h%2BnW3mmnbj%2FOdxdpxpSc2GI2uaMMCGW35tjOCJO7adUp6XhMI4%3D&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=6c37220623bb3d6e46578991a89139f2c609f9b806dce28073834e003970196d) - SEAT ALLOTMENT LIST 23-09-2025 Karnataka Examinations Authority

2. [UGNEET_ALLOT_2025_R2_Final_AYUSH30082025english.pdf](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/13793017/a63bd665-26cc-46e4-8e88-cbc3eb8f1229/UGNEET_ALLOT_2025_R2_Final_AYUSH30082025english.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Checksum-Mode=ENABLED&X-Amz-Credential=ASIA2F3EMEYESYAYSKH5%2F20261021%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261021T155241Z&X-Amz-Expires=3235&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDJxT2msn8GKXuy8UPKZUtxETaV27HJKRDOhchlG47DtQIgd023Jv9pvwp%2BsZkVmuEABFINiirbLihOdHMlx6HOAesqgAUIYRABGgw2OTk3NTMzMDk3MDUiDJ%2FyWoAlvQEOvymM%2FyrdBJ0Fa9G04vurQ2gaSVudQZWFzM44k9YbMYqUlqdNpFv1k7zE1ibcPuly%2BEp9Jlm8wmU7OesqA1Dq0PDNmnnKpwcnNNbEg79ThAIquRoXqyY5i7DFl18LdfJ26Dud1PVBcUwbpifi6vE4uqilTj7zHzzn0WQZovAJfBB%2BOFrNUKfYGjvreEEWiKoL80nOHtm6xW6RoUW26phzmwmPOCbhBB4tQa9Kczcq0fp5mU%2FXOZw2CwQVMp1AMmp2%2Bx3teFZJ5ALIBIy%2B4NpPFk4w6kjEBxRKoh0OmMwQ7b%2FNDNXBQP%2BR3qql4l4wP7KxFYHJKyXrxnJcAzCHD56bIvX0BKUPkUmC79XS2PQ0%2FkUO4RR5Fhi0Lv4p9TE9uBRdjK6zCRuQGZgHd6bGMsNta5vYjxu%2Bt5eOHeJmzBxa9hxdYr7TA4ozK9d1hspEG%2BN7jWqj8q5IZgGVr1AECHythaTrkCzROdmKHD%2BN5zlqPuUos%2BYdbemvrpciwGaFafYqD20YsC5NHLdd1TnM9jBMGLXaM8NjryhQ%2BPqH3pHnO28TvdAZcLuiLz3BDjDNimbs%2BtKv7kGlOXxMb9wTmU46JA%2Fs%2F4lYjSQ8xQDpQ1EjX6ncVZcRa3inKwahE5dXIHDWzIjf7%2FGnL0tS5aetzhb01L%2FL5ZYl2v7KHKaoe1SDti4vDU1umzRRKCHNynUkDNs%2FqfxPscDmn4EtD%2F2g3kNDUT4I5ZQPZbXVPyBRonfD44sA1%2BPchKEg0P9Wv0hgRbeKTMQul%2FADkYciuFVJ1BWIdEXr5SHJywUKUPUH41%2BSPBTABZAVMJm949YGOpgBc5GKHWjrGABm0hY57%2B3OQbRje%2Fe4aMuuk1h7vZ7xR4ntOMSoLGD2YaUo%2Fi2VnSG7CQq1g5xBoGfGcmdQMZ0PsDJiPQP0gSqeOyqsY7NBa%2B4cHXDHymAmPuFbOkiJzCA2ZdG0Wuuws47ELwqrmrrREAw04h%2BnW3mmnbj%2FOdxdpxpSc2GI2uaMMCGW35tjOCJO7adUp6XhMI4%3D&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=2c71a50aa3954878e7b8328ec989aea5e79a2471edff45c5f2ebd92f65cd3e6d) - SEAT ALLOTMENT LIST 30-08-2025 Karnataka Examinations Authority

3. [UGNEET_ALLOT_2026_AYUSH_R1_finalenglish_393a9af8f868a4efc9ed90ef97b42626.pdf](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/13793017/86149ee5-e19c-4b65-8e53-360305144ccb/UGNEET_ALLOT_2026_AYUSH_R1_finalenglish_393a9af8f868a4efc9ed90ef97b42626.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Checksum-Mode=ENABLED&X-Amz-Credential=ASIA2F3EMEYESYAYSKH5%2F20261021%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261021T155241Z&X-Amz-Expires=3235&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDJxT2msn8GKXuy8UPKZUtxETaV27HJKRDOhchlG47DtQIgd023Jv9pvwp%2BsZkVmuEABFINiirbLihOdHMlx6HOAesqgAUIYRABGgw2OTk3NTMzMDk3MDUiDJ%2FyWoAlvQEOvymM%2FyrdBJ0Fa9G04vurQ2gaSVudQZWFzM44k9YbMYqUlqdNpFv1k7zE1ibcPuly%2BEp9Jlm8wmU7OesqA1Dq0PDNmnnKpwcnNNbEg79ThAIquRoXqyY5i7DFl18LdfJ26Dud1PVBcUwbpifi6vE4uqilTj7zHzzn0WQZovAJfBB%2BOFrNUKfYGjvreEEWiKoL80nOHtm6xW6RoUW26phzmwmPOCbhBB4tQa9Kczcq0fp5mU%2FXOZw2CwQVMp1AMmp2%2Bx3teFZJ5ALIBIy%2B4NpPFk4w6kjEBxRKoh0OmMwQ7b%2FNDNXBQP%2BR3qql4l4wP7KxFYHJKyXrxnJcAzCHD56bIvX0BKUPkUmC79XS2PQ0%2FkUO4RR5Fhi0Lv4p9TE9uBRdjK6zCRuQGZgHd6bGMsNta5vYjxu%2Bt5eOHeJmzBxa9hxdYr7TA4ozK9d1hspEG%2BN7jWqj8q5IZgGVr1AECHythaTrkCzROdmKHD%2BN5zlqPuUos%2BYdbemvrpciwGaFafYqD20YsC5NHLdd1TnM9jBMGLXaM8NjryhQ%2BPqH3pHnO28TvdAZcLuiLz3BDjDNimbs%2BtKv7kGlOXxMb9wTmU46JA%2Fs%2F4lYjSQ8xQDpQ1EjX6ncVZcRa3inKwahE5dXIHDWzIjf7%2FGnL0tS5aetzhb01L%2FL5ZYl2v7KHKaoe1SDti4vDU1umzRRKCHNynUkDNs%2FqfxPscDmn4EtD%2F2g3kNDUT4I5ZQPZbXVPyBRonfD44sA1%2BPchKEg0P9Wv0hgRbeKTMQul%2FADkYciuFVJ1BWIdEXr5SHJywUKUPUH41%2BSPBTABZAVMJm949YGOpgBc5GKHWjrGABm0hY57%2B3OQbRje%2Fe4aMuuk1h7vZ7xR4ntOMSoLGD2YaUo%2Fi2VnSG7CQq1g5xBoGfGcmdQMZ0PsDJiPQP0gSqeOyqsY7NBa%2B4cHXDHymAmPuFbOkiJzCA2ZdG0Wuuws47ELwqrmrrREAw04h%2BnW3mmnbj%2FOdxdpxpSc2GI2uaMMCGW35tjOCJO7adUp6XhMI4%3D&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=a336b06e98b41e37fb7f5302f2bd41cf0f794e851c77a97e6fca69cc86294489)

4. [UGNEET_ALLOT_2025_R2_Final_AYUSH_30082025english.pdf](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/13793017/7c43d403-eade-4ce4-9481-d616cf9569fa/UGNEET_ALLOT_2025_R2_Final_AYUSH_30082025english.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Checksum-Mode=ENABLED&X-Amz-Credential=ASIA2F3EMEYESYAYSKH5%2F20261021%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261021T155241Z&X-Amz-Expires=3235&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDJxT2msn8GKXuy8UPKZUtxETaV27HJKRDOhchlG47DtQIgd023Jv9pvwp%2BsZkVmuEABFINiirbLihOdHMlx6HOAesqgAUIYRABGgw2OTk3NTMzMDk3MDUiDJ%2FyWoAlvQEOvymM%2FyrdBJ0Fa9G04vurQ2gaSVudQZWFzM44k9YbMYqUlqdNpFv1k7zE1ibcPuly%2BEp9Jlm8wmU7OesqA1Dq0PDNmnnKpwcnNNbEg79ThAIquRoXqyY5i7DFl18LdfJ26Dud1PVBcUwbpifi6vE4uqilTj7zHzzn0WQZovAJfBB%2BOFrNUKfYGjvreEEWiKoL80nOHtm6xW6RoUW26phzmwmPOCbhBB4tQa9Kczcq0fp5mU%2FXOZw2CwQVMp1AMmp2%2Bx3teFZJ5ALIBIy%2B4NpPFk4w6kjEBxRKoh0OmMwQ7b%2FNDNXBQP%2BR3qql4l4wP7KxFYHJKyXrxnJcAzCHD56bIvX0BKUPkUmC79XS2PQ0%2FkUO4RR5Fhi0Lv4p9TE9uBRdjK6zCRuQGZgHd6bGMsNta5vYjxu%2Bt5eOHeJmzBxa9hxdYr7TA4ozK9d1hspEG%2BN7jWqj8q5IZgGVr1AECHythaTrkCzROdmKHD%2BN5zlqPuUos%2BYdbemvrpciwGaFafYqD20YsC5NHLdd1TnM9jBMGLXaM8NjryhQ%2BPqH3pHnO28TvdAZcLuiLz3BDjDNimbs%2BtKv7kGlOXxMb9wTmU46JA%2Fs%2F4lYjSQ8xQDpQ1EjX6ncVZcRa3inKwahE5dXIHDWzIjf7%2FGnL0tS5aetzhb01L%2FL5ZYl2v7KHKaoe1SDti4vDU1umzRRKCHNynUkDNs%2FqfxPscDmn4EtD%2F2g3kNDUT4I5ZQPZbXVPyBRonfD44sA1%2BPchKEg0P9Wv0hgRbeKTMQul%2FADkYciuFVJ1BWIdEXr5SHJywUKUPUH41%2BSPBTABZAVMJm949YGOpgBc5GKHWjrGABm0hY57%2B3OQbRje%2Fe4aMuuk1h7vZ7xR4ntOMSoLGD2YaUo%2Fi2VnSG7CQq1g5xBoGfGcmdQMZ0PsDJiPQP0gSqeOyqsY7NBa%2B4cHXDHymAmPuFbOkiJzCA2ZdG0Wuuws47ELwqrmrrREAw04h%2BnW3mmnbj%2FOdxdpxpSc2GI2uaMMCGW35tjOCJO7adUp6XhMI4%3D&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=f0aa69b0d83cbb60327a79538bc9acd29f7ac513ef28c53adc006ab681848fcd) - SEAT ALLOTMENT LIST 30-08-2025 Karnataka Examinations Authority

5. [articles.findmycollege.com › news › kea-ayush-ugKEA AYUSH UG 2026 seat matrix released: 4,578 seats across 66 ...](https://articles.findmycollege.com/news/kea-ayush-ug-2026-seat-matrix-released-4578-seats-across-66-colleges/) - |Karnataka AYUSH UG 2026 round 1 mock allotment released; option entry open until October 14|Chhatti...

6. [ಯುಜಿ ನೀಟ್-2026 (Medical/Dental/AYUSH)](https://cetonline.karnataka.gov.in/kea/ugneet2026) - ಯುಜಿ ನೀಟ್-2026 (Medical/Dental/AYUSH) · UGNEET 2026 SECOND ROUND Medical Provisional seat matrix . ·...

7. [Karnataka AYUSH Counselling 2026 - BAMS, BHMS Guide](https://collegesinfo.org/karnataka-ayush-counselling) - KEA conducts common counselling for admission to UG Medical, Dental, and AYUSH seats in Karnataka as...

