Write the principles of [SUBJECT] in the following style and structure:

* Begin with one sentence of the form “A [noun] that is used to [purpose].”
* If that sentence uses jargon, continue immediately with “where [term] is a …” for each jargon term. Define the kind of thing the term is, not what it has or does.
* Example opening (Electromagnetic Waves): `A self-sustaining transverse wave of oscillating electric and magnetic fields that travels at the speed of light and carries energy and momentum, where a self-sustaining wave is a free electromagnetic disturbance that needs no material medium, and where a transverse wave is a wave whose oscillations stand perpendicular to the direction of travel.`
* Query Gemini Notebook first for the principles of the subject. Ground the written principles and the References section in Gemini Notebook. Then query ChatGPT only for the commented Topics and Problems lists appended at the end of the file. Do not use ChatGPT as a source for the live body.
* Write each principle as its own paragraph. Put a blank line between paragraphs. Do not number the principles.
* Begin each principle paragraph with the formal name of the principle, law, theorem, or concept, ending with a period, then state the principle.
* Example principle (Relativistic Electrodynamics): `Direction-dependent field transformations. Field components parallel to the relative motion are unchanged. Transverse components mix and scale with the Lorentz factor. A longitudinal component is a field part along the boost. A transverse component is a field part perpendicular to the boost. This principle is used to compute the fields of a moving charge from the rest-frame fields.`
* Each principle paragraph must not exceed 60 words. Named formulas and `where` lists do not count toward that limit.
* State each principle directly and accurately in accessible undergraduate-level language.
* After introducing any specialized or potentially unfamiliar term, immediately define it in plain language as what the term is.
* Do not assume the reader already knows subject-specific jargon.
* Explain what each principle is used for in a sentence beginning with “This principle is used to...” where appropriate.
* In any derivation file, do not use “This principle is used to...”.
* In any derivation file, reduce the principle-paragraph word count by 50 percent: each principle paragraph must not exceed 30 words. Named formulas and `where` lists do not count toward that limit.
* If a formula appears, name the formula first, then display it, then define every symbol in a `where` list:

```
The [formula name] is

$$
[equation]
$$

where

- [symbol] is [what the symbol is].
```

* Example formula block (Gauge Field):

```
The curvature is related to the potential by

- $F = dA + A \wedge A$ .

where

- $A$ is the gauge potential.
- $F$ is the gauge field.
- $d$ is the exterior derivative.
- $\wedge$ is the wedge product of forms.
```

* Keep the explanations concise but substantive.
* Preserve the conceptual meaning of canonical textbook formulations while avoiding unnecessary technical jargon.
* Do not oversimplify to the point of becoming scientifically inaccurate.
* Do not add a Note that lists the formal names of the principles. Those names already begin each principle paragraph.
* If synonyms exist, put them in a Note using “Also called”, not in the opening sentence.
* Use absolute, declarative statements rather than hedging language.
* Do not use “or” to introduce alternative terminology.
* Do not use slashes.
* Do not use bold formatting.
* When writing mathematical derivations or proofs in Markdown files, use the following formats.
* For derivations, use compact aligned LaTeX:

```
$$
\begin{aligned}
A
&= B \\
&= C \\
&= D
\end{aligned}
$$
```

* Each line should represent one clear mathematical step. Add only brief explanations when necessary.
* For proofs, use:

```
### Proof

Assume $P$.

Then,

$$
P \implies Q \implies R \implies S.
$$

Therefore,

$$
S.
$$

$\square$
```

* Keep proofs and derivations concise, linear, and conventional. Use `$...$` for inline mathematics and `$$...$$` for displayed mathematics. Avoid unnecessary prose.

## Query order

1. Query Gemini Notebook for the principles of the subject. Write the live body and the `# References` section from that answer. Cite the printed sources GN returns.
2. Query ChatGPT only after the live body is written. Use ChatGPT solely for the commented Topics and Problems lists at the end of the file.

## ChatGPT append block

After the main body of a subject file is written from Gemini Notebook, query ChatGPT for supplementary Topics and Problems lists. Append the reply to the end of the file inside an HTML comment block so PDF export strips it. Do not mix GN material into the comment block.

### ChatGPT query

Use this prompt pattern:

```
Do not search the web. Do not use URLs. Cite only printed textbooks.

Subject: [SUBJECT]

Write two sections.

Topics. Give 3 to 7 principles. Each paragraph: Name. Statement. This principle is used to ... At most 60 words. No numbers. No bold. No slashes. Do not use or for alternative names.

Problems. Give 3 to 10 specific questions inside [SUBJECT] that this subject settles. Style: Obtain ...; Establish ...; Show that .... Not applications. Not homework. At most 60 words each.
```

Adjust the subject name and field as needed. For probability-theory files, require questions that the theory settles directly, not applied stories.

### Topics list

* Give 3–7 topic items.
* Write each topic as one principle paragraph in the style above: formal name, statement, then “This principle is used to...” when appropriate.
* Each topic paragraph must not exceed 60 words. Named formulas and `where` lists do not count toward that limit.
* Put a blank line between topic paragraphs. Do not number the topics.

### Problems list

* Give 3–10 problem items.
* Each item must state a specific question that the subject settles, not a homework exercise or an applied scenario.
* Each problem item must not exceed 60 words.
* Use single backslashes in `$...$` math inside problems so LaTeX exports correctly.

### Append format

Append the ChatGPT output at the end of the file, fully commented out:

```
<!--
[topic paragraph]

[topic paragraph]

## Problems

- [problem item]
- [problem item]

## Textbooks

- [Author], [Title], [Chapter].
-->
```

* Wrap the entire block in `<!-- ... -->`.
* Write Topics as principle paragraphs with blank lines between them. Do not add a `## Topics` heading inside the comment.
* Add `## Problems` before the problem bullet list.
* Add `## Textbooks` when the ChatGPT query requests printed sources.
* Do not duplicate the comment block in the live body unless the author explicitly promotes items, for example a live `## Problems` section above the comment for PDF export.

### Example append block

```
<!--
Weak law of large numbers. For independent identically distributed random variables with finite mean, the sample mean converges in probability to the common mean. This principle is used to establish that large sample averages become arbitrarily close to the population mean with probability approaching one.

Strong law of large numbers. Under standard independence and integrability conditions, the sample mean converges almost surely to the common mean. This principle is used to establish pathwise convergence of sample averages for almost every infinite sequence of observations.

## Problems

- Establish $\bar{X}_n \xrightarrow{P} \mu$ for independent identically distributed random variables with finite mean.
- Establish $\bar{X}_n \xrightarrow{\mathrm{a.s.}} \mu$ for independent identically distributed integrable random variables.

## Textbooks

- Patrick Billingsley, Probability and Measure, Chapter 22, The Strong Law of Large Numbers.
-->
```
