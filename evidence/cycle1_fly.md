# Evidence brief - 2026 Drosophila MVA model: rapamycin vs chaperone/ROS/apoptosis rescue arms

**Adjudication question:** In the 2026 Drosophila model of MVA (PMID 41820377), what exactly did rapamycin rescue, what did it FAIL to rescue, and how large was the chaperone-overexpression rescue?

**Source:** González-Blanco A, Acuña-Higaki A, Boettger D, Joy J, Milán M. *Proteostasis failure and mitochondrial dysfunction contribute to chromosomal instability-induced microcephaly.* Nat Commun 17:3829 (2026). PMID 41820377; PMC13121444; doi:10.1038/s41467-026-70521-0. Full text retrieved via PubMed Central MCP (full text) and Europe PMC fullTextXML (figure-verified); quantitative values from the published Source Data workbook `41467_2026_70521_MOESM9_ESM.xlsx` (sheets "Figure S6", "Figure 6", "Figure 7"), downloaded from the Europe PMC supplementary-files endpoint for PMC13121444.

**Termination criterion (declared up front):** primary source = the article itself (full text + source data); every quote below is verbatim from the PMC full text; all numbers are recomputed/read from the authors' own Source Data file. No secondary sources required; none used.

---

## 0. Model identity - important caveat on the "BUB1B" framing

The fly model does **not** deplete BubR1 (BUB1B). It depletes two other SAC genes, in neural stem cells only:

> "We used the worniu-gal4 driver to induce chronic expression of RNAi forms against the SAC genes bub3 or rod specifically in NBs..." (Results, "Targeted depletion of SAC genes in neural stem cells induces microcephaly")

> "Here we generated a Drosophila model of MVA-driven microcephaly by targeting the SAC genes bub3 or rod specifically in the neural stem cell (NSC) compartment." (Discussion)

The rescue experiments shown in Fig. 6/7 and Supplementary Fig. 6 use **bub3-RNAi** (wor> bub3-i) throughout. The paper is a cell-autonomous NSC study; there are **no immune/NK/surveillance readouts of any kind** (the fly larval CNS lacks an NK-cell equivalent), so this model cannot directly test the mTORC1-immunosuppression/NK-clearance penalty claim (PMID 28633018) in either direction.

---

## 1. Rapamycin arm

### Dose and protocol (Methods, "Rapamycin treatment"):
> "Flies of interest were crossed and allowed to lay eggs for 12 h at 25 °C. Larvae were then kept for 48 h AEL at 25 °C before being shifted to 29 °C for 24 h. Afterwards, rapamycin was added to reach a final concentration of 40 µM, while controls received DMSO at a final concentration of 0.4%. Larvae were maintained for approximately 48 h more at 29 °C and then dissected."

i.e. 40 µM rapamycin in the food for the final ~48 h of larval development, in bub3-RNAi (CIN) larvae; vehicle control 0.4% DMSO. Data shown only in **Supplementary Fig. 6C** (not a main figure).

### What rapamycin RESCUED - neuroblast (NSC) number:
> "Interestingly, boosting autophagy (by overexpressing Atg1 or depleting the activity of Tor through Rheb depletion or the use of Tor mutants in heterozygosis) led to a significant rescue of the number of aneuploid NBs in mature CIN brains, without causing any major effect in otherwise control brains (Fig. 6D and Supplementary Fig. 6A). **A similar result was obtained by feeding larvae with the TOR inhibitor Rapamycin (Supplementary Fig. 6C).**" (Results, "Proteostasis failure and mitochondrial dysfunction contribute to the loss of stemness")

### What rapamycin/TOR inhibition FAILED to rescue - progeny cells and brain size:
> "However, we noticed that none of the genetic interventions aimed at increasing autophagy was able to rescue the number of Pros+ cells or the size of the larval brain (Fig. 6E and Supplementary Fig. 6C). These results suggest that TOR inhibition or non-physiological levels of autophagy might have a negative impact on the proliferative capacity of highly aneuploid NBs." (same section)

> "Activation of autophagy in these cells either by overexpression of Atg1 or depletion of TOR was able to partially rescue the reduced number of NSCs observed in SAC-depleted brains. The genetic interventions performed were unsuccessful in restoring progeny cell numbers or brain size. Future studies are required to ascertain whether TOR inhibition or aberrant autophagy levels negatively impact the proliferative capacity of highly aneuploid NSCs." (Discussion)

### Quantification from Source Data (sheet "Figure S6", unpaired t-tests reported by authors):
| Readout | bub3-i + DMSO | bub3-i + RAPA | Effect | Authors' statistic |
|---|---|---|---|---|
| NBs/lobe | mean 23.58 (n=12) | mean 28.44 (n=18) | +4.9 NBs (~+21%), significant *rescue* | t=2.125, df=28, p=0.0426 (*) |
| Brain lobe size (µm²) | mean 37,719 (n=12) | mean 29,698 (n=19) | **−8,022 µm² (~−21%), significant *reduction*** | t=2.139, df=29, p=0.041 (*) |

**So rapamycin did not merely fail to rescue brain size - it significantly shrank CIN brains further relative to DMSO-treated CIN larvae** (per the authors' own t-test). Pros+ progeny counts were also not rescued (grouped with the genetic autophagy interventions; Fig. 6E source data: bub3-i 394 Pros+ cells vs bub3-i+Atg1 479 vs control 977). No survival/eclosion readout was reported for rapamycin. Genetic parallels of the same arm (Atg1 OE, Rheb RNAi, Tor heterozygous mutants): NBs partially rescued (e.g. 20.3 → 28.5 with Atg1 vs control 53.4); brain size not rescued (bub3-i 33,664; bub3-i+Atg1 38,527; control 46,791).

---

## 2. Chaperone-overexpression arm (mitochondrial chaperones)

Intervention: NB-specific overexpression of mitochondria-specific chaperones **Hsp60 + Hsp60c** (wor-GAL4 > UAS-hsp60, UAS-hsp60c) in bub3-RNAi larvae.

> "Consistent with this, overexpression of mitochondria-specific chaperones Hsp60 and Hsp60c, or ROS scavengers Sod2 and GTPx-1 was able to significantly rescue the number of aneuploid NBs observed in mature CIN brains, without causing any major effect in otherwise control brains (Fig. 7E and Supplementary Fig. 7A). These genetic interventions also rescued the number of Pros+ cells (Fig. 7E) and, most interestingly, yielded a complete restoration of brain size (Fig. 7G and Supplementary Fig. 7A)." (Results)

> "The observation that overexpression of ROS scavengers and mitochondrial chaperones in NB cells fully restored brain size, but only partially NB cell counts, points to a role of mitochondrial dysfunction in compromising not only the fitness but also the mitotic activity of highly aneuploid NBs." (Results)

> "We noticed that the number of aneuploid NBs was not fully rescued by any of these genetic interventions, most probably as a result of the highly pleiotropic effects of aneuploidy on cell physiology and on the fact that the complete loss of chromosomes is incompatible with cell viability. By contrast, overexpression of mitochondrial chaperones or ROS scavengers significantly rescued the number of progeny cells and fully restored brain size." (Discussion)

### Quantification from Source Data (sheet "Figure 7", authors' Tukey ANOVA):
| Readout | Control (wor>) | CIN (bub3-i) | CIN + Hsp60/Hsp60c | Chaperones alone | Verdict |
|---|---|---|---|---|---|
| NBs/lobe | 49.8 | 21.5 | 32.0 | 51.5 | Partial (~+10.5 of a ~28-cell deficit, ~37% of deficit); still significantly below control (Tukey "wor> bub3i, hsp60, hsp60c vs. wor>" mean diff −17.85, ****) |
| Pros+ cells/lobe | 1,099.5 | 483.5 | 711.8 | 938.2 | Significant partial (~46% of deficit); still below control (Tukey −387.8, ***) |
| Brain lobe size (µm²) | 41,728 | 35,471 | **46,519** | 46,368 | **Complete restoration - n.s. vs control** (Tukey "wor> vs. > bub3-i, hsp60, hsp60c" mean diff −634, p=0.9946); vs CIN −11,048, p=0.0022 |

**Size of the chaperone rescue: brain lobe area fully restored to control (46,519 vs 41,728 µm²; statistically indistinguishable, p=0.99), NB counts only partially rescued (21.5 → 32.0 vs control 49.8), progeny (Pros+) counts ~half restored (483 → 712 vs control 1,100).**

---

## 3. ROS-scavenger arm (Sod2 + GTPx-1) - for comparison

> (quote as in §2: "overexpression of mitochondria-specific chaperones Hsp60 and Hsp60c, or ROS scavengers Sod2 and GTPx-1...")

Source Data (sheet "Figure 7"): NBs/lobe 20.3 (CIN) → 28.8 (+Sod2/GTPx-1) vs control 53.4 (partial; Tukey bub3-i vs bub3-i+sod2/GTPx-1: −8.45, p=0.0013). Brain lobe size 37,658 → **50,365** vs control 52,167 - **complete restoration** (Tukey "wor> vs. > bub3-i, GTPX1, sod2" mean diff +1,802, p=0.9354, n.s.). Pros+ cells (chaperone panel shown; ROS panel analogous): partial.

## 4. Apoptosis-inhibition arm (p35) - the other full brain-size rescue

> "Notably, the inhibition of apoptosis through p35 expression rescued the number of Pros+ cells and resulted in a complete restoration of brain size (Supplementary Fig. 4C" and Supplementary Fig. 7B), despite no concomitant rescue of NB numbers. These findings can be explained by inheritance of p35 by progeny cells and points to a role of apoptosis in the elimination of these cells." (Results)

## 5. Authors' own interpretation of partial-vs-full rescue and translational relevance

> "The experimental observations that these genetic interventions rescue brain size without fully rescuing NSC numbers point to existing homeostatic mechanisms aimed at restoring brain size in a situation of NSC depletion. Whether these homeostatic mechanisms rely on the ability of progeny cells to over proliferate in order to restore the final number of neurons and glial cells remains to be elucidated." (Discussion)

> "Thus, genetic interventions aimed at restoring mitochondria homeostasis or blocking apoptosis will undoubtedly offer new opportunities for drug discovery and disease treatment." (Discussion)

Note: the authors' forward-looking translational sentence names **mitochondrial-homeostasis restoration and apoptosis blockade** - NOT rapamycin/TOR inhibition, which they instead flag as possibly harmful ("Future studies are required to ascertain whether TOR inhibition or aberrant autophagy levels negatively impact the proliferative capacity of highly aneuploid NSCs").

---

## Readout-by-readout master table (all arms, bub3-RNAi CIN model)

| Intervention | NB (NSC) number | Pros+ progeny cells | Brain lobe size | Survival |
|---|---|---|---|---|
| **Rapamycin 40 µM food, ~48 h** (Suppl Fig 6C) | Significant partial rescue (+4.9; 23.6→28.4; p=0.043) | **Not rescued** | **Not rescued - significantly WORSE (−8,022 µm²; p=0.041)** | not tested |
| Atg1 OE (Fig 6D,E) | Significant partial (20.3→28.5 vs ctrl 53.4) | Not rescued (394→479 vs ctrl 977) | Not rescued (33.7k→38.5k vs ctrl 46.8k) | - |
| Rheb RNAi / Tor+ heterozygous (Fig 6D,E) | Significant partial (16.7→25.7 / 23.8 vs ctrl 51.6) | Not rescued | Not rescued | - |
| **Hsp60 + Hsp60c OE** (Fig 7E,G) | Significant partial (21.5→32.0 vs ctrl 49.8; still p<0.0001 below ctrl) | Significant partial (484→712 vs ctrl 1,100) | **COMPLETE restoration (35.5k→46.5k vs ctrl 41.7k; n.s. vs ctrl, p=0.99)** | - |
| Sod2 + GTPx-1 OE (Fig 7E,G) | Significant partial (20.3→28.8 vs ctrl 53.4) | (partial, analogous) | **COMPLETE restoration (37.7k→50.4k vs ctrl 52.2k; n.s. vs ctrl, p=0.94)** | - |
| p35 caspase inhibitor (Suppl Fig 7B) | **No rescue** of NB number | Rescued | **COMPLETE restoration** | - |

All values are means per brain lobe from the authors' Source Data (MOESM9); "complete" = post-hoc Tukey n.s. vs concurrent control.

## Analysis / adjudication notes

1. **Rapamycin in this model is a one-readout partial rescue that worsens the primary organ-level outcome.** It modestly increased NB counts (+~5 cells, p=0.043) but significantly *reduced* brain lobe size in CIN larvae (~−21%, p=0.041) and did not restore progeny-cell number. The authors' own mechanistic reading: TOR inhibition/non-physiological autophagy may impair the proliferative capacity of highly aneuploid NSCs.
2. **The strong rescue in this model is mitochondrial (Hsp60/Hsp60c chaperones, Sod2/GTPx-1 ROS scavengers) and anti-apoptotic (p35)** - both fully restore brain size (n.s. vs control) despite only partial NB-count rescue.
3. **Relevance to everolimus/rapalog candidacy:** the fly data provide no support for rapamycin as a brain-rescuing intervention in constitutive SAC deficiency; if anything they harden the PENALIZE side on organ-growth grounds (cell-autonomous anti-proliferative effect on aneuploid NSCs), which is mechanistically distinct from the NK-cell immunosurveillance argument (PMID 28633018) but points the same direction for this disease context. Caveats for extrapolation: (a) the model targets bub3/rod, not BUB1B/BubR1; (b) NSC-cell-autonomous larval brain growth, no immune system, no tumor-predisposition readout; (c) rapamycin was dosed only in a ~48 h larval window at 40 µM in food, not chronically.
4. Confidence in these statements: **high** for what the paper reports (verbatim quotes + authors' own source-data statistics recomputed); **low-to-moderate** only for extrapolation to human MVA1/BUB1B, which the paper itself does not attempt beyond the drug-discovery sentence naming mitochondrial homeostasis and apoptosis.

## References

- González-Blanco, A., Acuña-Higaki, A., Boettger, D., Joy, J., & Milán, M. (2026). Proteostasis failure and mitochondrial dysfunction contribute to chromosomal instability-induced microcephaly. *Nature Communications, 17*, 3829. https://doi.org/10.1038/s41467-026-70521-0 (PMID 41820377; PMCID PMC13121444; retrieved via PubMed/PMC and Europe PMC, 2026-09-12).
- Source Data workbook: 41467_2026_70521_MOESM9_ESM.xlsx (sheets "Figure S6", "Figure 6", "Figure 7"), Europe PMC supplementary-files endpoint for PMC13121444.
